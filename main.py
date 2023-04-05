# File created by: Chris Cozort
# Agenda:
# gIT GITHUB    
# Build file and folder structures
# Create libraries
# testing github changes
# I changed something - I changed something else tooooo!

# This file was created by: Chris Cozort
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: 

'''
Game structure
Goals: Create a health bar 
create a score 
create waves of enemies

'''

# import libs
import pygame as pg
import random
import os
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# create game class in order to pass properties to the sprites file

class Game:
    def __init__(self): 
        # init game window etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # starting a new game
        self.score = 0
        self.health = 100
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50,RED, "lava")
        self.plat2 = Platform(150, 10, 300, 300, GREEN, "bouncy")
        self.plat3 = Platform(150, 10, 40, 150, BLACK, "win")
        self.plat4 = Platform(150, 10, 400, 500, WHITE, "icy")
        self.plat5 = Platform(150, 10, 700, 530, WHITE, "normal")
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.plat1)
        self.platforms.add(self.plat1)
        self.all_sprites.add(self.plat2)
        self.platforms.add(self.plat2)
        self.all_sprites.add(self.plat3)
        self.platforms.add(self.plat3)
        self.all_sprites.add(self.plat4)
        self.platforms.add(self.plat4)
        self.all_sprites.add(self.plat5)
        self.platforms.add(self.plat5)
        self.all_sprites.add(self.player)
       
        # for plat in PLATFORM_LIST:
        #     p = Platform(*plat)
        #     self.all_sprites.add(p)
        #     self.platforms.add(p)
        for i in range(0,20):
            m = Mob(20,20,(0,255,0))
            self.enemies.add(m)
            self.all_sprites.add(m)
            
        self.run()
    def run(self):
        self.playing = True 
        while self.playing: 
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def update(self):
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                if hits[0].variant == "dissapearing":
                    hits[0].kill()
                elif hits[0].variant == "icy":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    PLAYER_FRICTION = -0.1
                elif hits[0].variant == "bouncy":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                elif hits[0].variant == "lava":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    self.health -= 1  
                elif hits[0].variant == "win":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    Win == True  
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    
                    
        

    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        self.draw_text("Health: " + str(self.health), 22, WHITE, WIDTH/2, HEIGHT/10) 
        if self.health <= 0:
            self.draw_text("YOU LOSE", 53, RED, WIDTH/2, HEIGHT/2)
        if Win == True:
            self.draw_text("You WIN!", 53, GREEN, WIDTH/2, HEIGHT/2)
            print("hi")
        
        pg.display.flip()
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('comic sans')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

g = Game()

while g.running:
    g.new()

pg.quit()