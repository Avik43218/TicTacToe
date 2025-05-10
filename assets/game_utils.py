from assets.game_config import CongigSettings as C
import pygame


def draw_lines(screen, color=C.WHITE):

    for i in range(1, C.BOARD_ROWS):
        pygame.draw.line(surface=screen, color=color, start_pos=(0, C.SQUARE_SIZE * i), end_pos=(C.WIDTH, C.SQUARE_SIZE * i))
        pygame.draw.line(surface=screen, color=color, start_pos=(C.SQUARE_SIZE * i, 0), end_pos=(C.SQUARE_SIZE * i, C.WIDTH))

def draw_figures(screen, board, color=C.WHITE):

    for row in range(C.BOARD_ROWS):
        for col in range(C.BOARD_COLS):

            if board[row][col] == 1:
                pygame.draw.circle(surface=screen, color=color, center=(int(col * C.SQUARE_SIZE + C.SQUARE_SIZE // 2),\
                                                                int(row * C.SQUARE_SIZE + C.SQUARE_SIZE // 2)),\
                                                                radius=C.CIRCLE_RADIUS,\
                                                                width=C.CIRCLE_WIDTH)
                
            elif board[row][col] == 2:
                pygame.draw.line(surface=screen, color=color, start_pos=(col * C.SQUARE_SIZE + C.SQUARE_SIZE // 4, row * C.SQUARE_SIZE + C.SQUARE_SIZE // 4),\
                                 end_pos=(col * C.SQUARE_SIZE + 3 * (C.SQUARE_SIZE // 4), row * C.SQUARE_SIZE + 3 * (C.SQUARE_SIZE // 4)),\
                                 width=C.LINE_WIDTH)
                
                pygame.draw.line(surface=screen, color=color, start_pos=(col * C.SQUARE_SIZE + 3 * (C.SQUARE_SIZE // 4), row * C.SQUARE_SIZE + C.SQUARE_SIZE // 4),\
                                 end_pos=(col * C.SQUARE_SIZE + C.SQUARE_SIZE // 4, row * C.SQUARE_SIZE + 3 * (C.SQUARE_SIZE // 4)),\
                                 width=C.LINE_WIDTH)

def mark_square(board, row, col, player):
    board[row][col] = player


def is_square_available(board, row, col):
    return board[row][col] == 0


def is_board_full(target_board):

    for row in range(C.BOARD_ROWS):
        for col in range(C.BOARD_COLS):
            if target_board[row][col] == 0:
                return False
    return True


def check_win(player, target_board):

    for col in range(C.BOARD_COLS):
        if target_board[0][col] == player and target_board[1][col] == player and target_board[2][col] == player:
            return True

    for row in range(C.BOARD_ROWS):
        if target_board[row][0] == player and target_board[row][1] == player and target_board[row][2] == player:
            return True

    if target_board[0][0] == player and target_board[1][1] == player and target_board[2][2] == player:
        return True
    
    elif target_board[2][0] == player and target_board[1][1] == player and target_board[0][2] == player:
        return True

    return False


def minimax_algorithm(minimax_board, depth, is_maximising):

    if check_win(player=2, target_board=minimax_board):
        return float('inf')
    elif check_win(player=1, target_board=minimax_board):
        return float('-inf')
    elif is_board_full(target_board=minimax_board):
        return 0

    
    if is_maximising:
        best_score = -1000
        for row in range(C.BOARD_ROWS):
            for col in range(C.BOARD_COLS):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 2
                    score = minimax_algorithm(minimax_board=minimax_board, depth=depth + 1, is_maximising=False)
                    minimax_board[row][col] = 0
                    best_score = max(score, best_score)
        return best_score

    else:
        best_score = 1000
        for row in range(C.BOARD_ROWS):
            for col in range(C.BOARD_COLS):
                if minimax_board[row][col] == 0:
                    minimax_board[row][col] = 1
                    score = minimax_algorithm(minimax_board=minimax_board, depth=depth + 1, is_maximising=True)
                    minimax_board[row][col] = 0
                    best_score = min(score, best_score)
        return best_score


def best_move(board):

    best_score = -1000
    move = (-1, -1)
    for row in range(C.BOARD_ROWS):
        for col in range(C.BOARD_COLS):
            if board[row][col] == 0:
                board[row][col] = 2
                score = minimax_algorithm(minimax_board=board, depth=0, is_maximising=False)
                board[row][col] = 0
                if score > best_score:
                    best_score = score
                    move = (row, col)
    
    if move != (-1, -1):
        mark_square(board=board, row=move[0], col=move[1], player=2)
        return True
    return False

def restart_game(screen, board):

    screen.fill(C.BLACK)
    draw_lines()
    
    for row in range(C.BOARD_ROWS):
        for col in range(C.BOARD_COLS):
            board[row][col] = 0

