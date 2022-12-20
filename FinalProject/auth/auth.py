import json
import re
from flask import Blueprint, render_template, flash, redirect, request, url_for,current_app, session
from auth.forms import ChangeUserPassword, DepositMoney, LoginForm, RegisterForm, TransferMoney, UserProfileEdit, CreateNewBankAccount, WithDrawMoney
from sql.db import DB

from flask_login import login_user, login_required, logout_user
from auth.models import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

from flask_principal import Identity, AnonymousIdentity, \
     identity_changed

auth = Blueprint('auth', __name__, url_prefix='/',template_folder='templates')


@auth.route("/register", methods=["GET","POST"])
def register():
    form = RegisterForm()
    # wtform validators are both client-side and server-side
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        try:
            hash = bcrypt.generate_password_hash(password)
            # save the hash, not the plaintext password
            result = DB.insertOne("INSERT INTO IS601_Users (username, email, password) VALUES (%s, %s, %s)", username, email, hash)
            if result.status:
                flash("Successfully registered","success")
        except Exception as e:
            #UCID:-oh45
            if re.search(f"Duplicate entry",str(e)):
                if re.search(f"{email}",str(e)):
                    flash(f"{email} is not available(Email is already registered)","warning")
                if re.search(f"{username}",str(e)):
                    flash(f"Username:-{username} is already taken","warning")
            else:
                flash(str(e), "danger")
    return render_template("register.html", form=form)

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        try:
            result = DB.selectOne("SELECT id, username, email, password FROM IS601_Users where email=%s", email)
            if result.status and result.row:
                hash = result.row["password"]
                if bcrypt.check_password_hash(hash, password):
                    from roles.models import Role
                    del result.row["password"] # don't carry password/hash beyond here
                    user = User(**result.row)
                    # get roles
                    result = DB.selectAll("""
                    SELECT name FROM IS601_Roles r JOIN IS601_UserRoles ur on r.id = ur.role_id WHERE ur.user_id = %s AND r.is_active = 1 AND ur.is_active = 1
                    """, user.id)
                    if result.status and result.rows:
                        print("role rows", result.rows)
                        user.roles = [Role(**r) for r in result.rows]
                    print(f"Roles: {user.roles}")
                    success = login_user(user) # login the user via flask_login
                    
                    if success:
                        # Tell Flask-Principal the identity changed
                        identity_changed.send(current_app._get_current_object(),
                                  identity=Identity(user.id))
                        # store user object in session as json
                        session["user"] = user.toJson()
                        flash("Log in successful", "success")
                        return redirect(url_for("auth.landing_page",))
                    else:
                        flash("Error logging in", "danger")
                else:
                    flash("Invalid password", "warning")
            else:
                # invalid user and invalid password together is too much info for a potential attacker
                # normally we return a single message for both "invalid username or password" so an attacker doens't know which part was correct
                flash("Invalid user", "warning")

        except Exception as e:
            #UCID:-oh45
            if re.search("object has no attribute 'row'",str(e)):
                flash("The email is not registered", "warning")
            else:
                flash(str(e), "danger")   
    return render_template("login.html", form=form)

@auth.route("/landing-page", methods=["GET","POST"])
@login_required
def landing_page():
    print("-----------------",session["user"])
    print("-------------------",type(session["user"]))
    #UCID:-oh45
    #Accessing logged In user from session
    user = json.loads(session["user"])
    #UCID:-oh45
    #Prefilling user profile edit form from session data
    userform = UserProfileEdit(obj=User(user['id'],user['username'],user['email'],user['roles']))
    passform = ChangeUserPassword()
    if userform.validate_on_submit():
        username = userform.username.data
        email = userform.email.data
        update = True
        if username == user['username'] and email==user['email']:
            update = False
        if update:
            try:
                result = DB.insertOne("UPDATE IS601_Users set username = %s, email = %s WHERE email = %s", username, email, user['email'])  
                if result.status:
                    flash("User profile successfully updated","success")
                    # UCID:-oh45
                    # Updating session 
                    newuser = {"id":user['id'],"username":username,"email":email,"roles":user['roles']}
                    print(newuser)
                    try:
                        usr = User(**newuser)
                        session["user"] = usr.toJSON()
                    except Exception as e:
                        flash("Their was an error updating user session","danger")
                        flash(f"Error message:-{str(e)}","danger")    
            except Exception as e:
            #UCID:-oh45
                if re.search(f"Duplicate entry",str(e)):
                    if re.search(f"{email}",str(e)):
                        flash(f"{email} is not available(Email is already registered)","warning")
                    if re.search(f"{username}",str(e)):
                        flash(f"Username:-{username} is already taken","warning")
                else:        
                    flash("Theie was an error updating username/email","danger")
                    flash(f"Error message:- {str(e)}","danger")
    #UCID:-oh45
    if passform.validate_on_submit():        
        oldpassword = passform.oldpassword.data
        newpassword = passform.newpassword.data
        try:
            result = DB.selectOne('SELECT password FROM IS601_Users where email=%s',user['email'])
            if result.status and result.row:
                if bcrypt.check_password_hash(result.row['password'], oldpassword):
                    try:
                        hash = bcrypt.generate_password_hash(newpassword)
                        result1 = DB.insertOne('UPDATE IS601_Users SET password=%s where email=%s', hash, user['email'])
                        if result1.status:
                            flash("Password successfully updated","success")
                    except Exception as e:
                        flash("Their was an error updating the user","danger")
                        flash(f"Error message:-{str(e)}","danger")    
                else:
                    flash("Wrong old password (please enter correct password)","warning")        
        except Exception as e:
            flash("Their was an error updating the password")
            flash(f"Error message:-{str(e)}","danger")
    return render_template("landing_page.html", form=userform, form1=passform)

