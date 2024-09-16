import turtle

from configs import settings


class Agent:
    def __init__(self) -> None:
        self._agent = turtle.Turtle()
        if (settings.MAP_SIZE / settings.CELL_SIZE) % 2 == 0:
            self._agent.penup()
            self._agent.goto(settings.CELL_SIZE / 2, settings.CELL_SIZE / 2)
            self._agent.pendown()

    def reached_goal(self) -> bool:
        if tuple(map(int, self._agent.pos())) == settings.goal_position:
            return True

    def move_forward(self) -> None:
        self._agent.forward(settings.cell_size)

    def turn_left(self) -> None:
        self._agent.left(90)

    def turn_right(self) -> None:
        self._agent.right(90)

    def stop(self) -> None:
        turtle.done()

    def is_in_front_of_wall(self) -> bool:
        x, y = self._agent.pos()
        map_boundary = settings.MAP_SIZE / 2
        return (
            x <= -map_boundary
            or x >= map_boundary
            or y <= -map_boundary
            or y >= map_boundary
        )
