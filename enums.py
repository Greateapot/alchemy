from __future__ import annotations

from aenum import Enum


class ExtendedEnum(Enum):
    _init_ = "_index _title"

    @classmethod
    def get(cls, key: int | str) -> ExtendedEnum:
        for value in list(cls):
            if key in value._value_:
                return value
        raise Exception(f"Not found key '{key}' in {cls}")

    @property
    def index(self) -> int:
        return self._index

    @property
    def title(self) -> str:
        return self._title

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return super().__str__()


class Log2Enum(ExtendedEnum):
    def _generate_next_value_(_, __, count, ___, *args, **____):
        return (2**count,) + args


class AbcCardType(Log2Enum):
    pass


class AbcElement(Log2Enum):
    pass


class AbcSpellType(Log2Enum):
    pass


__all__ = (
    ExtendedEnum,
    Log2Enum,
    AbcCardType,
    AbcElement,
    AbcSpellType,
)
