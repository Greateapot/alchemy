from alchemy.cards import Card
from alchemy.json_serializable import JsonSerializable


class Player(JsonSerializable):
    """Игрок, содержит: имя, список карт, очки, список созданных карт"""

    def __init__(self, name: str) -> None:
        self.cards: list[Card] = list()
        self.name: str = name
        self.points: int = 0

    def can_act(self) -> bool:
        """Может ли игрок действовать"""
        return len(self.cards) > 0


__all__ = (Player,)
