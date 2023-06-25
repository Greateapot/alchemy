from random import shuffle

from alchemy.cards import Card
from alchemy.json_serializable import JsonSerializable


class CardStack(JsonSerializable):
    """Стопка карт"""

    def __init__(self) -> None:
        self.cards: list[Card] = list()

    def can_pop(self) -> bool:
        """Можно ли взять карту"""
        return len(self.cards) > 0

    def pop(self) -> Card:
        """Взять карту"""
        assert self.can_pop()
        return self.cards.pop()

    def put(self, card: Card) -> None:
        """Положить карту в стопку

        Args:
            card (Card): карта, кт кладем в стопку
        """
        self.cards.append(card)

    def shuffle(self) -> None:
        shuffle(self.cards)


__all__ = (CardStack,)
