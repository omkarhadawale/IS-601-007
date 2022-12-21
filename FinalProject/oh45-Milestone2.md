<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Bank Project</td></tr>
<tr><td> <em>Student: </em> Omkar Karbhari Hadawale (oh45)</td></tr>
<tr><td> <em>Generated: </em> 12/21/2022 6:23:14 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-2-bank-project/grade/oh45" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Create Accounts table and setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot from the db of the system user (Users table)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208795012-c23c573b-88b9-4d97-97cb-3003e3782754.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Db screenshot showing system user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot from the db of the world account (Accounts table)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208796080-a954fbb8-6751-46da-bd31-687e7d74ee33.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Db screenshot showing world account type associated with system user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain the purpose and usage of these two entries and how they relate</td></tr>
<tr><td> <em>Response:</em> <p>In order to do any transactions we need user having an account. For<br>any transactions to exists like withdraw, deposit, transfer etc. user with account is<br>necessary as user_id in accounts table is a foreign key(refer to user&nbsp;<div>to which<br>the account belongs). And src and dest are foreign keys in Transactions table<br>referring id of accounts table which is unique for each account. Thus in<br>order to perform transaction the above entries are necessary.&nbsp; &nbsp;</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/omkarhadawale/IS-601-007/pull/8">https://github.com/omkarhadawale/IS-601-007/pull/8</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Dashboard </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the requested links/navigation</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208797459-3e43cf6d-e744-4dfb-bb33-8b2bc9ea6ab5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing all necessary functions on UI <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208797884-7dc39c88-6ac8-48e9-a471-7d0bae7b0301.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing Create New account page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208798195-86a83f80-79d7-4b02-8de5-e68555c3ffc6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing List accounts page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208798887-cfe09e8f-b0dd-4406-844c-318805da6df4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing Deposit Money page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208798981-632abc74-4b3f-4ea9-821f-7a52be6d48ae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing Withdraw Money page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208987220-75d06d9c-cf1c-4189-9a01-432255c7561d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing account balance and all transaction of the account.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain which ones are working for this milestone</td></tr>
<tr><td> <em>Response:</em> <p>All Links are working like:<div>1)Create New account(<a href="https://is601-oh45-prod-final.herokuapp.com/createBankAccount">https://is601-oh45-prod-final.herokuapp.com/createBankAccount</a>)</div><div>2)List accounts(<a href="https://is601-oh45-prod-final.herokuapp.com/listBankAccount">https://is601-oh45-prod-final.herokuapp.com/listBankAccount</a>)</div><div>3)Deposit Money(<a href="https://is601-oh45-prod-final.herokuapp.com/depositMoney">https://is601-oh45-prod-final.herokuapp.com/depositMoney</a>)</div><div>4)Withdraw Money (<a href="https://is601-oh45-prod-final.herokuapp.com/withdrawMoney">https://is601-oh45-prod-final.herokuapp.com/withdrawMoney</a>)</div><div><br></div><div><div><b><font size="5">Important</font></b></div><div><b><font size="4">The<br>above link requires a user to be logged in to access it create<br>a account here(</font></b><font size="4"><b><a href="https://is601-oh45-prod-final.herokuapp.com/register">https://is601-oh45-prod-final.herokuapp.com/register</a></b></font><b><font size="4">) and then login here(</font></b><font size="4"><b><a href="https://is601-oh45-prod-final.herokuapp.com/login">https://is601-oh45-prod-final.herokuapp.com/login</a></b></font><b><font size="4">)</font></b></div></div><div><br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/omkarhadawale/IS-601-007/pull/8">https://github.com/omkarhadawale/IS-601-007/pull/8</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Create a checking Account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the Create Account Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208799533-b7490625-ac2b-4691-8ebb-91c8f4dbb296.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Screenshot showing Create Account Page filled with data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots showing validation errors and success message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208800139-bd99855c-5b98-4346-b24c-be4f9c6baeb9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing minimum funding validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208799762-236fcdd7-2312-44ec-9bbe-61cf50afbdd0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing success message for task1(Create account)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208799980-4450a490-25b3-4bd1-ae13-41fc3f6de14c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing account no validation message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the transaction generated from the initial deposit (from the DB)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208800547-1f84f6e4-7d20-4645-abc2-8f2fab68851d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing transaction generated from above initial deposit which is positive fund move<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208801272-da17e9c5-b0d0-4fd9-9361-1d5778c28fb8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing transaction generated from withdrawal of money which is negative move of<br>funds<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain which account number generation you used and the account creation process including the transaction logic</td></tr>
<tr><td> <em>Response:</em> <p>I am taking account number as input from the user where I have<br>added validations like the account number should be exactly 12 digits long. The<br>user which is logged in is associated with the account which<div>is created. The<br>user id is fetch from the session data.</div><div><br></div><div><div><b><font size="5">Important</font></b></div><div><b><font size="4">The below link requires<br>a user to be logged in to access it create a account here(</font></b>&lt;font<br>size=&quot;4&quot;&gt;<b><a href="https://is601-oh45-prod-final.herokuapp.com/register">https://is601-oh45-prod-final.herokuapp.com/register</a></b></font><b><font size="4">) and then login here(</font></b><font size="4"><b><a href="https://is601-oh45-prod-final.herokuapp.com/login">https://is601-oh45-prod-final.herokuapp.com/login</a></b></font><b><font size="4">)</font></b></div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/omkarhadawale/IS-601-007/pull/8">https://github.com/omkarhadawale/IS-601-007/pull/8</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-oh45-prod-final.herokuapp.com/createBankAccount">https://is601-oh45-prod-final.herokuapp.com/createBankAccount</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> User will be able to list their accounts </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the user's account list view (show 5 accounts)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208816146-c7c8283b-99ce-4e5c-98fe-9b61ce9ca8bf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing user account list <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the page is displayed and the data lookup occurs</td></tr>
<tr><td> <em>Response:</em> <p>A select query selects accounts of user by where user id is equal<br>to logged in user which is stored in session. User accounts are retrieved<br>from database in form of list of dictionaries which is the passed&nbsp;<div>to jinja<br>template their the list is iterated and each dictionary values are printed in<br>respective rows.</div><div><br></div><div><div><b><font size="5">Important</font></b></div><div><b><font size="4">The below link requires a user to be logged in<br>to access it create a account here(</font></b><font size="4"><b><a href="https://is601-oh45-prod-final.herokuapp.com/register">https://is601-oh45-prod-final.herokuapp.com/register</a></b></font><b><font size="4">) and then login here(</font></b>&lt;font<br>size=&quot;4&quot;&gt;<b><a href="https://is601-oh45-prod-final.herokuapp.com/login">https://is601-oh45-prod-final.herokuapp.com/login</a></b></font><b><font size="4">)</font></b></div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/omkarhadawale/IS-601-007/pull/8">https://github.com/omkarhadawale/IS-601-007/pull/8</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-oh45-dev-final.herokuapp.com/listBankAccount">https://is601-oh45-dev-final.herokuapp.com/listBankAccount</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Account Transaction Details </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of an account's transaction history</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208993793-b01be97d-9eae-49af-992f-4f38d8dd8d16.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing account transactions page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the lookup and display occurs</td></tr>
<tr><td> <em>Response:</em> <p>A select query selects the records whose either src or dest columns contains<br>the account id of the current account of which transactions we want to<br>display.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/omkarhadawale/IS-601-007/pull/8">https://github.com/omkarhadawale/IS-601-007/pull/8</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-oh45-prod-final.herokuapp.com">https://is601-oh45-prod-final.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Deposit/Withdraw </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a Screenshot of the Deposit Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208987963-9f7b2e0f-0eda-4ff1-b49f-be928fc4e478.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing Deposit page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a Screenshot of the Withdraw Page (this potentially can be the same page with different views)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208988247-b449a2cf-9ad9-49ca-aded-c26423ca8145.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screen shot showing withdraw page with drop down to select account form which<br>to withdraw money from <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show validation error for negative numbers</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208988505-31f692c0-ac0b-4797-81bb-036c9aeb233c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screen shot showing validation error for negative numbers on withdraw page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Show validation error for withdrawing more than the account contains</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208988826-9d9fab15-1156-4f40-8c8b-2ff96051ff39.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screen shot showing validation error withdrawing more than the account contains<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Show a success message for deposit and withdraw (2 screenshots)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208989172-4b426064-3eb1-4851-8db9-096d48b2a200.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot Shows deposit success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208989340-64537bd6-aa4a-4f59-92d0-2780381bd340.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot Shows withdraw success message <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Show a screenshot of the transaction pairs in the DB for the above tests</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208990023-9219fadc-192d-4b90-8fe4-3538d499ef5b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Transaction pairs for deposit and withdrawal look at transactions with ids 17 and<br>18 respectively<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly explain how transactions work</td></tr>
<tr><td> <em>Response:</em> <p>For deposit/withdraw operation two are executed first query update the balance in accounts<br>table and the second query makes the new entry in transactions table. For<br>deposit/withdraw the src and dest&nbsp;<div>are same which the account id of that account.<br>For deposit the diff value is inserted with positive sign while for withdraw<br>diff value is inserted with negative sign.&nbsp;&nbsp;</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/omkarhadawale/IS-601-007/pull/8">https://github.com/omkarhadawale/IS-601-007/pull/8</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-oh45-prod-final.herokuapp.com">https://is601-oh45-prod-final.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>1)I learned passing of data from different page like via arguments or using<br>session data.<div>2)I learned Using WTF forms adding validations and backed validation for input<br>fields.</div><div>3) Learned to implement Sql queries on a problem statement.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-oh45-prod-final.herokuapp.com">https://is601-oh45-prod-final.herokuapp.com</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-2-bank-project/grade/oh45" target="_blank">Grading</a></td></tr></table>