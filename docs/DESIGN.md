# Design

## Game title: Richmond Chainsaw Massacre
Be prepared to actually multitask. Prepare your legs and brain.

*Good story! A little scary for me... :P*

## Story So Far...
Years ago, three senior computer science students were taking the class CMSC 323 Programming Languages, and they all were struggling the whole semester. They were very close to graduate and were very worried if they could pass this class or not so they could get a job after their last semesters. All of them had already got into a computer science job, which would start after graduating from college. In the last two weeks, to pass this class, these 3 students realized they all would have to take at least a 110 out of 100 in their final project, which was in group, to graduate. Unfortunately, they failed this class because it was impossible to reach this grade. This made them lose their prospective job and then the only job they got was in lumber and now they are hunting, with a chainsaw, every classmate that passed the class CMSC 323 Programming Languages. You are one of the few people who passed this class. Your goal is to run around the campus. You will be participating in the SpiderDash 5K, the official University of Richmond's annual running event. If they successfully find you, you are killed and have to restart the game until you actually run through the campus. These 3 students will be around the campus and you will have to reach the end of the run without getting hunted.

## Objective of the game!
Participate in the SpiderDash 5K event, and successfully run the entire event without getting caught by the three computer science enemies.

**

## The three characters...
1. **The Roboticist →** creates clones that will make the enemies confused. It can help you to see which enemy will be in certain spots.
2. **The Scientist →** this student is a Computer Science and Biology double major. When he graduated, he started studying snakes. During one of his studies, the Python snake bit him and they became very close friends. This snake was also created in a laboratory by programming language and is very clever at coding and can help you solve Python problems. It helps you to solve problems against the enemy “The Python Scarecrow". *This gets a ROFL from me!*
3. **The Mathematician →** gives you hints of which way might be the safest one, based on combinatorics and probability. Helps you to solve problems against the enemy “The Brave Calculator”.

*Enemies are thought out well. Remember to order them from the easy/common enement to the unique boss.*

## The three (or two so far) enemies...
1. **The Brave Calculator →** He definitely loved math so much but now, since he just uses his mind to lumber, he hates math. Therefore, he gives you 7 math problems; if you get 4+ correct, you win! Otherwise, x = fail.
2. **The Python Scarecrow →** This was a student who declared his Computer Science major in freshman year while taking CMSC 150, and after taking CMSC 301 Computer Organization, he gave up on computer science and just wanted his degree as soon as possible. To beat him, he gives you 5 Python debugging problems. If you get 3+ correct, you win! Else: print(”You failed. Restart the game").
3. **The … →** .


*** The SpiderDash 5K will have checkpoints where you can restart from a certain point.

*** If you are the mathematician, you will receive hints on how to solve a problem if you fight the math enemy

*** Create different levels of difficulty. Easy, medium, hard. Easy (sum and subtraction problems); medium (equation problems); hard (calculus problems)

*** During the run you can find the other characters and they will turn into your allies!

Here are the flowcharts explaining each of the functions to select the character, enemy, and checking level.
![Alt text](<generate_character function flowchart.png>)
![Alt text](<generate_enemy function flowchart.png>)
![Alt text](<check_level function flowchart.png>)

## Introducing the battle functions and subfunctions diagrams!
Main battle function:
![Alt text](<def battle main function.drawio.png>)
Battle questions subfunction:
![Alt text](<def battle questions.png>)
Battle combat subfunction:
![Alt text](<def battle combat.drawio.png>)

## How works the battle functions and subfunctions?
It is very simple. Every enemy have their own questions (subfunction) in which you have to answer. If you meet the requirements and win via brain intelligence (answering the questions), you do not need to do the combat and risk your life. If you do not get correct most of the questions, you will be directed to the combat subfunction, in which you will actually have to attack and defend! Each player (character and enemy) will have one turn to decide your action. You can either attack or defend.

### Keys to press while playing...
Press W to move up 1 space;

Press A to move left 1 space;

Press S to move down 1 space;

Press D to move right 1 space;

Press E to attack your enemy;

Press Q to defend from the enemy's attack.

## How does the navigate function works?
![Alt text](<Navigate function.drawio.png>)
The game grid is 5x5 and is made by a list. Depending on the pressed key, the position of the character will move! If the player stops in an empty space on the grid, the player can make a move again! If stops in the 'b' spot, it is going to run the battle function against the Brave Calculator! If stopped in 'p', battle function against Python Scarecrow! If stopped in 'w', battle function against the Website Destroyer, which is the boss!

## How does the full game loop works?
![Alt text](<Full game loop deliverable 3.drawio.png>)
The game loop is based on the character and boss health. While it is greater than 0, it is gonna be running the loop. At each iteration, it will loop the navigate function and check the character health and the boss health all the time. If either the boss or the character gets a health less or equal than 0, then the loop stops.