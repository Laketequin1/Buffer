##### -- Imports -- #####

import pygame, time, socket, random, os, ast # Imports

from src import lakeserver # Import personal server

pygame.init() # Initiate pygame

##### -- Constant Variables -- #####

AUDIO_FOLDER = "audio/" # The folder location that holds all the sound files
IMAGE_FOLDER = "images/" # The folder location that holds all the image files
ICON_FOLDER = IMAGE_FOLDER + "icons/" # The folder location that holds all the images of icons

##### -- Variables -- #####

pos = (0, 0) # Player position

##### -- Pygame Setup -- #####

# Screen
GAME_SIZE = (1280, 720)
SCREEN_SIZE = (pygame.display.Info().current_w, pygame.display.Info().current_h) #Gets computer screen resolution

DEFAULT_TICK = 160 #FPS

display_size = GAME_SIZE #Sets screen resolution (x, y)

clock = pygame.time.Clock()
display_surface = pygame.display.set_mode(display_size, pygame.RESIZABLE) #Surface that is getting displayed

class sprite: # Stores all image sprites
    player = pygame.image.load(IMAGE_FOLDER + "player.png") # Loads player image
    enemy = pygame.image.load(IMAGE_FOLDER + "enemy.png") # Loads player image

##### -- Server -- #####

my_client = lakeserver.Client(input("IP: "), 5050, True)
my_client.connect()

##### -- Class -- #####

class Map(): # Map size
    
    #### -- Class Variables -- ####
    
    SIZE = GAME_SIZE
    
    WIDTH = SIZE[0]
    HEIGHT = SIZE[1]
    
    TOP = 0
    BOTTOM = TOP + HEIGHT
    
    LEFT = 0
    RIGHT = LEFT + WIDTH
    

class Entity(): # An Inheritied class for all entities
    
    #### -- Init -- ####
    
    def __init__(self, image, pos):
        # Set variables
        self.image = image 
        self.set_pos(pos)
        
    #### -- Movement -- ####
    
    def move(self):
        pos = self.pos
        
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.set_left(pos[0] - 2)
        if key[pygame.K_d]:
            self.set_left(pos[0] + 2)
        if key[pygame.K_w]:
            self.set_top(pos[1] - 2)
        if key[pygame.K_s]:
            self.set_top(pos[1] + 2)
            
        self.set_pos(pos)
    
    def bind(self):
        
        if self.left < Map.LEFT:
            self.set_left(Map.LEFT)
        elif self.right > Map.RIGHT:
            self.set_right(Map.RIGHT)
        
        if self.top < Map.TOP:
            self.set_top(Map.TOP)
        elif self.bottom > Map.BOTTOM:
            self.set_bottom(Map.BOTTOM)
    
    #### -- Set -- ####
    
    def set_pos(self, pos):
        self.pos = pos
        
        self.left = pos[0] # Left of entity
        self.right = pos[0] + self.image.get_width() # Right of entity
        
        self.top = pos[1] # Top of entity
        self.bottom = pos[1] + self.image.get_height() # Bottom of entity  
    
    def set_left(self, pos):
        self.left = pos # Left of entity
        self.right = self.left + self.image.get_width() # Right of entity
        
        self.pos[0] = self.left
    
    def set_right(self, pos):
        self.right = pos # Left of entity
        self.left = self.right - self.image.get_width() # Right of entity
        
        self.pos[0] = self.left
    
    def set_top(self, pos):
        self.top = pos # Left of entity
        self.bottom = self.top + self.image.get_width() # Right of entity
        
        self.pos[1] = self.top
    
    def set_bottom(self, pos):
        self.bottom = pos # Left of entity
        self.top = self.bottom - self.image.get_width() # Right of entity
        
        self.pos[1] = self.top
    
    #### -- Get -- ####
    
    def get_pos(self): # Set entity pos
        return self.pos
    
    #### -- Display -- ####
    
    def display(self): # Display entity on screen at pos
        display_surface.blit(self.image, self.pos) # Draw image
        

class Player(Entity): # Inherit entity class
    pass

##### -- Functions -- #####

def eval_message(message): # Changes string recieved to a dict\
    if message:
        try:
            return ast.literal_eval(message) # Converts data string into dict
        except ValueError:
            pass # Continue to return empty
    return "" # Return empty

def display_enemy(pos):
    if type(pos) == list:
        display_surface.blit(sprite.enemy, pos) # Draw image

main_player = Player(sprite.player, [0, 0]) # Create a player

running = True
while running:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If exit button pressed
            running = False # Exit loop
        elif event.type == pygame.KEYDOWN: # Checks for key pressed key
            if event.key == pygame.K_ESCAPE: # Checks if escape is pressed
                running = False # Exit loop
    
    main_player.move()
    main_player.bind()
    
    my_client.set_data(main_player.get_pos())
    
    display_surface.fill((230, 230, 255)) # Blue screen
    
    for enemy_pos in my_client.get_server_data().values():
        enemy_pos = eval_message(enemy_pos)
        display_enemy(enemy_pos)
    
    main_player.display() # Display player
    
    pygame.display.flip() # Update screen
    
    clock.tick(DEFAULT_TICK) # Tick Speed

my_client.disconnect()
time.sleep(0.1)