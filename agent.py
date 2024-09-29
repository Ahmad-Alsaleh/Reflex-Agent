from contextlib import contextmanager
import turtle
from enum import Enum
from typing import Generator, Literal

from rich import print as pprint

from configs import settings


class Direction(Enum):
    FRONT = 0
    RIGHT = -90
    LEFT = 90


@contextmanager
def freeze_agent(agent: turtle.Turtle) -> Generator[None, None, None]:
    agent.penup()
    turtle.tracer(0)
    yield
    agent.pendown()
    turtle.tracer(1, 70)


class Agent:
    def __init__(self) -> None:
        self._agent = turtle.Turtle()
        self._agent.shapesize(2, 2)
        self._current_position = settings.agent_init_position
        with freeze_agent(self._agent):
            self._heading = settings.agent_init_heading
            self._go_to_cell(self._current_position)

    def _go_to_cell(self, cell_coordinates: tuple[int, int]) -> None:
        x, y = [
            (coord - settings.num_of_cells // 2) * settings.cell_size
            for coord in cell_coordinates
        ]
        if settings.num_of_cells % 2 == 0:
            x += settings.cell_size / 2
            y += settings.cell_size / 2
        self._agent.goto(x, y)

    @property
    def _heading(self) -> Literal[0, 90, 180, 270]:
        heading = int(self._agent.heading())
        if heading not in (0, 90, 180, 270):
            raise ValueError(
                f"Invalid heading: {heading}. Must be one of `[0, 90, 180, 270]`"
            )
        return heading  # type: ignore[return-value]

    @_heading.setter
    def _heading(self, direction: Literal["up", "down", "right", "left"]) -> None:
        heading_map = {"right": 0, "up": 90, "left": 180, "down": 270}
        angle = heading_map.get(direction)
        assert (
            angle is not None
        ), "heading should be one of `'up', 'down', 'right', 'left'`"
        self._agent.setheading(angle)

    def _check_obstacle(self, position: tuple[int, int]) -> bool:
        if position == settings.goal_position:
            return False
        if position in settings.obstacles_positions:
            return True
        return not all(0 <= coord < settings.num_of_cells for coord in position)

    def _calculate_new_position(self, move_direction: Direction) -> tuple[int, int]:
        direction_map = {0: (1, 0), 90: (0, 1), 180: (-1, 0), 270: (0, -1)}
        delta_x, delta_y = direction_map[(self._heading + move_direction.value) % 360]
        current_x, current_y = self._current_position
        return current_x + delta_x, current_y + delta_y

    def reached_goal(self) -> bool:
        return self._current_position == settings.goal_position

    def move_forward(self) -> None:
        new_position = self._calculate_new_position(Direction.FRONT)
        if self._check_obstacle(new_position):
            pprint("[red]ERROR:[/] Cannot move forward. There is a wall in front.")
            return
        self._current_position = new_position
        self._agent.forward(settings.cell_size)

    def turn_left(self) -> None:
        self._agent.left(90)

    def turn_right(self) -> None:
        self._agent.right(90)

    def check_wall_in_front(self) -> bool:
        new_position = self._calculate_new_position(Direction.FRONT)
        return self._check_obstacle(new_position)

    def check_wall_on_left(self) -> bool:
        new_position = self._calculate_new_position(Direction.RIGHT)
        return self._check_obstacle(new_position)

    def check_wall_on_right(self) -> bool:
        new_position = self._calculate_new_position(Direction.LEFT)
        return self._check_obstacle(new_position)

    def stop(self) -> None:
        turtle.done()
