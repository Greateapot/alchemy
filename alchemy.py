from __future__ import annotations

from queue import Queue
from typing import Callable

from alchemy.card_stack import CardStack
from alchemy.cards import CraftableCard
from alchemy.json_serializable import JsonSerializable
from alchemy.player import Player
from alchemy.shelf import Shelf


class Alchemy(JsonSerializable):
    """Игра. Здесь храняться игроки, стопка карт и шкаф элементов."""

    def __init__(
        self,
        card_stack: CardStack,
        players: list[Player],
        cards_count: int,
        handler: Callable[[Alchemy, Player], None],
    ) -> None:
        self.stack: CardStack = card_stack
        self.players = players
        self.cards_count: int = cards_count
        self.handler: Callable[[Alchemy, Player], None] = handler

        self.crafts: list[tuple[Player, CraftableCard]] = list()
        self.shelf: Shelf = Shelf()

        for _ in range(self.cards_count):
            self.shelf.put(self.stack.pop())
            for player in players:
                player.cards.append(self.stack.pop())

    def process(self) -> None:
        """Запуск игры"""
        queue: Queue[Player] = Queue(len(self.players))
        for player in self.players:
            queue.put(player)

        acts_count = 0
        cant_act_players: list[Player] = []

        while len(cant_act_players) != len(self.players):
            current_player = queue.get()

            # Добор карт в начале хода
            while (
                len(current_player.cards) < self.cards_count + 1
                and self.stack.can_pop()
            ):
                current_player.cards.append(self.stack.pop())

            # Действие игрока
            if current_player.can_act():
                if current_player in cant_act_players:
                    cant_act_players.remove(current_player)
                self.handler(self, current_player)
                acts_count += 1
            else:
                cant_act_players.append(current_player)

            queue.put(current_player)

        # TODO: end game stats
