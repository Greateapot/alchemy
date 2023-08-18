from __future__ import annotations

from random import shuffle

from alchemy.cards import CardModel


class CardStack:
    def __init__(self, cards: list[CardModel] = None):
        self._stack: list[CardModel] = cards if cards is not None else list()

    def __len__(self) -> int:
        return len(self._stack)
    
    def shuffle(self) -> None:
        return shuffle(self._stack)

    def put(self, card: CardModel):
        self._stack.insert(0, card)

    def put_down(self, card: CardModel):
        self._stack.append(card)

    def can_pop(self) -> bool:
        return len(self._stack) > 0

    def pop(self) -> CardModel:
        assert self.can_pop()

        return self._stack.pop(0)

    def pop_down(self) -> CardModel:
        assert self.can_pop()

        return self._stack.pop()

    def top(self) -> CardModel:
        assert self.can_pop()

        return self._stack[0]
