
import curses

#COLOR_BLACK
#COLOR_RED
#COLOR_GREEN
#COLOR_YELLOW
#COLOR_BLUE
#COLOR_MAGENTA
#COLOR_CYAN
#COLOR_WHITE

game_themes = {
    'classic': {
        "colors": {
            "default": (curses.COLOR_WHITE, curses.COLOR_BLACK),
            "bg": (curses.COLOR_WHITE, curses.COLOR_WHITE),
            "snake": (curses.COLOR_GREEN, curses.COLOR_GREEN),
            "apple": (curses.COLOR_RED, curses.COLOR_RED),
            "border": (curses.COLOR_YELLOW, curses.COLOR_YELLOW),
        },
        "tiles": {
        }
    },
    'minimal': {
        "colors": {
            "default": (curses.COLOR_WHITE, curses.COLOR_BLACK),
            "bg": (curses.COLOR_BLACK, curses.COLOR_BLACK),
            "snake": (curses.COLOR_WHITE, curses.COLOR_BLACK),
            "apple": (curses.COLOR_WHITE, curses.COLOR_BLACK),
            "border": (curses.COLOR_WHITE, curses.COLOR_BLACK),
        },
        "tiles": {
            "snake-body": '[]',
            "apple": '()',
            "border-h": '-',
            "border-v": ' |',
            "border-c": ' +',
        }
    },
    'jungle': {
        "colors": {
            "default": (curses.COLOR_WHITE, curses.COLOR_BLACK),
            "bg": (curses.COLOR_GREEN, curses.COLOR_BLACK),
            "snake": (curses.COLOR_WHITE, curses.COLOR_RED),
            "apple": (curses.COLOR_CYAN, curses.COLOR_BLACK),
            "border": (curses.COLOR_GREEN, curses.COLOR_GREEN),
        },
        "tiles": {
            "bg": '~',
            "snake-body": ' ',
            "apple": '@-',
        }
    },
}
