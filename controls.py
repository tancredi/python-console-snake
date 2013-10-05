
import graphics
import gamelogic
from config import keys


def update():
    key = graphics.screen.getch()

    if key > 0:

        if key == keys['DOWN']:
            gamelogic.direction = (0, 1)

        elif key == keys['LEFT']:
                gamelogic.direction = (-1, 0)

        elif key == keys['RIGHT']:
            gamelogic.direction = (1, 0)

        elif key == keys['UP']:
            gamelogic.direction = (0, -1)
