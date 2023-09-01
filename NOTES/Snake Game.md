# Pygame:

- Pygame is a cross-platform set of Python modules designed for writing video games.
- It provides functionality for creating 2D games, graphics, animations, and interactive applications.
- Using pygame we can handle: Graphics , Sound and Music, User Input, Event Handling, collision detection

```py

# Importing Libraries:

# This imports the Pygame library, allowing you to use its functions and modules for game development.
import pygame
import time  # provides various time-related functions.
import random # allows you to generate random numbers

# Initialize pygame
# This initializes the Pygame library. It's necessary to call this function before using any other Pygame functions or modules
pygame.init()

#-----------------------------------------
# Set up display
width = 1200  # 1200 pixels
height = 600

# This line creates a display surface (game window) with the specified width and height. It initializes the main window where the game graphics will be rendered.
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

#-----------------------------------------------
# Colors
# define color values using RGB values:
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

#---------------------------------------------------
# Snake properties
snake_block = 20  # Size of snake in pixels
snake_speed = 30  # Speed of snake

#-----------------------------------------
# Fonts
# This line initializes a font style to be used for rendering text in the game
# None means = Default font
# 50 = font size
font_style = pygame.font.SysFont(None, 50)

#------------------------------------------
score = 0

#-----------------------------------------------
# This line uses the render method of the font_style font object to create a rendered text surface. The rendered text will display the player's score,

# white color of text
# True: smoothing applied to text. the text will be displayed with smoother edges, making it easier to read and improving the visual quality of the text on the screen

# uses the blit method to draw the score_text surface onto the game display surface (display)

# The (10, 10) tuple specifies the position at which the top-left corner of the rendered text should be placed. In this case, it's positioned at coordinates (10, 10) pixels.

def show_score(score):
    score_text = font_style.render(f"Score: {score}", True, white)
    display.blit(score_text, (10, 10))

# ---------------------------------------------------
def snake_game():
    global score

    game_over = False # keeps track of whether the game is over or not.

    game_close = False # keeps track of whether the game has been closed

    # Snake initial position
    x1 = width // 2 # Initial x-coordinate of the snake.
    y1 = height // 2 #  Initial y-coordinate of the snake.

    x1_change = 0 #  Initial change in x-coordinate (no movement)
    y1_change = 0 # Initial change in y-coordinate (no movement).

    snake_list = [] # A list to store the coordinates of the snake's body segments.

    length_of_snake = 1 # Initial length of the snake's body.

    # Food initial position:

    #  This generates a random x-coordinate within the range [0, width - snake_block).

    # The width - snake_block ensures that the food doesn't appear too close to the right edge of the game window.

    # / 20.0: This division scales down the random x-coordinate by 20.0. This step is intended to ensure that the food is placed at specific intervals, making its position align with the grid.

    food_x = round(random.randrange(0, width - snake_block) / 20.0) * 20.0  # Increased size of food
    food_y = round(random.randrange(0, height - snake_block) / 20.0) * 20.0  # Increased size of food

    while not game_over:
    # central loop that controls the game's progression

        while game_close == True:
            # This loop runs when the game is in a "game over" state

            display.fill(black) # It fills the screen with a black background

            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update() # It updates the display to show the message

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        snake_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                # If 'LEFT' is pressed, the snake's x-coordinate changes by a negative value (x1_change = -snake_block), moving it to the left.
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # This block of code checks if the snake's head has reached the boundaries of the game window

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

       # Updating Coordinates and Clearing Screen:
        x1 += x1_change
        y1 += y1_change
        display.fill(black)

        # Drawing Food and Snake's Head:
        pygame.draw.rect(display, green, [food_x, food_y, snake_block, snake_block])

       # Updating Snake's Body:
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Collision Detection with Self:
        # This loop iterates through the segments of the snake's body (snake_list[:-1]) except for the head.
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # The snake function is called to draw the snake's body using the snake_list
        snake(snake_block, snake_list)

        show_score(score)
        pygame.display.update()

        # Food Consumption and Score Update:
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 20.0) * 20.0  # Increased size of food
            food_y = round(random.randrange(0, height - snake_block) / 20.0) * 20.0  # Increased size of food
            length_of_snake += 1
            score += 10

        pygame.display.update()

        # The clock.tick(snake_speed) ensures that the game runs at a controlled frame rate, regulating how quickly the game loop iterates.
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# drawing the snake's body segments on the game screen.
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, white, [x[0], x[1], snake_block, snake_block])

# displaying messages on the game screen, such as game ove
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [width / 3, height / 2])

clock = pygame.time.Clock()
snake_game()
```

> /20:

- In the given code, you'll notice that the initial position of the food is determined by generating random x and y coordinates within certain ranges. However, to make the food's position align with a grid-like pattern, the code divides the random coordinates by a value (in this case, 20.0) and then rounds the result. The purpose of this division and rounding is to ensure that the food is placed at specific intervals on the game grid, making the game visually more organized and aligned.

- Here's an example to illustrate:

- Let's say the snake_block size (the size of both the snake's body segments and the food) is 20 pixels. When the game generates random x and y coordinates for the food, these coordinates might not always align perfectly with the grid. For instance, a random x-coordinate of 37 might not be aligned with the grid.

- By dividing the random x-coordinate by 20.0 (the snake_block size) and rounding it, you're essentially "snapping" the coordinate to the nearest multiple of the snake_block size. In this case, dividing 37 by 20.0 gives you approximately 1.85. Rounding 1.85 to the nearest whole number gives you 2. Multiplying 2 by 20.0 gives you 40, which is a coordinate that aligns perfectly with the grid.

- This process ensures that the food is always placed at specific intervals of the snake_block size, making the food's position neatly align with the grid created by the snake's body segments. The result is a cleaner and more organized visual representation of the game.

> Co-ordinate system:

- In most graphical coordinate systems, the y-axis typically increases as you move downwards. This means that the top of the screen has a smaller y-coordinate value than the bottom of the screen. When dealing with screen coordinates, positive y values represent downward movement, and negative y values represent upward movement.
- In the context of the code you provided for the Snake game, the game screen's coordinate system follows this convention. Here's a simple illustration of the screen's coordinate system

```
(0,0) --------------------------->
  |
  |
  |
  |
  |
  V

```

- When the UP arrow key is pressed, the intention is to make the snake move upwards on the screen. To achieve this, you need to decrease the y-coordinate of the snake's position. Since negative y values represent upward movement in this coordinate system, changing the y-coordinate by a negative value will indeed move the snake upwards on the screen.
