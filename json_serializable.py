from __future__ import annotations

from copy import copy
from enum import Enum
from json import dumps
from typing import Any


class JsonSerializable:
    """Класс, упрощающий преобразование классов-наследников в строку"""

    def copy(self):
        return copy(self)

    def copy_with(self, **kwargs):
        c = copy(self)
        for k, v in kwargs.items():
            if hasattr(c, k):
                setattr(c, k, v)
        return c

    @staticmethod
    def default(obj: JsonSerializable) -> dict[str, Any]:
        data = dict()

        if hasattr(obj, "__dict__"):
            for attr_name in filter(lambda x: not x.startswith("_"), obj.__dict__):
                attr_value = getattr(obj, attr_name)
                if attr_value is not None:
                    if isinstance(attr_value, Enum):
                        data[attr_name] = str(attr_value)
                    elif (
                        isinstance(attr_value, list)
                        and len(attr_value) > 0
                        and isinstance(attr_value[0], Enum)
                        # а было бы возможно использовать generic...
                    ):
                        data[attr_name] = list(map(str, attr_value))
                    else:
                        data[attr_name] = attr_value

        return {"_": obj.__class__.__name__, **data}

    @staticmethod
    def serialize(obj: Any) -> str:
        return JsonSerializable.__str__(obj)

    def __str__(self) -> str:
        return dumps(
            self,
            indent=4,
            default=JsonSerializable.default,
            ensure_ascii=False,
        )

    def __repr__(self) -> str:
        return "{}({})".format(
            self.__class__.__name__,
            ", ".join(
                f"{attr}={repr(getattr(self, attr))}"
                for attr in filter(lambda x: not x.startswith("_"), self.__dict__)
                if getattr(self, attr) is not None
            ),
        )

    def __eq__(self, other: JsonSerializable) -> bool:
        for attr in self.__dict__:
            try:
                if attr.startswith("_"):
                    continue

                if getattr(self, attr) != getattr(other, attr):
                    return False
            except AttributeError:
                return False

        return True


__all__ = (JsonSerializable,)
