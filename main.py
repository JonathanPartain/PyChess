import pygame
import sys
from Tile import Tile
pygame.init()
width = 340
height = 340

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Chess')

pygame.font.init()
font = pygame.font.SysFont("monospace", 10)

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GRAY  = (100, 100, 100)
tilewidth = 40

# BOARD:
# P = PAWN
# R = ROOK
# K = KNIGHT
# B = BISHOP
# Q = QUEEN
# @ = KING
#
#        BLACK               COLORS
#    a b c d e f g h  |
#  8 R K B @ Q B K R  |   W B W B W B W B
#  7 P P P P P P P P  |   B W B W B W B W
#  6 % % % % % % % %  |   W B W B W B W B
#  5 % % % % % % % %  |   B W B W B W B W
#  4 % % % % % % % %  |   W B W B W B W B
#  3 % % % % % % % %  |   B W B W B W B W
#  2 P P P P P P P P  |   W B W B W B W B
#  1 R K B Q @ B K R  |   B W B W B W B W
#        WHITE
board = [[0 for x in range(8)] for y in range(8)]
tileList = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
numbers = [8, 7, 6, 5, 4, 3, 2, 1]
piece = None
print(numbers[7])
for num in range(0, 8):
    for let in range(0, 8):
        # Set piece
        if(numbers[num] == 8):
            if(letters[let] == 'a' or letters[let] == 'h'):
                piece = 'R'
            if(letters[let] == 'b' or letters[let] == 'g'):
                piece = 'K'
            if(letters[let] == 'c' or letters[let] == 'f'):
                piece = 'B'
            if(letters[let] == 'd'):
                piece = '@'
            if(letters[let] == 'e'):
                piece = 'Q'
        elif(numbers[num] == 7 or numbers[num] == 2):
            piece = 'P'
        elif(numbers[num] == 1):
            if(letters[let] == 'a' or letters[let] == 'h'):
                piece = 'R'
            if(letters[let] == 'b' or letters[let] == 'g'):
                piece = 'K'
            if(letters[let] == 'c' or letters[let] == 'f'):
                piece = 'B'
            if(letters[let] == 'd'):
                piece = 'Q'
            if(letters[let] == 'e'):
                piece = '@'
        else:
            piece = ''
        tmpTile = Tile(letters[let], numbers[num], piece)
        board[num][let] = tmpTile
        tmpList = tileList
        tmpList.append(tmpTile)
        tileList = tmpList
        # Change color of the tile
        color = WHITE
        if(num % 2 == 0 or num == 0):
            # Start with W
            if(let % 2 == 0 or let == 0):
                color = WHITE
            else:
                color = BLACK
        else:
            #start with B
            if(let % 2 == 0 or let == 0):
                color = BLACK
            else:
                color = WHITE

        # get all corner positions
        posy1 = num * tilewidth
        posx1 = let * tilewidth
        posy2 = posy1 + tilewidth
        posx2 = posx1 + tilewidth

        # set each tiles corner positions
        board[num][let].posx1 = posx1
        board[num][let].posx2 = posx2
        board[num][let].posy1 = posy1
        board[num][let].posy2 = posy2

        pygame.draw.rect(screen, color, (num * tilewidth, let * tilewidth, tilewidth, tilewidth))
        lbl = font.render(board[num][let].piece, 1, (0,255,0))
        screen.blit(lbl, (num*tilewidth+tilewidth/2, let * tilewidth + tilewidth/2))


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    mousex, mousey = pygame.mouse.get_pos()


    pygame.display.update()
