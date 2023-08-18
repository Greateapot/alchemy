from __future__ import annotations

from typing import Callable

from alchemy.cards import CardModel
from alchemy.enums import Element
from alchemy.stack import CardStack


def default_search_algorithm(search_key, key):
    return search_key & key


class IngredientShelf:
    def __init__(
        self,
        search_algorithm: Callable[[int, int], bool] = default_search_algorithm,
    ) -> None:
        self._shelf: dict[int, CardStack] = dict()

        # NOTE: may be custom for Element.any in DLC's
        self.search_algorithm = search_algorithm

    def can_get_element(self, element: Element) -> bool:
        search_key = element.index
        for key in self._shelf.keys():
            if self.search_algorithm(search_key, key):
                return True
        else:
            return False

    def get_element(self, element: Element) -> CardModel:
        assert self.can_get_element(element)

        search_key = element.index
        for key, stack in self._shelf.items():
            if self.search_algorithm(search_key, key):
                card = stack.pop()
                if not stack.can_pop():
                    self._shelf.pop(key)
                return card

    def get_card(self, card: CardModel) -> None:
        assert self.can_get_element(card.drop_elements[0])

        search_key = sum([element.index for element in card.drop_elements])
        for key, stack in self._shelf.items():
            if self.search_algorithm(search_key, key):
                stack.pop()
                if not stack.can_pop():
                    self._shelf.pop(key)
                return

    def put(self, card: CardModel) -> None:
        key = sum([element.index for element in card.drop_elements])

        if self._shelf.get(key, None) is None:
            self._shelf[key] = CardStack()

        self._shelf[key].put(card)

    def put_down(self, card: CardModel) -> None:
        key = sum([element.index for element in card.drop_elements])

        if self._shelf.get(key, None) is None:
            self._shelf[key] = CardStack()

        self._shelf[key].put_down(card)

    def toplist(self) -> list[CardModel]:
        return [stack.top() for stack in self._shelf.values() if stack.can_pop()]
