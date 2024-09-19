# Reflex Agent

## Overview

Reflex Agent is a simple grid-based game designed for the AI course (CMP 333) at the American University of Sharjah, UAE. In the game, the students should write a set of rules to navigate an agent to reach a goal autonomously. The game is built using Python and the Turtle graphics library.

## Features

- Grid-based map drawing
- Agent navigation with collision detection
- Configurable game settings
- Goal detection
- And more!

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Ahmad-Alsaleh/Reflex-Agent.git
    cd Reflex-Agent
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate # On macOS and Linux
    venv\Scripts\activate # On Windows
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Game settings can be configured in the `game.config` file. Here are the available settings:

> Note: The `[0, 0]` position is at the bottom-left corner of the grid.

### Main Settings

| Parameter             | Description                               | Note                                  | Default  |
|-----------------------|-------------------------------------------|---------------------------------------|----------|
| `AGENT_INIT_POSITION` | Initial position of the agent on the grid | None                                  | `[2, 3]` |
| `GOAL_POSITION`       | Position of the goal on the grid          | -1 and `NUM_OF_CELLS` + 1 are allowed | `[3, 6]` |

### Visual Settings (Optional)

| Parameter          | Description                          | Note                                  | Default           |
|--------------------|--------------------------------------|---------------------------------------|-------------------|
| `APP_NAME`         | Name of the application              | Used as the window name of the game   | `"Reflex Agent"`  |
| `NUM_OF_CELLS`     | Number of cells in the grid          | This is the number of cells per side  | `6`               |
| `WINDOW_SIZE`      | Size of the game window              | None                                  | `500`             |
| `BACKGROUND_COLOR` | Background color of the game window  | None                                  | `"white"`         |
| `GOAL_COLOR`       | Color of the goal                    | None                                  | `"green"`         |
| `GRID_COLOR`       | Color of the grid lines              | None                                  | `"gray"`          |
| `GRID_THICKNESS`   | Thickness of the grid lines          | None                                  | `5`               |

## Usage

1. Run the game:

    ```sh
    python main.py # If this didn't work, you might need to use `python3` on macOS and Linux or `py` on Windows
    ```

2. The agent will start at the initial position defined in the configuration. You can control the agent's movements by modifying the code in the `main.py` file.

## Code Structure

> Note: The only files you need to modify are main.py and game.config. The other files handle the game’s core functionality and shouldn’t be changed—unless you’re interested in experimenting with the game’s internals!

- `main.py`: Entry point of the game. Initializes the map and the agent.
- `agent.py`: Contains the `Agent` class which defines the agent's behavior and movements.
- `map.py`: Contains functions to draw the map and the goal.
- `configs.py`: Contains the `_Settings` class which loads and validates the game configuration.
- `game.config`: Configuration file for the game settings.

## Example

Here is an example of how to move the agent around the map in `main.py`:

```py
from rich import print as pprint

from agent import Agent
from map import draw_map

draw_map()

agent = Agent()

while True:
    if agent.reached_goal():
        pprint("[green]Goal reached!")
        agent.stop()
        break

    # Example movements
    agent.move_forward()
    agent.turn_right()
    agent.move_forward()
    agent.turn_left()
    agent.move_forward()
```
