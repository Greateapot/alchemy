from alchemy import Player, Alchemy

from alchemy_original_console.handlers.utils import print_card


def check_cards_handler(session: Alchemy, player: Player) -> None:
    print(f"Карты игрока {player.name}:\n")
    for card in player.cards:
        print_card(card, session.settings.tags_is_visible)


__all__ = (check_cards_handler,)
