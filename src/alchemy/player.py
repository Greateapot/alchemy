from alchemy.cards import CardModel


class Player:
    """Игрок, содержит: имя, список карт, очки, список созданных карт"""

    def __init__(self, name: str) -> None:
        self.cards: list[CardModel] = list()
        self.name: str = name
        self.points: int = 0

    def can_act(self) -> bool:
        """Может ли игрок действовать"""
        return len(self.cards) > 0


__all__ = (Player,)
