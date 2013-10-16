
import curses
import stage

colors_map = {}
theme = None
default_color = None


def init():
    global theme, colors_map, default_color

    theme = stage.chosen_theme
    colors_map = get_colors_map()
    default_color = theme['colors']['default']


def get_color(key):
    return curses.color_pair(colors_map.get(key, 0))


def get_tile(key):
    return theme['tiles'].get(key, ' ')


def get_colors_map():
    out = {}

    i = 1
    for col in theme['colors'].iteritems():
        curses.init_pair(i, col[1][0], col[1][1])
        out[col[0]] = i
        i += 1

    return out
