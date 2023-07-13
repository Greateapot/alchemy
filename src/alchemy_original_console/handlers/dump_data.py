from alchemy import Alchemy, JsonSerializable


def dump_data_handler(session: Alchemy) -> None:
    with open("log.txt", "w", encoding="utf-8") as file:
        file.write(JsonSerializable.serialize(session))
    print("Данные игры сохранены.")
