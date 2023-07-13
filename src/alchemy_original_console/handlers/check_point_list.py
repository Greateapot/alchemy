from alchemy import Alchemy


def check_point_list_handler(session: Alchemy) -> None:
    print("Кол-во очков у игроков:")
    max_player_name_length = max(*[len(player.name) for player in session.players])
    for player in session.players:
        print(f"{player.name: <{max_player_name_length}}: {player.points}")


__all__ = (check_point_list_handler,)
