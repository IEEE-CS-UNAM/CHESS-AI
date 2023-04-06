"""
Handles user input and main code. 
"""

import pygame as p
import ChessEngine 
import time 

p.init()

WIDTH = 520
HEIGHT = 520 

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (59, 59, 59) 

# Every number contains different color options for the board.
# Every list has a light - dark color combination in RGB
BOARD_COLORS = {0:[(234, 233, 210), (75, 115, 153)], 
                1:[(240, 217, 181), (181, 136, 99)],
                2:[(238, 238, 210), (118, 150, 86)],
                3:[(106, 114, 131), (42, 48, 61)]}
SQ_SIZE = WIDTH // 8 
screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("IEEE CS UNAM - CHESS AI")
# First, we set a grey background
screen.fill(GREY) 
p.display.update()                                         
# All images of chess pieces
IMAGES = {}
rects = []

# FONT 
font = p.font.SysFont("Arial", 16)
txtsurf = font.render("Select a chessboard color", True, WHITE)


# Draws all color options for the users to chose from. 
def draw_options(screen):
    global rects
    y_displacement = -120
    for key, value in BOARD_COLORS.items():
        c1, c2 = value[0], value[1] # Color pair (light and dark square)
        x = WIDTH/2 - 60            # x pos of rect
        y = HEIGHT/2 + key*SQ_SIZE + y_displacement # y pos of rect
        r1 = p.Rect(x, y, SQ_SIZE, SQ_SIZE) # pygame rect 1
        r2 = p.Rect(x + SQ_SIZE, y, SQ_SIZE, SQ_SIZE) # pygame rect 2
        p.draw.rect(screen, c1, r1) 
        p.draw.rect(screen, c2, r2)
        y_displacement += 20
        rects.append([r1, r2])
        p.display.update()

        
# This function loads all images and adds them to a dict. 
# Images MUST be named as shown in 'pieces' + .png 
# We only load this function once
def load_images():
    pieces = ["WP", "WK", "WQ", "WN", "WR", "WB", 
              "BP", "BK", "BQ", "BN", "BR", "BB"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(f"images/{piece}.png"), (SQ_SIZE, SQ_SIZE))

def draw_gameState(screen, gs):
    """
    Draws all graphics that corresponds to all gamestate
    """
    draw_pieces(screen, gs.board) #draws pieces on squares of board


def draw_board(screen, board_color_number):
    """
    Draws the squares on the board. 
    Board_color_number is the number that chooses which color set to use for the board.
    """
    colors = BOARD_COLORS[board_color_number]
    for i in range(8):
        for j in range(8):
            color = colors[((i+j)%2)]
            p.draw.rect(screen, color, p.Rect(j*SQ_SIZE, i*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces(screen, board):
    """
    Draws pieces on top of the squares. 
    """
    # Iterate through GameState.board
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != "--": # not an empty square
                screen.blit(IMAGES[piece], p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_game_over_text(screen):
    """
    Creates fonts objects and displays the 
    text when the game is over.
    """
    font = p.font.SysFont("Arial", 32, bold=True)
    txtsurf = font.render("Choose a color for the chessboard", False, WHITE) 
    font2 = p.font.SysFont("Arial", 16)
    txtsurf2 = font2.render("Created by IEEE UNAM CS", False, WHITE)
    txtsurf3 = font2.render("Version - -", False, WHITE)

    screen.blit(txtsurf, (50, 65))
    screen.blit(txtsurf2, (25, 500))
    screen.blit(txtsurf3, (400, 500))

def run():
    gs = ChessEngine.GameState()
    load_images()
    running = True # Running relates to closing pygame
    game_over = True # Losing or restarting the game
    color_selected = False 
    board_color = -1
    draw_options(screen) # draws all different board color options.
    while running: 

        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
            if not game_over:
                # Logic when the game is NOT over
                pass
            else:
                draw_game_over_text(screen)
                if event.type == p.MOUSEBUTTONDOWN:
                    pos = p.mouse.get_pos()
                    if not color_selected:
                        if rects[0][0].collidepoint(pos) or rects[0][1].collidepoint(pos):
                            board_color = 0
                            color_selected = True
                            game_over = False
                        elif rects[1][0].collidepoint(pos) or rects[1][1].collidepoint(pos):
                            board_color = 1
                            color_selected = True
                            game_over = False
                        elif rects[2][0].collidepoint(pos) or rects[2][1].collidepoint(pos):
                            board_color = 2
                            color_selected = True
                            game_over = False
                        elif rects[3][0].collidepoint(pos) or rects[3][1].collidepoint(pos):
                            board_color = 3
                            color_selected = True
                            game_over = False
                        
        
        if not game_over:
            draw_board(screen, board_color) # draws squares on board
            draw_gameState(screen, gs)
        else:
            # start menu
            pass


       
        p.display.update()
    p.quit()


if __name__ == "__main__":
    run()