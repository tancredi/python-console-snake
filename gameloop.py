
import time
import graphics
import game
import config
import controls

frame = 0
last_update = None
playing = False


def update():
    graphics.update()
    game.update()


def step():
    global last_update, frame

    controls.update()
    cur_time = time.time()

    if last_update:
        elapsed = cur_time - last_update
    else:
        elapsed = None

    if not elapsed or elapsed > config.frame_len:
        update()
        frame += 1
        last_update = cur_time


def start():
    global playing

    playing = True

    while playing:
        step()


def stop():
    global playing, frame, last_update

    playing = False
