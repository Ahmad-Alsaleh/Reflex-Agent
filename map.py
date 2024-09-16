import turtle

from configs import settings

type Pen = turtle.Turtle


def draw_map() -> None:
    _init_screen()

    grid_pen = _create_drawing_pen(settings.grid_color)
    _draw_grid(grid_pen)

    goal_pen = _create_drawing_pen(settings.goal_color, is_goal=True)
    _draw_goal(goal_pen)

    _finish_drawing()


def _init_screen() -> None:
    turtle.bgcolor(settings.background_color)
    turtle.title(settings.app_name)
    turtle.tracer(0)


def _create_drawing_pen(pen_color: str, is_goal: bool = False) -> Pen:
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color(pen_color)
    if is_goal:
        pen.shape("square")
        pen.shapesize(settings.cell_size / 20, settings.cell_size / 20)
    else:
        pen.pensize(settings.grid_thickness)
    pen.hideturtle()
    return pen


def _draw_grid(pen: Pen) -> None:
    for i in range(settings.num_of_cells + 1):
        position = -settings.window_size / 2 + i * settings.cell_size
        _draw_horizontal_line(pen, position)
        _draw_vertical_line(pen, position)


def _draw_horizontal_line(pen: Pen, position: int) -> None:
    pen.penup()
    pen.goto(-settings.window_size / 2, position)
    pen.pendown()
    pen.goto(settings.window_size / 2, position)


def _draw_vertical_line(pen: Pen, position: int) -> None:
    pen.penup()
    pen.goto(position, -settings.window_size / 2)
    pen.pendown()
    pen.goto(position, settings.window_size / 2)


def _draw_goal(pen: Pen) -> None:
    x, y = [
        (coord - settings.num_of_cells // 2) * settings.cell_size
        for coord in settings.goal_position
    ]
    if settings.num_of_cells % 2 == 0:
        x += settings.cell_size / 2
        y += settings.cell_size / 2
    pen.penup()
    pen.goto(x, y)
    pen.stamp()


def _finish_drawing() -> None:
    turtle.update()
    turtle.tracer(1)
