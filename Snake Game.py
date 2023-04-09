import tkinter as tk

import random

# Initialize constants

WIDTH = 500

HEIGHT = 500

DELAY = 100

DOT_SIZE = 10

MAX_DOTS = WIDTH * HEIGHT / DOT_SIZE**2

# Initialize variables

score = 0

direction = "Right"

# Initialize snake

snake_dots = [[0, 0], [DOT_SIZE, 0], [DOT_SIZE*2, 0]]

# Create the window

root = tk.Tk()

root.title("Snake Game")

root.resizable(False, False)

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

canvas.pack()

# Create the score label

score_label = tk.Label(root, text=f"Score: {score}")

score_label.pack()

# Create the food

food_dot = canvas.create_rectangle(0, 0, DOT_SIZE, DOT_SIZE, fill="red")

# Define functions

def move_snake():

    global direction, snake_dots, score

    

    # Move the snake

    head = snake_dots[-1].copy()

    if direction == "Up":

        head[1] -= DOT_SIZE

    elif direction == "Down":

        head[1] += DOT_SIZE

    elif direction == "Left":

        head[0] -= DOT_SIZE

    elif direction == "Right":

        head[0] += DOT_SIZE

    snake_dots.append(head)

    snake_dots.pop(0)

    

    # Check if snake collided with wall

    if (head[0] < 0 or head[0] >= WIDTH or

        head[1] < 0 or head[1] >= HEIGHT):

        game_over()

        return

    

    # Check if snake collided with itself

    if head in snake_dots[:-1]:

        game_over()

        return

    

    # Check if snake collided with food

    if canvas.coords(food_dot) == canvas.coords(snake_dots[-1]):

        score += 1

        score_label.config(text=f"Score: {score}")

        canvas.coords(food_dot, random.randint(0, WIDTH-DOT_SIZE),

                      random.randint(0, HEIGHT-DOT_SIZE),

                      random.randint(0, WIDTH-DOT_SIZE)+DOT_SIZE,

                      random.randint(0, HEIGHT-DOT_SIZE)+DOT_SIZE)

        snake_dots.insert(0, snake_dots[0])

    

    # Move the snake

    canvas.delete("snake")

    for dot in snake_dots:

        canvas.create_rectangle(dot[0], dot[1],

                                 dot[0]+DOT_SIZE, dot[1]+DOT_SIZE,

                                 fill="green", tags="snake")

    # Schedule next move

    root.after(DELAY, move_snake)

    

def game_over():

    global score

    score = 0

    score_label.config(text=f"Score: {score}")

    canvas.delete("snake")

    snake_dots.clear()

    snake_dots.extend([[0, 0], [DOT_SIZE, 0], [DOT_SIZE*2, 0]])

    canvas.coords(food_dot, random.randint(0, WIDTH-DOT_SIZE),

                  random.randint(0, HEIGHT-DOT_SIZE),

                  random.randint(0, WIDTH-DOT_SIZE)+DOT_SIZE,

                  random.randint(0, HEIGHT-DOT_SIZE)+DOT_SIZE)

    direction = "Right"

def change_direction(event):

    global direction

    if event.keysym == "Up" and direction != "Down":

        direction = "Up"

    elif event.keysym == "Down" and direction != "Up":

        direction = "Down"

