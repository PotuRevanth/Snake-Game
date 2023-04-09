import tkinter as tk
import random

# Set up the window
window = tk.Tk()
window.title("Snake Game")

# Set up the canvas
canvas_width = 400
canvas_height = 400
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
canvas.pack()

# Set up the initial position of the snake and the food
snake_x = canvas_width / 2
snake_y = canvas_height / 2
food_x = random.randint(0, canvas_width)
food_y = random.randint(0, canvas_height)

# Set up the initial velocity of the snake
velocity_x = 10
velocity_y = 0

# Draw the snake and the food
snake = canvas.create_rectangle(snake_x, snake_y, snake_x + 10, snake_y + 10, fill="green")
food = canvas.create_oval(food_x, food_y, food_x + 10, food_y + 10, fill="red")

# Set up the game loop
def game_loop():
    global snake_x, snake_y, velocity_x, velocity_y, food_x, food_y, score
    # Move the snake
    snake_x += velocity_x
    snake_y += velocity_y
    canvas.coords(snake, snake_x, snake_y, snake_x + 10, snake_y + 10)
    # Check if the snake has hit the wall
    if snake_x < 0 or snake_x > canvas_width or snake_y < 0 or snake_y > canvas_height:
        game_over()
        return
    # Check if the snake has hit the food
    if canvas.coords(snake) == canvas.coords(food):
        canvas.delete(food)
        food_x = random.randint(0, canvas_width)
        food_y = random.randint(0, canvas_height)
        food = canvas.create_oval(food_x, food_y, food_x + 10, food_y + 10, fill="red")
        score += 1
    # Set up the next loop
    window.after(100, game_loop)

# Set up the controls for the snake
def left(event):
    global velocity_x, velocity_y
    velocity_x = -10
    velocity_y = 0
def right(event):
    global velocity_x, velocity_y
    velocity_x = 10
    velocity_y = 0
def up(event):
    global velocity_x, velocity_y
    velocity_x = 0
    velocity_y = -10
def down(event):
    global velocity_x, velocity_y
    velocity_x = 0
    velocity_y = 10

# Set up the game over function
def game_over():
    canvas.create_text(canvas_width / 2, canvas_height / 2, text="Game Over!", font=("Helvetica", 20))
    window.unbind("<Left>")
    window.unbind("<Right>")
    window.unbind("<Up>")
    window.unbind("<Down>")

# Set up the score
score = 0
score_text = tk.Label(window, text="Score: {}".format(score))
score_text.pack()

# Bind the controls to the window
window.bind("<Left>", left)
window.bind("<Right>", right)
window.bind("<Up>", up)
window.bind("<Down>", down)

# Start the game loop
game_loop()

# Start the window
window.mainloop()
