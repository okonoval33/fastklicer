import pygame
import os

pygame.font.init()
pygame.init()

display_width = 800
display_heipgth = 600

FPS = pygame.time.Clock()


class Sprite_Game:
    def __init__(self, width, height, name_image, x,y, speed = 0, speed_X = 0):
        self.WIDTH = width
        self.HEIGHT = height
        self.NAME_IMEGE = name_image
        self.X = x
        self.Y = y
        self.SPEED = speed
        self.SPEED_X = speed_X
        self.END_IMAGE = ""
        self.RECT = pygame.Rect(x, y, width, height)

    def load_image(self):
        path_image = os.path.join(os.path.abspath(__file__ + "/.."), self.NAME_IMEGE)
        image1 = pygame.image.load(path_image)
        self.END_IMAGE = pygame.transform.scale(image1, (self.WIDTH, self.HEIGHT))

list_map = [
    "1111111111"
    "0001111000"
    "1111111111"
    "0001111000"
]
list_blok = list()

def start_mage()
    screen = pygame.display.set_mode((display_width))
