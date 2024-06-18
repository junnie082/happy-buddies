# Happy Buddies



https://github.com/junnie082/happy-buddies/assets/88719152/6c632ba1-f597-489c-b51b-2b0c2c6bde6a



### Why?
In 2022, I used to be a training manger in Scuba Diving club in my university. 
As a training manager, I had to investigate all the possible dates each student could go for training and make groups each date every semester.  
I thought it would be great if some kind of computer program could do this bothersome work for the next training mangers. 




## Algorithm
When we go for scuba diving, everybody should have at least one buddy for safety. We usually pair 2 people per buddy, and we have some rules for this. 

#### Rule 1. 
New students (who had been trained in the club for 2 or less semesters) must always be paired up with old students (been trained in the club for more than 2 semesters). If there is no old student left in that day for a new student to be paired, the new student will not be added to that day. 

#### Rule 2. 
If there is no other new students left, old students will be paired up following the rule that the gap between two semesters from two students should be always the greatest. 

#### Rule 3. 
Each student should go for training for 3 times each semester. 


## Data

Information of the members (current memebers in Seoul Tech Scuba Team) are saved in the program.
Names and the number of semesters they've been trained.




## Software




### Link

[Click here to visit website!](https://junnie082.github.io/happy-buddies/)



### Form Table

<kbd>
<img width="400" alt="Form Table" src="https://github.com/junnie082/happy-buddies/assets/88719152/3b2c0a47-1198-4207-aee3-828c19b60d03">
</kbd>

- You must select the date first.
- Press all the buttons of the names who said are able to go for training that day.
- If you press the button at first, the color of the button turns into blue.
- If you press the button again, the color turns into white.
- "Blue" button means the name is selected, where "White" button means the name is not selected.









## Input List

<kbd>
<img width="400" alt="Input List" src="https://github.com/junnie082/happy-buddies/assets/88719152/e49d596f-65c1-4c99-84b9-8deb294f8063">
</kbd>

- You can add the members in the input list by pressing the buttons of names (white to blue).
- When you press the blue button and make it white, the name of the button is removed from the input list.
- You can add the date by just selecting another date, and the other date section will be appended to the input list.









## Result

<kbd>
<img width="400" alt="Result" src="https://github.com/junnie082/happy-buddies/assets/88719152/f9b2eb64-6143-4232-bc17-4e091feb451f">
</kbd>

- If you press "Done" button, the result will come out.
- Every member in each date will be paired up and be shown under the "Result" box.
- The format follows "buddy1(semester) - buddy2(semester)".
- Every group will be updated as dates increase.
- If you press "Reset" button, dates, input list and result box will be reset again. All the buttons will go white and all the boxes in counted traing days will go red.









## Counted Training Days

<kbd>
<img width="400" alt="Result" src="https://github.com/junnie082/happy-buddies/assets/88719152/424aa26c-a518-4961-b095-0de016336af4">
</kbd>    

- Training manager can check how many days each member is participating for the training.
- If the member is going for the training for 0 day in this semester, the color of the box will be red.
- If he/she is going for 1 or 2 days, the color will be yellow.
- If he/she is going for 3 days, the color will be blue.




## Branches

- develop: all the codes added from other branches before merging to `main`
- develop-logic-python: origin codes to develop algorithm for the program
- develop-addMembers-inputfield: you can add members here by typing the names of members instead of clicking the provided buttons
- develp-to_use_with_file: you can add members by adding a text file, all dates and members written following the format
- develop-ui: develop UI (design, styling, etc...)
- develop-readme: modify readme.md


## FAQ 

You can visit [Issues](https://github.com/junnie082/happy-buddies/issues) to report any errors or any better ideas (UI, algorithms, new ides, etc...) for the program. 
Press `New Issue` button to do so.

  

# Development


### Developer
Hyojeong Jun, 37th member of Seoul Tech Scuba Club (Training Manger in 2022)



https://github.com/junnie082/happy-buddies/assets/88719152/29c1944a-d5de-4c17-afac-eca896a60086





### Tools

- Logic: Python
- Front End: javascript, html, css
- Web Server: Github Pages

### Period
2023.10.31. ~ 2023.12.04.

