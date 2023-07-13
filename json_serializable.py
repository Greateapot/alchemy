# этот кусок кода я одолжил у либы pyrogram, уж очень он мне понравился

from __future__ import annotations

import alchemy

from copy import copy
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

        if isinstance(obj, alchemy.ExtendedEnum):
            data["index"] = obj.index
            data["title"] = obj.title

        elif hasattr(obj, "__dict__"):
            for attr_name in filter(lambda x: not x.startswith("_"), obj.__dict__):
                attr_value = getattr(obj, attr_name)
                if attr_value is not None:
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
