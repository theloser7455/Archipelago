from BaseClasses import Item, ItemClassification
from typing import typing, NamedTuple

class PTItem(Item):
    game: str = "Pizza Tower"

class PTItemData(NamedTuple):
    code: typing.Optional[int]
    classification: any

item_progression = {
    "Toppin": PTItemData(101, ItemClassification.progression_skip_balancing),
    "Boss Key": PTItemData(102, ItemClassification.progression),
}

item_moveset = {
    "Mach 4": PTItemData(103, ItemClassification.useful),
    "Uppercut": PTItemData(104, ItemClassification.progression),
    "Superjump": PTItemData(105, ItemClassification.progression),
    "Grab": PTItemData(106, ItemClassification.progression),
    #"Piledrive": PTItemData(107, ItemClassification.useful), #redundant
    "Taunt": PTItemData(108, ItemClassification.progression),
    "Supertaunt": PTItemData(109, ItemClassification.useful),
    "Bodyslam": PTItemData(110, ItemClassification.progression),
    "Breakdance": PTItemData(111, ItemClassification.filler),
}

item_moveset_peppino = {
    "Peppino: Wallclimb": PTItemData(112, ItemClassification.progression),
    "Peppino: Dive": PTItemData(113, ItemClassification.progression),
    "Gustavo & Brick: Double Jump": PTItemData(114, ItemClassification.progression),
    "Gustavo & Brick: Rat Kick": PTItemData(115, ItemClassification.progression),
    "Gustavo & Brick: Walljump": PTItemData(116, ItemClassification.progression),
    "Gustavo: Spin Attack": PTItemData(117, ItemClassification.progression),
}

item_moveset_noise = {
    "Noise: Wallbounce": PTItemData(118, ItemClassification.progression),
    "Noise: Tornado": PTItemData(119, ItemClassification.useful),
    "Noise: Crusher": PTItemData(120, ItemClassification.progression),
}

item_trap = {
    "Clown Trap": PTItemData(121, ItemClassification.trap),
    "One-Minute Timer": PTItemData(122, ItemClassification.trap),
    "Pizzaface Trap": PTItemData(123, ItemClassification.trap),
    "Slow Trap": PTItemData(124, ItemClassification.trap),
    "Oktoberfest!": PTItemData(125, ItemClassification.trap),
}

item_other = {
    "Tower Secret Treasure": PTItemData(126, ItemClassification.filler),
    "Cross Buff": PTItemData(127, ItemClassification.filler),
    "Pizza Shield": PTItemData(128, ItemClassification.filler),
    "Rat-B-Gone": PTItemData(129, ItemClassification.filler),
    "1,000 Points": PTItemData(130, ItemClassification.filler),
}