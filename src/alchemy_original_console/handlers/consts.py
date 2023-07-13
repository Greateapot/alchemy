DEBUG_ACTIONS_ENABLED = True
SHORT_TITLE_ENABLED = True
MENU_MESSAGE = """
Меню:
1. Этот список
2. Кол-во очков всех игроков
3. Список своих карт
4. Список созданных всеми игроками рецептов
5. Список элементов в шкафу элементов
6. Сбросить карту в шкаф
7. Создать рецепт
8. Использовать заклинание
"""

if DEBUG_ACTIONS_ENABLED:
    MENU_MESSAGE += "9. Сохранить данные игры\n0. Завершить игру\n"

__all__ = (
    DEBUG_ACTIONS_ENABLED,
    SHORT_TITLE_ENABLED,
    MENU_MESSAGE,
)
