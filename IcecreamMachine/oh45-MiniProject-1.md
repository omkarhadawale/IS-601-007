<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - IceCream</td></tr>
<tr><td> <em>Student: </em> Omkar Karbhari Hadawale (oh45)</td></tr>
<tr><td> <em>Generated: </em> 10/24/2022 1:18:53 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-1-icecream/grade/oh45" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216">https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder IcecreamMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/197444420-7f4823b2-3547-45d9-982e-f2a1468e82f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This function calculates cost of current ice cream by interating over in inprogress_icecream<br>list and addind up cost element in each object in the list<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/197444911-ce4d8bc6-b2e8-4919-b274-fe1417ae9aa6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>This function calculates cost of current ice cream by iterating over in inprogress_icecream<br>list and adding up cost element in each object in the list.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/197448422-6f5dbfb2-a615-4c2e-a60a-5b9d6a68c2e9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Container stage exception handling code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/197448512-de52a566-ed43-4d21-8df7-0097c17dfef5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flavor stage exception handling code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/197448610-48005285-5090-4aae-a46c-98226d143dd4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Topping stage exception handling code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/197448661-72a2ca7c-b14b-4aa8-8114-e4b17bad0007.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Payment stage exception handling code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/197448947-6284d57a-a4c4-4493-bd10-33a50174f530.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Out of stock exceptions handled output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/197449146-ab88027a-965d-44aa-a99f-384ccc95a781.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>InvalidChoiceException handled Output:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/197449665-540239aa-6196-4d21-9341-1cd8a2e83b6f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ExceededRemainingChoicesException handled Output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/197450447-0d600cdf-8b4b-4886-8517-69b9202fee85.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>InvalidPaymentException handled Output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <div style="text-align: justify;">&nbsp;<b><u>1)InvalidChoiceException:</u></b> The InvalidChoiceException is handled by try except block. When the<br>exception is thrown the user is given appropriate message and the run() is<br>called again to ask user for another input.</div><div style="text-align: justify;"><b><u>2)NeedsCleaningException:</u></b>This exception is handled<br>by the "except NeedsCleaningException:" block. When the NeedsCleaningException is thrown the user is<br>prompted that the machine is</div><div style="text-align: justify;">&nbsp; cleaned and the clean_machine() is called.<br>Their after the run() is called recursively to ask user to make the<br>choice again.&nbsp; &nbsp;&nbsp;</div><div style="text-align: justify;"><u><b>3)ExceededRemainingChoicesException:</b></u>This exception is handled by the "except ExceededRemainingChoicesException:"&nbsp; block.When<br>the exception is thrown the user is prompted that you have exceeded the<br>maximum limit to select the item and the user is directed to the<br>next stage by setting the currently_selecting variable to next stage&nbsp; and calling run()<br>recursively.</div><div style="text-align: justify;"><b><u>4)OutOfStockException</u></b>: The out of stock exception is handled by try except<br>block. when the exception is thrown the user is given prompted to select<br>from available choices.</div><div style="text-align: justify;"><div><b><u>5)InvalidPaymentException:</u></b> The InvalidChoiceException is handled by try except block.<br>When the exception is thrown the user is to ask user to enter<br>exact amount to complete the payment and the run() is called again recursively<br>till the user enters exact value.</div></div><div style="text-align: justify;"><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/197445662-945fbbab-6d02-45d1-ad22-800066ae0a34.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/197445706-9cb91f0a-3949-4ce7-a6ab-65733f62b8b1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test2<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/197445741-264ff555-0c16-44aa-a730-51c0a9b4c438.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/197445763-c085382c-bfa2-4fd5-bddb-e49552a13cee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/197445790-8321859f-a65c-4997-b90a-6a699d364a73.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/197445824-06ff8ef7-92ba-4fcc-b358-305cf713d6a8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test6<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/197445871-fb011aeb-ad90-42b1-bd27-47771cf1d91b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test7 and Test8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/197445918-9a8381bd-d6f6-4349-afe0-d21e650f3abd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <div><b><u>Test-1:</u></b></div><div style="text-align: left;">&nbsp; &nbsp; Until the container is not picked we cannot select<br>flavour because the currently_selecting will still have</div><div style="text-align: left;">&nbsp; &nbsp; container as its<br>stage.Thus the pick flavour method will raise invalid choice exception even we make<br>right</div><div style="text-align: left;">&nbsp; &nbsp; choice as the other condition evalutes to false,where it<br>checks weather self.currently_selecting == STAGE.Flavor</div><div style="text-align: left;">&nbsp; &nbsp; and same for the toppings.</div><div<br>style="text-align: left;"><div><b><u>Test-2:</u></b></div><div style="text-align: left;">&nbsp;The test case verifies that user should not be able<br>to select the flavour if it's not in stock.<br></div><div style="text-align: left;">&nbsp;The OutOfStockException is<br>catched in the test case which is the indicator that when flavour not<br>in stock this exception is raised.Further in finally block we check weather the<br>lenght of inprogress icecream list&nbsp;</div><div style="text-align: left;">&nbsp; to verify that the flavour is<br>not added.</div><div style="text-align: left;"><div><b><u>Test-3:</u></b></div><div>&nbsp; &nbsp; The test case verifies that user should not<br>be able to select the topping if it's not in stock.</div><div>&nbsp; &nbsp; The<br>OutOfStockException is catched in the test case which is the indicator that when<br>topping not in</div><div>&nbsp; &nbsp; stock this exception is raised.Further in finally block we<br>check weather the lenght of inprogress icecream list&nbsp;</div><div>&nbsp; &nbsp; to verify that the<br>topping is not added.&nbsp;&nbsp;</div><div><div><b><u>Test-4:</u></b></div><div>&nbsp; &nbsp; The test case verifies the user should be<br>able to add max 3 scoops by setting remaining_scoops to zero and then<br>checking&nbsp;</div><div>&nbsp; &nbsp; weather the ExceededRemainingChoicesException is thrown or not.Further in finally block we<br>check weather the lenght of inprogress icecream list&nbsp;</div><div>&nbsp; &nbsp; to verify that the<br>flavour is not added.</div></div><div><div><b><u>Test-5:</u></b>&nbsp;</div><div>&nbsp; &nbsp; The test case verifies the user should be<br>able to add max 3 toppings by setting remaining_toppings to zero and then<br>checking&nbsp;</div><div>&nbsp; &nbsp; weather the ExceededRemainingChoicesException is thrown or not. Further in finally block<br>we check weather the lenght of inprogress icecream list&nbsp;</div><div>&nbsp; &nbsp; to verify that<br>the topping is not added.</div></div><div><div><b><u>Test-6:</u></b></div><div>&nbsp; &nbsp; The the test case buys a ice<br>cream with random combination of container, flavor and topping&nbsp;</div><div>&nbsp; &nbsp; and then comparing<br>the expected price with the actual price calculated by calculate_cost() method</div></div><div><div><b><u>Test-7:</u></b></div><div>&nbsp; &nbsp; The<br>test case buys 2 ice creams and then compares the expected total scales<br>price with&nbsp;</div><div>&nbsp; &nbsp; the actual total scales set by handle_pay method.</div></div><div><div><b><u>Test-8:</u></b></div><div>&nbsp; &nbsp; The<br>test case buys 2 ice creams and checks weather the total_icecream count is<br>2 or not.</div></div></div></div><div style="text-align: left;"><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/omkarhadawale/IS-601-007/pull/3">https://github.com/omkarhadawale/IS-601-007/pull/3</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>No issues.<div>Learned to handle exceptions and writing test cases in pytest. Have to<br>make some code changes while writing the test cases to meet the requirements.<br>Had a fun learning experience.&nbsp;</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/43115458/197452928-812a3533-d521-455d-b5c6-b572bc2180f6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Three different icecreams with different containers, flavors and toppings shown in above image<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-1-icecream/grade/oh45" target="_blank">Grading</a></td></tr></table>