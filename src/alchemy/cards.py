from __future__ import annotations
from typing import Any

from alchemy.enums import CardType, Element, Spell
from pydantic import BaseModel, field_serializer, field_validator, Field


class CardTag(BaseModel):
    tag: str

    def serialize(self) -> str:
        return self.tag


class CardModel(BaseModel):
    tag: CardTag
    title: str
    type: CardType
    drop_elements: list[Element]

    @field_validator("tag", mode="before")
    @classmethod
    def _tag_validator(cls, v: str) -> CardTag:
        return CardTag(tag=v)

    @field_serializer("tag")
    def _tag_serializer(self, v: CardTag, _info) -> str:
        return v.tag

    @field_validator("type", mode="before")
    @classmethod
    def _type_validator(cls, v: str) -> CardType:
        return CardType.validate(v)

    @field_serializer("type")
    def _type_serializer(self, v: CardType, _info) -> str:
        return v.serialize()

    @field_validator("drop_elements", mode="before")
    @classmethod
    def _drop_elements_validator(cls, v: list[str]) -> list[Element]:
        return [Element.validate(i) for i in v]

    @field_serializer("drop_elements")
    def _drop_elements_serializer(self, v: list[Element], _info) -> list[str]:
        return [i.serialize() for i in v]


class CraftableCardModel(CardModel):
    points: int
    craft_ingredients: list[Element | CardTag | CardType]
    buffer: list[CardModel] = Field(exclude=True, default=list())

    @field_validator("buffer", mode="before")
    @classmethod
    def _buffer_validator(cls, v: Any) -> list[CardModel]:
        return list() 

    @field_validator("craft_ingredients", mode="before")
    @classmethod
    def _craft_ingredients_validator(
        cls,
        v: list[str],
    ) -> list[Element | CardTag | CardType]:
        result = list()
        for obj in v:
            card_type = CardType.validate(obj)

            if obj.endswith("*"):
                result.append(card_type)
            elif card_type == CardType.element:
                result.append(Element.validate(obj))
            else:
                result.append(CardTag(tag=obj))

        return result

    @field_serializer("craft_ingredients")
    def _craft_ingredients_serializer(
        self,
        v: list[Element | CardTag | CardType],
        _info,
    ) -> list[str]:
        result = list()
        for obj in v:
            if isinstance(obj, Element):
                result.append(obj.serialize())
            elif isinstance(obj, CardType):
                result.append(obj.serialize())
            elif isinstance(obj, CardTag):
                result.append(obj.tag)
            else:
                raise Exception(
                    "Serialization error: unexpected "
                    f'object "{obj}" of type "{type(obj)}".'
                )
        return result


class SpellCardModel(CardModel):
    spell: Spell

    @field_validator("spell", mode="before")
    @classmethod
    def _spell_validator(cls, v: str) -> Spell:
        return Spell.validate(v)

    @field_serializer("spell")
    def _spell_serializer(self, v: Spell, _info) -> str:
        return v.serialize()


def load_cards(
    cards: list[dict[str, str | int | list[str]]],
) -> list[CardModel]:
    result = list()

    for card in cards:
        if card['type'] == 'spell:*': # TODO: check this correctly
            result.append(SpellCardModel.model_validate(card))
        else:
            result.append(CraftableCardModel.model_validate(card))

    return result


__all__ = (
    CardModel,
    CraftableCardModel,
    SpellCardModel,
    load_cards,
)

# if __name__ == "__main__":
#     data = {
#         "enums": {
#             "elements": [
#                 "ether_wave",
#                 "the_quintessence_of_will",
#                 "belladonna",
#                 "fiery_light",
#             ],
#             "spells": ["spell_of_knowledge"],
#             "card_types": ["potion", "elixir"],
#         },
#         "cards": [
#             {
#                 "tag": "spell:spell_of_knowledge",
#                 "title": "Заклятье Познания",
#                 "type": "spell:*",
#                 "drop_elements": ["element:belladonna"],
#                 "spell": "spell:spell_of_knowledge",
#             },
#             {
#                 "tag": "potion:elixir_of_fire",
#                 "title": "Эликсир Огня",
#                 "type": "potion:*",
#                 "drop_elements": ["element:the_quintessence_of_will"],
#                 "points": 2,
#                 "craft_ingredients": ["element:ether_wave", "element:fiery_light"],
#             },
#         ],
#     }

#     load_enums(data["enums"])
#     cards = load_cards(data["cards"])

#     s: SpellCardModel = cards[0]
#     sd = s.model_dump()
#     ns: SpellCardModel = SpellCardModel.model_validate(sd)
#     assert s == ns

#     c: CraftableCardModel = cards[1]
#     cd = c.model_dump()
#     nc: CraftableCardModel = CraftableCardModel.model_validate(cd)
#     assert c == nc
