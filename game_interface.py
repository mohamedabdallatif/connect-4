import pygame
from init_game import *
from Human_vs_AI import play_AI_vs_Human
from AI_vs_AI import play_AI_vs_AI 

intro = True
active = False
color_active = RED
color_passive = BRIGHT_RED
color = color_passive
game_mode = None

pygame.init()
pygame.display.set_caption('Connect 4 Game')
intro_screen = pygame.display.set_mode(size)
smallText = pygame.font.SysFont("monospace", 25)
mediumText = pygame.font.SysFont("monospace", 35)
largeText = pygame.font.SysFont("monospace", 110)

def button(msg, x, y, w, h, ic, ac, action=None):
    global with_alpha_beta
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(intro_screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(intro_screen, ic, (x, y, w, h))
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    intro_screen.blit(textSurf, textRect)

def text_objects(text, font):
    textsurface = font.render(text, True, BLACK)
    return textsurface, textsurface.get_rect()

def set_alpha_beta_option(val):
    global alpha_beta_option
    with_alpha_beta = val

def set_game_mode(mode):
    global game_mode
    game_mode = mode

def play_game():
    global game_mode, intro
    global input_depth
    if game_mode == None:
        pass
    intro = False
    game_mode(int(input_depth))

def main():    
    global input_depth, active, intro, color, color_active, color_passive
    depth_input_field = pygame.Rect((width / 2 - 30, 550, 50, 45))
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                active  = depth_input_field.collidepoint(event.pos)
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        input_depth = input_depth[: -1]
                    else:
                        input_depth += event.unicode
        color = color_active if active else color_passive
        intro_screen.fill(SCREEN_BACKGROUND)
        # Connect 4 Large Text
        TextSurf1, TextRect1 = text_objects("CONNECT 4", largeText)
        TextRect1.center = ((width / 2), 100)
        intro_screen.blit(TextSurf1, TextRect1)
        
        # Choose Mode Text
        TextSurf2, TextRect2 = text_objects("Select Game Mode", smallText)
        TextRect2.center = ((width / 2), 200)
        intro_screen.blit(TextSurf2, TextRect2)
        
        # Two Game Modes
        button("AI VS AI", 350, 250, 200, 50, RED, BRIGHT_RED, lambda : set_game_mode(play_AI_vs_AI))
        button("Human VS AI", 100, 250, 200, 50, GREEN, BRIGHT_GREEN, lambda : set_game_mode(play_AI_vs_Human))
        
        # Choose to apply alpha beta or not
        TextSurf3, TextRect3 = text_objects("Apply Alpha Beta Pruning ?", smallText)
        TextRect3.center = ((width / 2), 350)
        intro_screen.blit(TextSurf3, TextRect3)
        
        # Two AI Options
        button("YES", 100, 400, 200, 50, GREEN, BRIGHT_GREEN, lambda : set_alpha_beta_option(True))
        button("NO", 350, 400, 200, 50, RED, BRIGHT_RED, lambda : set_alpha_beta_option(False))
        
        # Entry Field to input AI Depth
        TextSurf4, TextRect4 = text_objects("Enter MinMax Tree Depth", smallText)
        TextRect4.center = ((width / 2), 500)
        intro_screen.blit(TextSurf4, TextRect4)
        
        # Draw Depth Input Field
        pygame.draw.rect(intro_screen, color, depth_input_field, 2)
        text_surface = mediumText.render(input_depth, True, BLACK)
        intro_screen.blit(text_surface, (depth_input_field.x + 5, depth_input_field.y + 5))
        depth_input_field.w = max(30, text_surface.get_width() + 10)

        # Play Button
        button("Play", 250, 620, 200, 50, TEAL, BRIGHT_TEAL, play_game)
        pygame.display.update()

main()
