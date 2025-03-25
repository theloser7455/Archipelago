from BaseClasses import Item, ItemClassification
from typing import NamedTuple

class PTItem(Item):
    game: str = "Pizza Tower"

class PTItemData(NamedTuple):
    code: typing.Optional[int]
    classification: any

item_progression = {
    "Toppin": PTItemData(100, ItemClassification.progression_skip_balancing),
    "Boss Key": PTItemData(101, ItemClassification.progression),
}

item_moveset = {
    "Mach 4": PTItemData(102, ItemClassification.useful),
    "Uppercut": PTItemData(103, ItemClassification.useful),
    "Superjump": PTItemData(104, ItemClassification.progression),
    "Grab": PTItemData(105, ItemClassification.progression),
    "Carry": PTItemData(106, ItemClassification.progression),
    "Piledrive": PTItemData(107, ItemClassification.useful),
    "Taunt": PTItemData(108, ItemClassification.useful),
    "Supertaunt": PTItemData(109, ItemClassification.useful),
    "Bodyslam": PTItemData(110, ItemClassification.progression),
    "Breakdance": PTItemData(111, ItemClassification.filler),
}

item_moveset_peppino = {
    "Peppino: Wallclimb": PTItemData(112, ItemClassification.progression),
    "Peppino: Dive": PTItemData(113, ItemClassification.useful),
    "Gustavo & Brick: Double Jump": PTItemData(114, ItemClassification.progression),
    "Gustavo & Brick: Rat Kick": PTItemData(115, ItemClassification.useful),
    "Gustavo & Brick: Walljump": PTItemData(116, ItemClassification.useful),
    "Gustavo: Spin Attack": PTItemData(117, ItemClassification.useful),
}

item_moveset_noise = {
    "Noise: Wallbounce": PTItemData(118, ItemClassification.progression),
    "Noise: Tornado": PTItemData(119, ItemClassification.useful),
    "Noise: Crusher": PTItemData(120, ItemClassification.progression),
}

item_trap = {
    "Clown Trap": PTItemData(121, ItemClassification.trap),
    "One-Minute War Timer": PTItemData(122, ItemClassification.trap),
    "Pizzaface Trap": PTItemData(123, ItemClassification.trap),
    "Mach 2 Trap": PTItemData(124, ItemClassification.trap),
    "Oktoberfest!": PTItemData(125, ItemClassification.trap),
}

item_other = {
    "Tower Secret Treasure": PTItemData(126, ItemClassification.filler),
    "Cross Buff": PTItemData(127, ItemClassification.filler),
    "Pizza Shield": PTItemData(128, ItemClassification.filler),
    "Rat-B-Gone": PTItemData(129, ItemClassification.filler),
    "1,000 Points": PTItemData(130, ItemClassification.filler)
}

item_transfo = {
    "Ball": PTItemData(131, ItemClassification.useful),
    "Knight": PTItemData(132, ItemClassification.useful),
    "Firemouth": PTItemData(133, ItemClassification.useful),
    "Ghost": PTItemData(134, ItemClassification.useful),
    "Mort": PTItemData(135, ItemClassification.useful),
    "Weenie": PTItemData(136, ItemClassification.progression),
    "Barrel": PTItemData(137, ItemClassification.useful),
    "Antigrav Bubble": PTItemData(138, ItemClassification.useful),
    "Rocket": PTItemData(139, ItemClassification.progression),
    "Rat Balloon": PTItemData(140, ItemClassification.useful),
    "Pizzabox": PTItemData(141, ItemClassification.useful),
    "Sticky Cheese": PTItemData(142, ItemClassification.useful),
    "Pepper Pizza": PTItemData(143, ItemClassification.useful),
    "Shotgun": PTItemData(144, ItemClassification.progression),
}

item_data_list = {
    **item_progression,
    **item_moveset,
    **item_moveset_peppino,
    **item_moveset_noise,
    **item_trap,
    **item_other,
}

item_list = {name: data.code for name, data in item_data_list.items()}
item_moveset_all = {
    **item_moveset,
    **item_moveset_peppino,
    **item_moveset_noise,
}