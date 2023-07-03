from alchemy.card_stack import CardStack
from alchemy.cards import Card, AbcIngredient
from alchemy.json_serializable import JsonSerializable


class Shelf(JsonSerializable):
    def __init__(self) -> None:
        self.card_stacks: dict[int, CardStack] = dict()

    def can_pop(self, ingredient: AbcIngredient) -> bool:
        """Можно ли достать карту из шкафа с конкретным ингредиентом

        Args:
            ingredient (Ingredient): искомый ингредиент

        Returns:
            bool: Истина если можно, Ложь если не можно
        """
        i_key = ingredient.index
        for key, card_stack in self.card_stacks.items():
            if i_key & key and card_stack.can_pop():
                return True
        else:
            return False

    def pop(self, ingredient: AbcIngredient) -> Card:
        """Достать карту с конкретным ингредиетом из шкафа

        Args:
            ingredient (Ingredient): искомый ингредиент

        Returns:
            Card: Карта с искомым ингредиентом
        """
        assert self.can_pop(ingredient)

        i_key = ingredient.index
        for key, card_stack in self.card_stacks.items():
            if i_key & key and card_stack.can_pop():
                card = card_stack.pop()
                if not card_stack.can_pop():
                    self.card_stacks.pop(key)
                return card

    def put(self, card: Card) -> None:
        """Положить карту в шкаф

        Args:
            card (Card): карта
        """
        key = 0
        for i in card.drop_ingredients:
            key += i.index

        if self.card_stacks.get(key, None) is None:
            self.card_stacks[key] = CardStack()

        self.card_stacks[key].put(card)

    def toplist(self) -> list[Card]:
        return [
            card_stack.top()
            for card_stack in self.card_stacks.values()
            if card_stack.can_pop()
        ]


__all__ = (Shelf,)
