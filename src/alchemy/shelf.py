from alchemy.card_stack import CardStack
from alchemy.cards import Card, AbcElement
from alchemy.json_serializable import JsonSerializable

class Shelf(JsonSerializable):
    def __init__(self) -> None:
        self.card_stacks: dict[int, CardStack] = dict()

    def can_pop(self, element: AbcElement) -> bool:
        """Можно ли достать карту из шкафа с конкретным элементом

        Args:
            element (AbcElement): искомый элемент

        Returns:
            bool: Истина если можно, Ложь если не можно
        """
        i_key = element.index
        for key, card_stack in self.card_stacks.items():
            if i_key & key and card_stack.can_pop():
                return True
        else:
            return False

    def pop(self, card: Card) -> None:
        """Удалить карту с конкретным элементом из шкафа

        Args:
            element (AbcElement): искомый элемент

        Returns:
            Card: Карта с искомым элементом
        """
        assert self.can_pop(card.drop_elements[0])

        for key, card_stack in self.card_stacks.items():
            if card_stack.top().short_title == card.short_title:
                card = card_stack.pop()
                if not card_stack.can_pop():
                    self.card_stacks.pop(key)
                break

    def put(self, card: Card) -> None:
        """Положить карту в шкаф

        Args:
            card (Card): карта
        """
        key = sum([i.index for i in card.drop_elements])

        if self.card_stacks.get(key, None) is None:
            self.card_stacks[key] = CardStack()

        self.card_stacks[key].put(card)

    def put_down(self, card: Card) -> None:
        """Положить карту в шкаф снизу

        Args:
            card (Card): карта
        """
        key = sum([i.index for i in card.drop_elements])

        if self.card_stacks.get(key, None) is None:
            self.card_stacks[key] = CardStack()

        self.card_stacks[key].put_down(card)

    def toplist(self) -> list[Card]:
        return [
            card_stack.top()
            for card_stack in self.card_stacks.values()
            if card_stack.can_pop()
        ]


__all__ = (Shelf,)
