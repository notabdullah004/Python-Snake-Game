# Python-Snake-Game
PyGame For Snake Game
Python-Snake-Game
Snake Game in Pygame

A simple Snake Game created using the Pygame library in Python. The objective is to control a snake that moves around the screen to collect food, growing in size with each item consumed. The game ends if the snake collides with itself or the boundaries of the screen.

Features

Basic Gameplay: Move the snake in four directions (Up, Down, Left, Right) to collect food.

Score System: Each food item eaten increases the score by 1.

Game Over: The game ends when the snake hits the border or itself.

Pygame Rendering: The game uses Pygame to handle graphics and user input.

Requirements

Python 3.x

Pygame library

Install Pygame:

If you don't have Pygame installed, you can install it using pip:

pip install pygame

Run the game:

python snake_game.py

Controls

Arrow Keys: Use the arrow keys to control the snake's direction:

Up: Move Up

Down: Move Down

Left: Move Left

Right: Move Right

Game Over Condition

The game ends if:

The snake hits the boundaries of the screen.

The snake collides with itself.

Customization

You can modify the following parameters to customize the game:

WIDTH and HEIGHT: Adjust the screen dimensions.

CELL_SIZE: Change the size of each snake segment and food.

clock.tick(15): Adjust the game speed (15 FPS by default).
