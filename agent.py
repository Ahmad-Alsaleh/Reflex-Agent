import turtle
from typing import Literal

from rich import print as pprint

from configs import settings


def check_wall(current_position: tuple[int, int], heading: float) -> bool:
    x, y = current_position
    heading = heading % 360
    if heading == 0:
        return x == settings.num_of_cells - 1
    elif heading == 90:
        return y == settings.num_of_cells - 1
    elif heading == 180:
        return x == 0
    elif heading == 270:
        return y == 0
    raise ValueError(
        f"Invalid `heading`: {heading}. Must be one of `[0, 90, 180, 270]`"
    )


class Agent:
    def __init__(self) -> None:
        self._agent = turtle.Turtle()
        self._agent.shapesize(2, 2)
        self._current_position = settings.agent_init_position
        self._go_to_cell(self._current_position)

    def _go_to_cell(self, cell_coordinates: tuple[int, int]) -> None:
        x, y = [
            (coord - settings.num_of_cells // 2) * settings.cell_size
            for coord in cell_coordinates
        ]
        if settings.num_of_cells % 2 == 0:
            x += settings.cell_size / 2
            y += settings.cell_size / 2
        self._agent.penup()
        turtle.tracer(0)
        self._agent.goto(x, y)
        self._agent.pendown()
        turtle.tracer(1, 40)

    @property
    def _heading(self) -> Literal[0, 90, 180, 270]:
        heading = int(self._agent.heading())
        if heading not in (0, 90, 180, 270):
            raise ValueError(
                f"Invalid heading: {heading}. Must be one of `[0, 90, 180, 270]`"
            )
        return heading  # type: ignore[return-value]

    def reached_goal(self) -> bool:
        return self._current_position == settings.goal_position

    def move_forward(self) -> None:
        if self.check_wall_in_front():
            pprint("[red]ERROR:[/] Cannot move forward. There is a wall in front.")
            return
        direction_map = {0: (1, 0), 90: (0, 1), 180: (-1, 0), 270: (0, -1)}
        dx, dy = direction_map[self._heading]
        current_x, current_y = self._current_position
        self._current_position = (current_x + dx, current_y + dy)
        self._agent.forward(settings.cell_size)

    def turn_left(self) -> None:
        self._agent.left(90)

    def turn_right(self) -> None:
        self._agent.right(90)

    def check_wall_in_front(self) -> bool:
        return check_wall(self._current_position, self._heading)

    def check_wall_on_left(self) -> bool:
        return check_wall(self._current_position, self._heading + 90)

    def check_wall_on_right(self) -> bool:
        return check_wall(self._current_position, self._heading - 90)

    def stop(self) -> None:
        turtle.done()
