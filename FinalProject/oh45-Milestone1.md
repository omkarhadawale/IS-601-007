<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Omkar Karbhari Hadawale (oh45)</td></tr>
<tr><td> <em>Generated: </em> 12/11/2022 8:24:18 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone1-deliverable/grade/oh45" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206888488-1718f54a-85d7-419e-88f4-b72b8c9ca796.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screen shot showing invalid email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206888567-be39cbbc-e71e-4ca1-9dba-e7482c46c7a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206888598-e34416b4-4b2c-4b33-a70f-1d9dda9a0c3e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing passwords not much validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206888646-281b9745-af3d-4ed0-aacc-675a7ecdc622.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing email not available validation (already registered)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206888732-8c9663b4-a2dc-4cb5-b2c4-913f8b382e19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing username not available validation (username is taken)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206888795-ca63a504-1409-446b-acd0-54f0846d6bf7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing valid data filled in before the form is submitted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206888898-7f8a769f-f659-4104-8b8d-49b9d89ed74b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing valid user data from Task 1 present in database.(User is<br>successfully registered)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/omkarhadawale/IS-601-007/pull/7">https://github.com/omkarhadawale/IS-601-007/pull/7</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>We create a form class inheriting WTF from class FlaskForm. In this<br>class fields, field types and validations are defined. Now we simply use the<br>form object in our endpoint function to access form fields and serve the<br>request.<div>2)The validation defined in the above custom form class we created are usually<br>handled internally by WTF forms on client side. But even on the server<br>side we are using valid_on_submit() a WTF from method which again validates the<br>form fields. If any validation fails now then validation errors are contained in<br>the errors field of the form object and the form object is return<br>to frontend where the validation error is displayed.</div><div>3)Whenever new user registers the password<br>is first hashed and then the hashed value is stored in the database.</div><br></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206890098-b3d7b58d-8b23-42d8-8442-595d663153ac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing password mismatch validation (doesn&#39;t match what&#39;s in the DB)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206890136-19db7d54-a780-4db5-8c4f-bb4f4d656756.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing validation based on non-existing user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206890175-6058a830-5848-4e36-8cee-f0244e803d99.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing successful login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/omkarhadawale/IS-601-007/pull/7">https://github.com/omkarhadawale/IS-601-007/pull/7</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>We create a form class inheriting WTF from class FlaskForm. In this<br>class fields, field types and validations are defined. Now we simply use the<br>form object in our endpoint function to access form fields and serve the<br>request.<div>2)The validation defined in the above custom form class we created are usually<br>handled internally by WTF forms on client side. But even on the server<br>side we are using valid_on_submit() a WTF from method which again validates the<br>form fields. If any validation fails now then validation errors are contained in<br>the errors field of the form object and the form object is return<br>to frontend where the validation error is displayed.</div><div>3)The password is first hashed and<br>then the hashed value is stored in the database. Whenever the user tries<br>to login the password entered by user is hashed and the hash value<br>is compared with hash value in the database.</div><br></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206890327-3a20e219-7669-4c69-8786-b3e73a548952.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing successful logout message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206890500-b9717496-64e8-462a-8b5c-1f4433706671.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing unauthorize access message to not logged in user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/omkarhadawale/IS-601-007/pull/7">https://github.com/omkarhadawale/IS-601-007/pull/7</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>Whenever any user tries to access a login protected page the session data<br>is checked whether the user is authenticated if the user haven&#39;t logged in<br>the is_authenticated flag remains false and the user will<div>not be able to access<br>the login protected pages. Basically whenever a user login&#39;s the session is set<br>with user details like username, email, password and roles. The session is short<br>lived and temporary valid till 30 mins&nbsp;</div><div>in that time the user will be<br>able to access login protected page without a need to login.&nbsp;</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206890500-b9717496-64e8-462a-8b5c-1f4433706671.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing unauthorize access message to not logged in user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206892059-54162aef-b933-4914-b78e-6eb9ccf9c819.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing permission denied as the user does not posses proper role<br>to access the roles/assign page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206892129-37dec2b1-12f8-4999-bf37-9b69feadb559.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing data in roles table in database<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206892242-af44e8d3-7462-488b-b85f-14819784462d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User with user id 1, 15, 16 and username omkar, varad and admin<br>respectively are the admin users<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/omkarhadawale/IS-601-007/pull/7">https://github.com/omkarhadawale/IS-601-007/pull/7</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>Whenever any user tries to access a login protected page the session data<br>is checked whether the user is authenticated if the user haven&#39;t logged in<br>the is_authenticated flag remains false and the user will<div>not be able to access<br>the login protected pages. Basically whenever a user login&#39;s the session is set<br>with user details like username, email, password and roles. The session is short<br>lived and temporary valid till 30 mins&nbsp;</div><div>in that time the user will be<br>able to access login protected page without a need to login.&nbsp;</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>Same as login the user roles are stored in session data when ever<br>the user tries to access roles protected page if the access will be<br>denied as in the jinja template we are checking the role of user&nbsp;<div>based<br>on that the UI is rendered, certain functions are only visible and access<br>able to admin user.&nbsp;</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206930949-766b6fad-1643-4e5c-b214-3dc1df395ae4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Style of User registration page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206930874-ca19f5de-e4d1-4018-8b97-14b2006e3edc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Style of User Login page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206930771-eddcc918-4e58-466f-806c-8ecb88d5ed6b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Style of user profile edit page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206931015-6006d996-786c-44cc-bfc5-9e54a6aea7ce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Style of role list page <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206931092-eceb4429-8e6f-49c5-a4d5-e8af93e3b29f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Style Roles add page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206931141-0ea5241e-5bce-4432-a77f-018f69222b95.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Style of role assign page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/omkarhadawale/IS-601-007/pull/7">https://github.com/omkarhadawale/IS-601-007/pull/7</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>For styling the in build form classes are used whose internal styling are<br>used. For navigation the navigation class is used whose styles are inherited.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206888488-1718f54a-85d7-419e-88f4-b72b8c9ca796.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screen shot showing invalid email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206888567-be39cbbc-e71e-4ca1-9dba-e7482c46c7a9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206888646-281b9745-af3d-4ed0-aacc-675a7ecdc622.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing email not available validation (already registered)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206888732-8c9663b4-a2dc-4cb5-b2c4-913f8b382e19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing username not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206888598-e34416b4-4b2c-4b33-a70f-1d9dda9a0c3e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing passwords not match validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206892059-54162aef-b933-4914-b78e-6eb9ccf9c819.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing permission denied as the user does not posses proper role<br>to access the roles/assign page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206890500-b9717496-64e8-462a-8b5c-1f4433706671.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing unauthorize access message to not logged in user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/omkarhadawale/IS-601-007/pull/7">https://github.com/omkarhadawale/IS-601-007/pull/7</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>For handling email/username already exist the duplicate key error is thrown by the<br>update/insert statement the error is catch by the except block. In the except<br>block regular expression search method is&nbsp;<div>is used to check weather duplicate word and<br>the username/email is present if present the user friendly message is displayed saying<br>username/email already taken.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206930771-eddcc918-4e58-466f-806c-8ecb88d5ed6b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing user profile page with username and email prefilled<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/omkarhadawale/IS-601-007/pull/7">https://github.com/omkarhadawale/IS-601-007/pull/7</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>The user data is taken from session data set in login. The session<br>data is then converted to dictionary using json.loads() function, then the dictionary items<br>are passed into the user object. Lastly the&nbsp;<div>filled user object is passed in<br>the from object then the passed data is internally prefilled by WTF forms.&nbsp;<br>&nbsp;</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206933178-6062a166-8daa-4d42-9106-89e14395aa71.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing username validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206933228-025e45cd-8699-42a0-98ea-582bc38c8bc0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing email validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206933788-7070aa7b-85af-4743-bca6-68f3d4f97f95.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing password validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206933879-d6edf326-bcb9-42f1-bc58-4f39d118c48c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing password mismatch message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206933962-e9f62c0c-52f3-4cf7-9a5e-48075befe78d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing email already in use message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206933343-5a4391e9-8aac-4b9d-8310-975dbefd5e1d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing invalid password message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206934066-e173ca37-f3e7-4180-9d6c-28597726a6a0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing username taken message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206934508-073b39f1-4c35-4096-8215-ab26aef8a491.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot of Users table Before user edits profile<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/206934617-bf8a0222-c09a-40a6-a8d7-a0007a417497.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot of Users table after user edits profile.(The username of user with<br>id 1 is changed from omkar1 to omkar.)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/omkarhadawale/IS-601-007/pull/7">https://github.com/omkarhadawale/IS-601-007/pull/7</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p><b><u><font size="4">Edit code Logic:-</font></u></b><div><font size="2" style="">1)I have created two separate forms one for<br>username, email edit and other for changing password.</font></div><div><font size="2" style="">2)I have created two<br>new form classes in forms.py and have added these forms on the landing<br>page of user.</font></div><div><font size="2" style="">3)Prefilled username and email&nbsp; from the session data set<br>from login endpoint. Got user entered username and password from form and then<br>checked if the old username and email are same from the session data<br>of they are same no update in performed. If they are not same<br>as old data then the update query is executed. If the update is<br>successful then the session is also updated. If the user enters existing username<br>as desired new username/email then duplicate key error will be thrown. This error<br>catch using except block and User friendly message is shown.</font></div><div><font size="2" style="">4)For second<br>form which is for changing user password if the old password entered by<br>user does not match a friendly message is shown. If the password matches<br>the original password from session then only the password is changed.</font></div><div><font size="2" style="">5)The<br>validation are specified in in the form classes created which are internally handled<br>by WTF forms. For validations like username/email already taken the duplicate key error<br>is catch and proper user friendly message is shown</font></div><div><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div><b><u><font size="4">Learnings:-</font></u></b></div><div>1)I learned the sessions which manage the user login, storing data in<br>session and using that data instead of querying database for the same data.&nbsp;</div><div>2)I<br>learned User login and log out mechanism using flask_login package.</div><div>3)I learned Roles mechanism<br>in flask using flask principle package.&nbsp;&nbsp;</div><div>4)I learned Using WTF forms prefilling and adding<br>validations and backed validation for input fields.</div><div><u style=""><b style=""><font size="4">Problems faced:-</font></b></u></div><div>1)I was getting<br>and invalid salt error when I was trying to update user password it<br>was due to I haven't included the hidden tag in the password update<br>form.</div><div>2)As the username and password on the user landing page are prefilled from<br>session data, when I update the username or email of user it changed<br>in database but the landing page was still showing&nbsp;</div><div>the old username/email which it<br>was taking from session data. Hence to solve this problem I updated the<br>session data whenever user updates his username or email.&nbsp;&nbsp;</div><div><b><u><font size="5">Important</font></u></b></div><div>The below input field<br>validation was not accepting my application url for prod as it may be<br>expecting "prod.herokuapp" format but I have named my heroku dyno as "prod-final.herokuapp" format.</div><div>Here<br>is the URL&nbsp;</div><div>prod URL : - <a href="https://is601-oh45-prod-final.herokuapp.com">https://is601-oh45-prod-final.herokuapp.com</a></div><div>dev URL :-&nbsp;<a href="https://is601-oh45-prod-final.herokuapp.com/">https://is601-oh45-dev-final.herokuapp.com</a></div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-oh45-prod-final.herokuapp.com">https://is601-oh45-prod-final.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone1-deliverable/grade/oh45" target="_blank">Grading</a></td></tr></table>