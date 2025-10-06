import math

from settings import *
from body import *


class Main:
    def __init__(self):
        # setup
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        pygame.display.set_caption('Gravity Simulator v2')

        # bodies
        self.body_sprites = pygame.sprite.Group()
        self.body_amount = BODY_AMOUNT

        self.body_being_set = False
        self.current_body_properties = {
            'pos': None,
            'mass': None,
            'radius': None,
            'velocity': None
        }
        self.can_set_body_properties = True
        self.body_property_setting_cooldown = 600
        self.last_property_setting_time = 0

        # input
        self.space_key_pressed = False

    def get_input(self):
        keys = pygame.key.get_pressed()

        if pygame.mouse.get_pressed()[0] and not self.body_being_set:
            self.body_being_set = True
        if keys[pygame.K_SPACE]:
            self.space_key_pressed = True
        else:
            self.space_key_pressed = False

    def display_radius(self):
        body_pos = self.current_body_properties['pos']
        radius = self.get_radius()

        pygame.draw.circle(self.display_surface, BODY_COLOR, body_pos, radius)

    def get_radius(self):
        if self.current_body_properties['radius']:
            radius = self.current_body_properties['radius']
        else:
            mouse_pos = pygame.mouse.get_pos()
            body_pos = self.current_body_properties['pos']
            displacement = pygame.math.Vector2(mouse_pos) - pygame.math.Vector2(body_pos)
            distance = math.sqrt(displacement.x ** 2 + displacement.y ** 2)
            radius = math.sqrt(distance)

        return radius

    def display_velocity(self):
        body_pos = self.current_body_properties['pos']
        end_pos = pygame.math.Vector2(body_pos) + self.get_velocity()

        pygame.draw.line(self.display_surface, (220, 220, 220), body_pos, end_pos, 3)

    def get_velocity(self):
        mouse_pos = pygame.mouse.get_pos()
        body_pos = self.current_body_properties['pos']
        velocity = pygame.math.Vector2(mouse_pos) - pygame.math.Vector2(body_pos)

        return velocity

    def check_can_set_body_properties(self):
        if pygame.time.get_ticks() - self.last_property_setting_time > self.body_property_setting_cooldown:
            self.can_set_body_properties = True
            self.last_property_setting_time = pygame.time.get_ticks()

    def display_body_properties(self):
        self.display_radius() # So that the user can always see the body whose properties are being set.

        if self.current_body_properties['velocity'] is None and self.current_body_properties['radius']: # Ensures that
            # the body's radius and velocity are not shown to change at the same time.
            self.display_velocity()

    def get_body_properties(self):
        if self.current_body_properties['pos'] is None:
            self.current_body_properties['pos'] = pygame.mouse.get_pos()

        if self.space_key_pressed and self.can_set_body_properties:
            if self.current_body_properties['mass'] is None:
                self.current_body_properties['mass'] = 1
            elif self.current_body_properties['radius'] is None:
                print('Setting radius...')
                self.current_body_properties['radius'] = self.get_radius()
            elif self.current_body_properties['velocity'] is None:
                self.current_body_properties['velocity'] = self.get_velocity()

            self.can_set_body_properties = False

        all_properties_filled = True
        for key, value in self.current_body_properties.items():
            if value is None:
                all_properties_filled = False

        if all_properties_filled:
            self.create_body()

    def create_body(self):
        body_pos = self.current_body_properties['pos']
        body_mass = self.current_body_properties['mass']
        body_radius = self.current_body_properties['radius']
        body_velocity = self.current_body_properties['velocity']

        Body((self.body_sprites), body_pos, body_mass, body_radius, body_velocity)

        self.body_being_set = False
        for key in self.current_body_properties:
            self.current_body_properties[key] = None
        self.body_amount -= 1

    def main_loop(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update
            if self.body_amount > 0:
                self.check_can_set_body_properties()
                self.get_input()

                if self.body_being_set:
                    self.get_body_properties()
            else:
                self.body_sprites.update(dt)

            # draw
            self.display_surface.fill(BACKGROUND_COLOR)
            self.body_sprites.draw(self.display_surface)

            if self.body_being_set:
                self.display_body_properties()

            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    main = Main()
    main.main_loop()