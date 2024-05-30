First bug: I did not have some docstrings in some functions, so I added them. The functions I added the docstrings were:
brave_calculator_questions(user_name, num_questions), in engine module
python_scarecrow_questions(user_name, num_questions), in engine module
website_destroyer_questions(user_name, num_questions), in engine module
battle_combat(character_stats_dict, chose_character, enemy), in engine module
battle(character_stats_dict, enemy), in engine module
navigate(character_stats_dict, game_grid), in engine module

I fixed the navigate function, in the main module, which now is only taking the stats dictionary and the game grid.
I fixed the character.generate_character(user_name, chose_character), which was returning 5 variables and now it is returning only a dictionary with all this information inside the dictionary so the main file does not to create one.

Fixed the exception at runtime. I was incorrectly managing the variables and arguments so now it is working.