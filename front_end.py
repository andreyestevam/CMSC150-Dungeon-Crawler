import arcade
import engine
import math
import random
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_ENEMY = 0.7
SPRITE_SCALING_LOOT = 0.2
LOOT_COUNT = 15
sprite_stepsize_y = 100
sprite_stepsize_x = 100
image_width = 96
image_height = 128

class DungeonCrawler(arcade.Window):

    def __init__(self, title="Richmond Chainsaw Massacre", player_class=None, chose_character=None, grid=None, cell_size=100):
        self._title = title
        self._game_grid = grid
        self._chose_character = chose_character
        self._player_class = player_class
        self.boss_defeated = False
        self._cell_size = cell_size
        self._width = len(grid) * cell_size
        self._height = len(grid) * cell_size
        super().__init__(self._width, self._height, self._title)
        # Variables that will hold sprite lists.
        self.player_list = None #Create a list with all the character sprites!
        self.enemy_list = None #Create a list with all the enemy sprites!
        self.loot_list = None #Create a list with all the loots sprites!

        # Set up the player info
        self._player_sprite = None
        # Add HEALTH, XP... everything in here!

        self.brave_calculator = None #First enemy!
        self.python_scarecrow = None #Second enemy!
        self.website_destroyer = None #Third enemy! The boss!

        self.loot = None #The loots that give you XP!

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # King of like before, we can set the color here!
        arcade.set_background_color(arcade.color.BABY_BLUE)
    
    def setup(self):
        """ Set up the game and initialize the variables. """
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.loot_list = arcade.SpriteList()

        # Set up the player
        # Character image from kenney.nl
        if self._chose_character == 'mathematician':
            self._player_sprite = arcade.Sprite("images/the_mathematician.png", SPRITE_SCALING_PLAYER)
            self._player_sprite.width = self._cell_size
            self._player_sprite.height = self._cell_size
            self._player_sprite.center_x = 250
            self._player_sprite.center_y = 250
            self.player_list.append(self._player_sprite)
        
        elif self._chose_character == 'scientist':
            self._player_sprite = arcade.Sprite("images/the_scientist.png", SPRITE_SCALING_PLAYER)
            self._player_sprite.width = self._cell_size
            self._player_sprite.height = self._cell_size
            self._player_sprite.center_x = 250
            self._player_sprite.center_y = 250
            self.player_list.append(self._player_sprite)
        
        elif self._chose_character == 'web developer':
            self._player_sprite = arcade.Sprite("images/the_web_developer.png", SPRITE_SCALING_PLAYER)
            self._player_sprite.width = self._cell_size
            self._player_sprite.height = self._cell_size
            self._player_sprite.center_x = 250
            self._player_sprite.center_y = 250
            self.player_list.append(self._player_sprite)


        self.brave_calculator = arcade.Sprite("images/brave_calculator_mad.png", SPRITE_SCALING_ENEMY)
        self.brave_calculator.center_x = 150
        self.brave_calculator.center_y = 150
        self.enemy_list.append(self.brave_calculator)

        self.python_scarecrow = arcade.Sprite("images/python_scarecrow_mad.png", SPRITE_SCALING_ENEMY)
        self.python_scarecrow.center_x = 350
        self.python_scarecrow.center_y = 350
        self.enemy_list.append(self.python_scarecrow)

        self.website_destroyer = arcade.Sprite("images/website_destroyer_mad.png", SPRITE_SCALING_ENEMY)
        self.website_destroyer.center_x = 450
        self.website_destroyer.center_y = 100
        self.enemy_list.append(self.website_destroyer)

        self.loot = arcade.Sprite("images/loot.png", SPRITE_SCALING_LOOT)
        self.loot.center_x = 50
        self.loot.center_y = 450
        self.loot_list.append(self.loot)

        self.loot = arcade.Sprite("images/loot.png", SPRITE_SCALING_LOOT)
        self.loot.center_x = 50
        self.loot.center_y = 350
        self.loot_list.append(self.loot)

        self.loot = arcade.Sprite("images/loot.png", SPRITE_SCALING_LOOT)
        self.loot.center_x = 50
        self.loot.center_y = 250
        self.loot_list.append(self.loot)

        self.loot = arcade.Sprite("images/loot.png", SPRITE_SCALING_LOOT)
        self.loot.center_x = 50
        self.loot.center_y = 150
        self.loot_list.append(self.loot)

        self.loot = arcade.Sprite("images/loot.png", SPRITE_SCALING_LOOT)
        self.loot.center_x = 50
        self.loot.center_y = 50
        self.loot_list.append(self.loot)

        self.loot = arcade.Sprite("images/loot.png", SPRITE_SCALING_LOOT)
        self.loot.center_x = 250
        self.loot.center_y = 50
        self.loot_list.append(self.loot)

        self.loot = arcade.Sprite("images/loot.png", SPRITE_SCALING_LOOT)
        self.loot.center_x = 250
        self.loot.center_y = 150
        self.loot_list.append(self.loot)

        self.loot = arcade.Sprite("images/loot.png", SPRITE_SCALING_LOOT)
        self.loot.center_x = 350
        self.loot.center_y = 50
        self.loot_list.append(self.loot)

        self.loot = arcade.Sprite("images/loot.png", SPRITE_SCALING_LOOT)
        self.loot.center_x = 350
        self.loot.center_y = 150
        self.loot_list.append(self.loot)

        self.loot = arcade.Sprite("images/loot.png", SPRITE_SCALING_LOOT)
        self.loot.center_x = 350
        self.loot.center_y = 250
        self.loot_list.append(self.loot)

        self.loot = arcade.Sprite("images/loot.png", SPRITE_SCALING_LOOT)
        self.loot.center_x = 450
        self.loot.center_y = 150
        self.loot_list.append(self.loot)

        self.loot = arcade.Sprite("images/loot.png", SPRITE_SCALING_LOOT)
        self.loot.center_x = 450
        self.loot.center_y = 250
        self.loot_list.append(self.loot)

        self.loot = arcade.Sprite("images/loot.png", SPRITE_SCALING_LOOT)
        self.loot.center_x = 450
        self.loot.center_y = 350
        self.loot_list.append(self.loot)

        self.loot = arcade.Sprite("images/loot.png", SPRITE_SCALING_LOOT)
        self.loot.center_x = 150
        self.loot.center_y = 450
        self.loot_list.append(self.loot)

        self.loot = arcade.Sprite("images/loot.png", SPRITE_SCALING_LOOT)
        self.loot.center_x = 250
        self.loot.center_y = 450
        self.loot_list.append(self.loot)

        self.loot = arcade.Sprite("images/loot.png", SPRITE_SCALING_LOOT)
        self.loot.center_x = 350
        self.loot.center_y = 450
        self.loot_list.append(self.loot)

        self.loot = arcade.Sprite("images/loot.png", SPRITE_SCALING_LOOT)
        self.loot.center_x = 450
        self.loot.center_y = 450
        self.loot_list.append(self.loot)



    def on_draw(self):
        # Leave this here!
        arcade.start_render()
        #
        ###
        #   You can play with these.
        ###
        self.player_list.draw()
        self.enemy_list.draw()
        self.loot_list.draw()
        welcome = "Welcome to Richmond Chainsaw Massacre!"
        # Put the text on the screen.
        xp_str_on_screen = f"XP: {self._player_class.xp}"
        level_str_on_screen = f"Level: {self._player_class.level}"
        arcade.draw_text(xp_str_on_screen, 10, 40, arcade.color.WHITE, 14)
        arcade.draw_text(level_str_on_screen, 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, symbol, modifiers):
        
        if symbol == arcade.key.W:
            print(f'Moved up 1 space')
            sprite_new_y = self._player_sprite.center_y + sprite_stepsize_y
            if sprite_new_y <= self._height:
                self._player_sprite.center_y += sprite_stepsize_y
            move = 'w'
            self.boss_defeated = engine.navigate(self._player_class, self._game_grid, move, self.boss_defeated)
            if self.boss_defeated:
                arcade.exit()
            elif self._player_class.health <= 0:
                arcade.exit()
        if symbol == arcade.key.S:
            print(f'Moved down 1 space')
            sprite_new_y = self._player_sprite.center_y - sprite_stepsize_y
            if self._player_sprite.center_y > 50:
                self._player_sprite.center_y -= sprite_stepsize_y
            move = 's'
            self.boss_defeated = engine.navigate(self._player_class, self._game_grid, move, self.boss_defeated)
            if self.boss_defeated:
                arcade.exit()
            elif self._player_class.health <= 0:
                arcade.exit()
        if symbol == arcade.key.A:
            print(f'Moved left 1 space')
            sprite_new_x = self._player_sprite.center_x - sprite_stepsize_x
            if sprite_new_x > 0:
                self._player_sprite.center_x -= sprite_stepsize_x
            move = 'a'
            self.boss_defeated = engine.navigate(self._player_class, self._game_grid, move, self.boss_defeated)
            if self.boss_defeated:
                arcade.exit()
            elif self._player_class.health <= 0:
                arcade.exit()
        if symbol == arcade.key.D:
            print(f'Moved right 1 space')
            sprite_new_x = self._player_sprite.center_x + sprite_stepsize_x
            if sprite_new_x <= self._width:
                self._player_sprite.center_x += sprite_stepsize_x
            move = 'd'
            self.boss_defeated = engine.navigate(self._player_class, self._game_grid, move, self.boss_defeated)
            if self.boss_defeated:
                arcade.exit()
            elif self._player_class.health <= 0:
                arcade.exit()
        # You will modify this function to respond to your Up, Down, Left, Right keys.
        # Each key should print something about your character moving.
        #   Ex: "Moved up 1 space"

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.loot_list.update()

        # Generate a list of all sprites that collided with the player.
        loot_hit_list = arcade.check_for_collision_with_list(self._player_sprite, self.loot_list) #DEFINE HERE WITH ALL THE PLAYERS, CHARACTERS

        # Loop through each colliding sprite, remove it, and add to the score.
        for loot in loot_hit_list:
            loot.remove_from_sprite_lists()