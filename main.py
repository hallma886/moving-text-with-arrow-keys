# Draw Lines in Pygame / No Functions

# Pygame game template

import pygame
import sys
import config  # Import the config module

def draw_text(screen, text, x, y, font_size, color, font_name=None, bold=False, italic=False):
    if font_name:
        font = pygame.font.Font(font_name, font_size)
    else:
        font = pygame.font.Font(None, font_size)
    
    font.set_bold(bold)
    font.set_italic(italic)

    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False  # Return False to indicate quitting
    return True  # Continue running if no quit event

def main():

    screen = init_game()  # Initialize the game and get the screen
    clock = pygame.time.Clock() # Initialize the clock objecct
    
    # Define text properties and initial position
    text1 = "Sup"
    font_size1 = 48
    color1 = config.PURPLE
    x1, y1 = (300, 300)
 
    # Main game loop
    running = True
    while running:
        running = handle_events()  # Handle events and check if we should continue running

        # Handle key presses for movement
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w or pygame.K_UP]:
            y1 -= 5  # Move Up
        if keys[pygame.K_s or pygame.K_DOWN]:
            y1 += 5  # Move Down
        if keys[pygame.K_a or pygame.K_LEFT]:
            x1 -= 5  # Move Left
        if keys[pygame.K_d or pygame.K_RIGHT]:
            x1 += 5  # Move Right

        # Fill the screen with a background color 
        screen.fill(config.WHITE) 

        # Draw text on the screen using variables
        draw_text(screen, text1, x1, y1, font_size1, color1)



        pygame.display.flip()  # Update the display

        clock.tick(config.FPS) # Limit frame rate to specified number of frames per second (FPS)

    pygame.quit()  # Quit Pygame
    sys.exit()  # Exit the program

if __name__ == "__main__":
    main()  































