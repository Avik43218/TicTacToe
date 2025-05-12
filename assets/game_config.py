class CongigSettings:

    # Colors

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    GRAY = (180, 180, 180)
    DARK_GRAY = (30, 30, 30)

    # Board Settings

    WIDTH = 600
    HEIGHT = 600
    LINE_WIDTH = 5
    CROSS_LINE_WIDTH = 10
    BOARD_ROWS = 3
    BOARD_COLS = 3
    SQUARE_SIZE = WIDTH // BOARD_COLS
    CIRCLE_RADIUS = SQUARE_SIZE // 3
    CIRCLE_WIDTH = 15
    CROSS_WIDTH = 25

    # Main Menu
    # Button Styles

    EASY_BUTTON = (200, 200, 200, 50)
    MEDIUM_BUTTON = (200, 280, 200, 50)
    HARD_BUTTON = (200, 360, 200, 50)

    EASY_BUTTON_COLOR = (40, 180, 60)
    MEDIUM_BUTTON_COLOR = (200, 180, 60)
    HARD_BUTTON_COLOR = (200, 30, 30)

    # Title

    TITLE_COORDINATE = (191, 120)
    FONT_SIZE = 40

    # Difficulty Levels

    DIFFICULTY_LEVELS = {
        'EASY': {'max_depth': 1, 'noise': 2, 'skip_chances': 0.5},
        'MEDIUM': {'max_depth': 3, 'noise': 1, 'skip_chances': 0.2},
        'HARD': {'max_depth': 9, 'noise': 0, 'skip_chances': 0.0}
    }

    # Coordinates

    ORIGIN_X = 0
    ORIGIN_Y = 0