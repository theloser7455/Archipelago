from BaseClasses import Item, ItemClassification
from typing import typing, NamedTuple

class PTItem(Item):
    game: str = "Pizza Tower"

class PTItemData(NamedTuple):
    code: typing.Optional[int]
    classification: any

pt_items = {
    "Toppin": PTItemData(101, ItemClassification.progression_skip_balancing),
    "Boss Key": PTItemData(102, ItemClassification.progression),
    "Lap 2 Portals": PTItemData(132, ItemClassification.useful),

    "Mach 4": PTItemData(103, ItemClassification.useful),
    "Uppercut": PTItemData(104, ItemClassification.useful),
    "Superjump": PTItemData(105, ItemClassification.progression),
    "Grab": PTItemData(106, ItemClassification.progression),
    #ID 107 has been reassigned to "Noise: Bomb"
    "Taunt": PTItemData(108, ItemClassification.progression),
    "Supertaunt": PTItemData(109, ItemClassification.progression),
    "Bodyslam": PTItemData(110, ItemClassification.progression),
    "Breakdance": PTItemData(111, ItemClassification.filler),

    "Peppino: Wallclimb": PTItemData(112, ItemClassification.progression),
    "Peppino: Dive": PTItemData(113, ItemClassification.useful),
    "Gustavo & Brick: Double Jump": PTItemData(114, ItemClassification.progression),
    "Gustavo & Brick: Rat Kick": PTItemData(115, ItemClassification.progression),
    "Gustavo & Brick: Wall Jump": PTItemData(116, ItemClassification.progression),
    "Gustavo: Spin Attack": PTItemData(117, ItemClassification.useful),

    "Noise: Wallbounce": PTItemData(118, ItemClassification.progression),
    "Noise: Tornado": PTItemData(119, ItemClassification.useful),
    "Noise: Crusher": PTItemData(120, ItemClassification.progression),
    "Noise: Bomb": PTItemData(107, ItemClassification.progression),

    "Clown Trap": PTItemData(121, ItemClassification.trap),
    "Timer Trap": PTItemData(122, ItemClassification.trap),
    "Pizzaface": PTItemData(123, ItemClassification.trap),
    "Fake Santa Trap": PTItemData(124, ItemClassification.trap),
    "Oktoberfest!": PTItemData(125, ItemClassification.trap),
    "Granny Trap": PTItemData(147, ItemClassification.trap),

    "Permanent 10 Points": PTItemData(126, ItemClassification.filler),
    "Permanent 50 Points": PTItemData(127, ItemClassification.filler),
    "Permanent 100 Points": PTItemData(128, ItemClassification.filler),
    "1000 Points": PTItemData(129, ItemClassification.filler),
    "Cross Buff": PTItemData(130, ItemClassification.filler),
    "Pizza Shield": PTItemData(131, ItemClassification.filler),

    "Ball": PTItemData(132, ItemClassification.progression),
    "Knight": PTItemData(133, ItemClassification.progression),
    "Firemouth": PTItemData(134, ItemClassification.progression),
    "Ghost": PTItemData(135, ItemClassification.progression),
    "Mort": PTItemData(136, ItemClassification.progression),
    "Weenie": PTItemData(137, ItemClassification.progression),
    "Barrel": PTItemData(138, ItemClassification.progression),
    "Anti-Grav Bubble": PTItemData(139, ItemClassification.progression),
    "Rocket": PTItemData(140, ItemClassification.progression),
    "Pizzabox": PTItemData(141, ItemClassification.progression),
    "Sticky Cheese": PTItemData(142, ItemClassification.progression),
    "Satan's Choice": PTItemData(143, ItemClassification.progression),
    "Shotgun": PTItemData(144, ItemClassification.progression),
    "Revolver": PTItemData(145, ItemClassification.progression),

    "Sorry Nothing": PTItemData(146, ItemClassification.filler), #may or may not ever get used

    "Jumpscare": PTItemData(148, ItemClassification.filler) #replaces oktoberfest if options.jumpscare == true
}