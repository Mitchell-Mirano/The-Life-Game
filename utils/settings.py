from functools import lru_cache
from pydantic import BaseSettings


class GameSettings(BaseSettings):
    width:int
    height:int
    background_color:list[int]
    n_cells_x:int
    n_cells_y:int
    class Config:
        env_file =".conf"

@lru_cache()
def get_game_settings():
    return GameSettings()