import pygame
import math

# setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1260, 840
BACKGROUND_COLOR = '#1e1e1e'
BODY_COLOR = '#38d4ff'

# properties
GRAVITATIONAL_CONSTANT = 1
BODY_AMOUNT = 3
BODY_DENSITY = 10
MAX_BODY_MASS = math.pi * (300 ** 2) * BODY_DENSITY