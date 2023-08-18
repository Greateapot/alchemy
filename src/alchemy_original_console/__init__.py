# Оригинальные правила (вроде) настольной игры.

from __future__ import annotations

from typing import Any

from alchemy import Alchemy, Player

from .handlers import handler


def create_session(
    config: dict[str, Any],
    players: list[str],
) -> Alchemy:
    return Alchemy(
        config,
        [Player(name) for name in players if name],
        handler,
    )


__all__ = (create_session,)
