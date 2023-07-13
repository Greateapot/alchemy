from alchemy import Player

from alchemy_original_console.handlers.consts import SHORT_TITLE_ENABLED
from alchemy_original_console.handlers.utils import print_card


def check_cards_handler(player: Player) -> None:
    print(f"Карты игрока {player.name}:\n")
    for card in player.cards:
        print_card(card, SHORT_TITLE_ENABLED)


__all__ = (check_cards_handler,)
