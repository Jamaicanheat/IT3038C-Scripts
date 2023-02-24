import pygame
import random

# Set up the game window
pygame.init()
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the font
font = pygame.font.SysFont(None, 30)

# Set up the clock
clock = pygame.time.Clock()

# Set up the game variables
SNAKE_SIZE = 10
SNAKE_SPEED = 15
FOOD_SIZE = 10
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (WINDOW_WIDTH // 10)) * 10,
            random.randrange(1, (WINDOW_HEIGHT // 10)) * 10]
food_spawn = True
direction = "RIGHT"
change_to = direction
score = 0

# Define a function to display the score
def display_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    game_window.blit(score_text, [0, 0])

# Define a function to draw the snake
def draw_snake(snake_body):
    for pos in snake_body:
        pygame.draw.rect(game_window, GREEN,
                         pygame.Rect(pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))

# Define a function to draw the food
def draw_food(food_pos):
    pygame.draw.rect(game_window, RED,
                     pygame.Rect(food_pos[0], food_pos[1], FOOD_SIZE, FOOD_SIZE))

# Define a function to check for collisions
def check_collisions(snake_pos, snake_body, food_pos):
    # Check for collision with walls
    if snake_pos[0] >= WINDOW_WIDTH or snake_pos[0] < 0:
        return True
    if snake_pos[1] >= WINDOW_HEIGHT or snake_pos[1] < 0:
        return True
    # Check for collision with snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            return True
    # Check for collision with food
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        return True
    return False

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"

    # Update direction if necessary
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
