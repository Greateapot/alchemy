from alchemy import Alchemy


from alchemy_original_console.handlers.utils import print_card


def check_shelf_handler(session: Alchemy) -> None:
    print("Карты в шкафу:\n")
    for card in session.shelf.toplist():
        print_card(card, session.settings.tags_is_visible)


__all__ = (check_shelf_handler,)
