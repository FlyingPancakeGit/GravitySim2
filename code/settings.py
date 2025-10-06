import pygame
import math

# setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1260, 840
BACKGROUND_COLOR = '#1e1e1e'
BODY_COLOR = '#38d4ff'

# properties
GRAVITATIONAL_CONSTANT = 1
BODY_AMOUNT = 10
BODY_DENSITY = 10