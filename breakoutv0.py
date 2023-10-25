# Version: 0.0.0
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
BALL_RADIUS = 10
BRICK_WIDTH = 60
BRICK_HEIGHT = 20

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Breakout')

# Initialize paddle
paddle = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)

# Initialize ball
ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_dx = 5
ball_dy = -5

# Initialize bricks
bricks = [pygame.Rect(x * (BRICK_WIDTH + 10), y * (BRICK_HEIGHT + 5) + 30, BRICK_WIDTH, BRICK_HEIGHT) for x in range(10) for y in range(4)]

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        paddle.move_ip(-10, 0)
    if keys[pygame.K_RIGHT]:
        paddle.move_ip(10, 0)
        
    # Move the ball
    ball.move_ip(ball_dx, ball_dy)
    
    # Ball collision with walls
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_dx *= -1
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_dy *= -1
    
    # Ball collision with paddle
    if ball.colliderect(paddle):
        ball_dy *= -1
        
    # Ball collision with bricks
    for brick in bricks[:]:
        if ball.colliderect(brick):
            ball_dy *= -1
            bricks.remove(brick)
    
    # Clear screen
    screen.fill(WHITE)
    
    # Draw paddle
    pygame.draw.rect(screen, BLUE, paddle)
    
    # Draw ball
    pygame.draw.ellipse(screen, GREEN, ball)
    
    # Draw bricks
    for brick in bricks:
        pygame.draw.rect(screen, BLUE, brick)
        
    pygame.display.update()
    
    # Check for game over conditions
    if len(bricks) == 0:
        print("You win!")
        pygame.quit()
        sys.exit()
    if ball.bottom >= SCREEN_HEIGHT:
        print("You lose!")
        pygame.quit()
        sys.exit()
    
    pygame.time.delay(30)
