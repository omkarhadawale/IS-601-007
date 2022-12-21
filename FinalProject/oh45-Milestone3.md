<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Bank Project</td></tr>
<tr><td> <em>Student: </em> Omkar Karbhari Hadawale (oh45)</td></tr>
<tr><td> <em>Generated: </em> 12/21/2022 6:10:12 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-3-bank-project/grade/oh45" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> User will be able to transfer between their accounts </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of transfer page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/209004659-6696c5d9-7819-4dee-a0ea-0902f1875106.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of transfer page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot showing dropdown values</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/209004782-f9fd2e2e-566f-4541-a60c-c0c37c70a390.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing account list in the dropdown.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot showing user can't transfer more funds than they have</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/209005027-abd34849-c907-4a9f-81b2-c71a37068c34.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing user can&#39;t transfer more funds than they have<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot showing user can't transfer to the same account</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/209005245-ee24289a-b0e0-44d9-930e-6943f8483dbf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing user can&#39;t transfer to the same account<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/209005780-f67be215-45fe-4d1d-a103-0ef554e4c2e8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code snippet that prevents transfer to the same account on the server-side<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshot showing you can't transfer an negative balance</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/209006006-4bea20d9-18cf-45d6-9401-39f3fe4fb1d9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing you can&#39;t transfer an negative balance<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/209006306-758c2979-cdf2-40ac-bf4e-d7f8b54f4a5a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added validation in WTF forms in the form class.(No need to check after<br>weather the amount is negative as negative numbers will not be accepted and<br>submitted by the form itself in the front end)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshot of the generated transaction history from the db</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/209007619-f047fded-4968-40c4-99e5-b4617cc96f06.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Transaction generated for transfer of 100 between account 000000000000 to 000000000001 (Look at<br>transaction with id 22)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a screenshot of the Accounts table showing both affected accounts</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/209012443-6749b96e-fe2f-41df-b52d-039619cf9e98.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing balance of accounts 000000000000 and 000000000001 after transfer<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Briefly explain the code process/flow of a transfer including how the accounts are fetched for the dropdowns</td></tr>
<tr><td> <em>Response:</em> <p>1)A select query fetches all accounts of the current logged in user(user_id is<br>fetched from session data).The accounts fetched by the select query is passed as<br>list to jinja template of transfermoney page where the list is iterated each<br>iteration creating dropdown option.<div>2)One select query for each source account and destination account<br>respectively fetches the respective balances. If the source balance is less than amount<br>to transfer or while transferring to non existing account/ same account appropriate error<br>message is shown to the user.</div><div>3)One update query reduces amount from source account<br>balance and other update query adds amount to balance of destination account balance.<br>After both queries are successful a new record is inserted in the transactions<br>table adding source and destination account no in details&nbsp; and amount transfer including<br>other details.</div><div><br></div><div><b><font size="5">Important</font></b></div><div><b><font size="4">The below link requires a user to be logged in<br>to access it create a account here(</font></b><font size="4"><b><a href="https://is601-oh45-prod-final.herokuapp.com/register">https://is601-oh45-prod-final.herokuapp.com/register</a></b></font><b><font size="4">) and then login here(</font></b>&lt;font<br>size=&quot;4&quot;&gt;<b><a href="https://is601-oh45-prod-final.herokuapp.com/login">https://is601-oh45-prod-final.herokuapp.com/login</a></b></font><b><font size="4">)</font></b></div><div>&nbsp; &nbsp;&nbsp;</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 9: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/omkarhadawale/IS-601-007/pull/8">https://github.com/omkarhadawale/IS-601-007/pull/8</a> </td></tr>
<tr><td> <em>Sub-Task 10: </em> Add link to transfer page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-oh45-prod-final.herokuapp.com/transferMoney">https://is601-oh45-prod-final.herokuapp.com/transferMoney</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Transaction History Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of transaction history page showing the new transfer transaction</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/209008132-012ecc5f-e80a-4b6f-8f79-c218e9239b5e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing transactions page of account 000000000000 (Look at highlighted record with id<br>22)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/209008980-e1800b83-9e71-4974-8bdb-cff2f8e19298.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing transactions page of account 000000000001 (Look at highlighted record with id<br>22)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots demonstrating the filters and pagination</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/208993793-b01be97d-9eae-49af-992f-4f38d8dd8d16.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Haven&#39;t included them<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how the filters/pagination work</td></tr>
<tr><td> <em>Response:</em> <p>Haven&#39;t included them<div><span style="font-size: 13px;">Highlight things such as how the page gets passed/used</span><br></div><div>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;Highlight how the filters/sorting is applied with pagination</span><span style="font-size: 13px;"><br></span></div><div><span style="font-size: 13px;"><br></span></div><div><div><b>&lt;font<br>size=&quot;5&quot;&gt;Important</font></b></div><div><b><font size="4">The below link requires a user to be logged in to access<br>it create a account here(</font></b><font size="4"><b><a href="https://is601-oh45-prod-final.herokuapp.com/register">https://is601-oh45-prod-final.herokuapp.com/register</a></b></font><b><font size="4">) and then login here(</font></b><font size="4"><b><a href="https://is601-oh45-prod-final.herokuapp.com/login">https://is601-oh45-prod-final.herokuapp.com/login</a></b></font><b><font size="4">)</font></b></div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/omkarhadawale/IS-601-007/pull/8">https://github.com/omkarhadawale/IS-601-007/pull/8</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add link to Transaction History page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-oh45-prod-final.herokuapp.com/listAccountTransactions">https://is601-oh45-prod-final.herokuapp.com/listAccountTransactions</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User's profile First name and Last name </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the user's profile with the new fields</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/209013465-dc65a9d4-a584-4a2d-8155-515609657098.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> User&#39;s profile where user can update their profile(change username, email, password) Important<br>The below link requires a user to be logged in to access it<br>create a account here(<a href="https://is601-oh45-prod-final.herokuapp.com/register">https://is601-oh45-prod-final.herokuapp.com/register</a>) and then login here(<a href="https://is601-oh45-prod-final.herokuapp.com/login">https://is601-oh45-prod-final.herokuapp.com/login</a>)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/omkarhadawale/IS-601-007/pull/8">https://github.com/omkarhadawale/IS-601-007/pull/8</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Add link to profile page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-oh45-prod-final.herokuapp.com/landing-page">https://is601-oh45-prod-final.herokuapp.com/landing-page</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> User will be able to transfer funds to another user </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the external transfer page with filled in data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/209004659-6696c5d9-7819-4dee-a0ea-0902f1875106.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of transfer page (I have made single page for internal as well<br>as external transfer.)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot showing user can't send more than they have</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/209015416-7ead6ce3-db77-4fd1-93fc-995abad4ac31.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing user can&#39;t send more than they have error message on UI<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/209015933-8464ecf8-062e-485f-a9d3-6234e756cf36.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing back end code of user can&#39;t send more than they have<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot showing they can't send a negative amount</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/209006006-4bea20d9-18cf-45d6-9401-39f3fe4fb1d9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing you can&#39;t transfer an negative balance<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/209006306-758c2979-cdf2-40ac-bf4e-d7f8b54f4a5a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added validation in WTF forms in the form class.(No need to check after<br>weather the amount is negative as negative numbers will not be accepted and<br>submitted by the form itself in the front end)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot(s) showing message if a user doesn't exist and/or a destination account wasn't found</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/209016778-e013f966-b8b1-4c1d-ae86-5f97e1364b6d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing message destination account wasn&#39;t found<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/209017019-db4891c0-319c-45e1-8f3a-275ca6d62185.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing code snippet that prevents transfer to non existing account <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshot of the transactions table showing the recorded transfer</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/209017664-0339c651-e226-4b5c-990f-6e2efcf8bb34.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Transaction generated for transfer of 100 between account 000000000001 to 000000000095 (Look at<br>transaction with id 23)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshot(s) showing the updated account balances</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/209018086-1176a43b-2c0c-46eb-9cf3-973be6a91475.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing balance of accounts 000000000001 and 000000000095 after transfer<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly explain the process of looking up the target user's account and the validation logic</td></tr>
<tr><td> <em>Response:</em> <p>The select query is ran searching for destination account entered by user. If<br>the account is found transfer is made and if the select query returns<br>nothing the proper error message is shown.<div><br></div><div><div><b><font size="5">Important</font></b></div><div><b><font size="4">The below link requires a<br>user to be logged in to access it create a account here(</font></b><font size="4"><b><a href="https://is601-oh45-prod-final.herokuapp.com/register">https://is601-oh45-prod-final.herokuapp.com/register</a></b></font><b>&lt;font<br>size=&quot;4&quot;&gt;) and then login here(</font></b><font size="4"><b><a href="https://is601-oh45-prod-final.herokuapp.com/login">https://is601-oh45-prod-final.herokuapp.com/login</a></b></font><b><font size="4">)</font></b></div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/omkarhadawale/IS-601-007/pull/8">https://github.com/omkarhadawale/IS-601-007/pull/8</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add link to external transfer page from heroku</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-oh45-prod-final.herokuapp.com/transferMoney">https://is601-oh45-prod-final.herokuapp.com/transferMoney</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>1)I learned passing of data from different page like via arguments or using<br>session data.<div>2)I learned Using WTF forms adding validations and backed validation for input<br>fields.</div><div>3) Learned to implement Sql queries on a problem statement.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-3-bank-project/grade/oh45" target="_blank">Grading</a></td></tr></table>