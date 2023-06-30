from __future__ import annotations

from alchemy.enums import AbcIngredient, AbcCardType, AbcSpellType
from alchemy.json_serializable import JsonSerializable


class Card(JsonSerializable):
    """
    Карта, содержит название, короткое название, ингредиенты,
    кт можно получить сбросив карту в шкаф.
    """

    def __init__(
        self,
        card_type: AbcCardType,
        title: str,
        short_title: str,
        drop_ingredients: tuple[AbcIngredient],
    ) -> None:
        self.card_type: AbcCardType = card_type
        self.title: str = title
        self.short_title: str = short_title
        self.drop_ingredients: tuple[AbcIngredient] = drop_ingredients


class CraftableCard(Card):
    """
    Создаваемая карта, дополнительно хранит очки за создание и список
    необходимых ингредиентов для создания.

    toml:
    [[cards]]
    type = 'potion'
    title = 'Эликсир Вечного Сна'
    points = 2
    short_title = 'ELoES'
    drop_ingredients = ['ingredient.fiery_light']
    craft_ingredients = ['ingredient.belladonna', 'ingredient.spring_water']
    """

    def __init__(
        self,
        card_type: AbcCardType,
        title: str,
        short_title: str,
        drop_ingredients: tuple[AbcIngredient],
        points: int,
        craft_ingredients: tuple[AbcIngredient | CraftableCard | AbcCardType],
    ) -> None:
        super().__init__(card_type, title, short_title, drop_ingredients)
        self.points = points
        self.craft_ingredients = craft_ingredients
        self.buffer: list[Card] = list()


class SpellCard(Card):
    """
    Заклинание. Содержит тип заклинания (`enums.spell_type`).

    toml:
    [[cards]]
    type = "spell"
    spell_type = "spell_of_destruction"
    title = "Заклинание Разрушения"
    short_title = "SPoD"
    drop_ingredients = ["ingredient.snake_eye"]
    """

    def __init__(
        self,
        card_type: AbcCardType,
        title: str,
        short_title: str,
        drop_ingredients: tuple[AbcIngredient],
        spell_type: AbcSpellType,
    ) -> None:
        super().__init__(card_type, title, short_title, drop_ingredients)
        self.spell_type: AbcSpellType = spell_type


__all__ = (
    Card,
    CraftableCard,
    SpellCard,
)
