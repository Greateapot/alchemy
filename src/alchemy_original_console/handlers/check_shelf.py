from alchemy import Alchemy


from alchemy_original_console.handlers.consts import SHORT_TITLE_ENABLED
from alchemy_original_console.handlers.utils import print_card


def check_shelf_handler(session: Alchemy) -> None:
    print("Карты в шкафу:\n")
    for card in session.shelf.toplist():
        print_card(card, SHORT_TITLE_ENABLED)


__all__ = (check_shelf_handler,)
