import random

width = 60
height = 30
snake_skin = "@"
fence = "*"
food = "$"
snake_x = random.randint(1, width-2)
snake_y = random.randint(1, height-2)
boardgame = [[" " for _ in range(width)] for _ in range(height)]
num_food_collected = 0
num_snakes = 1


def initialize_boardgame():
    for i in range(height):
        boardgame[i][0] = fence
        boardgame[i][width-1] = fence

    for x in range(width):
        boardgame[0][x] = fence
        boardgame[height-1][x] = fence

    boardgame[snake_y][snake_x] = snake_skin
    place_food()


def draw_boardgame():
    for row in boardgame:
        print("".join(row))


def place_food():
    global num_food_collected

    while True:
        food_x = random.randint(1, width-2)
        food_y = random.randint(1, height-2)
        if boardgame[food_y][food_x] == " ":
            boardgame[food_y][food_x] = food
            break

    num_food_collected += 1


def grow_snake():
    global num_snakes
    num_snakes += 1
    place_food()


def update_game():
    global snake_x, snake_y
    print("A kukac ennyi gyümölcsöt evett:", num_food_collected - 1, "db")
    move = input("Hova?").lower()

    if move == "balra":
        snake_x -= 1
    elif move == "jobbra":
        snake_x += 1
    elif move == "fel":
        snake_y -= 1
    elif move == "le":
        snake_y += 1
    elif move == "meguntam":
        return False

    if (
        snake_x == 0 or
        snake_x == width - 1 or
        snake_y == 0 or
        snake_y == height - 1
    ):
        return False

    if boardgame[snake_y][snake_x] == food:
        grow_snake()

    if num_snakes > 1:
        snake_body = find_snake_body()
        if snake_body:
            body_x, body_y = snake_body[0]
            boardgame[body_y][body_x] = " "

    for y in range(height):
        for x in range(width):
            if boardgame[y][x] == snake_skin:
                boardgame[y][x] = " "

    for _ in range(num_snakes):
        boardgame[snake_y][snake_x] = snake_skin

    draw_boardgame()

    return True


def find_snake_body():
    snake_body = []
    for y in range(height):
        for x in range(width):
            if boardgame[y][x] == snake_skin:
                snake_body.append((x, y))
    return snake_body


initialize_boardgame()
draw_boardgame()
while update_game():
    pass

print("A kukac ennyi gyümölcsöt evett:", num_food_collected-1, "db")
print("Most ennyi volt, szép napot!")
