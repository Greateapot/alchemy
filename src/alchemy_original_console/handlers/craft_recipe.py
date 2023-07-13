from alchemy import Alchemy, Player, cards

from alchemy_original_console.enums import CardType, Element
from alchemy_original_console.handlers.consts import SHORT_TITLE_ENABLED
from alchemy_original_console.handlers.utils import player_input, print_card


def choice_element_card(
    cards: list[cards.Card],
    player: Player,
) -> cards.Card:
    if len(cards) < 1:
        raise Exception("No cards")

    print("Доступные карты в шкафу:\n")
    num: int = 1
    mxl: int = len(str(len(cards)))
    for c in cards:
        print(f"{num: >{mxl}}.", end=" ")
        num += 1
        print_card(c, SHORT_TITLE_ENABLED)

    card_number = player_input(player, 1, mxl)
    return cards[card_number]


def choice_crafted_card(
    crafts: list[tuple[Player, cards.CraftableCard]],
    player: Player,
) -> tuple[Player, cards.CraftableCard]:
    if len(crafts) < 1:
        raise Exception("No crafts")

    print("Доступные карты созданные игроками:\n")
    last_p: Player = None
    num: int = 1
    mxl: int = len(str(len(crafts)))
    for p, c in sorted(crafts, key=lambda x: x[0].name):
        if p != last_p:
            last_p = p
            print(f"Карты, созданные игроком {p.name}:\n")
        print(f"{num: >{mxl}}.", end=" ")
        num += 1
        print_card(c, SHORT_TITLE_ENABLED, p == player)

    craft_number = player_input(player, 1, mxl)
    return crafts[craft_number]


def can_craft(session: Alchemy, card: cards.CraftableCard) -> bool:
    cards_used: list[cards.Card] = list()
    for ingredient in card.craft_ingredients:
        if isinstance(ingredient, Element):
            if not session.shelf.can_pop(ingredient):
                return False
        elif isinstance(ingredient, CardType):
            match ingredient:
                case CardType.element:
                    ...  # Любой элемент в оригинале не используется
                case CardType.spell:
                    ...  # Заклинание как ингредиент в оригинале не используется
                case _:
                    for _, craft in session.crafts:
                        if craft.card_type == ingredient and craft not in cards_used:
                            cards_used.append(craft)
                            break
                    else:
                        return False
        else:  # CraftableCard
            for _, craft in session.crafts:
                if (
                    craft.short_title == ingredient.short_title
                    and craft not in cards_used
                ):
                    cards_used.append(craft)
                    break
            else:
                return False
    return True


def craft(session: Alchemy, player: Player, card: cards.CraftableCard) -> None:
    for ingredient in card.craft_ingredients:
        if isinstance(ingredient, Element):
            c = choice_element_card(
                list(
                    filter(
                        lambda x: ingredient in x.drop_elements,
                        session.shelf.toplist(),
                    )
                ),
                player,
            )
            session.shelf.pop(c)
            card.buffer.append(c)
        elif isinstance(ingredient, CardType):
            match ingredient:
                case CardType.element:
                    ...  # Любой элемент в оригинале не используется
                case CardType.spell:
                    ...  # Заклинание как ингредиент в оригинале не используется
                case _:
                    p, c = choice_crafted_card(
                        list(
                            filter(
                                lambda x: x[1].card_type == ingredient,
                                session.crafts,
                            )
                        ),
                        player,
                    )
                    session.crafts.remove((p, c))
                    p.cards.remove(c)
                    p.points += card.points // 2
                    for i in c.buffer:
                        session.shelf.put(i)
                    card.buffer.append(c)
            ...
        else:  # CraftableCard
            p, c = choice_crafted_card(
                list(
                    filter(
                        lambda x: x[1].short_title == ingredient.short_title,
                        session.crafts,
                    )
                ),
                player,
            )
            session.crafts.remove((p, c))
            p.points += card.points // 2
            for i in c.buffer:
                session.shelf.put(i)
            card.buffer.append(c)

    player.cards.remove(card)
    player.points += card.points
    session.crafts.append((player, card))


def craft_recipe_handler(session: Alchemy, player: Player) -> bool:
    craftable_cards = list(
        filter(
            lambda x: isinstance(x, cards.CraftableCard),
            player.cards,
        )
    )
    print("Создание рецепта. Список карт:\n")
    for index, card in enumerate(craftable_cards):
        print(
            f"{index + 1}. {card.title}"
            + (f" ({card.short_title})" if SHORT_TITLE_ENABLED else "")
        )
    print("0. Отмена")

    card_number = player_input(player, 0, len(craftable_cards))

    if card_number == 0:
        print("Отмена.")
        return False

    card = craftable_cards[card_number - 1]

    if not can_craft(session, card):
        print("Недостаточно ингредиентов.")
        return False

    craft(session, player, card)
    return True


__all__ = (craft_recipe_handler,)
