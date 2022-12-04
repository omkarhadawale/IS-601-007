from flask import Blueprint, render_template, request, flash
from sql.db import DB
employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    query = "SELECT id, first_name, last_name, company_id, email FROM IS601_MP2_Employees WHERE 1=1"
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    fn =  request.args.get("firstname")
    ln =  request.args.get("lastname")
    email = request.args.get("email")
    company_id = request.args.get("company_id")
    col =  request.args.get("field")
    order = request.args.get("order")
    limit = request.args.get("limit")
    # TODO search-3 append like filter for first_name if provided
    if fn:
        query += " AND first_name like %s"
        args.append(f"%{fn}%")
    # TODO search-4 append like filter for last_name if provided
    if ln:
        query += " AND last_name like %s"
        args.append(f"%{ln}%")
    # TODO search-5 append like filter for email if provided
    if email:
        query += " AND email like %s"
        args.append(f"%{email}%")
    # TODO search-6 append equality filter for company_id if provided
    if company_id:
        query += " AND company_id=%s"
        args.append(f"%{company_id}%")
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    if col and order:
            if col in ["id", "first_name", "last_name", "company_id", "email","created","modified"] \
            and order in ["asc", "desc"]:
                query += f" ORDER BY {col} {order}"
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    if limit!=None:
        if limit and int(limit) > 0 and int(limit) <= 100:
            query += " LIMIT %s"
            args.append(int(limit))
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
        else:
            flash("Limit out of bound(1 to 100) or not selected","warning")
            query += " LIMIT %s"
            limit = 10
            args.append(int(limit))
    else:
        limit = 10
        query += " LIMIT %s"
        args.append(int(limit))         
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-10 make message user friendly
        flash(e, "error")
    # hint: use allowed_columns in template to generate sort dropdown
    allowed_columns = [(v,v) for v in allowed_columns]
    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_columns)

@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        first_name = request.form.get("first_name", None)
        last_name = request.form.get("last_name", None)
        email = request.form.get("email", None)
        company_id = request.form.get("company", None)
        # TODO add-2 first_name is required (flash proper error message)
        if len(first_name) == 0:
            flash("First Name field is required","warning")
        # TODO add-3 last_name is required (flash proper error message)
        if len(last_name) == 0:
            flash("Last Name field is required","warning")
        # TODO add-4 company (may be None)
        if len(company_id) == 0:
            flash("Company field is required","warning")
        # TODO add-5 email is required (flash proper error message)
        if len(email) == 0:
            flash("Email field is required","warning")
        if len(first_name) != 0 and len(last_name) != 0 and len(company_id) != 0 and len(email) != 0:
            try:
                result = DB.insertOne("INSERT INTO IS601_MP2_Employees (first_name,last_name,company_id,email) VALUES (%s,%s,%s,%s)",first_name,last_name,company_id,email) # <-- TODO add-6 add query and add arguments
                if result.status:
                    flash("Successfully added Employee", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                flash(str(e), "danger")
    return render_template("add_employee.html")

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    if True: # TODO update this for TODO edit-1
        if request.method == "POST":
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            # TODO edit-2 first_name is required (flash proper error message)
            # TODO edit-3 last_name is required (flash proper error message)
            # TODO edit-4 company may be None
            # TODO edit-5 email is required (flash proper error message)
            
            # data = [first_name, last_name, company_id, email]
            data.append(id)
            try:
                # TODO edit-6 fill in proper update query
                result = DB.update("""
                UPDATE QUERY
                """, *data)
                if result.status:
                    flash("Updated record", "success")
            except Exception as e:
                # TODO edit-7 make this user-friendly
                flash(e, "danger")
        try:
            # TODO edit-8 fetch the updated data (including company_name)
            # company_name should be 'N/A' if the employee isn't assigned to a copany
            result = DB.selectOne("SELECT ... FROM ... LEFT JOIN ...  WHERE ...", id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            flash(str(e), "danger")
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", ...)

@employee.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete employee by id
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    pass