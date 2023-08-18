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

# TODO: check output of serialized cards
def print_card(
    card: cards.CardModel,
    tags_is_visible: bool = False,
    buffer: bool = False,
) -> None:
    print(f"{card.title}" + (f" ({card.tag.tag}):" if tags_is_visible else ":"))
    drop_elements = ", ".join(map(lambda x: x.serialize(), card.drop_elements))
    print(f"элемент(-ы): {drop_elements}")
    if isinstance(card, cards.CraftableCardModel):
        craft_ingredients = ", ".join(
            map(lambda x: x.serialize(), card.craft_ingredients)
        )
        print(f"Рецепт: {craft_ingredients}")
        if buffer and len(card.buffer) > 0:
            print("Карты на этой карте:")
            for buf_card in card.buffer:
                print(
                    f"{buf_card.title}"
                    + (f" ({buf_card.tag.tag})" if tags_is_visible else "")
                )
    elif isinstance(card, cards.SpellCardModel):
        print(f"Тип заклинания: {card.spell}")
    print()


__all__ = (
    player_input,
    print_card,
)