@auth.route("/logout", methods=["GET"])
def logout():
    logout_user()
    # Remove session keys set by Flask-Principal
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)

    # Tell Flask-Principal the user is anonymous
    identity_changed.send(current_app._get_current_object(),
                          identity=AnonymousIdentity())
    flash("Successfully logged out", "success")
    return redirect(url_for("auth.login"))


@auth.route("/createBankAccount", methods=["GET","POST"])
@login_required
def createBankAccount():
    user = json.loads(session["user"])
    form = CreateNewBankAccount()
    if form.validate_on_submit():
        accountNo = form.accountNo.data
        accountType = form.accountType.data
        initialDeposit = form.initialDeposit.data
        try:            
            result = DB.insertOne("INSERT INTO IS601_S_Accounts (account, account_type, user_id, balance) VALUES (%s,%s,%s,%s)",accountNo, accountType, user['id'], initialDeposit)  
            if result.status:
                flash("Account Created Successfully","success")
                result0 = DB.selectOne("SELECT id FROM IS601_S_Accounts WHERE account=%s",accountNo)
                if result0.status and result0.row:
                    account_id = result0.row['id']
                    result1 = DB.insertOne("INSERT INTO IS601_S_Transactions (src, dest, diff, reason, details) VALUES(%s , %s, %s ,'Initial deposit','New account opening initial deposit')", account_id, account_id, initialDeposit)    
                    if result1.status:
                        flash("Transaction Successful","success")
        except Exception as e:
            #UCID:-oh45
            if re.search(f"Duplicate entry",str(e)):
                if re.search(f"{accountNo}",str(e)):
                    flash(f"The account no:- {accountNo} is already taken.Please choose other account number","warning")
                
            else:
                flash(f"{str(e)}","danger")     
        
    return render_template("createBankAccount.html",form=form)



@auth.route("/listBankAccount", methods=["GET"])
@login_required
def listBankAccount():
    user = json.loads(session["user"])
    rows = None
    try:
        result = DB.selectAll("SELECT account as Account,account_type as AccountType, balance as Balance, created, modified FROM IS601_S_Accounts WHERE user_id=%s",int(user['id']))  
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        flash(f"{str(e)}","danger")
    return render_template("listBankAccount.html", rows=rows,username=user['username'])


@auth.route("/depositMoney", methods=["GET","POST"])
@login_required
def depositMoney():
    form = DepositMoney()
    user = json.loads(session["user"])
    accounts = []
    if form.validate_on_submit():
        accountNo = form.accountNo.data
        amount = form.amount.data
        try:
            result = DB.update("UPDATE IS601_S_Accounts SET balance=balance+%s WHERE account=%s", amount, accountNo)
            if result.status:
                flash("Money Deposited Successfully","success")
                result0 = DB.selectOne("SELECT id FROM IS601_S_Accounts WHERE account=%s",accountNo)
                if result0.status and result0.row:
                    account_id = result0.row['id']
                    result1 = DB.insertOne("INSERT INTO IS601_S_Transactions (src, dest, diff, reason, details) VALUES(%s , %s, %s ,'Self deposit','Self deposit')", account_id, account_id, amount)    
                    if result1.status:
                        flash("Transaction Successful","success")
        except Exception as e:
            flash("Their was an error depositing the money","danger")
            flash(f"{str(e)}","danger") 
    
    try:
        result = DB.selectAll("SELECT account FROM IS601_S_Accounts WHERE user_id=%s",user['id'])
        if result.status:
            for account in result.rows:
                accounts.append(account['account'])
    except Exception as e:
        flash(f"{str(e)}")    

    return render_template("depositMoney.html",form=form,accounts=accounts)  


