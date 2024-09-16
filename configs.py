import random
from typing import Literal, Self

from pydantic import model_validator
from pydantic_settings import BaseSettings
from rich import print as pprint


def _get_random_point(num_of_cells: int) -> tuple[int, int]:
    return tuple(random.randrange(num_of_cells) for _ in range(2))


class _Settings(BaseSettings):
    app_name: str
    background_color: str
    grid_color: str
    grid_thickness: int
    window_size: int
    num_of_cells: int
    goal_position: tuple[int, int] | Literal["random"]
    goal_color: str
    agent_init_position: tuple[int, int] | Literal["random"]

    @property
    def cell_size(self) -> int:
        return self.window_size / self.num_of_cells

    @model_validator(mode="after")
    def validate_CELL_SIZE(self) -> Self:
        if self.goal_position == "random":
            self.goal_position: tuple[int, int] = _get_random_point(self.num_of_cells)
            while self.agent_init_position == self.goal_position:
                self.goal_position = _get_random_point(self.num_of_cells)
            pprint(
                f"[bold blue]INFO:[/] Using random `GOAL_POSITION = {self.goal_position}`"
            )
        elif not all(0 <= coord < self.num_of_cells for coord in self.goal_position):
            raise ValueError(
                f"GOAL_POSITION = {self.goal_position} is out of bounds. "
                f"Should be between 0 and {self.num_of_cells - 1}"
            )

        if self.agent_init_position == "random":
            self.agent_init_position: tuple[int, int] = _get_random_point(
                self.num_of_cells
            )
            while self.agent_init_position == self.goal_position:
                self.agent_init_position = _get_random_point(self.num_of_cells)
            pprint(
                f"[bold blue]INFO:[/] Using random `AGENT_INIT_POSITION = {self.agent_init_position}`"
            )
        elif not all(
            0 <= coord < self.num_of_cells for coord in self.agent_init_position
        ):
            raise ValueError(
                f"AGENT_INIT_POSITION = {self.agent_init_position} is out of bounds. "
                f"Should be between 0 and {self.num_of_cells - 1}"
            )

        if self.goal_position == self.agent_init_position:
            raise ValueError(
                f"GOAL_POSITION and AGENT_INIT_POSITION cannot be the same. "
                f"GOAL_POSITION = {self.goal_position}, AGENT_INIT_POSITION = {self.agent_init_position}"
            )

        return self

    class Config:
        env_file = "game.config"


settings = _Settings()
