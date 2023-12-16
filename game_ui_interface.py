import pygame

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (400, 200)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pygame Window")

# Set colors
WHITE = pygame.Color('white')
BLACK = pygame.Color('black')

# Create fonts
font = pygame.font.Font(None, 24)

# Create text fields
text_field1 = pygame.Rect(50, 50, 300, 30)
text_field2 = pygame.Rect(50, 100, 300, 30)

# Create buttons
button1 = pygame.Rect(50, 150, 100, 30)
button2 = pygame.Rect(250, 150, 100, 30)

# Run the main loop
while True:
    text_field2_text = 'Text Field 2'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if button1.collidepoint(mouse_pos):
                    text_field1_text = "Button 1 clicked!"
                elif button2.collidepoint(mouse_pos):
                    text_field2_text = "Button 2 clicked!"

    # Fill the window with white color
    window.fill(WHITE)

    # Draw the text fields
    pygame.draw.rect(window, BLACK, text_field1, 2)
    pygame.draw.rect(window, BLACK, text_field2, 2)

    # Draw the buttons
    pygame.draw.rect(window, BLACK, button1)
    pygame.draw.rect(window, BLACK, button2)

    # Render text
    text1 = font.render("Text Field 1", True, BLACK)
    text2 = font.render(text_field2_text, True, BLACK)
    text_button1 = font.render("Button 1", True, BLACK)
    text_button2 = font.render("Button 2", True, BLACK)

    # Blit the text onto the window
    window.blit(text1, (text_field1.x + 5, text_field1.y + 5))
    window.blit(text2, (text_field2.x + 5, text_field2.y + 5))
    window.blit(text_button1, (button1.x + 5, button1.y + 5))
    window.blit(text_button2, (button2.x + 5, button2.y + 5))

    # Update the display
    pygame.display.update()
