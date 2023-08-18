from alchemy_original_console import create_session
from toml import load

if __name__ == "__main__":
    with open("example/original_config.toml", "r", encoding="utf-8") as file:
        config = load(file)
    session = create_session(
        config,
        list(map(lambda x: f"Player#{x}", range(4))),
    )
    session.process()
