
import stage
import gameloop
import gamelogic
import theme
import curses

screen = None


def drawTile(x, y, tile, color):
    x += stage.padding[3] + stage.game_size[0]
    y += stage.padding[0] + stage.game_size[1] / 2

    screen.addstr(y, x, tile, color)
    screen.addstr(y, x + 1, tile, color)


def drawSnake():
    for part in gamelogic.snake:
        drawTile(
            part[0],
            part[1],
            theme.get_tile('snake-body'),
            theme.get_color('snake')
            )


def drawFrame():
    padded_frame = str(gameloop.frame).zfill(2)

    screen.addstr(
        stage.padding[0],
        stage.inner_size[0] + stage.padding[0] - len(padded_frame),
        padded_frame
        )


def update():
    screen.clear()

    for y in range(0, stage.inner_size[1]):

        for x in range(0, stage.inner_size[0]):
            screen.addstr(
                stage.padding[0] + y, stage.padding[3] + x,
                theme.get_tile('bg'),
                theme.get_color('bg')
                )

    drawFrame()
    drawSnake()

    screen.refresh()


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
