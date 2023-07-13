from alchemy import Alchemy, Player

from alchemy_original_console.handlers.consts import SHORT_TITLE_ENABLED
from alchemy_original_console.handlers.utils import print_card


def check_crafts_handler(session: Alchemy, player: Player) -> None:
    print("Созданные игроками карты:\n")
    last_p: Player = None
    for p, c in sorted(session.crafts, key=lambda x: x[0].name):
        if p != last_p:
            last_p = p
            print(f"Карты, созданные игроком {p.name}:\n")
        print_card(c, SHORT_TITLE_ENABLED, p == player)


__all__ = (check_crafts_handler,)
