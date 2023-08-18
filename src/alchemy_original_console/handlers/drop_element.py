from alchemy import Alchemy, Player


from alchemy_original_console.handlers.utils import player_input


def drop_elements_handler(session: Alchemy, player: Player) -> bool:
    print("Сброс карты в шкаф. Список карт:\n")
    for index, card in enumerate(player.cards):
        print(f"{index + 1}. {card.title}")
    print("0. Отмена")
    card_number = player_input(player, 0, len(player.cards))
    if card_number > 0:
        card = player.cards.pop(card_number - 1)
        for ingredient in card.drop_elements:
            if not session.shelf.can_get_element(ingredient):
                player.points += 1
        session.shelf.put(card)
        print("Карта перемещена в шкаф.")
        return True
    else:
        print("Отмена...")
        return False


__all__ = (drop_elements_handler,)
