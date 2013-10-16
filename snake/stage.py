
import console
import math
import config
import parser
import themes


def init():
    global size, width, height, padding, boundaries, chosen_theme

    available_size = (width, height) = console.getTerminalSize()

    chosen_size = config.game_sizes[parser.options.size]

    if parser.options.fullscreen:
        width = available_size[0] / 2 - 2
        height = available_size[1]
    else:
        if chosen_size[0] > available_size[0] / 2:
            width = available_size[0] / 2
        else:
            width = chosen_size[0]

        if chosen_size[1] > available_size[1]:
            height = available_size[1]
        else:
            height = chosen_size[1]

    size = (width, height)

    padding_x = int(math.floor(available_size[0] - width) / 4)
    padding_y = int(math.floor(available_size[1] - height) / 2)

    padding = (padding_y, padding_x, padding_y, padding_x)

    boundaries = {
        "bottom": int(math.floor(height / 2)),
        "left": int(math.floor(-width / 2)),
        "right": int(math.floor(width / 2)),
        "top": int(math.floor(-height / 2)),
    }

    chosen_theme = themes.game_themes[parser.options.theme]
