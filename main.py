import pygame
import sys
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Snake settings
snake = [(100, 100), (80, 100), (60, 100)]
direction = 'RIGHT'
change_to = direction

# Food settings
food_pos = (random.randrange(1, WIDTH//CELL_SIZE) * CELL_SIZE,
            random.randrange(1, HEIGHT//CELL_SIZE) * CELL_SIZE)
food_spawn = True

# Score
score = 0
font = pygame.font.SysFont('Arial', 24)

def game_over():
    go_font = pygame.font.SysFont('Arial', 48)
    go_surf = go_font.render('Game Over', True, RED)
    screen.blit(go_surf, (WIDTH//2 - go_surf.get_width()//2, HEIGHT//2 - go_surf.get_height()//2))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    direction = change_to

    # Move snake
    x, y = snake[0]
    if direction == 'UP':
        y -= CELL_SIZE
    elif direction == 'DOWN':
        y += CELL_SIZE
    elif direction == 'LEFT':
        x -= CELL_SIZE
    elif direction == 'RIGHT':
        x += CELL_SIZE
    new_head = (x, y)

    # Check collisions
    if (x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or new_head in snake):
        game_over()

    snake.insert(0, new_head)

    # Check food
    if new_head == food_pos:
        score += 1
        food_spawn = False
    else:
        snake.pop()

    if not food_spawn:
        food_pos = (random.randrange(1, WIDTH//CELL_SIZE) * CELL_SIZE,
                    random.randrange(1, HEIGHT//CELL_SIZE) * CELL_SIZE)
        food_spawn = True

    # Draw everything
    screen.fill(BLACK)
    for pos in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

    score_surf = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_surf, (10, 10))

    pygame.display.update()
    clock.tick(15)