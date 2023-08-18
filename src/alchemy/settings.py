from __future__ import annotations

from pydantic import BaseModel


class Settings(BaseModel):
    hand_cards_count: int = 4
    shuffle_cards_on_load: bool = False
    tags_is_visible: bool = False

def load_settings(settings: dict[str, str | int | bool]) -> Settings:
    return Settings.model_validate(settings)