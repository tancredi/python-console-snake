import stage
import game
import theme
import curses

screen = None


def draw_tile(x, y, tile='', color=None):
    color = color or theme.get_color('default')

    x = x * 2 + stage.padding[3] * 2 + stage.width / 2
    y += stage.padding[0] + stage.height / 2

    screen.addstr(y, x, tile, color)
    if len(tile) < 2:
        screen.addstr(y, x + 1, tile, color)


def draw_game_over():
    draw_tile(-4, -1, " GAME OVER ", theme.get_color('border'))
    draw_tile(-7, 1, " Press ENTER to restart ", theme.get_color('border'))


def draw_score():
    score_formatted = str(game.score).zfill(2)
    draw_tile(
        (stage.width / 2) - 1,
        (-stage.height / 2) - 1,
        score_formatted,
        theme.get_color('border')
    )


def draw_lives():
    posx = (-stage.width / 2) + 3
    for x in xrange(1, game.lives + 1):
        posx += 1
        draw_tile(
            posx,
            (-stage.height / 2) - 1,
            theme.get_tile('lives'),
            theme.get_color('lives')
        )
        posx += 1
        draw_tile(
            posx,
            (-stage.height / 2) - 1,
            theme.get_tile('border-h'),
            theme.get_color('border')
        )


def draw_snake():
    for part in game.snake:
        draw_tile(
            part[0],
            part[1],
            theme.get_tile('snake-body'),
            theme.get_color('snake')
        )
    # Clean last tile
    draw_tile(
        game.lastPos[0],
        game.lastPos[1],
        theme.get_tile('bg'),
        theme.get_color('bg')
    )


def draw_apples():
    for apple in game.apples:
        draw_tile(
            apple[0],
            apple[1],
            theme.get_tile('apple'),
            theme.get_color('apple')
        )


def draw_game():
    for y in range(stage.boundaries['top'], stage.boundaries['bottom']):
        for x in range(stage.boundaries['left'], stage.boundaries['right']):
            draw_tile(x, y, theme.get_tile('bg'), theme.get_color('bg'))
    draw_borders()
    draw_text()


def draw_borders():
    tile_v = theme.get_tile('border-v')
    tile_h = theme.get_tile('border-h')
    tile_c = theme.get_tile('border-c')
    color = theme.get_color('border')

    x_left = stage.boundaries['left']
    x_right = stage.boundaries['right']

    y_top = stage.boundaries['top']
    y_bottom = stage.boundaries['bottom']

    for y in range(y_top, y_bottom):
        draw_tile(x_left - 1, y, tile_v, color)
        draw_tile(x_right, y, tile_v, color)

    for x in range(x_left, x_right):
        draw_tile(x, y_top - 1, tile_h, color)
        draw_tile(x, y_bottom, tile_h, color)

    draw_tile(x_left - 1, y_top - 1, tile_c, color)
    draw_tile(x_left - 1, y_bottom, tile_c, color)
    draw_tile(x_right, y_top - 1, tile_c, color)
    draw_tile(x_right, y_bottom, tile_c, color)


def draw_text():
    color = theme.get_color('border')
    draw_tile((stage.width / 2) - 4, (-stage.height / 2) - 1, "score:", color)
    draw_tile((-stage.width / 2), (-stage.height / 2) - 1, "lives:", color)
    draw_tile(-5, (stage.height / 2), " Press Q to quit ", color)


def update():
    draw_snake()
    draw_apples()
    draw_score()
    draw_lives()


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
