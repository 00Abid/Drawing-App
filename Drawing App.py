import pygame
import numpy as np

# Initialize pygame
pygame.init()

# Set the window size
window_size = (800, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption('Drawing App')

# Run the app until the user closes the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Check if the left mouse button is pressed
    if pygame.mouse.get_pressed()[0]:
        # Draw a circle at the mouse position
        pygame.draw.circle(screen, (255, 0, 0), mouse_pos, 5)

    # Update the window
    pygame.display.flip()

# Quit pygame
pygame.quit()
