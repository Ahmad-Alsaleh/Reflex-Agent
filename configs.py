import random
from typing import Literal, Self

from pydantic import model_validator
from pydantic_settings import BaseSettings
from rich import print as pprint


class _Settings(BaseSettings):
    APP_NAME: str
    BACKGROUND_COLOR: str
    GRID_COLOR: str
    GRID_THICKNESS: int
    MAP_SIZE: int
    CELL_SIZE: int
    GOAL_POSITION: tuple[int, int] | Literal["random"]
    GOAL_COLOR: str

    @model_validator(mode="after")
    def validate_CELL_SIZE(self) -> Self:
        # check if CELL_SIZE is an even number
        if self.CELL_SIZE % 2:
            self.CELL_SIZE += 1
            pprint(
                "[bold yellow]WARNING:[/] `CELL_SIZE` should be an even number. "
                f"The value `CELL_SIZE = {self.CELL_SIZE}` will be used instead of the provided value."
            )

        # check if MAP_SIZE is a multiple of CELL_SIZE
        if self.MAP_SIZE % self.CELL_SIZE:
            self.MAP_SIZE = self.MAP_SIZE - self.MAP_SIZE % self.CELL_SIZE
            pprint(
                "[bold yellow]WARNING:[/] `MAP_SIZE` should be a multiple of `CELL_SIZE`. "
                f"The value `MAP_SIZE = {self.MAP_SIZE}` will be used instead of the provided value."
            )

        if self.GOAL_POSITION == "random":
            self.GOAL_POSITION: tuple[int, int] = tuple(
                random.randrange(
                    -self.MAP_SIZE // 2, self.MAP_SIZE // 2, self.CELL_SIZE
                )
                for _ in range(2)
            )
            pprint(f"[bold blue]INFO:[/] Random `GOAL_POSITION = {self.GOAL_POSITION}`")

        # check if GOAL_POSITION is a multiple of CELL_SIZE
        elif any(coordinate % self.CELL_SIZE for coordinate in self.GOAL_POSITION):
            self.GOAL_POSITION = tuple(
                coordinate - coordinate % self.CELL_SIZE
                for coordinate in self.GOAL_POSITION
            )
            pprint(
                "[bold yellow]WARNING:[/] `GOAL_POSITION` should be a multiple of `CELL_SIZE`. "
                f"The value `GOAL_POSITION = {self.GOAL_POSITION}` will be used instead of the provided value."
            )
        return self

    class Config:
        env_file = "config.env"


settings = _Settings()
