"""
Handles user input and main code. 
"""

import pygame as p
import ChessEngine 

WIDTH = 520
HEIGHT = 520 
# Every number contains different color options for the board.
BOARD_COLORS = {1:[(234, 233, 210), (75, 115, 153)], 
                2:[(240, 217, 181), (181, 136, 99)],
                3:[(255, 255, 255), (0,0,0)]}
SQ_SIZE = WIDTH // 8 
# All images of chess pieces
IMAGES = {}

# This function loads all images and adds them to a dict. 
# Images MUST be named as shown in 'pieces' + .png 
def load_images():
    pieces = ["WP", "WK", "WQ", "WN", "WR", "WB", 
              "BP", "BK", "BQ", "BN", "BR", "BB"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(f"images/{piece}.png"), (SQ_SIZE, SQ_SIZE))

def draw_gameState(screen, gs):
    """
    Draws all graphics that corresponds to all gamestate
    """
    draw_board(screen, 2) # draws squares on board
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
    pass

def run():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    #load_images()
    running = True
    while running: 
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False

        draw_gameState(screen, gs)
        p.display.flip()
    p.quit()


if __name__ == "__main__":
    run()