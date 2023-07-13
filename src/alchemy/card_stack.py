from random import shuffle

from alchemy.cards import Card
from alchemy.json_serializable import JsonSerializable


class CardStack(JsonSerializable):
    """Стопка карт"""

    def __init__(self, cards: list[Card] = None) -> None:
        self.cards: list[Card] = cards if cards is not None else list()

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

    def put_down(self, card: Card) -> None:
        """Положить карту в стопку снизу

        Args:
            card (Card): карта, кт кладем в стопку
        """
        self.cards.insert(0, card)

    def shuffle(self) -> None:
        shuffle(self.cards)

    def top(self) -> Card:
        assert self.can_pop()
        return self.cards[-1]


__all__ = (CardStack,)
