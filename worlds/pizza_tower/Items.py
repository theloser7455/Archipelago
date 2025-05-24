from BaseClasses import Item, ItemClassification

class PTItem(Item):
    game: str = "Pizza Tower"

pt_items = {
    "Toppin": (101, ItemClassification.progression_skip_balancing),
    "Boss Key": (102, ItemClassification.progression),
    "Lap 2 Portals": (149, ItemClassification.useful),

    "Mach 4": (103, ItemClassification.progression),
    "Uppercut": (104, ItemClassification.progression),
    "Superjump": (105, ItemClassification.progression),
    "Grab": (106, ItemClassification.progression),
    #ID 107 has been reassigned to "Bomb"
    "Taunt": (108, ItemClassification.progression),
    "Supertaunt": (109, ItemClassification.progression),
    "Bodyslam": (110, ItemClassification.progression),
    "Breakdance": (111, ItemClassification.filler),

    "Wallclimb": (112, ItemClassification.progression),
    #"Dive": (113, ItemClassification.useful),
    "Double Jump": (114, ItemClassification.progression),
    "Rat Kick": (115, ItemClassification.progression),
    "Wall Jump": (116, ItemClassification.progression),
    "Spin Attack": (117, ItemClassification.useful),

    "Wallbounce": (118, ItemClassification.progression),
    "Tornado": (119, ItemClassification.progression),
    "Crusher": (120, ItemClassification.progression),
    "Bomb": (107, ItemClassification.progression),

    "Clown Trap": (121, ItemClassification.trap),
    "Timer Trap": (122, ItemClassification.trap),
    "Ghost Trap": (123, ItemClassification.trap),
    "Fake Santa Trap": (124, ItemClassification.trap),
    "Oktoberfest!": (125, ItemClassification.trap),
    "Granny Trap": (147, ItemClassification.trap),

    "Permanent 10 Points": (126, ItemClassification.filler),
    "Permanent 50 Points": (127, ItemClassification.filler),
    "Permanent 100 Points": (128, ItemClassification.filler),
    "Primo Burg": (129, ItemClassification.filler),
    "Cross Buff": (130, ItemClassification.filler),
    "Pizza Shield": (131, ItemClassification.filler),

    #transfo items; may get used someday but not right now
    "Ball": (132, ItemClassification.progression),
    "Knight": (133, ItemClassification.progression),
    "Firemouth": (134, ItemClassification.progression),
    "Ghost": (135, ItemClassification.progression),
    "Mort": (136, ItemClassification.progression),
    "Weenie": (137, ItemClassification.progression),
    "Barrel": (138, ItemClassification.progression),
    "Anti-Grav Bubble": (139, ItemClassification.progression),
    "Rocket": (140, ItemClassification.progression),
    "Pizzabox": (141, ItemClassification.progression),
    "Sticky Cheese": (142, ItemClassification.progression),
    "Satan's Choice": (143, ItemClassification.progression),
    "Shotgun": (144, ItemClassification.progression),
    "Revolver": (145, ItemClassification.progression),

    "Nothing": (146, ItemClassification.filler),

    "Jumpscare": (148, ItemClassification.filler) #replaces oktoberfest if options.jumpscare == true
}