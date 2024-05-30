import arcade
import math

class Character:
    def __init__(self, user_name, chose_character):
        self._user_name = user_name
        self._chose_character = chose_character
        self.xp = None
        self.level = None
        self.health = None
        self.attack = None
        self.defense = None
        self.x = None
        self.y = None
    
    def generate_character(self):
        """
        This is the function which shows the stats of the player according to what the user types (used two parameters).
        ---
        Parameters:
        name = name of the user (string)
        self._chose_character = name of the character (string)
        
        Returns
        ---
        A boolean based on the self._chose_character string and returns its experience points, level, health, attack, and defense.
        """
        if self._chose_character == 'web developer':
            self.xp = 0
            self.level = 1
            self.health = 80
            self.attack = 5
            self.defense = 5 #If you defend it cancels out the attack from the enemy
            self.x = 2
            self.y = 2
        elif self._chose_character == 'scientist':
            self.xp = 0
            self.level = 1
            self.health = 95
            self.attack = 5
            self.defense = 5
            self.x = 2
            self.y = 2
        elif self._chose_character == 'mathematician':
            self.xp = 0
            self.level = 1
            self.health = 70
            self.attack = 5
            self.defense = 5
            self.x = 2
            self.y = 2
        else:
            self._chose_character = input("Error. Type your character name again, please: ").lower()
            return Character.generate_character(self)
    
    def __str__(self):
        """
        When printing the object, this is what is going to be printed! All the information/stats related to the character.
        """
        return f"Name: {self._chose_character}\nXP: {self.xp}\nLevel: {self.level}\nHealth: {self.health}\nAttack: {self.attack}\nDefense: {self.defense}\nX: {self.x}\nY: {self.y}"




class Enemy:
    def __init__(self, enemy_type):
        self._enemy_type = enemy_type
        self.attack = None
        self.defense = None
        self.health = None
        self.difficulty = None

    def generate_enemy(self):
        """
        This is the function which shows the stats of the enemy (used only one parameter).
        ---
        Parameters:
        enemy_type = refers to the enemy nam
        
        Returns
        ---
        A boolean based on the enemy_type string and returns its attack, defense, health, and difficulty
        """
        if self._enemy_type == 'Brave Calculator':
            self.attack = 5
            self.defense = 5
            self.health = 50
            self.difficulty = 5
        elif self._enemy_type == 'Python Scarecrow':
            self.attack = 5
            self.defense = 5
            self.health = 80
            self.difficulty = 8
        elif self._enemy_type == 'Website Destroyer':
            self.attack = 5
            self.defense = 5
            self.health = 100
            self.difficulty = 10
    
    def __str__(self):
        """
        When printing the object, this is what is going to be printed! All the information/stats related to the enemy.
        """
        return f"Enemy: {self._enemy_type}\nAttack: {self.attack}\nDefense: {self.defense}\nHealth: {self.health}\nDifficulty: {self.difficulty}"