
from lib import graphics, theme, gameloop, game, parser, stage


def exit():
    graphics.exit()
    print 'Come back soon!'


def run():
    try:
        parser.init()
        stage.init()
        graphics.init()
        theme.init()
        game.reset()
        gameloop.start()

    except KeyboardInterrupt:
        exit()

run()
