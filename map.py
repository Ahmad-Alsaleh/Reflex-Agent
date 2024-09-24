import turtle
from enum import Enum, auto

from configs import settings

# type alias
Pen = turtle.Turtle


class PenType(Enum):
    BOX = auto()
    LINE = auto()


def draw_map() -> None:
    _init_screen()
    _draw_grid()
    _draw_obstacles()
    _draw_goal()
    _finish_drawing()


def _init_screen() -> None:
    turtle.bgcolor(settings.background_color)
    turtle.title(settings.app_name)
    turtle.tracer(0)


def _create_drawing_pen(pen_color: str, pen_type: PenType) -> Pen:
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color(pen_color)
    if pen_type == PenType.BOX:
        pen.shape("square")
        pen.shapesize(settings.cell_size / 20, settings.cell_size / 20)
    elif pen_type == PenType.LINE:
        pen.pensize(settings.grid_thickness)
    else:
        raise ValueError("Invalid value for `pen_type`.")
    pen.hideturtle()
    return pen


def _draw_grid() -> None:
    pen = _create_drawing_pen(settings.grid_color, PenType.LINE)
    for i in range(settings.num_of_cells + 1):
        position = -settings.window_size / 2 + i * settings.cell_size
        _draw_horizontal_line(pen, position)
        _draw_vertical_line(pen, position)


def _draw_horizontal_line(pen: Pen, position: float) -> None:
    pen.penup()
    pen.goto(-settings.window_size / 2, position)
    pen.pendown()
    pen.goto(settings.window_size / 2, position)


def _draw_vertical_line(pen: Pen, position: float) -> None:
    pen.penup()
    pen.goto(position, -settings.window_size / 2)
    pen.pendown()
    pen.goto(position, settings.window_size / 2)


def _fill_cell(pen: Pen, cell_position: tuple[int, int]) -> None:
    x, y = [
        (coord - settings.num_of_cells // 2) * settings.cell_size
        for coord in cell_position
    ]
    if settings.num_of_cells % 2 == 0:
        x += settings.cell_size / 2
        y += settings.cell_size / 2
    pen.penup()
    pen.goto(x, y)
    pen.stamp()


def _draw_goal() -> None:
    pen = _create_drawing_pen(settings.goal_color, PenType.BOX)
    _fill_cell(pen, settings.goal_position)


def _draw_obstacles() -> None:
    pen = _create_drawing_pen(settings.obstacles_color, PenType.BOX)
    for obstacle_position in settings.obstacles_positions:
        _fill_cell(pen, obstacle_position)


def _finish_drawing() -> None:
    turtle.update()
    turtle.tracer(1)
