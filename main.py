import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Простой Марио")

BLUE = (135, 206, 235)
GREEN = (0, 200, 0)

player_width, player_height = 60, 80
player_x = WIDTH // 2
player_y = HEIGHT - player_height - 40
player_vel = 5
jump_speed = 15
gravity = 1

player_y_speed = 0
is_jumping = False

mario_image = pygame.image.load("image 1.png")
mario_image = pygame.transform.scale(mario_image, (player_width, player_height))

platform_y = HEIGHT - 40

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    screen.fill(BLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_vel
    if keys[pygame.K_RIGHT]:
        player_x += player_vel
    if keys[pygame.K_SPACE] and not is_jumping:
        is_jumping = True
        player_y_speed = -jump_speed

    if is_jumping:
        player_y += player_y_speed
        player_y_speed += gravity

        if player_y >= HEIGHT - player_height - 40:
            player_y = HEIGHT - player_height - 40
            is_jumping = False
            player_y_speed = 0

    pygame.draw.rect(screen, GREEN, (0, platform_y, WIDTH, 40))
    screen.blit(mario_image, (player_x, player_y))
    pygame.display.flip()

pygame.quit()
sys.exit()
