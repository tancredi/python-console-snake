
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


def drawGameOver():
    drawTile(-4, -1, " GAME OVER ", theme.get_color('border'))
    drawTile(-7, 1, " Press ENTER to restart ", theme.get_color('border'))


def drawScore():
    score_formatted = str(game.score).zfill(2)
    drawTile((stage.width / 2) - 1, (-stage.height / 2) - 1, score_formatted, theme.get_color('border'))


def drawLives():
    posx = (-stage.width / 2) + 3
    for x in xrange(1, game.lives + 1):
        posx += 1
        drawTile(posx, (-stage.height / 2) - 1, theme.get_tile('lives'), theme.get_color('lives'))
        posx += 1
        drawTile(posx, (-stage.height / 2) - 1, theme.get_tile('border-h'), theme.get_color('border'))


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
    drawText()


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


def drawText():
    drawTile((stage.width / 2) - 4, (-stage.height / 2) - 1, "score:", theme.get_color('border'))
    drawTile((-stage.width / 2), (-stage.height / 2) - 1, "lives:", theme.get_color('border'))
    drawTile(-5, (stage.height / 2), " Press Q to quit ", theme.get_color('border'))


def update():

    drawSnake()
    drawApples()
    drawScore()
    drawLives()


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
