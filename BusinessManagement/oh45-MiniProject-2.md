<table><tr><td> <em>Assignment: </em> IS601 Mini Project 2  Business Management</td></tr>
<tr><td> <em>Student: </em> Omkar Karbhari Hadawale (oh45)</td></tr>
<tr><td> <em>Generated: </em> 12/4/2022 9:41:54 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-2-business-management/grade/oh45" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>checkout dev and pull any latest changes</li><li>Create a branch called MiniProject-2</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li>Immediate add/commit/push to github</li><li>Open a pull request and keep it open until you're done adding the submission file</li><li>&nbsp;(optional) updated the deploy dev yml file and add MiniProject-2 so you can deploy to dev without needing to merge into dev</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item)<br></li><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 5</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together</li><li>Ensure all screenshots are properly captioned in the deliverable section</li></ol><li>You may save your progress when filling out this submission as often as you want</li><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from dev to prod and merge it</li><li>Navigate to the submission file under the BusinessManagement folder</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F22-MiniProject-2">https://github.com/MattToegel/IS601/tree/F22-MiniProject-2</a></div><div>May want to download branch as a zip, then copy/paste the files into your repo</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205519845-7c40937c-6a19-4e07-bcd6-c8f8764667f6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of layout.html updated the UCID<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205520194-2c1df169-9b71-43ba-a920-ede0a760a4c7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Font end screenshot showing updated UCID in layout.html<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205520249-f00ad616-fbae-4ce1-b02c-351c64fa9389.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing updated brought you by in index.html<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205520435-eba190d8-17b7-4d70-a108-e95bd1c734f3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing connection to the database showing employee and company tables<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205520601-ec359b4f-d77a-4f07-bc7e-a691a69d89fa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing data in company table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205520658-238a65a2-f807-4a47-b999-4fc10901bdd8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing data in employee table<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205520918-97de0731-038b-48ce-afeb-fab7df87aeb7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the code which is checking the file extension and rejecting with<br>proper flash message if not csv<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205521150-21707c99-0abd-4b52-92bf-4d441c28650e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>1)Screenshot showing csv file read from stream as dict 2)Extracted data is appended<br>in company and employee list as dict<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205521431-218f0f68-283a-4de7-a736-6451349ed934.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing all flash messages for 1) how many records were processed 2)If<br>a particular list was empty a flash message should note that the particular<br>list wasn&#39;t loaded or was empty <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205521873-4716db60-e5c6-4f93-bebe-bd10451f0fd2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing proper success message with proper count message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205521927-c858a07d-d5b8-49c8-9abf-17bd904b600c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing error message when file extension is not csv<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205522066-3bf12809-4523-4289-b001-fd0e33bcb698.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the error message when the form was submitted without a file<br>attached<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205522461-b51a21b1-1c53-45bd-ae8f-9c00e9550d00.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing some employee data was uploaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205522563-ecfb3a84-497d-4378-b581-2addc3bb5bb5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing some company data was uploaded<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205522226-bf03be60-3f27-46e7-b56c-6b7ece6be5e8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot Showing following:- 1)Retrieved first_name, last_name, company (id), email 2)first_name is required (flash<br>proper error message) 3)last_name is required (flash proper error message) 4)email is required<br>(flash proper error message)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205523125-844e2148-c3a5-4322-bf88-807e9b9c4a2c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing 1)INSERT query 2)User friendly message flashed and a print() of the<br>exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205523348-f6eaf076-8c24-4d4f-9d5f-7d9f941d99ee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot Showing filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205523404-12659a78-ea13-4537-8f97-a216046a44e5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot Showing success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205523517-dcb8a0c0-3979-4e6e-a5db-40a7ee03a950.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot Showing first_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205523648-7c6453fe-8227-4cce-a51e-2cba1ae066f7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot Showing last_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205523791-c5e99363-9a50-4597-ab17-5c37dad9e85f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot Showing email error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205524044-ba4351e8-585b-431f-bace-898fc06fe586.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>heroku dev URL visible for add employee<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205524273-38b148a8-a325-47e7-8020-bda7ff6295e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot Showing Employee data inserted in the database<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205524786-5a70164e-6328-4af5-84cd-f578e90c0c5a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing SELECT query should be filled in properly to pull employ<br>id, first_name, last_name, email, company_id, company_name via a LEFT JOIN<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205525022-efb31a88-e875-472e-891d-01e9c918801e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing Check request args for fn, ln, email, company, column, order,<br>limit (exact naming is required)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205525146-c2cf4c07-9c5d-4ef3-8b9c-f89c99d46dc9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append like filter for first_name, last_name and email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205525267-1debae32-aa38-4fff-a59c-caabc0908207.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>1)append equality filter for company_id if provided 2)append sorting if column and order<br>are provided and within the allowed columns and order options (asc, desc) allowed_columns<br>= [&quot;first_name&quot;, &quot;last_name&quot;, &quot;email&quot;, &quot;company_name&quot;]  3)append limit (default 10) or limit greater<br>than 1 and less than or equal to 100 4)provide a proper error<br>message if limit isn&#39;t a number or if it&#39;s out of bounds<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205525527-e0516825-bf3c-49b6-b5b7-1a21bb97886a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except block should have a user friendly message flashed and a print() of<br>the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205525865-c1fdbca0-1bda-4335-ad4b-435d2d2944f4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with first_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205525949-995850b9-97dc-4615-91e2-259d697c77e1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with last_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205526043-da2b3e67-cb46-4467-9888-f15e2897b413.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with email filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205526137-d6523a31-c91d-4292-bf47-5950b448e699.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with company filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205526517-e52261bc-01fc-4f9a-aa21-be461e1d3267.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one desc filter applied (clearly label which column was chosen)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205526597-972672c7-6c9a-4b9d-ae52-0569c31e29c2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one asc filter applied (clearly label which column was chosen)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205527175-f6edeeb3-8d83-442a-ad59-5bf565749d66.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>1)Code should retrieve id (from request args) first_name, last_name, company (id), email from<br>form 2)first_name is required (flash proper error message) 3)last_name is required (flash proper<br>error message)4)company doesn&#39;t require a flash and may be empty/None 5)email is required<br>(flash proper error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205527390-6a72e5ff-951e-44a2-a8e6-0be4a42b6bac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>1)Proper UPDATE query should be visible 2)Except blocks (two) should have a user<br>friendly message flashed and a print() of the exception 3)Proper SELECT query should<br>be visible 4)Employee data should be passed to the render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205528543-9caa8fdc-cf7c-492e-bd57-fc5d93add518.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205528730-264fdda3-6c3b-43dc-95a6-a8873b015375.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data after an edit (first name chaged of employee with id 4852)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205528652-67426703-0143-44bd-b799-d7a0d25c40fb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB data before of employee edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205528783-7b00345c-f7f7-4ced-835f-8c086af7a02b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB data after of employee edit<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205529062-9d23e0a9-4596-436b-aa8f-6a64ba1213d4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>1)code should retrieve form data for name, address, city, state, country, zip, website<br>2)name,adress,city,state,country is required (flash proper error message) 3)website is not required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205529295-c3fcede7-1ae8-4fb4-a09f-2d17db48c789.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>1)Proper INSERT query should be visible 2)Except block should have a user friendly<br>message flashed and a print() of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205529968-2c8ca31e-b59a-47a7-aa94-2592af7980d4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SS Showing filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205530055-6679f5eb-686a-4b00-b7ab-ff4aa2c7769b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SS Showing success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205530151-6d4bfa6d-90fb-42ab-beef-d380b617a13c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing all errors<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205530355-f79b8ed8-e093-470a-a15b-ec7cf6cdc312.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Heroku dev URL visible<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205530601-aa859caf-cebd-49b7-bacb-048a78f00b20.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company added visible in database<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205531114-4c0ddd1a-c6ed-406f-b480-4a2b92cce0a0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>1)SELECT query should fetch id, name, address, city, country, state, zip, website, employee<br>count for the company (likely a sub-query is needed) 2)Check request args for<br>name, country, state, column, order, limit 3)append a LIKE name, country, state <br><br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205531503-362e5e66-5cb2-4a21-9489-f04ba78eb8da.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>1)append sorting if column and order are provided and within the allows columsn<br>and allowed order asc,desc allowed_columns = [&quot;name&quot;, &quot;city&quot;, &quot;country&quot;, &quot;state&quot;] 2) append limit<br>(default 10) or limit greater than 1 and less than or equal to<br>100 3)provide a proper error message if limit isn&#39;t a number or if<br>it&#39;s out of bounds 4)provide a proper error message if limit isn&#39;t a<br>number or if it&#39;s out of bounds 5)Except block should have a user<br>friendly message flashed and a print() of the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205532015-7d1c48d4-648f-41d0-8c74-c87974c73cf0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows results with name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205532015-7d1c48d4-648f-41d0-8c74-c87974c73cf0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows results with country filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205532015-7d1c48d4-648f-41d0-8c74-c87974c73cf0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with state filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205532015-7d1c48d4-648f-41d0-8c74-c87974c73cf0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one asc filter applied (clearly label which column was chosen)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205532015-7d1c48d4-648f-41d0-8c74-c87974c73cf0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one desc filter applied (clearly label which column was chosen)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205533005-96762a42-04b5-4eb5-8197-2c51c9aaa426.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should retrieve id (from request args) name, address, city, state, country, zip,<br>website from form<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205533153-78645f23-6b11-4057-aa5f-5b0e98fe4693.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name,address,city,state,country required flash messages<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205533473-3ad29725-f919-4a35-ba4f-06cd43d528e9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>1)Proper UPDATE query should be visible 2)Except blocks (two) should have a user<br>friendly message flashed and a print() of the exception 3) Proper SELECT query<br>should be visible<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205533767-4838f4c1-bf86-4ab7-a15a-513943e3dfb0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205533973-52a2b68b-7b8c-4073-a9ea-2ab85cc683d6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows data after an edit (should be different)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205533880-4cc613ac-a5ff-4243-a90c-88a5f944a1cb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Database before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205534099-f8629255-83b2-4d52-99b5-8d33618ff65f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Database after edit<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205534547-ce26ff88-3282-4521-b73e-b596cfe33263.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>1)Delete employee by id 2)Redirect to employee search 3)All request args (minus id)<br>are passed to the redirect route 4)Success message should be flashed if the<br>process worked<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205534735-050c76d4-dc47-49d6-84e6-0c7254799835.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website Before Database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205535048-3d089f49-f492-42c6-89ed-4a93873d190a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Website after delete<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205535321-54fcc9ab-bc70-4095-8d8f-b8f15632aac6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>1)Delete company by id 2)Redirect to company search 3)All request args (minus id)<br>are passed to the redirect route<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205535522-c054242b-2bcf-426c-9376-32cc68a7b522.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting the company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205535733-8e560da3-c283-4b5b-ba6b-5e1848e897a1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting the company<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/205537358-2fc68172-e9d1-4176-af64-1cb5d13f148a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing passed and failed test cases<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>I learned flask using jinja templates, flask blueprints ,flask factories got the idea<br>of data flow from frontend to backend. Different http requests type like post,<br>get, delete etc, passing data by arguments in URL, through post forms etc.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-2-business-management/grade/oh45" target="_blank">Grading</a></td></tr></table>