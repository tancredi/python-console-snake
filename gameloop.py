
import time
import graphics
import gamelogic
import config
import controls

frame = 0
last_update = None
playing = False


def update():
    graphics.update()
    gamelogic.update()


def start():
    global last_update, frame, playing

    playing = True

    while playing:
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


def stop():
    global playing, frame, last_update

    playing = False
