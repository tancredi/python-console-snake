
import stage
import gameloop
import math
import random
import config

direction = (0, 0)
lastPos = (0, 0)
snake = []
speed = 1
apples = []
grow = config.initial_size - 1
score = 0
lives = 3


def init():
    global score, lives

    reset()
    score = 0
    lives = 3


def update():
    moveSnake()
    checkCatch()
    checkPositionAllowed()


def checkCatch():
    if not len(snake) or not len(apples):
        return

    for i, apple in enumerate(apples):
        if (snake[0][0]) == apple[0] and (snake[0][1]) == apple[1]:
            eatApple(i)


def eatApple(i):
    global grow, score

    apples.pop(i)
    spawnApple()
    grow += config.food_values['apple']
    score += 1


def moveSnake():
    global grow, lastPos

    last_unchanged = None
    lastPos = (snake[len(snake)-1][0], snake[len(snake)-1][1])
    for i, part in enumerate(snake):
        if i == 0:
            x = part[0] + speed * direction[0]
            y = part[1] + speed * direction[1]
        else:
            x = last_unchanged[0]
            y = last_unchanged[1]

        last_unchanged = (snake[i][0], snake[i][1])
        snake[i] = (x, y)

    if grow:
        snake.append(last_unchanged)
        grow -= 1


def getGameArea():
    w = math.fabs(stage.boundaries['right'] - stage.boundaries['left'])
    h = math.fabs(stage.boundaries['top'] - stage.boundaries['bottom'])

    return int(math.floor(w * h))


def reset():
    global direction, snake, apples_count, apples, score, grow, lives

    direction = (1, 0)
    snake = [(0, 0)]
    gameloop.frame = 1
    apples_count = 1
    apples = []
    grow = config.initial_size - 1

    apples_count += int(math.floor(getGameArea() / config.apple_domain))

    for i in range(0, apples_count):
        spawnApple()


def spawnApple():
    if len(apples) >= getGameArea():
        return

    x = random.randrange(stage.boundaries['left'], stage.boundaries['right'])
    y = random.randrange(stage.boundaries['top'], stage.boundaries['bottom'])

    position_free = True

    for apple in apples:
        if apple[0] == x and apple[1] == y:
            position_free = False

    for part in snake:
        if part[0] == x and part[1] == y:
            position_free = False

    if position_free and not isOutOfBoundaries(x, y):
        apples.append((x, y))
    else:
        spawnApple()


def isOutOfBoundaries(x, y):
    if x < stage.boundaries['left'] or x > stage.boundaries['right'] - 1:
        return True

    elif y < stage.boundaries['top'] or y > stage.boundaries['bottom'] - 1:
        return True

    return False


def checkPositionAllowed():
    global lives

    collides_with_body = False
    x = snake[0][0]
    y = snake[0][1]

    for i in range(1, len(snake) - 1):
        if x == snake[i][0] and y == snake[i][1]:
            collides_with_body = True
            break

    if (collides_with_body or isOutOfBoundaries(x, y)):
        gameloop.reset()
        lives -= 1
        if lives == 0:
            gameloop.state = 1
