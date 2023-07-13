from alchemy import Alchemy, Player

from alchemy_original_console.enums import PlayerAct

from alchemy_original_console.handlers.consts import DEBUG_ACTIONS_ENABLED
from alchemy_original_console.handlers.utils import player_input
from alchemy_original_console.handlers.check_act_list import check_act_list_handler
from alchemy_original_console.handlers.check_cards import check_cards_handler
from alchemy_original_console.handlers.check_crafts import check_crafts_handler
from alchemy_original_console.handlers.check_point_list import check_point_list_handler
from alchemy_original_console.handlers.check_shelf import check_shelf_handler
from alchemy_original_console.handlers.craft_recipe import craft_recipe_handler
from alchemy_original_console.handlers.drop_element import drop_elements_handler
from alchemy_original_console.handlers.cast_spell import cast_spell_handler
from alchemy_original_console.handlers.dump_data import dump_data_handler


def handler(session: Alchemy, player: Player) -> bool:
    print(f"Ходит {player.name}")
    check_act_list_handler()
    stop: bool = False
    while not stop:
        match player_input(
            player,
            0 if DEBUG_ACTIONS_ENABLED else 1,
            9 if DEBUG_ACTIONS_ENABLED else 8,
        ):
            case PlayerAct.check_act_list:
                check_act_list_handler()
            case PlayerAct.check_point_list:
                check_point_list_handler(session)
            case PlayerAct.check_cards:
                check_cards_handler(player)
            case PlayerAct.check_crafts:
                check_crafts_handler(session, player)
            case PlayerAct.check_shelf:
                check_shelf_handler(session)
            case PlayerAct.drop_element:
                stop = drop_elements_handler(session, player)
            case PlayerAct.craft_recipe:
                stop = craft_recipe_handler(session, player)
            case PlayerAct.cast_spell:
                stop = cast_spell_handler(session, player)
            # DEBUG cases
            case PlayerAct.dump_data:
                dump_data_handler(session)
            case PlayerAct.end_process:
                print("Игра окончена!")
                return True
    return False


__all__ = (handler,)
