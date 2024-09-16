from typing import Self

from pydantic import model_validator
from pydantic_settings import BaseSettings


class _Settings(BaseSettings):
    app_name: str
    background_color: str
    grid_color: str
    grid_thickness: int
    window_size: int
    num_of_cells: int
    goal_position: tuple[int, int]
    goal_color: str
    agent_init_position: tuple[int, int]

    @property
    def cell_size(self) -> int:
        return self.window_size / self.num_of_cells

    @model_validator(mode="after")
    def validate_agent_position(self) -> Self:
        if not all(-1 <= coord <= self.num_of_cells for coord in self.goal_position):
            raise ValueError(
                f"GOAL_POSITION = {self.goal_position} is out of bounds. "
                f"Should be between 0 and {self.num_of_cells - 1}"
            )
        if not all(
            0 <= coord < self.num_of_cells for coord in self.agent_init_position
        ):
            raise ValueError(
                f"`AGENT_INIT_POSITION` = {self.agent_init_position} is out of bounds. "
                f"Should be between 0 and {self.num_of_cells - 1}"
            )
        if self.agent_init_position == self.goal_position:
            raise ValueError(
                "`AGENT_INIT_POSITION` and `GOAL_POSITION` cannot be the same."
            )
        return self

    class Config:
        env_file = "game.config"


settings = _Settings()
