import arcade
import math
import character
import random
from character import Character, Enemy

def brave_calculator_questions(character_stats: Character, num_questions):
    """
    This is the function where contains all the questions made from the Brave Calculator. This is where will return the value True or False based on the percentage of correct answers the user answered.
    """
    correct_answers = 0
    if num_questions == 1:
        print(f"Hello, {character_stats._user_name}! I am the Brave Calculator. Are you prepared to solve Math problems? Well, I do not care. You better solve them or I will fight with you!")
        print(f"Let's start with an easy problem... not too hard to do not scare you!\n What is the value of 5+6x3?")
        print(f"A) 33\nB) 48\nC) 23")
        user_answer = input('Please type your answer: ').upper()
        num_questions += 1
        while user_answer != 'A' and user_answer != 'B' and user_answer != 'C':
            user_answer = input('Please rewrite your answer in the correct format: ').upper()
        if user_answer == 'A':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is C) 23.")
        elif user_answer == 'B':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is C) 23.")
        elif user_answer == 'C':
            correct_answers += 1
            print(f"Correct answer, {character_stats._user_name}!!! The correct answer is C) 23, as you said. Now, you have a total of {correct_answers} correct answers!")
    if num_questions == 2:
        print(f"Ready for question 2? Well, ready or not... Here we go!\n If a rectangle has a length of 14 units and a width 8 units, what is its perimeter?")
        print(f"A) 44\nB) 22\nC) 112")
        num_questions += 1
        user_answer = input('Please type your answer: ').upper()
        while user_answer != 'A' and user_answer != 'B' and user_answer != 'C':
            user_answer = input('Please rewrite your answer in the correct format: ').upper()
        if user_answer == 'A':
            correct_answers += 1
            print(f"Correct answer, {character_stats._user_name}!!! The correct answer is A) 44, as you said. Now, you have a total of {correct_answers} correct answers!")
        elif user_answer == 'B':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is A) 44.")
        elif user_answer == 'C':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is A) 44.")
    if num_questions == 3:
        num_questions += 1
        print(f"Now question 3! A motorcycle travels at an average speed of 90 miles per hour. How long will it take to travel 315 miles?")
        print(f"A) 4 hours\nB) 3.5 hours\nC) 10 hours")
        user_answer = input('Please type your answer: ').upper()
        while user_answer != 'A' and user_answer != 'B' and user_answer != 'C':
            user_answer = input('Please rewrite your answer in the correct format: ').upper()
        if user_answer == 'A':
            correct_answers += 1
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is B) 3.5 hours.")
        elif user_answer == 'B':
            correct_answers += 1
            print(f"Correct answer, {character_stats._user_name}!!! The correct answer is B) 3.5 hours, as you said. Now, you have a total of {correct_answers} correct answers!")
        elif user_answer == 'C':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is B) 3.5 hours.")
    if num_questions == 4:
        num_questions += 1
        print(f"You are at the question 4 now! A store item costs $80, and the store is offering 25% off. How much does the item cost with the applied discount?")
        print(f"A) $40\nB) $20\nC) $60")
        user_answer = input('Please type your answer: ').upper()
        while user_answer != 'A' and user_answer != 'B' and user_answer != 'C':
            user_answer = input('Please rewrite your answer in the correct format: ').upper()
        if user_answer == 'A':
            correct_answers += 1
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is C) $60.")
        elif user_answer == 'B':
            correct_answers += 1
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is C) $60.")
        elif user_answer == 'C':
            correct_answers += 1
            print(f"Correct answer, {character_stats._user_name}!!! The correct answer is C) $60, as you said. Now, you have a total of {correct_answers} correct answers!")
    if num_questions == 5:
        print(f"Are you ready for the question 5, {character_stats._user_name}? Let's go! Solve for x if 5 + 2x = 15.")
        print(f"A) X=4\nB) X=2\nC) X=5")
        user_answer = input('Please type your answer: ').upper()
        while user_answer != 'A' and user_answer != 'B' and user_answer != 'C':
            user_answer = input('Please rewrite your answer in the correct format: ').upper()
        num_questions += 1
        if user_answer == 'A':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is C) X=5.")
        elif user_answer == 'B':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is C) X=5.")
        elif user_answer == 'C':
            correct_answers += 1
            print(f"Correct answer, {character_stats._user_name}!!! The correct answer is C) X=5, as you said. Now, you have a total of {correct_answers} correct answers!")
    if num_questions == 6:
        num_questions += 1
        print(f"Almost the last question, {character_stats._user_name}! Let's go to the 6th problem. A cylindrical tank with a radius of 5 feet and a height of 12 feet is filled with water to a depth of 10 feet. What is the volume of water left to completely fill the tank?")
        print(f"A) 50π cubic feet\nB) 250π cubic feet\nC) 300π cubic feet")
        user_answer = input('Please type your answer: ').upper()
        while user_answer != 'A' and user_answer != 'B' and user_answer != 'C':
            user_answer = input('Please rewrite your answer in the correct format: ').upper()
        if user_answer == 'A':
            correct_answers += 1
            print(f"Correct answer, {character_stats._user_name}!!! The correct answer is A) 50π cubic feet, as you said. Now, you have a total of {correct_answers} correct answers!")
        elif user_answer == 'B':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is A) 50π cubic feet.")
        elif user_answer == 'C':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is A) 50π cubic feet.")
    if num_questions == 7:
        num_questions += 1
        print(f"Last question! Are you ready? I hope you are! Three friends, Mark, Kim, and John together have $300. If Mark gives $30 to Kim, Kim gives $20 to John, and John gives $10 to Mark, how much money do they have?")
        print(f"A) $240\nB) $300\nC) $360")
        user_answer = input('Please type your answer: ').upper()
        while user_answer != 'A' and user_answer != 'B' and user_answer != 'C':
            user_answer = input('Please rewrite your answer in the correct format: ').upper()
        if user_answer == 'A':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is B) $300.")
        elif user_answer == 'B':
            correct_answers += 1
            print(f"Correct answer, {character_stats._user_name}!!! The correct answer is B) $300, as you said. Now, you have a total of {correct_answers} correct answers!")
        elif user_answer == 'C':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is B) $300.")
    if num_questions > 7:
        return correct_answers/num_questions

