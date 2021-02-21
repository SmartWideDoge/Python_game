import pygame
pygame.init()
from levels import *
running = True

# creating window
resolution = (800, 600)
window = pygame.display.set_mode(resolution)
width, height = pygame.display.get_window_size()

# adding colors
WHITE,  BLACK, GREY = (255, 255, 255), (0, 0, 0), (90, 128, 128)
DARK_RED, BLUE, LIGHT_BLACK = (97, 0, 0), (97, 85, 166), (169, 169, 169)

# adding buttons
Game_back_button, back_button = pygame.image.load('back_button.png'), pygame.image.load('back_button.png')
back_button_rect = back_button.get_rect(bottomright=(260, 500))
Game_back_button_rect = Game_back_button.get_rect(bottomright=(60, 50))

font = pygame.font.SysFont('inkfree', 60)
small_font = pygame.font.SysFont('inkfree', 30)

# Black text
BText_continue = font.render('CONTINUE', True, BLACK)
BText_new_game = font.render('NEW GAME', True, BLACK)
BText_settings = font.render('SETTINGS', True, BLACK)
BText_quit = font.render('QUIT', True, BLACK)

# White text
WText_continue = font.render('CONTINUE', True, WHITE)
WText_new_game = font.render('NEW GAME', True, WHITE)
WText_settings = font.render('SETTINGS', True, WHITE)
WText_quit = font.render('QUIT', True, WHITE)

# another text
BlueText_settings = small_font.render('SETTINGS', True, BLUE)
BlueText_difficulty = small_font.render('Difficulty', True, BLUE)
BText_question = small_font.render('Are you sure?', True, BLACK)

BText_yes = small_font.render('YES', True, BLACK)
BText_no = small_font.render('NO', True, BLACK)
WText_yes = small_font.render('YES', True, WHITE)
WText_no = small_font.render('NO', True, WHITE)


def game():
    going = True
    while going:
        window.fill(DARK_RED)
        pygame.draw.rect(window, BLUE, pygame.Rect(400, 300, 60, 60))
        window.blit(Game_back_button, Game_back_button_rect)
        pygame.display.update()
        mouse_X, mouse_Y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if 15 < mouse_X < 53 and 13 < mouse_Y < 35 and event.type == pygame.MOUSEBUTTONDOWN:
                going = False


def new_game():
    doing = True
    while doing:
        pygame.draw.rect(window, BLACK, pygame.Rect(203, 297, 400, 200))
        pygame.draw.rect(window, WHITE, pygame.Rect(200, 300, 400, 200))
        window.blit(back_button, back_button_rect)
        window.blit(BText_question, (width / 2 - 75, height / 2))
        window.blit(BText_yes, (width / 2 - 100, height / 2 + 65))
        window.blit(BText_no, (width / 2 + 25, height / 2 + 65))
        mouse_X, mouse_Y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif 215 < mouse_X < 254 and 462 < mouse_Y < 487 and event.type == pygame.MOUSEBUTTONDOWN:
                doing = False
            elif 300 < mouse_X < 350 and 360 < mouse_Y < 410:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print('YES')
                window.blit(WText_yes, (width / 2 - 100, height / 2 + 65))
                pygame.display.update()
            elif 425 < mouse_X < 470 and 370 < mouse_Y < 390:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print('NO')
                    doing = False

                window.blit(WText_no, (width / 2 + 25, height / 2 + 65))
                pygame.display.update()
            else:
                window.blit(BText_yes, (width / 2 - 100, height / 2 + 65))
                window.blit(BText_no, (width / 2 + 25, height / 2 + 65))
                pygame.display.update()
    pygame.time.delay(100)


def settings():
    run = True
    while run:
        pygame.draw.rect(window, BLACK, pygame.Rect(203, 97, 400, 400))
        pygame.draw.rect(window, WHITE, pygame.Rect(200, 100, 400, 400))
        window.blit(BlueText_settings, (width / 2 - 95, height / 2 - 180))
        window.blit(BlueText_difficulty, (width / 2 - 70, height / 2 - 100))
        window.blit(back_button, back_button_rect)
        pygame.display.update()
        mouse_posX, mouse_posY = pygame.mouse.get_pos()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                quit()

            if 215 < mouse_posX < 254 and 462 < mouse_posY < 487 and i.type == pygame.MOUSEBUTTONDOWN:
                run = False


while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
    window.fill(GREY)
    mouse_X, mouse_Y = pygame.mouse.get_pos()
    if 398 < mouse_X < 715 and 280 < mouse_Y < 337:
        if i.type == pygame.MOUSEBUTTONDOWN:
            print('CONTINUE')
            game()
        window.blit(WText_continue, (width / 2, height / 2 - 40))
        window.blit(BText_new_game, (width / 2, height / 2 + 30))
        window.blit(BText_settings, (width / 2, height / 2 + 100))
        window.blit(BText_quit, (width / 2 + 50, height / 2 + 170))
        pygame.display.update()
    elif 398 < mouse_X < 715 and 337 < mouse_Y < 406:
        if i.type == pygame.MOUSEBUTTONDOWN:
            print('NEW GAME')
            new_game()
        window.blit(BText_continue, (width / 2, height / 2 - 40))
        window.blit(WText_new_game, (width / 2, height / 2 + 30))
        window.blit(BText_settings, (width / 2, height / 2 + 100))
        window.blit(BText_quit, (width / 2 + 50, height / 2 + 170))
        pygame.display.update()
    elif 398 < mouse_X < 715 and 406 < mouse_Y < 476:
        if i.type == pygame.MOUSEBUTTONDOWN:
            print('SETTINGS')
            settings()
        window.blit(BText_continue, (width / 2, height / 2 - 40))
        window.blit(BText_new_game, (width / 2, height / 2 + 30))
        window.blit(WText_settings, (width / 2, height / 2 + 100))
        window.blit(BText_quit, (width / 2 + 50, height / 2 + 170))
        pygame.display.update()
    elif 398 < mouse_X < 715 and 476 < mouse_Y < 564:
        if i.type == pygame.MOUSEBUTTONDOWN:
            print('QUIT')
            running = False
        window.blit(BText_continue, (width / 2, height / 2 - 40))
        window.blit(BText_new_game, (width / 2, height / 2 + 30))
        window.blit(BText_settings, (width / 2, height / 2 + 100))
        window.blit(WText_quit, (width / 2 + 50, height / 2 + 170))
        pygame.display.update()
    else:
        window.blit(BText_continue, (width / 2, height / 2 - 40))
        window.blit(BText_new_game, (width / 2, height / 2 + 30))
        window.blit(BText_settings, (width / 2, height / 2 + 100))
        window.blit(BText_quit, (width / 2 + 50, height / 2 + 170))

    pygame.display.update()
