from enum import Enum, auto


class Log2Enum(int, Enum):
    @staticmethod
    def _generate_next_value_(_, __, count, ___):
        return 2**count


CardType = Log2Enum
Ingredient = Log2Enum
SpellType = Log2Enum


__all__ = (
    auto,
    CardType,
    Ingredient,
    SpellType,
)