def python_scarecrow_questions(character_stats: Character, num_questions):
    """
    This is the function where contains all the questions made from the Python Scarecrow. This is where will return the value True or False based on the percentage of correct answers the user answered.
    """
    print(f"Hey, {character_stats._user_name}! I am the Python Scarecrow. Are you willing to solve Python problems? Willing or not, you will have to! Otherwise... I will try to kill you during our combat!") # REWRITE THIS!
    num_questions = 1
    correct_answers = 0
    if num_questions == 1:
        num_questions += 1
        print(f"Question 1: what is a SyntaxError?")
        print(f"A) It is an error when you indent incorrectly\nB) It is an error that occurs when the language of Python is violated\nC) It is an error that occurs when a function is called with the wrong number of arguments")
        user_answer = input('Please type your answer: ').upper()
        while user_answer != 'A' and user_answer != 'B' and user_answer != 'C':
            user_answer = input('Please rewrite your answer in the correct format: ').upper()
        if user_answer == 'A':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is B) It is an error that occurs when the language of Python is violated.")
        elif user_answer == 'B':
            correct_answers += 1
            print(f"Correct answer, {character_stats._user_name}!!! The correct answer is B) It is an error that occurs when the language of Python is violated, as you said. Now, you have a total of {correct_answers} correct answers!")
        elif user_answer == 'C':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is B) It is an error that occurs when the language of Python is violated.")
    if num_questions == 2:
        num_questions += 1
        print(f"Let's go to question 2! Assume that the variable num_cars exist. Does the print function print('Dogs: ' num_dogs) has any errors?")
        print(f"A) Yes, it is missing a comma\nB) Yes, it has an additional space after 'Dogs:'\nC) No, there are no errors")
        user_answer = input('Please type your answer: ').upper()
        while user_answer != 'A' and user_answer != 'B' and user_answer != 'C':
            user_answer = input('Please rewrite your answer in the correct format: ').upper()
        if user_answer == 'A':
            correct_answers += 1
            print(f"Correct answer, {character_stats._user_name}!!! The correct answer is A) Yes, it is missing a comma, as you said. Now, you have a total of {correct_answers} correct answers!")
        elif user_answer == 'B':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is A) Yes, it is missing a comma.")
        elif user_answer == 'C':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is A) Yes, it is missing a comma.")
    if num_questions == 3:
        num_questions += 1
        print(f"Time for question 3! Which type of error does the following line of code represent? int('Andrey')")
        print(f"A) TypeError\nB) SyntaxError\nC) ValueError")
        user_answer = input('Please type your answer: ').upper()
        while user_answer != 'A' and user_answer != 'B' and user_answer != 'C':
            user_answer = input('Please rewrite your answer in the correct format: ').upper()
        if user_answer == 'A':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is C) ValueError.")
        elif user_answer == 'B':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is C) ValueError.")
        elif user_answer == 'C':
            correct_answers += 1
            print(f"Correct answer, {character_stats._user_name}!!! The correct answer is C) ValueError, as you said. Now, you have a total of {correct_answers} correct answers!")
    if num_questions == 4:
        num_questions += 1
        print(f"Almost the last question! Let's go for question 4: what does the % symbol represents in Python?")
        print(f"A) It means percentage\nB) It means floor-division, returning the integer part of the division result\nC) It means the modulo operator, which returns the remainder of the division of two numbers.")
        user_answer = input('Please type your answer: ').upper()
        while user_answer != 'A' and user_answer != 'B' and user_answer != 'C':
            user_answer = input('Please rewrite your answer in the correct format: ').upper()
        if user_answer == 'A':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is C) It means the modulo operator, which returns the remainder of the division of two numbers.")
        elif user_answer == 'B':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is C) It means the modulo operator, which returns the remainder of the division of two numbers.")
        elif user_answer == 'C':
            correct_answers += 1
            print(f"Correct answer, {character_stats._user_name}!!! The correct answer is C) It means the modulo operator, which returns the remainder of the division of two numbers, as you said. Now, you have a total of {correct_answers} correct answers!")
    if num_questions == 5:
        num_questions += 1
        print(f"Last question! Are you ready? What is the correct way to modify a list by returning the last item and removing the last item from the list?")
        print(f"A) .pop()\nB) .remove()\nC) .delete(last)")
        user_answer = input('Please type your answer: ').upper()
        while user_answer != 'A' and user_answer != 'B' and user_answer != 'C':
            user_answer = input('Please rewrite your answer in the correct format: ').upper()
        if user_answer == 'A':
            correct_answers += 1
            print(f"Correct answer, {character_stats._user_name}!!! The correct answer is A) .pop(), as you said. Now, you have a total of {correct_answers} correct answers!")
        elif user_answer == 'B':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is A) .pop().")
        elif user_answer == 'C':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is A) .pop().")
    if num_questions > 5:
        return correct_answers/num_questions

