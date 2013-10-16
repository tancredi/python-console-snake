
import time
import graphics
import game
import config
import controls

last_update = None
playing = False
state = 0


def update():
    game.update()
    graphics.update()


def step():
    global last_update

    cur_time = time.time()

    if last_update:
        elapsed = cur_time - last_update
    else:
        elapsed = 0

    if not elapsed or elapsed > config.frame_len:

        if not elapsed:
            until_next = config.frame_len
        else:
            until_next = elapsed - config.frame_len
            time.sleep(until_next)

        update()
        last_update = time.time()


def start():
    global playing, state

    playing = True

    init()
    while playing:
        controls.update()
        if state == 0:
            step()
        elif state == 1:
            graphics.drawGameOver()


def stop():
    global playing, frame, last_update

    playing = False


def init():
    global state

    game.init()
    graphics.drawGame()
    state = 0


def reset():
    game.reset()
    graphics.drawGame()
