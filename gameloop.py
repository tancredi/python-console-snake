
import time
import stage
import theme
import graphics
import gameloop
import gamelogic
import config

frame = 0
last_update = None


def draw():

    for y in range(0, stage.inner_size[1]):

        for x in range(0, stage.inner_size[0]):
            graphics.screen.addstr(
                stage.padding[0] + y, stage.padding[3] + x,
                theme.get_tile('bg'),
                theme.get_color('bg')
                )

    graphics.drawFrame()
    graphics.drawSnake()


def update():
    graphics.screen.clear()
    draw()
    graphics.screen.refresh()


def start():
    while True:
        cur_time = time.time()

        if gameloop.last_update:
            elapsed = cur_time - gameloop.last_update
        else:
            elapsed = None

        if not elapsed or elapsed > config.frame_len:
            update()
            gamelogic.frame += 1
            gamelogic.last_update = cur_time
