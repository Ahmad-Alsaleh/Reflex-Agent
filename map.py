import turtle

from configs import settings

type Pen = turtle.Turtle


def draw_map() -> None:
    _init_screen()

    grid_pen = _create_drawing_pen(settings.GRID_COLOR)
    _draw_grid(grid_pen)

    goal_pen = _create_drawing_pen(settings.GOAL_COLOR, is_goal=True)
    _draw_goal(goal_pen)

    _finish_drawing()


def _init_screen() -> None:
    turtle.bgcolor(settings.BACKGROUND_COLOR)
    turtle.title(settings.APP_NAME)
    turtle.tracer(0)


def _create_drawing_pen(pen_color: str, is_goal: bool = False) -> Pen:
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color(pen_color)
    if is_goal:
        pen.shape("square")
        pen.shapesize(settings.CELL_SIZE / 20, settings.CELL_SIZE / 20)
    else:
        pen.pensize(settings.GRID_THICKNESS)
    pen.hideturtle()
    return pen


def _draw_grid(pen: Pen) -> None:
    for position in range(
        -settings.MAP_SIZE // 2,
        settings.MAP_SIZE // 2 + settings.CELL_SIZE,
        settings.CELL_SIZE,
    ):
        _draw_horizontal_line(pen, position)
        _draw_vertical_line(pen, position)


def _draw_horizontal_line(pen: Pen, position: int) -> None:
    pen.penup()
    pen.goto(-settings.MAP_SIZE / 2, position)
    pen.pendown()
    pen.goto(settings.MAP_SIZE / 2, position)


def _draw_vertical_line(pen: Pen, position: int) -> None:
    pen.penup()
    pen.goto(position, -settings.MAP_SIZE / 2)
    pen.pendown()
    pen.goto(position, settings.MAP_SIZE / 2)


def _draw_goal(pen: Pen) -> None:
    pen.penup()
    x, y = settings.GOAL_POSITION
    if (settings.MAP_SIZE / settings.CELL_SIZE) % 2 == 0:
        x -= settings.CELL_SIZE / 2
        y -= settings.CELL_SIZE / 2
    pen.goto(x, y)
    pen.stamp()


def _finish_drawing() -> None:
    turtle.update()
    turtle.tracer(1)