@auth.route("/withdrawMoney", methods=["GET","POST"])
@login_required
def withdrawMoney():
    user = json.loads(session["user"])
    accounts = []
    form = WithDrawMoney()
    if form.validate_on_submit():
        accountNo = form.accountNo.data
        amount = form.amount.data
        try:
            result = DB.selectOne("SELECT balance FROM IS601_S_Accounts WHERE account=%s",accountNo)
            if result.status and result.row:
                if amount <= result.row['balance']:
                    result1 = DB.update("UPDATE IS601_S_Accounts SET balance=balance-%s WHERE account=%s", amount, accountNo)
                    if result1.status:
                        flash(f"Successfully withdrawn ${amount}. Please collect","success")
                        result0 = DB.selectOne("SELECT id FROM IS601_S_Accounts WHERE account=%s",accountNo)
                        if result0.status and result0.row:
                            account_id = result0.row['id']
                            result1 = DB.insertOne("INSERT INTO IS601_S_Transactions (src, dest, diff, reason, details) VALUES(%s , %s, -%s ,'Self withdraw','Self Cash withdraw')", account_id, account_id, amount)    
                            if result1.status:
                                flash("Transaction Successful","success")
                else:
                    flash(f"You have insufficient balance to withdraw the amount. Your current account balance is ${result.row['balance']}","warning")    
        except Exception as e:
            flash(f"{str(e)}","danger")    
    
    try:
        result = DB.selectAll("SELECT account FROM IS601_S_Accounts WHERE user_id=%s",user['id'])
        if result.status:
            for account in result.rows:
                accounts.append(account['account'])
    except Exception as e:
        flash(f"{str(e)}")

    return render_template("withdrawMoney.html",form=form,accounts=accounts)



@auth.route("/transferMoney", methods=["GET","POST"])
@login_required
def transferMoney():
    user = json.loads(session["user"])
    accounts = []
    form = TransferMoney()
    if form.validate_on_submit():
        srcAccountNo = form.srcAccountNo.data
        desAccountNo = form.destAccountNo.data
        amount = form.amount.data
        try:
            result = DB.selectOne("SELECT balance FROM IS601_S_Accounts WHERE account=%s",srcAccountNo)
            if result.status and result.row:
                if amount <= result.row['balance']:
                    result1 = DB.update("UPDATE IS601_S_Accounts SET balance=balance-%s WHERE account=%s", amount, srcAccountNo)
                    if result1.status:
                        result2 = DB.update("UPDATE IS601_S_Accounts SET balance=balance+%s WHERE account=%s", amount, desAccountNo)    
                        if result2.status:
                            flash("Transfer successful","success")
                            src_id = DB.selectOne("SELECT id FROM IS601_S_Accounts WHERE account=%s",srcAccountNo)
                            dest_id = DB.selectOne("SELECT id FROM IS601_S_Accounts WHERE account=%s",desAccountNo)
                        if src_id.status and src_id.row and dest_id.status and dest_id.row:
                            src_account_id = src_id.row['id']
                            dest_account_id = dest_id.row['id']
                            result1 = DB.insertOne("INSERT INTO IS601_S_Transactions (src, dest, diff, reason, details) VALUES(%s , %s, %s ,'Transfer',\"From '%s' to '%s'\")", src_account_id, dest_account_id, amount, srcAccountNo, desAccountNo)    
                            if result1.status:
                                flash("Transaction Successful Recorded","success")
                else:
                    flash(f"You have insufficient balance to transfer the amount. Your current account balance is ${result.row['balance']}","warning")

        except Exception as e:
            flash(f"{str(e)}","danger")    


    try:
        result = DB.selectAll("SELECT account FROM IS601_S_Accounts WHERE user_id=%s",user['id'])
        if result.status:
            for account in result.rows:
                accounts.append(account['account'])
    except Exception as e:
        flash(f"{str(e)}")
    return render_template("transferMoney.html",form=form,accounts=accounts)




@auth.route("/listAccountTransactions", methods=["GET"])
@login_required
def listAccountTransactions():
    user = json.loads(session["user"])
    account = request.args.get("account")
    rows = None
    balance = None
    try:
        result = DB.selectAll("SELECT * FROM IS601_S_Transactions WHERE src IN(SELECT id FROM IS601_S_Accounts WHERE account=%s) OR dest IN(SELECT id FROM IS601_S_Accounts WHERE account=%s)",account,account)  
        if result.status and result.rows:
            rows = result.rows
        result1 = DB.selectOne("SELECT balance FROM IS601_S_Accounts WHERE account=%s", account)
        if result1.status and result1.row:
            balance = result1.row['balance']
    except Exception as e:
        flash(f"{str(e)}","danger")

    return render_template("listAccountTransactions.html",rows=rows,account=account,username=user['username'],balance=balance) 
    