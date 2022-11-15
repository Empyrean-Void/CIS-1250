# Imports #
import pygame
import os

# Constants #
WIDTH, HEIGHT = 1500, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 120

VEL = 5
ATTACK_VEL = 10
HEAVY_ATTACK_VEL = 5

MAX_HEAVY_ATTACK = 5

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 80, 80

SPACESHIP_YELLOW_IMAGE = pygame.image.load(
    os.path.join('assets', 'spaceship_yellow.png'))
SPACESHIP_YELLOW = pygame.transform.rotate(pygame.transform.scale(
    SPACESHIP_YELLOW_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

SPACESHIP_RED_IMAGE = pygame.image.load(
    os.path.join('assets', 'spaceship_red.png'))
SPACESHIP_RED = pygame.transform.rotate(
    pygame.transform.scale(SPACESHIP_RED_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)


# Functions #
def set_title():
    pygame.display.set_caption('Space Wars')


def controls_yellow(keys_pressed, yellow):
    # Movment
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # Up
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < 800:  # Down
        yellow.y += VEL
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # Left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < 1500:  # Right
        yellow.x += VEL

    # Rotation
    if keys_pressed[pygame.K_q]:  # Left
        pass
    if keys_pressed[pygame.K_e]:  # Right
        pass

    # Attack
    if keys_pressed[pygame.K_f]:  # Light
        pass
    if keys_pressed[pygame.K_g]:  # Heavy
        pass


def controls_red(keys_pressed, red):
    # Movment
    if keys_pressed[pygame.K_o] and red.y - VEL > 0:  # Up
        red.y -= VEL
    if keys_pressed[pygame.K_l] and red.y - VEL + red.height < 800:  # Down
        red.y += VEL
    if keys_pressed[pygame.K_k] and red.x - VEL > 0:  # Left
        red.x -= VEL
    if keys_pressed[pygame.K_SEMICOLON] and red.x - VEL + red.width < 1500:  # Right
        red.x += VEL

    # Rotation
    if keys_pressed[pygame.K_i]:  # Left
        pass
    if keys_pressed[pygame.K_p]:  # Right
        pass

    # Attack
    if keys_pressed[pygame.K_j]:  # Light
        pass
    if keys_pressed[pygame.K_h]:  # Heavy
        pass


def handle_attacks(yellow_attacks, red_attacks, yellow, red):
    pass


def handle_heavy_attacks(yellow_heavy_attacks, red_heavy_attacks, yellow, red):
    pass


def draw_window(yellow, red):
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    colors = [WHITE, RED, BLUE]

    WIN.fill((colors[0]))

    WIN.blit(SPACESHIP_YELLOW, (yellow.x, yellow.y))
    WIN.blit(SPACESHIP_RED, (red.x, red.y))

    pygame.display.update()


def main():
    set_title()

    yellow = pygame.Rect(300, 100, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(700, 100, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    yellow_attacks = []
    yellow_heavy_attacks = []

    red_attacks = []
    red_heavy_attacks = []

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:  # Yellow light attack
                    attack = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height / 2 - 2, 10, 5)
                    yellow_attacks.append(attack)
                # Yellow heavy attack
                if event.key == pygame.K_g and len(yellow_heavy_attacks) < MAX_HEAVY_ATTACK:
                    heavy_attack = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height / 2 - 2, 10, 5)
                    yellow_heavy_attacks.append(heavy_attack)

                if event.key == pygame.K_j:  # Red light attack
                    attack = pygame.Rect(
                        red.x + red.width, red.y + red.height / 2 - 2, 10, 5)
                    red_attacks.append(attack)
                # Red heavy attack
                if event.key == pygame.K_h and len(red_heavy_attacks) < MAX_HEAVY_ATTACK:
                    heavy_attack = pygame.Rect(
                        red.x + red.width, red.y + red.height / 2 - 2, 10, 5)
                    red_heavy_attacks.append(heavy_attack)

        keys_pressed = pygame.key.get_pressed()

        controls_yellow(keys_pressed, yellow)
        controls_red(keys_pressed, red)

        handle_attacks(yellow_attacks, red_attacks, yellow, red)
        handle_heavy_attacks(yellow_heavy_attacks,
                             red_heavy_attacks, yellow, red)

        draw_window(yellow, red)

    pygame.quit()


# Main #
if __name__ == "__main__":
    main()
