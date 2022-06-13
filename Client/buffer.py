##### -- Imports -- #####

import pygame, random, os, sys # Imports

sys.path.insert(1, os.getcwd()) # Import personal server
import lakeserver

pygame.init() # Initiate pygame

##### -- Constant Variables -- #####

AUDIO_FOLDER = "audio/" # The folder location that holds all the sound files
IMAGE_FOLDER = "images/" # The folder location that holds all the image files
ICON_FOLDER = IMAGE_FOLDER+"icons/" # The folder location that holds all the images of icons

##### -- Variables -- #####

pos = (0, 0) # Player position

##### -- Pygame Setup -- #####

# Screen
GAME_SIZE = (1920, 1080)
SCREEN_SIZE = (pygame.display.Info().current_w, pygame.display.Info().current_h) #Gets computer screen resolution

DEFAULT_TICK = 60 #FPS

display_size = (852, 480) #Sets screen resolution (x, y)

clock = pygame.time.Clock()
display_surface = pygame.display.set_mode(display_size, pygame.RESIZABLE) #Surface that is getting displayed

class sprite: # Stores all image sprites
    player = pygame.image.load(IMAGE_FOLDER + "player.png") # Loads player image
    player = pygame.image.load(IMAGE_FOLDER + "enemy.png") # Loads player image
    
##### -- Class -- #####

class entity(): # An Inheritied class for all entities
    
    #### -- Init -- ####
    
    def __init__(self, image, pos):
        # Set variables
        self.image = image
        self.pos = pos
    
    #### -- Set -- ####
    
    def set_pos(self, pos): # Set entity pos
        self.pos = pos
    
    #### -- Get -- ####
    
    def get_pos(self, pos): # Set entity pos
        return self.pos
    
    #### -- Display -- ####
    
    def display(self): # Display entity on screen at pos
        display_surface.blit(self.image, self.pos) # Draw image
        

class player(entity): # Inherit entity class
    pass


main_player = player()