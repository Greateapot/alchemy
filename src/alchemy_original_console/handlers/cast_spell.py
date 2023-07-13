from alchemy import Alchemy, Player, cards

from alchemy_original_console.enums import SpellType
from alchemy_original_console.handlers.consts import SHORT_TITLE_ENABLED
from alchemy_original_console.handlers.utils import player_input, print_card


def cast_spell_of_destruction(
    session: Alchemy,
    player: Player,
    card: cards.SpellCard,
) -> bool:
    player_crafts = list(filter(lambda x: x[0] == player, session.crafts))

    if len(player_crafts) == 0:
        print("У вас нет созданных рецептов.")
        return False

    print("Список созданных вами рецептов:")
    sv = len(str(len(player_crafts)))
    for index, player_craft in enumerate(player_crafts):
        print(f"{index+1: >{sv}}.", end=" ")
        print_card(player_craft[1], SHORT_TITLE_ENABLED, True)
    print("0. Отмена")

    craft_number = player_input(player, 0, len(player_crafts))

    if craft_number == 0:
        print("Отмена.")
        return False

    player_craft = player_crafts[craft_number - 1]
    craft = player_craft[1]
    craft_cards = [craft] + craft.buffer

    print("Список карт для применения заклинания:")
    sv = len(str(len(craft_cards)))
    for index, craft_card in enumerate(craft_cards):
        print(f"{index+1: >{sv}}.", end=" ")
        print_card(craft_card, SHORT_TITLE_ENABLED)
    print("0. Отмена")

    craft_card_number = player_input(player, 0, len(craft_cards))

    if craft_card_number == 0:
        print("Отмена.")
        return False

    craft_card = craft_cards[craft_card_number - 1]

    session.crafts.remove(player_craft)
    player.cards.remove(card)
    craft.buffer.clear()
    craft_cards.remove(craft_card)
    session.crafts.append((player, craft_card))

    for c in craft_cards:
        session.shelf.put(c)

    session.shelf.put_down(card)

    print("Заклинание успешно применено.")
    return False


def cast_spell_of_knowledge(
    session: Alchemy,
    player: Player,
    card: cards.SpellCard,
) -> bool:
    shelf_cards = session.shelf.toplist()
    print("Карты в шкафу:\n")
    for shelf_card in shelf_cards:
        print_card(shelf_card, SHORT_TITLE_ENABLED)
    print("0. Отмена")

    shelf_card_number = player_input(player, 0, len(shelf_cards))

    if shelf_card_number == 0:
        print("Отмена.")
        return False

    shelf_card = shelf_cards[shelf_card_number - 1]

    session.shelf.pop(shelf_card)
    player.cards.remove(card)
    player.cards.append(shelf_card)

    session.shelf.put_down(card)

    print("Заклинание успешно применено.")
    return False


def cast_spell_of_transform(
    session: Alchemy,
    player: Player,
    card: cards.SpellCard,
) -> bool:
    player_crafts = list(filter(lambda x: x[0] == player, session.crafts))

    if len(player_crafts) == 0:
        print("У вас нет созданных рецептов.")
        return False

    print("Список созданных вами рецептов:")
    sv = len(str(len(player_crafts)))
    for index, player_craft in enumerate(player_crafts):
        print(f"{index+1: >{sv}}.", end=" ")
        print_card(player_craft[1], SHORT_TITLE_ENABLED, True)
    print("0. Отмена")

    craft_number = player_input(player, 0, len(player_crafts))

    if craft_number == 0:
        print("Отмена.")
        return False

    player_craft = player_crafts[craft_number - 1]

    shelf_cards = session.shelf.toplist()
    print("Карты в шкафу:\n")
    for shelf_card in shelf_cards:
        print_card(shelf_card, SHORT_TITLE_ENABLED)
    print("0. Отмена")

    shelf_card_number = player_input(player, 0, len(shelf_cards))

    if shelf_card_number == 0:
        print("Отмена.")
        return False

    shelf_card = shelf_cards[shelf_card_number - 1]

    player.cards.remove(card)
    session.shelf.pop(shelf_card)
    session.crafts.remove(player_craft)
    session.crafts.append((player, shelf_card))

    for c in player_craft[1].buffer:
        session.shelf.put(c)

    session.shelf.put(player_craft[1])

    session.shelf.put_down(card)

    print("Заклинание успешно применено.")
    return False


def cast_spell_handler(session: Alchemy, player: Player) -> bool:
    spells = list(
        filter(
            lambda x: isinstance(x, cards.SpellCard),
            player.cards,
        )
    )

    print("Применение заклинания. Список доступных заклинаний:\n")
    for index, card in enumerate(spells):
        print(
            f"{index + 1}. {card.title}"
            + (f" ({card.short_title})" if SHORT_TITLE_ENABLED else "")
        )
    print("0. Отмена")

    card_number = player_input(player, 0, len(spells))

    if card_number == 0:
        print("Отмена.")
        return False

    card: cards.SpellCard = spells[card_number - 1]

    # NOTE: в оригинале все заклинания позволяют сыграть еще одну карту,
    # след. все функции заклинаний должны возвращать False, даже если
    # заклинание успешно применено.
    match card.spell_type:
        case SpellType.spell_of_destruction:
            return cast_spell_of_destruction(session, player, card)
        case SpellType.spell_of_knowledge:
            return cast_spell_of_knowledge(session, player, card)
        case SpellType.spell_of_transform:
            return cast_spell_of_transform(session, player, card)
        case _:
            raise Exception(f"Неизвестный тип заклинания: {card.spell_type}")
