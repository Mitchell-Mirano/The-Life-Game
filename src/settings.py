from functools import lru_cache
from pydantic_settings import BaseSettings,SettingsConfigDict


class GameSettings(BaseSettings):
    width:int
    height:int
    background_color:list[int]
    n_cells_x:int
    n_cells_y:int
    model_config = SettingsConfigDict(env_file=".conf",extra='ignore')

@lru_cache()
def get_game_settings():
    return GameSettings()