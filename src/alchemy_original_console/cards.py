from alchemy import CraftableCard, SpellCard, CardStack

from alchemy_original_console.enums import CardType, Element, SpellType


def create_card_stack() -> CardStack:
    ELoF = CraftableCard(
        CardType.potion,
        "Эликсир Огня",
        "ELoF",
        (Element.the_quintessence_of_will,),
        2,
        (
            Element.ether_wave,
            Element.fiery_light,
        ),
    )
    ELoEY = CraftableCard(
        CardType.potion,
        "Эликсир Вечной Молодости",
        "ELoEY",
        (Element.dragon_tooth,),
        2,
        (
            Element.ether_wave,
            Element.phoenix_feather,
        ),
    )
    SoE = CraftableCard(
        CardType.potion,
        "Раствор Вечности",
        "SoE",
        (Element.mandrake_root,),
        2,
        (
            Element.mushrooms,
            Element.phoenix_feather,
        ),
    )
    FoD = CraftableCard(
        CardType.potion,
        "Настой Прорицания",
        "FoD",
        (Element.blood_stone,),
        2,
        (
            Element.mushrooms,
            Element.air_crystal,
        ),
    )
    ELoI = CraftableCard(
        CardType.potion,
        "Эликсир Невидимости",
        "ELoI",
        (Element.astral_energy,),
        2,
        (
            Element.thought_energy,
            Element.air_crystal,
        ),
    )
    IM = CraftableCard(
        CardType.potion,
        "Исидас Мортум",
        "IM",
        (Element.snake_eye,),
        2,
        (
            Element.thought_energy,
            Element.batwing,
        ),
    )
    ELoO = CraftableCard(
        CardType.potion,
        "Эликсир Забвения",
        "ELoO",
        (Element.fern_flower,),
        2,
        (
            Element.belladonna,
            Element.batwing,
        ),
    )
    ELoES = CraftableCard(
        CardType.potion,
        "Эликсир Вечного Сна",
        "ELoES",
        (Element.fiery_light,),
        2,
        (
            Element.belladonna,
            Element.spring_water,
        ),
    )
    EoP = CraftableCard(
        CardType.potion,
        "Эманация Власти",
        "EoP",
        (Element.ether_wave,),
        2,
        (
            Element.the_quintessence_of_will,
            Element.spring_water,
        ),
    )
    SA = CraftableCard(
        CardType.potion,
        "Раствор-Оберег",
        "SA",
        (Element.phoenix_feather,),
        2,
        (
            Element.the_quintessence_of_will,
            Element.dragon_tooth,
        ),
    )
    ELoL = CraftableCard(
        CardType.potion,
        "Эликсир Верности",
        "ELoL",
        (Element.mushrooms,),
        2,
        (
            Element.mandrake_root,
            Element.dragon_tooth,
        ),
    )
    LP = CraftableCard(
        CardType.potion,
        "Любовное Зелье",
        "LP",
        (Element.air_crystal,),
        2,
        (
            Element.mandrake_root,
            Element.blood_stone,
        ),
    )
    ELoP = CraftableCard(
        CardType.potion,
        "Эликсир Силы",
        "ELoP",
        (Element.thought_energy,),
        2,
        (
            Element.astral_energy,
            Element.blood_stone,
        ),
    )
    ELoAS = CraftableCard(
        CardType.potion,
        "Эликсир Тайного Зрения",
        "ELoAS",
        (Element.batwing,),
        2,
        (
            Element.astral_energy,
            Element.snake_eye,
        ),
    )
    PP = CraftableCard(
        CardType.potion,
        'Зелье "Полиглотум"',
        "PP",
        (Element.belladonna,),
        2,
        (
            Element.fern_flower,
            Element.snake_eye,
        ),
    )
    ELoK = CraftableCard(
        CardType.potion,
        "Эликсир Знания",
        "ELoK",
        (Element.spring_water,),
        2,
        (
            Element.fern_flower,
            Element.fiery_light,
        ),
    )

    GEoR = CraftableCard(
        CardType.great_elixir,
        "Великий Эликсир Возрождения",
        "GEoR",
        (Element.batwing,),
        6,
        (
            ELoF,
            ELoEY,
        ),
    )
    GEoO = CraftableCard(
        CardType.great_elixir,
        "Великий Эликсир Предзнаменования",
        "GEoO",
        (Element.spring_water,),
        6,
        (
            SoE,
            FoD,
        ),
    )
    GEoV = CraftableCard(
        CardType.great_elixir,
        "Великий Эликсир Исчезновения",
        "GEoV",
        (Element.dragon_tooth,),
        6,
        (
            ELoI,
            IM,
        ),
    )
    GEoT = CraftableCard(
        CardType.great_elixir,
        "Великий Эликсир Безвремения",
        "GEoT",
        (Element.blood_stone,),
        6,
        (
            ELoO,
            ELoES,
        ),
    )
    GEoP = CraftableCard(
        CardType.great_elixir,
        "Великий Эликсир Защиты",
        "GEoP",
        (Element.snake_eye,),
        6,
        (
            EoP,
            SA,
        ),
    )
    GEoEL = CraftableCard(
        CardType.great_elixir,
        "Великий Эликсир Вечной Любви",
        "GEoEL",
        (Element.fiery_light,),
        6,
        (
            ELoL,
            LP,
        ),
    )
    GEoM = CraftableCard(
        CardType.great_elixir,
        "Великий Эликсир Могущества",
        "GEoM",
        (Element.phoenix_feather,),
        6,
        (
            ELoP,
            ELoAS,
        ),
    )
    GEoI = CraftableCard(
        CardType.great_elixir,
        "Великий Эликсир Прозрения",
        "GEoI",
        (Element.air_crystal,),
        6,
        (
            PP,
            ELoK,
        ),
    )

    ELoW = CraftableCard(
        CardType.elixir,
        "Эликсир Мудрости",
        "ELoW",
        (Element.the_quintessence_of_will,),
        3,
        (
            Element.mandrake_root,
            Element.astral_energy,
            Element.air_crystal,
        ),
    )
    ELoPM = CraftableCard(
        CardType.elixir,
        "Эликсир Повелителя Растений",
        "ELoPM",
        (Element.thought_energy,),
        3,
        (
            Element.belladonna,
            Element.fiery_light,
            Element.the_quintessence_of_will,
        ),
    )
    TP = CraftableCard(
        CardType.elixir,
        "Телепатическое Снадобье",
        "TP",
        (Element.ether_wave,),
        3,
        (
            Element.blood_stone,
            Element.thought_energy,
            Element.mushrooms,
        ),
    )
    ELoFl = CraftableCard(
        CardType.elixir,
        "Эликсир Полета",
        "ELoFl",
        (Element.astral_energy,),
        3,
        (
            Element.ether_wave,
            Element.spring_water,
            Element.fern_flower,
        ),
    )

    AoT = CraftableCard(
        CardType.amulet,
        "Талисман Телепортации",
        "AoT",
        (Element.blood_stone,),
        8,
        (
            SoE,
            ELoFl,
        ),
    )
    AoHK = CraftableCard(
        CardType.amulet,
        "Талисман Скрытого Знания",
        "AoHK",
        (Element.fiery_light,),
        8,
        (
            ELoO,
            ELoW,
        ),
    )
    AoBM = CraftableCard(
        CardType.amulet,
        "Талисман Повелителя Зверей",
        "AoBM",
        (Element.spring_water,),
        8,
        (
            PP,
            ELoPM,
        ),
    )
    AP = CraftableCard(
        CardType.amulet,
        "Талисман Палантириум",
        "AP",
        (Element.air_crystal,),
        8,
        (
            ELoL,
            TP,
        ),
    )

    PoI = CraftableCard(
        CardType.powder,
        "Порошок Бестелесности",
        "PoI",
        (Element.mandrake_root,),
        4,
        (
            ELoES,
            Element.batwing,
        ),
    )
    PoT = CraftableCard(
        CardType.powder,
        "Порошок Истины",
        "PoT",
        (Element.mushrooms,),
        4,
        (
            ELoK,
            Element.snake_eye,
        ),
    )
    PoD = CraftableCard(
        CardType.powder,
        "Порошок Судьбы",
        "PoD",
        (Element.belladonna,),
        4,
        (
            FoD,
            Element.phoenix_feather,
        ),
    )
    PoC = CraftableCard(
        CardType.powder,
        "Порошок Контроля",
        "PoC",
        (Element.fern_flower,),
        4,
        (
            LP,
            Element.dragon_tooth,
        ),
    )

    ESoBN = CraftableCard(
        CardType.entity,
        "Сущность Баньши",
        "ESoBN",
        (Element.dragon_tooth,),
        8,
        (
            EoP,
            PoI,
        ),
    )
    ESoH = CraftableCard(
        CardType.entity,
        "Сущность Гиппогрифа",
        "ESoH",
        (Element.mushrooms,),
        8,
        (
            IM,
            ELoFl,
        ),
    )
    ESoIG = CraftableCard(
        CardType.entity,
        "Сущность Незримого Стража",
        "ESoIG",
        (Element.batwing,),
        8,
        (
            ELoI,
            PoD,
        ),
    )
    ESoBS = CraftableCard(
        CardType.entity,
        "Сущность Василиска",
        "ESoBS",
        (Element.mandrake_root,),
        8,
        (
            ELoAS,
            TP,
        ),
    )
    ESoAC = CraftableCard(
        CardType.entity,
        "Сущность Авокадо-Кадавра",
        "ESoAC",
        (Element.fern_flower,),
        8,
        (
            ELoEY,
            ELoPM,
        ),
    )
    ESoD = CraftableCard(
        CardType.entity,
        "Сущность Дракона",
        "ESoD",
        (Element.snake_eye,),
        8,
        (
            ELoP,
            PoC,
        ),
    )
    ESoU = CraftableCard(
        CardType.entity,
        "Сущность Единорога",
        "ESoU",
        (Element.belladonna,),
        8,
        (
            SA,
            ELoW,
        ),
    )
    ESoFS = CraftableCard(
        CardType.entity,
        "Сущность Огненной Саламандры",
        "ESoFS",
        (Element.phoenix_feather,),
        8,
        (
            ELoF,
            PoT,
        ),
    )

    SPoT = SpellCard(
        CardType.spell,
        "Заклятье Трансформы",
        "SPoT",
        (Element.mandrake_root,),
        SpellType.spell_of_transform,
    )
    SPoK = SpellCard(
        CardType.spell,
        "Заклятье Познания",
        "SPoK",
        (Element.belladonna,),
        SpellType.spell_of_knowledge,
    )
    SPoD = SpellCard(
        CardType.spell,
        "Заклятье Разрушения",
        "SPoD",
        (Element.snake_eye,),
        SpellType.spell_of_destruction,
    )

    GAoM = CraftableCard(
        CardType.great_amulet,
        "Великий Талисман Магии",
        "GAoM",
        (
            Element.phoenix_feather,
            Element.thought_energy,
            Element.dragon_tooth,
        ),
        10,
        (
            CardType.amulet,
            CardType.amulet,
        ),
    )
    SE = CraftableCard(
        CardType.supreme_elixir,
        "Верховный Эликсир",
        "SE",
        (
            Element.astral_energy,
            Element.the_quintessence_of_will,
            Element.ether_wave,
        ),
        10,
        (
            CardType.great_elixir,
            CardType.great_elixir,
        ),
    )

    return CardStack(
        [
            # Зелья
            ELoF,
            ELoEY,
            SoE,
            FoD,
            ELoI,
            IM,
            ELoO,
            ELoES,
            EoP,
            SA,
            ELoL,
            LP,
            ELoP,
            ELoAS,
            PP,
            ELoK,
            # Копии зелий (т.к. должны быть 2 экземплярах)
            ELoF.copy(),
            ELoEY.copy(),
            SoE.copy(),
            FoD.copy(),
            ELoI.copy(),
            IM.copy(),
            ELoO.copy(),
            ELoES.copy(),
            EoP.copy(),
            SA.copy(),
            ELoL.copy(),
            LP.copy(),
            ELoP.copy(),
            ELoAS.copy(),
            PP.copy(),
            ELoK.copy(),
            # Великие Эликсиры
            GEoR,
            GEoO,
            GEoV,
            GEoT,
            GEoP,
            GEoEL,
            GEoM,
            GEoI,
            # Эликсиры
            ELoW,
            ELoPM,
            TP,
            ELoFl,
            # Копии Эликсиров (т.к. должны быть 3 экземплярах)
            ELoW.copy(),
            ELoPM.copy(),
            TP.copy(),
            ELoFl.copy(),
            # Копии Эликсиров, но с другим ингредиентом (2-я копия)
            ELoW.copy_with(drop_elements=(Element.thought_energy,)),
            ELoPM.copy_with(drop_elements=(Element.ether_wave,)),
            TP.copy_with(drop_elements=(Element.astral_energy,)),
            ELoFl.copy_with(drop_elements=(Element.the_quintessence_of_will,)),
            # Талисманы
            AoT,
            AoHK,
            AoBM,
            AP,
            # Великий Талисман Магии и Верховный Эликсир
            GAoM,
            SE,
            # Порошки
            PoI,
            PoT,
            PoD,
            PoC,
            # Сущности
            ESoBN,
            ESoH,
            ESoIG,
            ESoBS,
            ESoAC,
            ESoD,
            ESoU,
            ESoFS,
            # Заклятья
            SPoT,
            SPoK,
            SPoD,
            # Копии заклятий, но с другим ингредиентом (должно быть 2 экземпляра)
            SPoT.copy_with(drop_elements=(Element.batwing,)),
            SPoK.copy_with(drop_elements=(Element.mushrooms,)),
            SPoD.copy_with(drop_elements=(Element.fern_flower,)),
        ]
    )
