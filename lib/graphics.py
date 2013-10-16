
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
    drawTile(
        (stage.width / 2) - 1,
        (-stage.height / 2) - 1,
        score_formatted,
        theme.get_color('border')
        )


def drawLives():
    posx = (-stage.width / 2) + 3
    for x in xrange(1, game.lives + 1):
        posx += 1
        drawTile(
            posx,
            (-stage.height / 2) - 1,
            theme.get_tile('lives'),
            theme.get_color('lives')
            )
        posx += 1
        drawTile(
            posx,
            (-stage.height / 2) - 1,
            theme.get_tile('border-h'),
            theme.get_color('border')
            )


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
    tile_v = theme.get_tile('border-v')
    tile_h = theme.get_tile('border-h')
    tile_c = theme.get_tile('border-c')
    color = theme.get_color('border')

    x_left = stage.boundaries['left']
    x_right = stage.boundaries['right']

    y_top = stage.boundaries['top']
    y_bottom = stage.boundaries['bottom']

    for y in range(y_top, y_bottom):
        drawTile(x_left - 1, y, tile_v, color)
        drawTile(x_right, y, tile_v, color)

    for x in range(x_left, x_right):
        drawTile(x, y_top - 1, tile_h, color)
        drawTile(x, y_bottom, tile_h, color)

    drawTile(x_left - 1, y_top - 1, tile_c, color)
    drawTile(x_left - 1, y_bottom, tile_c, color)
    drawTile(x_right, y_top - 1, tile_c, color)
    drawTile(x_right, y_bottom, tile_c, color)


def drawText():
    color = theme.get_color('border')
    drawTile((stage.width / 2) - 4, (-stage.height / 2) - 1, "score:", color)
    drawTile((-stage.width / 2), (-stage.height / 2) - 1, "lives:", color)
    drawTile(-5, (stage.height / 2), " Press Q to quit ", color)


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
