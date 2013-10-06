
import graphics
import game
from config import keys


def update():
    key = graphics.screen.getch()
    grown = len(game.snake) > 1

    if key > 0:

        if key == keys['DOWN']:
            if grown and game.direction[1] == -1:
                return

            game.direction = (0, 1)

        elif key == keys['LEFT']:
            if grown and game.direction[0] == 1:
                return

            game.direction = (-1, 0)

        elif key == keys['RIGHT']:
            if grown and game.direction[0] == -1:
                return

            game.direction = (1, 0)

        elif key == keys['UP']:
            if grown and game.direction[1] == 1:
                return

            game.direction = (0, -1)
