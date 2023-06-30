from enum import Enum


class Log2Enum(int, Enum):
    @staticmethod
    def _generate_next_value_(_, __, count, ___):
        return 2**count


AbcCardType = Log2Enum
AbcIngredient = Log2Enum
AbcSpellType = Log2Enum


__all__ = (
    AbcCardType,
    AbcIngredient,
    AbcSpellType,
)
