from __future__ import annotations

from queue import Queue
from typing import Callable

from alchemy.card_stack import CardStack
from alchemy.cards import Card, CraftableCard
from alchemy.json_serializable import JsonSerializable
from alchemy.player import Player
from alchemy.shelf import Shelf


class Alchemy(JsonSerializable):
    """Игра. Здесь храняться игроки, стопка карт и шкаф ингредиентов."""

    def __init__(
        self,
        cards: list[Card],
        players: list[str],
        cards_count: int,
        handler: Callable[[Alchemy, Player], None],
    ) -> None:
        self.stack: CardStack = CardStack()
        self.shelf: Shelf = Shelf()
        self.players: list[Player] = list()

        self.cards_count: int = cards_count
        self.handler: Callable[[Alchemy, Player], None] = handler

        self.crafts: list[tuple[Player, CraftableCard]] = list()

        self.stack.cards = cards
        self.stack.shuffle()

        for _ in range(self.cards_count):
            self.shelf.put(self.stack.pop())

        for player_name in players:
            player = Player(player_name)
            for _ in range(self.cards_count):
                player.cards.append(self.stack.pop())
            self.players.append(player)

        # self.process()

    def process(self) -> None:
        queue: Queue[Player] = Queue(len(self.players))
        for player in self.players:
            queue.put(player)

        acts_count = 0

        while not queue.empty():
            current_player = queue.get()

            # Добор карт в начале хода
            while (
                len(current_player.cards) < self.cards_count + 1
                and self.stack.can_pop()
            ):
                current_player.cards.append(self.stack.pop())

            # Действие игрока
            if current_player.can_act():
                self.handler(self, current_player)
                acts_count += 1
                queue.put(current_player)
