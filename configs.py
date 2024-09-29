from itertools import chain
from typing import Self

from pydantic import model_validator
from pydantic_settings import BaseSettings


class _Settings(BaseSettings):
    agent_init_position: tuple[int, int]
    goal_position: tuple[int, int]
    num_of_cells: int
    obstacles_positions: list[tuple[int, int]]
    enable_steps: bool
    app_name: str
    window_size: int
    background_color: str
    goal_color: str
    grid_color: str
    grid_thickness: int
    obstacles_color: str

    @property
    def cell_size(self) -> float:
        return self.window_size / self.num_of_cells

    @model_validator(mode="after")
    def validate_positions(self) -> Self:
        if not all(-1 <= coord <= self.num_of_cells for coord in self.goal_position):
            raise ValueError(
                f"`GOAL_POSITION={self.goal_position}` is out of bounds. "
                f"Should be between -1 and {self.num_of_cells}"
            )
        if not all(
            0 <= coord < self.num_of_cells for coord in self.agent_init_position
        ):
            raise ValueError(
                f"`AGENT_INIT_POSITION={self.agent_init_position}` is out of bounds. "
                f"Should be between 0 and {self.num_of_cells - 1}"
            )
        if self.agent_init_position == self.goal_position:
            raise ValueError(
                "`AGENT_INIT_POSITION` and `GOAL_POSITION` cannot be the same."
            )
        if not all(
            0 <= coord < self.num_of_cells
            for coord in chain.from_iterable(self.obstacles_positions)
        ):
            raise ValueError(
                f"All values in `OBSTACLES_POSITIONS` should be between 0 and {self.num_of_cells - 1}."
            )
        return self

    class Config:
        env_file = "game.config"


settings = _Settings()  # type: ignore[call-arg]
