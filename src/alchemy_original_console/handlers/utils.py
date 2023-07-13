from alchemy import Player, cards


def player_input(player: Player, a: int, b: int) -> int:
    value: int = b + 1
    while not (a <= value <= b):
        raw_value = input(f"{player.name}, введите номер опции: ")
        if raw_value.isdigit() and a <= int(raw_value) <= b:
            value = int(raw_value)
        else:
            print("Некорректный ввод!")
    return value


def print_card(
    card: cards.Card,
    short_title: bool = False,
    buffer: bool = False,
) -> None:
    print(f"{card.title}" + (f" ({card.short_title}):" if short_title else ":"))
    drop_elements = ", ".join(map(lambda x: x.title, card.drop_elements))
    print(f"элемент(-ы): {drop_elements}")
    if isinstance(card, cards.CraftableCard):
        craft_ingredients = ", ".join(map(lambda x: x.title, card.craft_ingredients))
        print(f"Рецепт: {craft_ingredients}")
        if buffer and len(card.buffer) > 0:
            print("Карты на этой карте:")
            for buf_card in card.buffer:
                print(
                    f"{buf_card.title}"
                    + (f" ({buf_card.short_title})" if short_title else "")
                )
    elif isinstance(card, cards.SpellCard):
        print(f"Тип заклинания: {card.spell_type}")
    print()


__all__ = (
    player_input,
    print_card,
)
