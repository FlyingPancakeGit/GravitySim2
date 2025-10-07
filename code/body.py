from settings import *


class Body(pygame.sprite.Sprite):
    def __init__(self, groups, pos, mass, radius, velocity, colour):
        # setup
        super().__init__(groups)
        self.image = pygame.Surface((radius * 2, radius * 2))
        self.image.fill(BACKGROUND_COLOR)
        pygame.draw.circle(self.image, colour, (radius, radius), radius)
        self.rect = self.image.get_frect(center=pos)

        # properties
        self.velocity = velocity
        self.mass = mass
        self.radius = radius
        self.colour = colour

    def update(self, dt):
        pass