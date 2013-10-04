
import console

size = (width, height) = console.getTerminalSize()

padding = (5, 5, 5, 5)

inner_size = (
    size[0] - padding[1] - padding[3],
    size[1] - padding[0] - padding[2] - 1
    )

game_size = (
    inner_size[0] / 2,
    inner_size[1]
    )

game_size = (
    inner_size[0] / 2,
    inner_size[1]
    )

inner_size = (
    size[0] - padding[1] - padding[3],
    size[1] - padding[0] - padding[2] - 1
    )
