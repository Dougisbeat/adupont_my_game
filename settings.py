from random import randint
WIDTH = 800
HEIGHT = 600
PLAYER_ACC = 1
PLAYER_FRICTION = -0.3
PLAYER_JUMP = 20
# make player go higher
PLAYER_BOOST = 25
PLAYER_GRAV = 1
MOB_ACC = 2
BLACK = (0,0,0)
BLUE = (50,50,255)
RED = (255,50,50)
WHITE = (255,255,255)
GREEN = (50, 255, 50)
DGREEN = (47, 72, 62)

FPS = 60
RUNNING = True
SCORE = 0
PAUSE = False
HEALTH = 100
Win = True


# # Starting platforms
# PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, (200,200,200), "normal"),
#                  (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, (200,200,200), "bouncey"),
#                  (125, HEIGHT - 350, 100, 5, (200,200,200), "disappearing "),
#                  (350, 200, 100, 20, (200,200,200), "normal"),
#                  (175, 100, 50, 20, (200,200,200), "normal")]