def website_destroyer_questions(character_stats: Character, num_questions):
    """
    This is the function where contains all the questions made from the Website Destroyer. This is where will return the value True or False based on the percentage of correct answers the user answered.
    """
    print(f"What's up, {character_stats._user_name}! I am the Website Destroyer. Either wanting to solve logic/debugging problems or not... you will have to!")
    num_questions = 1
    correct_answers = 0
    if num_questions == 1:
        num_questions += 1
        print(f"Let's start this! What does the slicing part of this list mean? Assume that dog_names is a created list. dog_names[5:8]")
        print(f"A) Includes the items 5, 6, and 7\nB) Includes the items 6, 7, and 8\nC) Includes the items 5, 6, 7, amd 8")
        user_answer = input('Please type your answer: ').upper()
        while user_answer != 'A' and user_answer != 'B' and user_answer != 'C':
            user_answer = input('Please rewrite your answer in the correct format: ').upper()
        if user_answer == 'A':
            correct_answers += 1
            print(f"Correct answer, {character_stats._user_name}!!! The correct answer is A) Includes the items 5, 6, and 7, as you said. Now, you have a total of {correct_answers} correct answers!")
        elif user_answer == 'B':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is A) Includes the items 5, 6, and 7.")
        elif user_answer == 'C':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is A) Includes the items 5, 6, and 7.")
    if num_questions == 2:
        num_questions += 1
        print(f"Question 2! Let's go for it. Assume names is a list. What would names[-1] return?")
        print(f"A) Would return the first item on the list, but in a form of negative value\nB) Would be an Python Error\nC) Would return the last item in the list")
        user_answer = input('Please type your answer: ').upper()
        while user_answer != 'A' and user_answer != 'B' and user_answer != 'C':
            user_answer = input('Please rewrite your answer in the correct format: ').upper()
        if user_answer == 'A':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is C) Would return the last item in the list.")
        elif user_answer == 'B':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is C) Would return the last item in the list.")
        elif user_answer == 'C':
            correct_answers += 1
            print(f"Correct answer, {character_stats._user_name}!!! The correct answer is C) Would return the last item in the list, as you said. Now, you have a total of {correct_answers} correct answers!")
    if num_questions == 3:
        num_questions += 1
        print(f"I am hoping you are burning some of your brain energy to solve these problems! Assume str1 is a string. How would str1 be modified if written a line str1.upper()?")
        print(f"A) It would remove every other letter, starting from the second letter\nB) It would transform every letter in capslock\nC) This command does not exist")
        user_answer = input('Please type your answer: ').upper()
        while user_answer != 'A' and user_answer != 'B' and user_answer != 'C':
            user_answer = input('Please rewrite your answer in the correct format: ').upper()
        if user_answer == 'A':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is B) It would transform every letter in capslock.")
        elif user_answer == 'B':
            correct_answers += 1
            print(f"Correct answer, {character_stats._user_name}!!! The correct answer is B) It would transform every letter in capslock, as you said. Now, you have a total of {correct_answers} correct answers!")
        elif user_answer == 'C':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is B) It would transform every letter in capslock.")
    if num_questions == 4:
        num_questions += 1
        print(f"I am liking it! Let's keep with these types of question. You got only two more questions left! What does str1.count('hey') mean?)")
        print(f"A) It means it will count how many letters 'hey' has\nB) It means it will count how many times 'hey' appears in the string\nC) This command is an error.")
        user_answer = input('Please type your answer: ').upper()
        while user_answer != 'A' and user_answer != 'B' and user_answer != 'C':
            user_answer = input('Please rewrite your answer in the correct format: ').upper()
        if user_answer == 'A':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is B) It means it will count how many times 'hey' appears in the string.")
        elif user_answer == 'B':
            correct_answers += 1
            print(f"Correct answer, {character_stats._user_name}!!! The correct answer is B) It means it will count how many times 'hey' appears in the string, as you said. Now, you have a total of {correct_answers} correct answers!")
        elif user_answer == 'C':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is B) It means it will count how many times 'hey' appears in the string.")
    if num_questions == 5:
        num_questions += 1
        print(f"Last question!!! Type the alternative which shows a TypeError.")
        print(f"A) x = 5, y = 'hello', result = x + y\nB) my_list = [1, 2, 3,], my_list[3]\nC) print('Hello World)")
        user_answer = input('Please type your answer: ').upper()
        while user_answer != 'A' and user_answer != 'B' and user_answer != 'C':
            user_answer = input('Please rewrite your answer in the correct format: ').upper()
        if user_answer == 'A':
            correct_answers += 1
            print(f"Correct answer, {character_stats._user_name}!!! The correct answer is A) x = 5, y = 'hello', result = x + y, as you said. Now, you have a total of {correct_answers} correct answers!")
        elif user_answer == 'B':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is A) x = 5, y = 'hello', result = x + y.")
        elif user_answer == 'C':
            print(f"Wrong answer, {character_stats._user_name}! The correct answer is A) x = 5, y = 'hello', result = x + y.")
    if num_questions > 5:
        return correct_answers/num_questions

def battle_questions(character_stats: Character, enemy: Enemy):
    '''
    This is the function which determines the questions asked when the character approaches the enemy.
    Each enemy have specific questions and each character have hints to solve the problems against the enemies.
    First, pick the character you have.
    Then, pick the enemy
    Each enemy will have the questions
    Respond based on 1 2 3
    If correct, questions_correct += 1
    Always num_questions += 1
    '''
    num_questions = 1
    if character_stats._chose_character == 'web developer':
        if enemy._enemy_type == 'Brave Calculator':
            result_brave_calculator = brave_calculator_questions(character_stats, num_questions)
            if result_brave_calculator > 0.5:
                return True
            else:
                return False
        elif enemy._enemy_type == 'Python Scarecrow':
            result_python_scarecrow = python_scarecrow_questions(character_stats, num_questions)
            if result_python_scarecrow > 0.5:
                return True
            else:
                return False
        elif enemy._enemy_type == 'Website Destroyer': #PRESS H FOR HINT!
            result_website_destroyer = website_destroyer_questions(character_stats, num_questions)
            if result_website_destroyer > 0.5:
                return True
            else:
                return False
    elif character_stats._chose_character == 'scientist':
        if enemy._enemy_type == 'Brave Calculator':
            result_brave_calculator = brave_calculator_questions(character_stats, num_questions)
            if result_brave_calculator > 0.5:
                return True
            else:
                return False
        elif enemy._enemy_type == 'Python Scarecrow':
            result_python_scarecrow = python_scarecrow_questions(character_stats, num_questions)
            if result_python_scarecrow > 0.5:
                return True
            else:
                return False
        elif enemy._enemy_type == 'Website Destroyer': #PRESS H FOR HINT!
            result_website_destroyer = website_destroyer_questions(character_stats, num_questions)
            if result_website_destroyer > 0.5:
                return True
            else:
                return False
    elif character_stats._chose_character == 'mathematician':
        if enemy._enemy_type == 'Brave Calculator':
            result_brave_calculator = brave_calculator_questions(character_stats, num_questions)
            if result_brave_calculator > 0.5:
                return True
            else:
                return False
        elif enemy._enemy_type == 'Python Scarecrow':
            result_python_scarecrow = python_scarecrow_questions(character_stats, num_questions)
            if result_python_scarecrow > 0.5:
                return True
            else:
                return False
        elif enemy._enemy_type == 'Website Destroyer': #PRESS H FOR HINT!
            result_website_destroyer = website_destroyer_questions(character_stats, num_questions)
            if result_website_destroyer > 0.5:
                return True
            else:
                return False


