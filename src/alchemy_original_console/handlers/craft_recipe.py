from alchemy import Alchemy, Player, cards, enums

from alchemy_original_console.handlers.utils import player_input, print_card


def choice_element_card(
    session: Alchemy,
    cards: list[cards.CardModel],
    player: Player,
) -> cards.CardModel:
    print("Доступные карты в шкафу:\n")
    num: int = 1
    mxl: int = len(str(len(cards)))
    for c in cards:
        print(f"{num: >{mxl}}.", end=" ")
        num += 1
        print_card(c, session.settings.tags_is_visible)

    card_number = player_input(player, 1, mxl)
    return cards[card_number - 1]


def choice_crafted_card(
    session: Alchemy,
    crafts: list[tuple[Player, cards.CraftableCardModel]],
    player: Player,
) -> tuple[Player, cards.CraftableCardModel]:
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
        print_card(c, session.settings.tags_is_visible, p == player)

    craft_number = player_input(player, 1, mxl)
    return crafts[craft_number - 1]


def can_craft(session: Alchemy, card: cards.CraftableCardModel) -> bool:
    cards_used: list[cards.CardModel] = list()
    for ingredient in card.craft_ingredients:
        if isinstance(ingredient, enums.Element):
            if not session.shelf.can_get_element(ingredient):
                return False
        elif isinstance(ingredient, enums.CardType):
            for _, craft in session.crafts:
                if craft.type == ingredient and craft not in cards_used:
                    cards_used.append(craft)
                    break
                else:
                    return False
        elif isinstance(ingredient, cards.CardTag):
            for _, craft in session.crafts:
                if craft.tag == ingredient and craft not in cards_used:
                    cards_used.append(craft)
                    break
            else:
                return False
    return True


def craft(session: Alchemy, player: Player, card: cards.CraftableCardModel) -> None:
    for ingredient in card.craft_ingredients:
        if isinstance(ingredient, enums.Element):
            c = choice_element_card(
                session,
                list(
                    filter(
                        lambda x: ingredient in x.drop_elements,
                        session.shelf.toplist(),
                    )
                ),
                player,
            )
            session.shelf.get_card(c)
            card.buffer.append(c)
        elif isinstance(ingredient, enums.CardType):
            p, c = choice_crafted_card(
                session,
                list(
                    filter(
                        lambda x: x[1].type == ingredient,
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
        elif isinstance(ingredient, cards.CardTag):
            p, c = choice_crafted_card(
                session,
                list(
                    filter(
                        lambda x: x[1].tag == ingredient,
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
            lambda x: isinstance(x, cards.CraftableCardModel),
            player.cards,
        )
    )
    print("Создание рецепта. Список карт:\n")
    for index, card in enumerate(craftable_cards):
        print(
            f"{index + 1}. {card.title}"
            + (f" ({card.tag.tag})" if session.settings.tags_is_visible else "")
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
