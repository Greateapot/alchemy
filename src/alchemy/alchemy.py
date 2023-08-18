from __future__ import annotations

from queue import Queue
from typing import Any, Callable

from alchemy.enums import load_enums
from alchemy.settings import Settings, load_settings
from alchemy.stack import CardStack
from alchemy.cards import CraftableCardModel, load_cards
from alchemy.player import Player
from alchemy.shelf import IngredientShelf


class Alchemy:
    """Игра. Здесь храняться игроки, стопка карт и шкаф элементов."""

    def __init__(
        self,
        config: dict[str, Any],
        players: list[Player],
        handler: Callable[[Alchemy, Player], bool],
    ) -> None:
        self.players = players
        self.handler: Callable[[Alchemy, Player], bool] = handler

        self.crafts: list[tuple[Player, CraftableCardModel]] = list()
        self.shelf: IngredientShelf = IngredientShelf()

        load_enums(config["enums"])
        self.stack: CardStack = CardStack(load_cards(config["cards"]))
        self.settings: Settings = load_settings(config["settings"])

        self._prepare_complete = False

    def prepare(self) -> None:
        if self._prepare_complete:
            return
        
        if self.settings.shuffle_cards_on_load:
            self.stack.shuffle()

        for _ in range(self.settings.hand_cards_count):
            self.shelf.put(self.stack.pop())
            for player in self.players:
                player.cards.append(self.stack.pop())
        
        self._prepare_complete = True

    def process(self) -> None:
        """Запуск игры"""

        self.prepare()
        queue: Queue[Player] = Queue(len(self.players))
        for player in self.players:
            queue.put(player)

        acts_count = 0
        cant_act_players: list[Player] = []
        stop = False

        while not stop and len(cant_act_players) != len(self.players):
            current_player = queue.get()

            # Добор карт в начале хода
            while (
                len(current_player.cards) < self.settings.hand_cards_count + 1
                and self.stack.can_pop()
            ):
                current_player.cards.append(self.stack.pop())

            # Действие игрока
            if current_player.can_act():
                if current_player in cant_act_players:
                    cant_act_players.remove(current_player)
                stop = self.handler(self, current_player)
                acts_count += 1
            else:
                cant_act_players.append(current_player)

            queue.put(current_player)
