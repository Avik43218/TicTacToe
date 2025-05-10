import sys
import pygame
import numpy as np

from assets.game_config import CongigSettings as C
from assets.game_utils import (draw_figures, draw_lines, is_square_available, mark_square,
                               check_win, best_move, is_board_full, restart_game)


pygame.init()


screen = pygame.display.set_mode((C.WIDTH, C.HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(C.BLACK)

board = np.zeros((C.BOARD_ROWS, C.BOARD_COLS))

draw_lines(screen=screen)

game_over = False
player = 1


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] // C.SQUARE_SIZE
            mouseY = event.pos[1] // C.SQUARE_SIZE

            if is_square_available(board=board, row=mouseY, col=mouseX):
                mark_square(board=board, row=mouseY, col=mouseX, player=player)
                draw_figures(screen=screen, board=board)

                if check_win(player=player, target_board=board):
                    game_over = True
                player = 3 - player

                if not game_over:
                    if best_move(board=board):
                        if check_win(player=2, target_board=board):
                            game_over = True
                        player = 3 - player

                if not game_over:
                    if is_board_full(target_board=board):
                        game_over = True
                         

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:

                restart_game(screen=screen, board=board)
                game_over = False
                player = 1

    if not game_over:
        draw_figures(screen=screen, board=board)

    else:
        
        if check_win(player=1, target_board=board):
            draw_lines(screen=screen, color=C.GREEN)
            draw_figures(screen=screen, board=board, color=C.GREEN)

        elif check_win(player=2, target_board=board):
            draw_lines(screen=screen, color=C.RED)
            draw_figures(screen=screen, board=board, color=C.RED)

        elif is_board_full(target_board=board):
            draw_lines(screen=screen, color=C.GRAY)
            draw_figures(screen=screen, board=board, color=C.GRAY)

    pygame.display.update()
