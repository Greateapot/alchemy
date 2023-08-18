from alchemy import Alchemy, Player


from alchemy_original_console.handlers.utils import player_input
from alchemy_original_console.handlers.check_act_list import check_act_list_handler
from alchemy_original_console.handlers.check_cards import check_cards_handler
from alchemy_original_console.handlers.check_crafts import check_crafts_handler
from alchemy_original_console.handlers.check_point_list import check_point_list_handler
from alchemy_original_console.handlers.check_shelf import check_shelf_handler
from alchemy_original_console.handlers.craft_recipe import craft_recipe_handler
from alchemy_original_console.handlers.drop_element import drop_elements_handler
from alchemy_original_console.handlers.cast_spell import cast_spell_handler


def handler(session: Alchemy, player: Player) -> bool:
    print(f"Ходит {player.name}")
    check_act_list_handler()
    stop: bool = False
    while not stop:
        match player_input(player, 1, 8):
            case 1:  # check_act_list
                check_act_list_handler()
            case 2:  # check_point_list
                check_point_list_handler(session)
            case 3:  # check_cards
                check_cards_handler(session, player)
            case 4:  # check_crafts
                check_crafts_handler(session, player)
            case 5:  # check_shelf
                check_shelf_handler(session)
            case 6:  # drop_element
                stop = drop_elements_handler(session, player)
            case 7:  # craft_recipe
                stop = craft_recipe_handler(session, player)
            case 8:  # cast_spell
                stop = cast_spell_handler(session, player)
    return False


__all__ = (handler,)
