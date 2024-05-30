import arcade
import math
import character
import engine
import front_end

def check_level(xp): # I have to say somewhere in the game that the initial xp is 0, but level 1
    level = math.floor((xp+5)/5) #Every 5 new xp, you have 1 level.
    return level

if __name__ == '__main__':
    game_grid = [['l', 'l', 'l', 'l', 'l',],
                 ['l', ' ', ' ', 'p', 'l',],
                 ['l', ' ', ' ', 'l', 'l',],
                 ['l', 'b', 'l', 'l', 'l',],
                 ['l', ' ', 'l', 'l', 'w',]]
    width = 500
    height = 500
    user_name = input("Enter your name: ")
    print(f'Welcome to Richmond Chainsaw Massacre, {user_name}!')
    print("Be prepared to run while solving problems...")
    print("Years ago, three senior computer science students were taking the class CMSC 323 Programming Languages, and they all were struggling the whole semester. They were very close to graduate and were very worried if they could pass this class or not so they could get a job after their last semesters. All of them had already got into a computer science job, which would start after graduating from college. In the last two weeks, to pass this class, these 3 students realized they all would have to take at least a 110 out of 100 in their final project, which was in group, to graduate. Unfortunately, they failed this class because it was impossible to reach this grade. This made them lose their prospective job and then the only job they got was in lumber and now they are hunting, with a chainsaw, every classmate that passed the class CMSC 323 Programming Languages. You are one of the few people who passed this class. Your goal is to run around the campus. You will be participating in the SpiderDash 5K, the official University of Richmond's annual running event. If they successfully find you, you are killed and have to restart the game until you actually run through the campus. These 3 students will be around the campus and you will have to reach the end of the run without getting hunted.")
    print("Your goal is to participate in the SpiderDash 5K event, and successfully run the entire event without getting caught by the three computer science enemies.")
    
    # Introducing the characters and the stats in the lines below!
    print("You will have the opportunity to choose between 3 different characters, and each of them will fight their own enemies.")
    print("That being said... let's introduce the characters!")
    print("Starting with... Web Developer! This student is currently working on developing websites and has made some great tons of money with this job. He is very clever at debugging lines of code and gives you hint against the enemy The Website Destroyer.")
    print("The second one is the Scientist! This student is a Computer Science and Biology double major. When he graduated, he started studying snakes. During one of his studies, the Python snake bit him and they became very close friends. This snake was also created in a laboratory by programming language and is very clever at coding and can help you solve Python problems. It helps you to solve problems against the enemy The Python Scarecrow.")
    print("Last but not least... Mathematician! This character is passionate about investigating math problems and doing quick math solutions. The Mathematician helps you to solve problems against the enemy The Brave Calculator.")

    # Ask which of the characters the user wants to be!
    print("Which character do you want to be? Be careful... one decision changes everything!")
    chose_character = input("Type your character name: ").lower()
    player_class = character.Character(user_name, chose_character)
    player_class.generate_character()
    print(f"You selected the {player_class._chose_character.title()}, {user_name}! Your stats are...\n Attack: {player_class.attack}\n Defense: {player_class.defense}\n Health: {player_class.health}\n Experience points (XP): {player_class.xp}\n Level: {player_class.level}.\n Every 5 XP you gain 1 Level.")

    brave_calculator_str = "Brave Calculator" #This is just to transform the Brave Calculator into a string.
    brave_calculator = character.Enemy(brave_calculator_str)
    brave_calculator.generate_enemy()

    python_scarecrow_str = "Python Scarecrow" #Same as brave_calculator_str.
    python_scarecrow = character.Enemy(python_scarecrow_str)
    python_scarecrow.generate_enemy()

    website_destroyer_str = "Website Destroyer"
    website_destroyer = character.Enemy(website_destroyer_str)
    website_destroyer.generate_enemy()

    # Now I will talk about the enemies!
    print(f'Since you decided who your character is, now you will take a look in the enemies that you will fight against!')
    print(f"The first enemy is the Brave Calculator! He definitely loved math so much but now, since he just uses his mind to lumber, he hates math. Therefore, he gives you 7 math problems; if you get 4+ correct, you win! Otherwise, x = fail.\n The Brave Calculator's stats are:\n Attack: {brave_calculator.attack}\n Defense: {brave_calculator.defense}\n Health (from 0-100): {brave_calculator.health}\n Difficulty (from 0-10): {brave_calculator.difficulty}")
    print(f"The second enemy is the Python Scarecrow. This was a student who declared his Computer Science major in freshman year while taking CMSC 150, and after taking CMSC 301 Computer Organization, he gave up on computer science and just wanted his degree as soon as possible. To beat him, he gives you 5 Python debugging problems. If you get 3+ correct, you win! Else: print('You failed. Restart the game').\n The Python Scarecrow's stats are:\n Attack: {python_scarecrow.attack}\n Defense: {python_scarecrow.defense}\n Health (from 0-100): {python_scarecrow.health}\n Difficulty (from 0-10): {python_scarecrow.difficulty}")
    print(f"The third, and last enemy is the Website Destroyer. This student was planning to create websites and now he is planning to break the richmond.edu's website. He will give you programming errors in the line codes and you will have to figure out what is wrong. The Web Destroyer's stats are:\n Attack: {website_destroyer.attack}\n Defense: {website_destroyer.defense}\n Health (from 0-100): {website_destroyer.health}\n Difficulty (from 0-10): {website_destroyer.difficulty}")
    print(f"Are you ready to play? Then let's go!!!")
    print(f"Character location:\nX: {player_class.x}\nY: {player_class.y}")

    #Running the game!
    dungeon_crawler = front_end.DungeonCrawler("Richmond Chainsaw Massacre", player_class, player_class._chose_character, game_grid, 100)
    dungeon_crawler.setup()
    arcade.run()

    #Navigating throughout the game!
    #boss_defeated = False
    #while player_class.health > 0 and boss_defeated == False:
    #    print(f"Current position:\nX: {player_class.x}\nY: {player_class.y}")
    #    move = input('Pick a direction: ').lower()
    #    boss_defeated = engine.navigate(player_class, game_grid, move) #DO WHAT IN HERE?
    #    if boss_defeated:
    #        print(f"You won the game! You defeated the boss!")
    # We have an important change: we are using a Python class form of our window!
    # It will allow us to handle key events!