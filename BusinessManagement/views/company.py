from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count for the company
    # don't do SELECT *
    query = "SELECT id, name, address, city, country , state, zip, website, created, modified FROM IS601_MP2_Companies WHERE 1=1"
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    # TODO search-2 get name, country, state, column, order, limit request args
    name =  request.args.get("name")
    col =  request.args.get("field")
    order = request.args.get("order")
    state = request.args.get("state")   
    country = request.args.get("country")
    limit = request.args.get("limit")
    # TODO search-3 append a LIKE filter for name if provided
    if name:
        query += " AND name like %s"
        args.append(f"%{name}%")
    # TODO search-4 append an equality filter for country if provided
    if country:
        query += " AND country=%s"
        args.append(f"%{country}%")
    # TODO search-5 append an equality filter for state if provided
    if state:
        query += " AND state=%s"
        args.append(f"%{state}%")
    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    if col and order:
            if col in ["name","address","city","country","state","zip","website","created","modified"] \
            and order in ["asc", "desc"]:
                query += f" ORDER BY {col} {order}"
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    if limit!=None:
        if limit and int(limit) > 0 and int(limit) <= 100:
            query += " LIMIT %s"
            args.append(int(limit))
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
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
        # TODO search-9 make message user friendly
        flash(str(e), "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    allowed_columns = [(v,v) for v in allowed_columns]
    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_columns)

@company.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        name = request.form.get("name", None)
        address = request.form.get("address", None)
        city = request.form.get("city", None)
        website = request.form.get("website", None)
        state = request.form.get("state", None)
        country = request.form.get("country", None)
        zip_code = request.form.get("zip", None)
        has_error = False # use this to control whether or not an insert occurs
        
        # TODO add-2 name is required (flash proper error message)
        if len(name) == 0:
            has_error = True
            flash("Name field is required","warning")
        # TODO add-3 address is required (flash proper error message)
        if len(address) == 0:
            has_error = True
            flash("Address field is required","warning")
        # TODO add-4 city is required (flash proper error message)
        if len(city) == 0:
            has_error = True
            flash("City field is required","warning")
        # TODO add-5 state is required (flash proper error message)
        if len(state) == 0:
            has_error = True
            flash("State field is required","warning")
        # TODO add-6 country is required (flash proper error message)
        if len(country) == 0:
            has_error = True
            flash("Country field is required","warning")
        # TODO add-7 website is not required
        flash("Website field is optional","")

        if not has_error:
            try:
                result = DB.insertOne("INSERT INTO IS601_MP2_Companies (name,address,city,country,state,zip,website) VALUES (%s,%s,%s,%s,%s,%s,%s)",name,address,city,country,state,zip_code,website) # <-- TODO add-8 add query and add arguments
                if result.status:
                    flash("Company added successfully", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                flash("Something went wrong their was error creating the company","danger")
                flash(str(e), "danger")

    return render_template("add_company.html")

@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get("id")
    if id: # TODO update this for TODO edit-1
        data = []
        # allowed_columns = ["name", "city", "country", "state"]
        has_error = False
        if request.method == "POST":
            # TODO edit-2 retrieve form data for name, address, city, state, country, zip, website
            name = request.form.get("name", None)
            address = request.form.get("address", None)
            city = request.form.get("city", None)
            website = request.form.get("website", None)
            state = request.form.get("state", None)
            country = request.form.get("country", None)
            zip_code = request.form.get("zip", None)
            # TODO edit-3 name is required (flash proper error message)
            if len(name) == 0:
                flash("Name field is required","warning")
                has_error = True
            # TODO edit-4 address is required (flash proper error message)
            if len(address) == 0:
                flash("Address field is required","warning")
                has_error = True
            # TODO edit-5 city is required (flash proper error message)
            if len(city) == 0:
                flash("City field is required","warning")
                has_error = True
            # TODO edit-6 state is required (flash proper error message)
            if len(state) == 0:
                flash("State field is required","warning")
                has_error = True
            # TODO edit-7 country is required (flash proper error message)
            if len(country) == 0:
                flash("Country field is required","warning")
                has_error = True
            if len(zip_code) == 0:
                flash("Zip Code field is required","warning")
                has_error = True
            # TODO edit-8 website is not required
            flash("Website field is optional","")
            # 
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            #data = [name, address, city, state, country, zipcode, website]
            data = [name,address,city,state,country,zip_code,website]
            data.append(id)
            if not has_error:
                try:
                    # TODO edit-9 fill in proper update query
                    result = DB.update("UPDATE IS601_MP2_Companies SET name=%s,address=%s,city=%s,state=%s,country=%s,zip=%s,website=%s WHERE id=%s",*data)
                    if result.status:
                        flash("Updated record", "success")
                        return redirect(url_for('company.search', name="", country="", state="",order="asc", column="", limit=10))
                except Exception as e:
                    # TODO edit-10 make this user-friendly
                    flash("Their was and issue updating the record","danger")
                    flash(str(e), "danger")
        try:
            # TODO edit-11 fetch the updated data
            result = DB.selectOne("SELECT id, name, address, city, country , state, zip, website, created, modified FROM IS601_MP2_Companies WHERE id=%s", id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-12 make this user-friendly
            flash("Their was and error retriving updated record")
            flash(str(e), "danger")
    else:
        flash("No such record exists that is being updated","warning")       
    # TODO edit-13 pass the company data to the render template
    return render_template("edit_company.html",company=row)

@company.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete company by id (unallocate any employees)
    id = request.args.get("id")
    try:
        result = DB.update(f"UPDATE IS601_MP2_Employees SET company_id=NULL WHERE company_id={id}")
        if result.status:
            flash("Successfully unallocated employees in the company", "success")
        result1 = DB.delete(f"DELETE FROM IS601_MP2_Companies WHERE id={id}")    
        if result1.status:
            flash("Successfully deleted the company", "success")
    except Exception as e:
        flash("Their was and issue unallocating the employees or deleting the company","danger")
        flash(str(e), "danger")

    # TODO delete-2 redirect to company search
    return redirect(url_for('company.search', name="", country="", state="",order="asc", column="", limit=10))
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    