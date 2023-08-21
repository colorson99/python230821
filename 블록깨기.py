import pygame
import random

# Initialize Pygame
pygame.init()

# Game window dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Block Breaker")

# Ball properties
ball_radius = 20
ball_speed_x = 5
ball_speed_y = 5
ball_color = red
ball = pygame.Rect(screen_width // 2 - ball_radius, screen_height // 2 - ball_radius, ball_radius * 2, ball_radius * 2)

# Paddle properties
paddle_width = 150
paddle_height = 20
paddle_color = blue
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - paddle_height - 10, paddle_width, paddle_height)

# Block properties
block_width = 80
block_height = 30
block_color = white
blocks = [pygame.Rect(x, y, block_width, block_height) for x in range(0, screen_width - block_width + 1, block_width) for y in range(50, 200, block_height)]

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= 5
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.x += 5
    
    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Ball collision with walls
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x = -ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y
    
    # Ball collision with paddle
    if ball.colliderect(paddle):
        ball_speed_y = -ball_speed_y
    
    # Ball collision with blocks
    for block in blocks:
        if ball.colliderect(block):
            ball_speed_y = -ball_speed_y
            blocks.remove(block)
    
    # Draw everything
    screen.fill(black)
    pygame.draw.rect(screen, paddle_color, paddle)
    pygame.draw.circle(screen, ball_color, ball.center, ball_radius)
    for block in blocks:
        pygame.draw.rect(screen, block_color, block)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
