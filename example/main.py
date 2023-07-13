from alchemy_original_console import create_session


if __name__ == "__main__":
    session = create_session(map(lambda x: f"Player#{x}", range(4)))
    print("А тут вот статистика должна быть... Воооот")
