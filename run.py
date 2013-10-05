
import graphics
import theme
import gameloop


def exit():
    graphics.exit()
    print 'Come back soon!'


def run():
    try:

        graphics.init()
        theme.init()
        gameloop.start()

    except KeyboardInterrupt:
        exit()

run()
