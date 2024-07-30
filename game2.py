import pygame
import sys
import random
pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
player_size = 30
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 25
bullet_size = 10
bullet_speed = 5
bullets = []
enemy_size = 20
enemy_speed = 2
enemies = []
def draw_player(x, y):
    pygame.draw.rect(win, WHITE, (x, y, player_size, player_size))
def draw_bullet(x, y):
    pygame.draw.rect(win, WHITE, (x, y, bullet_size, bullet_size))
def draw_enemy(x, y):
    pygame.draw.rect(win, RED, (x, y, enemy_size, enemy_size))
def game_over():
    font = pygame.font.SysFont(None, 70)
    text = font.render("Game Over", True, WHITE)
    win.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 - 30))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        bullets.append([player_x + player_size // 2 - bullet_size // 2, player_y])
    bullets = [[bx, by - bullet_speed] for bx, by in bullets if by > 0]
    if random.random() < 0.02:
        enemies.append([random.randint(0, WIDTH - enemy_size), 0])
    enemies = [[ex, ey + enemy_speed] for ex, ey in enemies if ey < HEIGHT]
    for bx, by in bullets:
        for ex, ey in enemies:
            if ex < bx < ex + enemy_size and ey < by < ey + enemy_size:
                bullets.remove([bx, by])
                enemies.remove([ex, ey])
    for ex, ey in enemies:
        if player_x < ex < player_x + player_size and player_y < ey < player_y + player_size:
            game_over()
    win.fill((0, 0, 0))
    draw_player(player_x, player_y)
    for bx, by in bullets:
        draw_bullet(bx, by)
    for ex, ey in enemies:
        draw_enemy(ex, ey)
    pygame.display.flip()
    clock.tick(30)