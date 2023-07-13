# Оригинальные правила (вроде) настольной игры. 

from __future__ import annotations

from alchemy import Alchemy, Player

from .cards import create_card_stack
from .handlers import handler


def create_session(players: list[str]) -> Alchemy:
    card_stack = create_card_stack()
    card_stack.shuffle()
    return Alchemy(
        card_stack,
        [Player(name) for name in players if name],
        4,
        handler,
    )


__all__ = (create_session,)
