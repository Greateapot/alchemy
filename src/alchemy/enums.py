from __future__ import annotations

import re

from aenum import Enum, extend_enum

_ELEMENT_PATTERN = re.compile(r"^element:([a-z_]+)$")
_SPELL_PATTERN = re.compile(r"^spell:([a-z_]+)$")
_CARD_TYPE_PATTERN = re.compile(r"^([a-z0-9_]+):.*?$")


class Log2Enum(Enum):
    def _generate_next_value_(
        name,
        start,
        count,
        last_values,
        *args,
        **kwds,
    ):
        return (name, 2**count)

    def __new__(cls, name, index):
        obj = object.__new__(cls)
        obj._value_ = name
        obj._index_ = index
        cls._value2member_map_[index] = obj
        return obj

    @property
    def index(self) -> int:
        return self._index_

    @property
    def value(self) -> str:
        return self._value_

    @classmethod
    def extend(cls, value: str, *args, **kwds):
        extend_enum(cls, value, *args, **kwds)


class Element(Log2Enum):
    def serialize(self) -> str:
        return f"element:{self.value}"

    @classmethod
    def validate(cls, obj: str) -> Element:
        value: re.Match[str] | None = _ELEMENT_PATTERN.match(obj)
        if value is None or value.group(1) not in Element:
            raise Exception(f"ValidationError: cannot validate obj: {obj}")
        return Element(value.group(1))


class Spell(Log2Enum):
    def serialize(self) -> str:
        return f"spell:{self.value}"

    @classmethod
    def validate(cls, obj: str) -> Spell:
        value: re.Match[str] | None = _SPELL_PATTERN.match(obj)
        if value is None or value.group(1) not in Spell:
            raise Exception(f"ValidationError: cannot validate obj: {obj}")
        return Spell(value.group(1))


class CardType(Log2Enum):
    def serialize(self) -> str:
        return f"{self.value}:*"

    @classmethod
    def validate(cls, obj: str) -> CardType:
        value: re.Match[str] | None = _CARD_TYPE_PATTERN.match(obj)
        if value is None or value.group(1) not in CardType:
            raise Exception(f"ValidationError: cannot validate obj: {obj}")
        return CardType(value.group(1))


def load_elements(elements: list[str]):
    for element in elements:
        Element.extend(element)


def load_spells(spells: list[str]):
    for spell in spells:
        Spell.extend(spell)


def load_card_types(card_types: list[str]):
    CardType.extend("element")
    CardType.extend("spell")

    for card_type in card_types:
        CardType.extend(card_type)


def load_enums(enums: dict[str, list[str]]):
    load_elements(enums["elements"])
    load_spells(enums["spells"])
    load_card_types(enums["card_types"])


__all__ = (
    Log2Enum,
    Element,
    Spell,
    CardType,
    load_elements,
    load_spells,
    load_card_types,
    load_enums,
)

if __name__ == "__main__":
    data = {
        "enums": {
            "elements": ["snake_eye", "mandrake_root"],
            "spells": ["spell_of_knowledge"],
            "card_types": ["potion2", "potion3"],
        }
    }

    load_enums(data["enums"])

    e: Element = list(Element)[-1]
    ed = e.serialize()
    ne: Element = Element.validate(ed)
    assert e == ne

    s: Spell = list(Spell)[-1]
    sd = s.serialize()
    ns: Spell = Spell.validate(sd)
    assert s == ns

    ct: CardType = list(CardType)[-1]
    ctd = ct.serialize()
    nct: CardType = CardType.validate(ctd)
    assert ct == nct
