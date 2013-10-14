
import stage
import game
import theme
import curses

screen = None


def drawTile(x, y, tile='', color=None):
    color = color or theme.get_color('default')

    x = x * 2 + stage.padding[3] * 2 + stage.width / 2
    y += stage.padding[0] + stage.height / 2

    screen.addstr(y, x, tile, color)
    if (len(tile) < 2):
        screen.addstr(y, x + 1, tile, color)


def drawScore():
    score_formatted = str(game.score).zfill(2)
    drawTile(0, -stage.height / 2, score_formatted)


def drawSnake():
    for part in game.snake:
        drawTile(
            part[0],
            part[1],
            theme.get_tile('snake-body'),
            theme.get_color('snake')
            )
    # Clean last tile
    drawTile(
        game.lastPos[0],
        game.lastPos[1],
        theme.get_tile('bg'),
        theme.get_color('bg')
        )
    

def drawApples():
    for apple in game.apples:
        drawTile(
            apple[0],
            apple[1],
            theme.get_tile('apple'),
            theme.get_color('apple')
            )


def drawGame():
    for y in range(stage.boundaries['top'], stage.boundaries['bottom']):
        for x in range(stage.boundaries['left'], stage.boundaries['right']):
            drawTile(x, y, theme.get_tile('bg'), theme.get_color('bg'))
    drawBorders()


def drawBorders():
    for y in range(stage.boundaries['top'], stage.boundaries['bottom']):
        drawTile(stage.boundaries['left'] - 1, y, theme.get_tile('border-v'), theme.get_color('border'))
        drawTile(stage.boundaries['right'], y, theme.get_tile('border-v'), theme.get_color('border'))

    for x in range(stage.boundaries['left'], stage.boundaries['right']):
        drawTile(x, stage.boundaries['top'] - 1, theme.get_tile('border-h'), theme.get_color('border'))
        drawTile(x, stage.boundaries['bottom'], theme.get_tile('border-h'), theme.get_color('border'))
            
    drawTile(stage.boundaries['left'] - 1, stage.boundaries['top'] - 1, theme.get_tile('border-c'), theme.get_color('border'))
    drawTile(stage.boundaries['left'] - 1, stage.boundaries['bottom'], theme.get_tile('border-c'), theme.get_color('border'))
    drawTile(stage.boundaries['right'], stage.boundaries['top'] - 1, theme.get_tile('border-c'), theme.get_color('border'))
    drawTile(stage.boundaries['right'], stage.boundaries['bottom'], theme.get_tile('border-c'), theme.get_color('border'))


def update():

    drawSnake()
    drawApples()


def init():
    global screen

    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    curses.start_color()
    screen.nodelay(1)


def exit():
    screen.clear()
    screen.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
