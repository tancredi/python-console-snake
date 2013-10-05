
direction = (1, 0)
snake = [(0, 0)]
speed = 1


def update():
    move_snake()


def move_snake():
    prev_part = None

    for index, part in enumerate(snake):
        part_dir = direction

        if prev_part:
            if prev_part[0] > part[0]:
                dir[0] = 1
            else:
                dir[0] = -1

            if prev_part[1] > part[1]:
                dir[1] = 1
            else:
                dir[1] = -1

        x = part[0] + speed * part_dir[0]
        y = part[1] + speed * part_dir[1]

        snake[index] = (x, y)

        prev_part = part
