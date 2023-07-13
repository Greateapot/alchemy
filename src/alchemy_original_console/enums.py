from alchemy import AbcCardType, AbcElement, AbcSpellType

from enum import IntEnum


class Element(AbcElement):
    snake_eye = "Глаз змеи"
    mandrake_root = "Корень мандрагоры"
    blood_stone = "Камень крови"
    mushrooms = "Мушрумы"
    phoenix_feather = "Перо феникса"
    air_crystal = "Кристалл воздуха"
    spring_water = "Родниковая вода"
    thought_energy = "Энергия мысли"
    fern_flower = "Цеток папоротника"
    batwing = "Крыло летучей мыши"
    the_quintessence_of_will = "Квинтэссенция воли"
    fiery_light = "Огненный свет"
    astral_energy = "Астральная энергия"
    ether_wave = "Волны эфира"
    dragon_tooth = "Зуб дракона"
    belladonna = "Белладонна"


class CardType(AbcCardType):
    element = "Элемент"
    spell = "Заклинание"
    potion = "Зелье"
    elixir = "Эликсир"
    powder = "Порошок"
    great_elixir = "Великий эликсир"
    supreme_elixir = "Верховный эликсир"
    amulet = "Талисман"
    great_amulet = "Великий талисман"
    entity = "Сущность"


class SpellType(AbcSpellType):
    spell_of_knowledge = "Заклинание Знаний"
    spell_of_destruction = "Заклинание Разрушения"
    spell_of_transform = "Заклинание Трансформы"


class PlayerAct(IntEnum):
    check_act_list = 1
    check_point_list = 2
    check_cards = 3
    check_crafts = 4
    check_shelf = 5
    drop_element = 6
    craft_recipe = 7
    cast_spell = 8
    dump_data = 9
    end_process = 0
