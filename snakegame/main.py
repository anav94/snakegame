from turtle import Screen, Turtle
from snake import Snake
from food import Food
import time

def setup_screen():
    screen = Screen()
    screen.setup(height=600, width=600)
    screen.bgcolor("black")
    screen.title("Snakes on a Plane")
    screen.tracer(0)
    return screen

def create_score_display():
    score_display = Turtle()
    score_display.color("white")
    score_display.penup()
    score_display.hideturtle()
    score_display.goto(0, 260)  # Position it at the top center
    return score_display

def play_game(screen, score_display):
    # Initialize game objects
    snake = Snake()
    food = Food()
    score = 0

    # Function to update the score display
    def update_score():
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    # Update the score display initially
    update_score()

    # Listen for key presses
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # Move the snake
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            score += 1
            update_score()  # Update the score display
            snake.extend_snake()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            score_display.goto(0, 0)
            score_display.write("Game Over!", align="center", font=("Courier", 24, "normal"))

        # Detect collision with body
        for body_part in snake.snake_body[1:]:
            if snake.head.distance(body_part) < 10:
                game_is_on = False
                score_display.goto(0, 0)
                score_display.write("Game Over!", align="center", font=("Courier", 24, "normal"))

    # Ask the user if they want to play again
    play_again = screen.textinput("Game Over", "Do you want to play again? (yes/no)")
    if play_again and play_again.lower() in ["yes", "y"]:
        screen.clearscreen()
        screen = setup_screen()  # Reinitialize the screen
        score_display = create_score_display()  # Reinitialize the score display
        play_game(screen, score_display)
    else:
        screen.bye()

# Setup the screen and score display
screen = setup_screen()
score_display = create_score_display()

# Initial start prompt
start_game = screen.textinput("Welcome", "Press Enter to start the game")

if start_game is not None:
    # Start the game
    play_game(screen, score_display)

# Keep the window open
screen.mainloop()