def battle_combat(character_stats: Character, enemy: Enemy):
    '''
    This is the function which will do the combat! It is based in which character the user picked and which enemy the user is playing against.
    The combat is made by turns (this means the character pick one action, the enemy pick another action, and then the function decides what is the result of the two actions)
    '''
    if character_stats._chose_character ==  'web developer':
        if enemy._enemy_type == 'Brave Calculator':
            while character_stats.health > 0 and enemy.health > 0:
                print("It's your turn! Press E to attack or Q to defend. The enemy will pick their action after you choose yours.")
                pressed_attack_or_defense = input().lower()
                while pressed_attack_or_defense != 'e' and pressed_attack_or_defense != 'q':
                    pressed_attack_or_defense = input('Unknown command. Please type your action again: ').lower()
                print("Now it's the enemy turn!")
                enemy_options = ['E', 'Q']
                enemy_random_choice = random.choice(enemy_options)
                print(f"Enemy's random choice: {enemy_random_choice}")
                if pressed_attack_or_defense == 'e' and enemy_random_choice == enemy_options[0]: #Attack from both. Both lose health and you gain XP.
                    character_stats.health -= 5 #Lose 5 of health
                    character_stats.xp += 5 #If you attack and the enemy does not defend, you win 5 of XP!
                    character_stats.level += 1
                    enemy.health -= 5 #Lose 5 of health
                    print(f"Both of you attacked! Both of you lost 5 of health.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.\n In addition to it, you won 5 XP and 1 Level! Your current XP: {character_stats.xp}\n Your current Level: {character_stats.level}.")
                elif pressed_attack_or_defense == 'e' and enemy_random_choice == enemy_options[1]: #Attack from character, defense from the enemy. No one lose health and no gain of xp!
                    print(f"You attacked and the {enemy} defended! None of you lost any health or gained XP.")
                elif pressed_attack_or_defense == 'q' and enemy_random_choice == enemy_options[0]: #Defense from the character, attack from the enemy. No one lose health and no gain of xp!
                    print(f"You defended and the {enemy} attacked! None of you lost any health or gained XP.")
                elif pressed_attack_or_defense == 'q' and enemy_random_choice == enemy_options[1]: #Defense from both! You gain health and no xp!
                    if character_stats.health <= 95:
                        character_stats.health += 5
                        print(f"Both of you defended! You gained 5 of health and 0 XP. The enemy did not lose or gained anything.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                    elif character_stats.health > 95 and character_stats.health < 100:
                        character_stats.health = 100
                        print(f"Both of you defended! Now, you have full health and did not gain any XP. The enemy did not lose or gained any stats.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                    elif character_stats.health >= 100:
                        print(f"Both of you defended! You did not gain any health because you already have the max health possible! You did not gain any xp. The enemy also did not lose or gained any stats.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                if character_stats.health > 0 and enemy.health > 0:
                    print("Let's go to the next turn!")
                else:
                    break
        elif enemy._enemy_type == 'Python Scarecrow':
            while character_stats.health > 0 or enemy.health > 0:
                print("It's your turn! Press E to attack or Q to defend. The enemy will pick their action after you choose yours.")
                pressed_attack_or_defense = input().lower()
                while pressed_attack_or_defense != 'e' and pressed_attack_or_defense != 'q':
                    pressed_attack_or_defense = input('Unknown command. Please type your action again: ').lower()
                print("Now it's the enemy turn!")
                enemy_options = ['E', 'Q']
                enemy_random_choice = random.choice(enemy_options)
                print(f"Enemy's random choice: {enemy_random_choice}")
                if pressed_attack_or_defense == 'e' and enemy_random_choice == enemy_options[0]: #Attack from both. Both lose health and you gain XP.
                    character_stats.health -= 5 #Lose 5 of health
                    character_stats.xp += 5 #If you attack and the enemy does not defend, you win 5 of XP!
                    character_stats.level += 1
                    enemy.health -= 5 #Lose 5 of health
                    print(f"Both of you attacked! Both of you lost 5 of health.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.\n In addition to it, you won 5 XP and 1 Level! Your current XP: {character_stats.xp}\n Your current Level: {character_stats.level}.")
                elif pressed_attack_or_defense == 'e' and enemy_random_choice == enemy_options[1]: #Attack from character, defense from the enemy. No one lose health and no gain of xp!
                    print(f"You attacked and the {enemy} defended! None of you lost any health or gained XP.")
                elif pressed_attack_or_defense == 'q' and enemy_random_choice == enemy_options[0]: #Defense from the character, attack from the enemy. No one lose health and no gain of xp!
                    print(f"You defended and the {enemy} attacked! None of you lost any health or gained XP.")
                elif pressed_attack_or_defense == 'q' and enemy_random_choice == enemy_options[1]: #Defense from both! You gain health and no xp!
                    if character_stats.health <= 95:
                        character_stats.health += 5
                        print(f"Both of you defended! You gained 5 of health and 0 XP. The enemy did not lose or gained anything.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                    elif character_stats.health > 95 and character_stats.health < 100:
                        character_stats.health = 100
                        print(f"Both of you defended! Now, you have full health and did not gain any XP. The enemy did not lose or gained any stats.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                    elif character_stats.health >= 100:
                        print(f"Both of you defended! You did not gain any health because you already have the max health possible! You did not gain any xp. The enemy also did not lose or gained any stats.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                if character_stats.health > 0 and enemy.health > 0:
                    print("Let's go to the next turn!")
                else:
                    break
        elif enemy._enemy_type == 'Website Destroyer':
            while character_stats.health > 0 or enemy.health > 0:
                print("It's your turn! Press E to attack or Q to defend. The enemy will pick their action after you choose yours.")
                pressed_attack_or_defense = input().lower()
                while pressed_attack_or_defense != 'e' and pressed_attack_or_defense != 'q':
                    pressed_attack_or_defense = input('Unknown command. Please type your action again: ').lower()
                print("Now it's the enemy turn!")
                enemy_options = ['E', 'Q']
                enemy_random_choice = random.choice(enemy_options)
                print(f"Enemy's random choice: {enemy_random_choice}")
                if pressed_attack_or_defense == 'e' and enemy_random_choice == enemy_options[0]: #Attack from both. Both lose health and you gain XP.
                    character_stats.health -= 5 #Lose 5 of health
                    character_stats.xp += 5 #If you attack and the enemy does not defend, you win 5 of XP!
                    character_stats.level += 1
                    enemy.health -= 5 #Lose 5 of health
                    print(f"Both of you attacked! Both of you lost 5 of health.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.\n In addition to it, you won 5 XP and 1 Level! Your current XP: {character_stats.xp}\n Your current Level: {character_stats.level}.")
                elif pressed_attack_or_defense == 'e' and enemy_random_choice == enemy_options[1]: #Attack from character, defense from the enemy. No one lose health and no gain of xp!
                    print(f"You attacked and the {enemy} defended! None of you lost any health or gained XP.")
                elif pressed_attack_or_defense == 'q' and enemy_random_choice == enemy_options[0]: #Defense from the character, attack from the enemy. No one lose health and no gain of xp!
                    print(f"You defended and the {enemy} attacked! None of you lost any health or gained XP.")
                elif pressed_attack_or_defense == 'q' and enemy_random_choice == enemy_options[1]: #Defense from both! You gain health and no xp!
                    if character_stats.health <= 95:
                        character_stats.health += 5
                        print(f"Both of you defended! You gained 5 of health and 0 XP. The enemy did not lose or gained anything.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                    elif character_stats.health > 95 and character_stats.health < 100:
                        character_stats.health = 100
                        print(f"Both of you defended! Now, you have full health and did not gain any XP. The enemy did not lose or gained any stats.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                    elif character_stats.health >= 100:
                        print(f"Both of you defended! You did not gain any health because you already have the max health possible! You did not gain any xp. The enemy also did not lose or gained any stats.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                if character_stats.health > 0 and enemy.health > 0:
                    print("Let's go to the next turn!")
                else:
                    break
    elif character_stats._chose_character == 'scientist':
        if enemy._enemy_type == 'Brave Calculator':
            while character_stats.health > 0 or enemy.health > 0:
                print("It's your turn! Press E to attack or Q to defend. The enemy will pick their action after you choose yours.")
                pressed_attack_or_defense = input().lower()
                while pressed_attack_or_defense != 'e' and pressed_attack_or_defense != 'q':
                    pressed_attack_or_defense = input('Unknown command. Please type your action again: ').lower()
                print("Now it's the enemy turn!")
                enemy_options = ['E', 'Q']
                enemy_random_choice = random.choice(enemy_options)
                print(f"Enemy's random choice: {enemy_random_choice}")
                if pressed_attack_or_defense == 'e' and enemy_random_choice == enemy_options[0]: #Attack from both. Both lose health and you gain XP.
                    character_stats.health -= 5 #Lose 5 of health
                    character_stats.xp += 5 #If you attack and the enemy does not defend, you win 5 of XP!
                    character_stats.level += 1
                    enemy.health -= 5 #Lose 5 of health
                    print(f"Both of you attacked! Both of you lost 5 of health.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.\n In addition to it, you won 5 XP and 1 Level! Your current XP: {character_stats.xp}\n Your current Level: {character_stats.level}.")
                elif pressed_attack_or_defense == 'e' and enemy_random_choice == enemy_options[1]: #Attack from character, defense from the enemy. No one lose health and no gain of xp!
                    print(f"You attacked and the {enemy} defended! None of you lost any health or gained XP.")
                elif pressed_attack_or_defense == 'q' and enemy_random_choice == enemy_options[0]: #Defense from the character, attack from the enemy. No one lose health and no gain of xp!
                    print(f"You defended and the {enemy} attacked! None of you lost any health or gained XP.")
                elif pressed_attack_or_defense == 'q' and enemy_random_choice == enemy_options[1]: #Defense from both! You gain health and no xp!
                    if character_stats.health <= 95:
                        character_stats.health += 5
                        print(f"Both of you defended! You gained 5 of health and 0 XP. The enemy did not lose or gained anything.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                    elif character_stats.health > 95 and character_stats.health < 100:
                        character_stats.health = 100
                        print(f"Both of you defended! Now, you have full health and did not gain any XP. The enemy did not lose or gained any stats.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                    elif character_stats.health >= 100:
                        print(f"Both of you defended! You did not gain any health because you already have the max health possible! You did not gain any xp. The enemy also did not lose or gained any stats.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                if character_stats.health > 0 and enemy.health > 0:
                    print("Let's go to the next turn!")
                else:
                    break
        elif enemy._enemy_type == 'Python Scarecrow':
            while character_stats.health > 0 or enemy.health > 0:
                print("It's your turn! Press E to attack or Q to defend. The enemy will pick their action after you choose yours.")
                pressed_attack_or_defense = input().lower()
                while pressed_attack_or_defense != 'e' and pressed_attack_or_defense != 'q':
                    pressed_attack_or_defense = input('Unknown command. Please type your action again: ').lower()
                print("Now it's the enemy turn!")
                enemy_options = ['E', 'Q']
                enemy_random_choice = random.choice(enemy_options)
                print(f"Enemy's random choice: {enemy_random_choice}")
                if pressed_attack_or_defense == 'e' and enemy_random_choice == enemy_options[0]: #Attack from both. Both lose health and you gain XP.
                    character_stats.health -= 5 #Lose 5 of health
                    character_stats.xp += 5 #If you attack and the enemy does not defend, you win 5 of XP!
                    character_stats.level += 1
                    enemy.health -= 5 #Lose 5 of health
                    print(f"Both of you attacked! Both of you lost 5 of health.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.\n In addition to it, you won 5 XP and 1 Level! Your current XP: {character_stats.xp}\n Your current Level: {character_stats.level}.")
                elif pressed_attack_or_defense == 'e' and enemy_random_choice == enemy_options[1]: #Attack from character, defense from the enemy. No one lose health and no gain of xp!
                    print(f"You attacked and the {enemy} defended! None of you lost any health or gained XP.")
                elif pressed_attack_or_defense == 'q' and enemy_random_choice == enemy_options[0]: #Defense from the character, attack from the enemy. No one lose health and no gain of xp!
                    print(f"You defended and the {enemy} attacked! None of you lost any health or gained XP.")
                elif pressed_attack_or_defense == 'q' and enemy_random_choice == enemy_options[1]: #Defense from both! You gain health and no xp!
                    if character_stats.health <= 95:
                        character_stats.health += 5
                        print(f"Both of you defended! You gained 5 of health and 0 XP. The enemy did not lose or gained anything.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                    elif character_stats.health > 95 and character_stats.health < 100:
                        character_stats.health = 100
                        print(f"Both of you defended! Now, you have full health and did not gain any XP. The enemy did not lose or gained any stats.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                    elif character_stats.health >= 100:
                        print(f"Both of you defended! You did not gain any health because you already have the max health possible! You did not gain any xp. The enemy also did not lose or gained any stats.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                if character_stats.health > 0 and enemy.health > 0:
                    print("Let's go to the next turn!")
                else:
                    break
        elif enemy._enemy_type == 'Website Destroyer':
            while character_stats.health > 0 or enemy.health > 0:
                print("It's your turn! Press E to attack or Q to defend. The enemy will pick their action after you choose yours.")
                pressed_attack_or_defense = input().lower()
                while pressed_attack_or_defense != 'e' and pressed_attack_or_defense != 'q':
                    pressed_attack_or_defense = input('Unknown command. Please type your action again: ').lower()
                print("Now it's the enemy turn!")
                enemy_options = ['E', 'Q']
                enemy_random_choice = random.choice(enemy_options)
                print(f"Enemy's random choice: {enemy_random_choice}")
                if pressed_attack_or_defense == 'e' and enemy_random_choice == enemy_options[0]: #Attack from both. Both lose health and you gain XP.
                    character_stats.health -= 5 #Lose 5 of health
                    character_stats.xp += 5 #If you attack and the enemy does not defend, you win 5 of XP!
                    character_stats.level += 1
                    enemy.health -= 5 #Lose 5 of health
                    print(f"Both of you attacked! Both of you lost 5 of health.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.\n In addition to it, you won 5 XP and 1 Level! Your current XP: {character_stats.xp}\n Your current Level: {character_stats.level}.")
                elif pressed_attack_or_defense == 'e' and enemy_random_choice == enemy_options[1]: #Attack from character, defense from the enemy. No one lose health and no gain of xp!
                    print(f"You attacked and the {enemy} defended! None of you lost any health or gained XP.")
                elif pressed_attack_or_defense == 'q' and enemy_random_choice == enemy_options[0]: #Defense from the character, attack from the enemy. No one lose health and no gain of xp!
                    print(f"You defended and the {enemy} attacked! None of you lost any health or gained XP.")
                elif pressed_attack_or_defense == 'q' and enemy_random_choice == enemy_options[1]: #Defense from both! You gain health and no xp!
                    if character_stats.health <= 95:
                        character_stats.health += 5
                        print(f"Both of you defended! You gained 5 of health and 0 XP. The enemy did not lose or gained anything.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                    elif character_stats.health > 95 and character_stats.health < 100:
                        character_stats.health = 100
                        print(f"Both of you defended! Now, you have full health and did not gain any XP. The enemy did not lose or gained any stats.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                    elif character_stats.health >= 100:
                        print(f"Both of you defended! You did not gain any health because you already have the max health possible! You did not gain any xp. The enemy also did not lose or gained any stats.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                if character_stats.health > 0 and enemy.health > 0:
                    print("Let's go to the next turn!")
                else:
                    break
    elif character_stats._chose_character == 'mathematician':
        if enemy._enemy_type == 'Brave Calculator':
            while character_stats.health > 0 or enemy.health > 0:
                print("It's your turn! Press E to attack or Q to defend. The enemy will pick their action after you choose yours.")
                pressed_attack_or_defense = input().lower()
                while pressed_attack_or_defense != 'e' and pressed_attack_or_defense != 'q':
                    pressed_attack_or_defense = input('Unknown command. Please type your action again: ').lower()
                print("Now it's the enemy turn!")
                enemy_options = ['E', 'Q']
                enemy_random_choice = random.choice(enemy_options)
                print(f"Enemy's random choice: {enemy_random_choice}")
                if pressed_attack_or_defense == 'e' and enemy_random_choice == enemy_options[0]: #Attack from both. Both lose health and you gain XP.
                    character_stats.health -= 5 #Lose 5 of health
                    character_stats.xp += 5 #If you attack and the enemy does not defend, you win 5 of XP!
                    character_stats.level += 1
                    enemy.health -= 5 #Lose 5 of health
                    print(f"Both of you attacked! Both of you lost 5 of health.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.\n In addition to it, you won 5 XP and 1 Level! Your current XP: {character_stats.xp}\n Your current Level: {character_stats.level}.")
                elif pressed_attack_or_defense == 'e' and enemy_random_choice == enemy_options[1]: #Attack from character, defense from the enemy. No one lose health and no gain of xp!
                    print(f"You attacked and the {enemy} defended! None of you lost any health or gained XP.")
                elif pressed_attack_or_defense == 'q' and enemy_random_choice == enemy_options[0]: #Defense from the character, attack from the enemy. No one lose health and no gain of xp!
                    print(f"You defended and the {enemy} attacked! None of you lost any health or gained XP.")
                elif pressed_attack_or_defense == 'q' and enemy_random_choice == enemy_options[1]: #Defense from both! You gain health and no xp!
                    if character_stats.health <= 95:
                        character_stats.health += 5
                        print(f"Both of you defended! You gained 5 of health and 0 XP. The enemy did not lose or gained anything.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                    elif character_stats.health > 95 and character_stats.health < 100:
                        character_stats.health = 100
                        print(f"Both of you defended! Now, you have full health and did not gain any XP. The enemy did not lose or gained any stats.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                    elif character_stats.health >= 100:
                        print(f"Both of you defended! You did not gain any health because you already have the max health possible! You did not gain any xp. The enemy also did not lose or gained any stats.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                if character_stats.health > 0 and enemy.health > 0:
                    print("Let's go to the next turn!")
                else:
                    break
        elif enemy._enemy_type == 'Python Scarecrow':
            while character_stats.health > 0 or enemy.health > 0:
                print("It's your turn! Press E to attack or Q to defend. The enemy will pick their action after you choose yours.")
                pressed_attack_or_defense = input().lower()
                while pressed_attack_or_defense != 'e' and pressed_attack_or_defense != 'q':
                    pressed_attack_or_defense = input('Unknown command. Please type your action again: ').lower()
                print("Now it's the enemy turn!")
                enemy_options = ['E', 'Q']
                enemy_random_choice = random.choice(enemy_options)
                print(f"Enemy's random choice: {enemy_random_choice}")
                if pressed_attack_or_defense == 'e' and enemy_random_choice == enemy_options[0]: #Attack from both. Both lose health and you gain XP.
                    character_stats.health -= 5 #Lose 5 of health
                    character_stats.xp += 5 #If you attack and the enemy does not defend, you win 5 of XP!
                    character_stats.level += 1
                    enemy.health -= 5 #Lose 5 of health
                    print(f"Both of you attacked! Both of you lost 5 of health.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.\n In addition to it, you won 5 XP and 1 Level! Your current XP: {character_stats.xp}\n Your current Level: {character_stats.level}.")
                elif pressed_attack_or_defense == 'e' and enemy_random_choice == enemy_options[1]: #Attack from character, defense from the enemy. No one lose health and no gain of xp!
                    print(f"You attacked and the {enemy} defended! None of you lost any health or gained XP.")
                elif pressed_attack_or_defense == 'q' and enemy_random_choice == enemy_options[0]: #Defense from the character, attack from the enemy. No one lose health and no gain of xp!
                    print(f"You defended and the {enemy} attacked! None of you lost any health or gained XP.")
                elif pressed_attack_or_defense == 'q' and enemy_random_choice == enemy_options[1]: #Defense from both! You gain health and no xp!
                    if character_stats.health <= 95:
                        character_stats.health += 5
                        print(f"Both of you defended! You gained 5 of health and 0 XP. The enemy did not lose or gained anything.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                    elif character_stats.health > 95 and character_stats.health < 100:
                        character_stats.health = 100
                        print(f"Both of you defended! Now, you have full health and did not gain any XP. The enemy did not lose or gained any stats.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                    elif character_stats.health >= 100:
                        print(f"Both of you defended! You did not gain any health because you already have the max health possible! You did not gain any xp. The enemy also did not lose or gained any stats.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                if character_stats.health > 0 and enemy.health > 0:
                    print("Let's go to the next turn!")
                else:
                    break
        elif enemy._enemy_type == 'Website Destroyer':
            while character_stats.health > 0 or enemy.health > 0:
                print("It's your turn! Press E to attack or Q to defend. The enemy will pick their action after you choose yours.")
                pressed_attack_or_defense = input().lower()
                while pressed_attack_or_defense != 'e' and pressed_attack_or_defense != 'q':
                    pressed_attack_or_defense = input('Unknown command. Please type your action again: ').lower()
                print("Now it's the enemy turn!")
                enemy_options = ['E', 'Q']
                enemy_random_choice = random.choice(enemy_options)
                print(f"Enemy's random choice: {enemy_random_choice}")
                if pressed_attack_or_defense == 'e' and enemy_random_choice == enemy_options[0]: #Attack from both. Both lose health and you gain XP.
                    character_stats.health -= 5 #Lose 5 of health
                    character_stats.xp += 5 #If you attack and the enemy does not defend, you win 5 of XP!
                    character_stats.level += 1
                    enemy.health -= 5 #Lose 5 of health
                    print(f"Both of you attacked! Both of you lost 5 of health.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.\n In addition to it, you won 5 XP and 1 Level! Your current XP: {character_stats.xp}\n Your current Level: {character_stats.level}.")
                elif pressed_attack_or_defense == 'e' and enemy_random_choice == enemy_options[1]: #Attack from character, defense from the enemy. No one lose health and no gain of xp!
                    print(f"You attacked and the {enemy} defended! None of you lost any health or gained XP.")
                elif pressed_attack_or_defense == 'q' and enemy_random_choice == enemy_options[0]: #Defense from the character, attack from the enemy. No one lose health and no gain of xp!
                    print(f"You defended and the {enemy} attacked! None of you lost any health or gained XP.")
                elif pressed_attack_or_defense == 'q' and enemy_random_choice == enemy_options[1]: #Defense from both! You gain health and no xp!
                    if character_stats.health <= 95:
                        character_stats.health += 5
                        print(f"Both of you defended! You gained 5 of health and 0 XP. The enemy did not lose or gained anything.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                    elif character_stats.health > 95 and character_stats.health < 100:
                        character_stats.health = 100
                        print(f"Both of you defended! Now, you have full health and did not gain any XP. The enemy did not lose or gained any stats.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                    elif character_stats.health >= 100:
                        print(f"Both of you defended! You did not gain any health because you already have the max health possible! You did not gain any xp. The enemy also did not lose or gained any stats.\n Your current health is {character_stats.health}.\n The enemy's health is {enemy.health}.")
                if character_stats.health > 0 and enemy.health > 0:
                    print("Let's go to the next turn!")
                else:
                    break


def battle(character_stats: Character, enemy: Enemy):
    """
    This is the most important function for the battles between the user and the enemies.
    This function organizes the sequence in how the user will fight against the enemy. First, the user will go to the battle questions, which instead of fighting the user will have their knowledge tested.
    After this, the user will go to the actual combat if they got less than 50% of the questions correct.
    """
    print(f"Let's start with the Questions! Please read each of them very carefully and do your best with your mind if you do not want to fight for your life. When you are about to answer, please type only the letter of the alternative (e.g. A), without apostrophes or quotation marks or writing the whole answer. Type only the letter of the alternative.")
    result_battle_questions = battle_questions(character_stats, enemy)
    if result_battle_questions: #Since battle_questions returns True or false, depending on the result, it will print it out or go to the combat!/
        print("You won without risking your blood!")
    else:
        battle_combat(character_stats, enemy)
        if character_stats.health <= 0: #If character_health is less or equal than zero... hope this not happens!
            print("You lost the game.")
        else:
            if enemy.health <= 0: #If enemy_health is less or equal than zero, this means... he is dead!
                print(f"You defeated the {enemy._enemy_type}! Good job!!!")

def move_right(character_stats: Character, game_grid):
    '''
    It is easier to manage your indices inside of here.
    If you don't hit a wall, then you can increment the x value.
    '''
    if character_stats.x + 1 < len(game_grid[character_stats.y]):
        character_stats.x += 1

def move_left(character_stats: Character, game_grid):
    '''
    Same idea here, but for y. Moving up is reducing the index!
    '''
    if character_stats.x - 1 >= 0:
        character_stats.x -= 1

def move_up(character_stats: Character, game_grid):
    '''
    Same idea here, but for y. Moving up is reducing the index!
    '''
    if character_stats.y - 1 >= 0:
        character_stats.y -= 1

def move_down(character_stats: Character, game_grid):
    '''
    It is easier to manage your indices inside of here.
    If you don't hit a wall, then you can increment the x value.
    '''
    if character_stats.y + 1 < len(game_grid[character_stats.y]):
        character_stats.y += 1

def navigate(character_stats: Character, game_grid, move, boss_defeated):
    """
    The navigate function is the responsible for making the user to move around the game grid.
    Every part of the grid has a specific attribute and it performs an action, which might include calling another functions for the battle, giving XP to the user or just simply do nothing.
    """
    if character_stats.health > 0 and boss_defeated == False:
        print(f"Current position:\nX: {character_stats.x}\nY: {character_stats.y}")
        if move == 'w':
            # Try to move up!
            move_up(character_stats, game_grid)
        elif move == 'a':
            # Try to move left!
            move_left(character_stats, game_grid)
        elif move == 's':
            # Try to move down!
            move_down(character_stats, game_grid)
        elif move == 'd':
            # Try to move right!
            move_right(character_stats, game_grid)
        else:
            pass
        print(f"New position:\nX: {character_stats.x}\nY: {character_stats.y}")
        # Now handle what is in that cell!
        player_pos = game_grid[character_stats.y][character_stats.x]
        if player_pos == ' ': #Nothing!
            boss_defeated = False
            return boss_defeated
        elif player_pos == 'b': #Brave Calculator Enemy!
            print(f"You are going to combat the Brave Calculator! Good luck!")
            brave_calculator_str = "Brave Calculator" #This is just to transform the Brave Calculator into a string.
            brave_calculator = character.Enemy(brave_calculator_str)
            brave_calculator.generate_enemy()
            battle(character_stats, brave_calculator)
            boss_defeated = False
            return boss_defeated
        elif player_pos == 'p': #Python Scarecrow Enemy!
            print(f"Time to fight against the Python Scarecrow! Good luck!")
            python_scarecrow_str = "Python Scarecrow" #Same as brave_calculator_str.
            python_scarecrow = character.Enemy(python_scarecrow_str)
            python_scarecrow.generate_enemy()
            battle(character_stats, python_scarecrow)
            boss_defeated = False
            return boss_defeated
        elif player_pos == 'w': #Website Destroyer Enemy!
            print(f"Uh-oh... time to fight the boss, the Website Destroyer! Good luck!")
            website_destroyer_str = "Website Destroyer"
            website_destroyer = character.Enemy(website_destroyer_str)
            website_destroyer.generate_enemy()
            battle(character_stats, website_destroyer)
            if website_destroyer.health <= 0:
                boss_defeated = True
                print(f"Congrats! You defeated the boss. These are your stats:\n{character_stats}")
                return boss_defeated
            else:
                boss_defeated = False
                return boss_defeated
        elif player_pos == 'l': #Loots!
            character_stats.xp += 10
            character_stats.level += 2
            game_grid[character_stats.y][character_stats.x] = ' '
            print(f"You won 10 XP and 2 Levels! Your current XP is {character_stats.xp} and current Level is {character_stats.level}.")
            boss_defeated = False
            return boss_defeated
        return boss_defeated
        

# Focus on creating the battle_combat and battle_questions. The main battle function serves as a way to just allocate everything and make it easy
# Transform the character and enemy stats into lists. It might be easier.