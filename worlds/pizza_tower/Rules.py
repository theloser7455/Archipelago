from AutoWorld import World, MultiWorld
from BaseClasses import Location, Region
from .Locations import PTLocation


pt_rules = { #TODO add player parameter to all of these cuz i forgot
#John Gutter
    "John Gutter Complete": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"])),
    "John Gutter Mushroom Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb", "Uppercut", "Grab"])),
    "John Gutter Cheese Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb", "Uppercut", "Grab"])),
    "John Gutter Tomato Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb", "Uppercut", "Grab"])),
    "John Gutter Sausage Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"])),
    "John Gutter Pineapple Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"])),
    "John Gutter S Rank": lambda state: (state.has("Peppino: Wallclimb")),

#Pizzascape
    "Pizzascape Complete": lambda state: (state.has_any(["Grab", "Uppercut"]) and state.has(["Peppino: Wallclimb"])),
    "Pizzascape Mushroom Toppin": None,
    "Pizzascape Cheese Toppin": None,
    "Pizzascape Tomato Toppin": lambda state: (state.has_any(["Grab", "Uppercut"])),
    "Pizzascape Sausage Toppin": lambda state: (state.has_any(["Grab", "Uppercut"])),
    "Pizzascape Pineapple Toppin": lambda state: (state.has_any(["Grab", "Uppercut"])),
    "Pizzascape S Rank": lambda state: (state.has_any(["Grab", "Uppercut"]) and state.has(["Peppino: Wallclimb"])),

#Ancient Cheese
    "Ancient Cheese Complete": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"]) and state.has_any(["Bodyslam", "Peppino: Dive"])),
    "Ancient Cheese Mushroom Toppin": None,
    "Ancient Cheese Cheese Toppin": None,
    "Ancient Cheese Tomato Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"]),
    "Ancient Cheese Sausage Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"]) and state.has_any(["Bodyslam", "Peppino: Dive"])),
    "Ancient Cheese Pineapple Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"]) and state.has_any(["Bodyslam", "Peppino: Dive"])),
    "Ancient Cheese S Rank": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"]) and state.has_any(["Bodyslam", "Peppino: Dive"])),

#Bloodsauce Dungeon
    "Bloodsauce Dungeon Complete": lambda state: ((state.has_any(["Bodyslam", "Peppino: Dive", "Grab"])) and state.has_any(["Superjump", "Peppino: Wallclimb"])),
    "Bloodsauce Dungeon Mushroom Toppin": None,
    "Bloodsauce Dungeon Cheese Toppin": None,
    "Bloodsauce Dungeon Tomato Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive", "Grab"])),
    "Bloodsauce Dungeon Sausage Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive", "Grab"])),
    "Bloodsauce Dungeon Pineapple Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive", "Grab"])),
    "Bloodsauce Dungeon S Rank": lambda state: ((state.has_any(["Bodyslam", "Peppino: Dive", "Grab"])) and state.has_any(["Superjump", "Peppino: Wallclimb"])),

#Oregano Desert
    "Oregano Desert Complete": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"] or state.has_all(["Grab", "Uppercut"]))),
    "Oregano Desert Mushroom Toppin": lambda state: (state.has_any(["Uppercut", "Superjump", "Peppino: Wallclimb"])),
    "Oregano Desert Cheese Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"] or state.has_all(["Grab", "Uppercut"]))),
    "Oregano Desert Tomato Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"] or state.has_all(["Grab", "Uppercut"]))),
    "Oregano Desert Sausage Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"] or state.has_all(["Grab", "Uppercut"]))),
    "Oregano Desert Pineapple Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"] or state.has_all(["Grab", "Uppercut"]))),
    "Oregano Desert S Rank": lambda state: ((state.has_any(["Superjump", "Peppino: Wallclimb"] or state.has_all(["Grab", "Uppercut"]))) and state.has_any(["Bodyslam", "Peppino: Dive"])),

#Wasteyard
    "Wasteyard Complete": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"])),
    "Wasteyard Mushroom Toppin": None,
    "Wasteyard Cheese Toppin": None,
    "Wasteyard Tomato Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"])),
    "Wasteyard Sausage Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"])),
    "Wasteyard Pineapple Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"])),
    "Wasteyard S Rank": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"])),

#Fun Farm
    "Fun Farm Complete": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"]) and (state.has_any(["Superjump", "Peppino: Wallclimb"]))),
    "Fun Farm Mushroom Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"]) and state.has_any(["Superjump", "Peppino: Wallclimb", "Uppercut"])),
    "Fun Farm Cheese Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"]) and state.has_any(["Superjump", "Peppino: Wallclimb", "Uppercut"])),
    "Fun Farm Tomato Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"]) and (state.has_any(["Superjump", "Peppino: Wallclimb"]) or state.has_all("Grab", "Uppercut"))),
    "Fun Farm Sausage Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"]) and (state.has_any(["Superjump", "Peppino: Wallclimb"]) or state.has_all("Grab", "Uppercut"))),
    "Fun Farm Pineapple Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"]) and (state.has_any(["Superjump", "Peppino: Wallclimb"]))),
    "Fun Farm S Rank": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"]) and (state.has_any(["Superjump", "Peppino: Wallclimb"]))),

#Fastfood Saloon
    "Fastfood Saloon Complete": lambda state: state.has("Grab") and (state.has_all(["Superjump", "Peppino: Dive"]) or state.has("Peppino: Wallclimb")),
    "Fastfood Saloon Mushroom Toppin": lambda state: state.has("Superjump"),
    "Fastfood Saloon Cheese Toppin": lambda state: state.has_all(["Superjump", "Grab"]),
    "Fastfood Saloon Tomato Toppin": lambda state: state.has("Grab") and (state.has_all(["Superjump", "Peppino: Dive"]) or state.has("Peppino: Wallclimb")),
    "Fastfood Saloon Sausage Toppin": lambda state: state.has("Grab") and (state.has_all(["Superjump", "Peppino: Dive"]) or state.has("Peppino: Wallclimb")),
    "Fastfood Saloon Pineapple Toppin": lambda state: state.has("Grab") and (state.has_all(["Superjump", "Peppino: Dive"]) or state.has("Peppino: Wallclimb")),
    "Fastfood Saloon S Rank": lambda state: state.has("Grab") and (state.has_all(["Superjump", "Peppino: Dive"]) or state.has("Peppino: Wallclimb")),

#Crust Cove
    "Crust Cove Complete": lambda state: state.has(["Peppino: Wallclimb"]),
    "Crust Cove Mushroom Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"]),
    "Crust Cove Cheese Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"]),
    "Crust Cove Tomato Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"]),
    "Crust Cove Sausage Toppin": lambda state: state.has("Peppino: Wallclimb"),
    "Crust Cove Pineapple Toppin": lambda state: state.has("Peppino: Wallclimb"),
    "Crust Cove S Rank": lambda state: state.has_all(["Peppino: Wallclimb", "Taunt"]),

#Gnome Forest
    "Gnome Forest Complete": lambda state: (state.has_any(["Bodyslam", "Grab", "Peppino: Dive"]) and state.has("Gustavo & Brick: Double Jump") and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"]) and state.has_any(["Superjump", "Peppino: Wallclimb"])),
    "Gnome Forest Mushroom Toppin": lambda state: (state.has_any(["Bodyslam", "Grab", "Peppino: Dive"]) and state.has("Gustavo & Brick: Double Jump") and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"])),
    "Gnome Forest Cheese Toppin": lambda state: (state.has_any(["Bodyslam", "Grab", "Peppino: Dive"]) and state.has("Gustavo & Brick: Double Jump") and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"])),
    "Gnome Forest Tomato Toppin": lambda state: (state.has_any(["Bodyslam", "Grab", "Peppino: Dive"]) and state.has("Gustavo & Brick: Double Jump") and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"])),
    "Gnome Forest Sausage Toppin": lambda state: (state.has_any(["Bodyslam", "Grab", "Peppino: Dive"]) and state.has("Gustavo & Brick: Double Jump") and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"])),
    "Gnome Forest Pineapple Toppin": lambda state: (state.has_any(["Bodyslam", "Grab", "Peppino: Dive"]) and state.has("Gustavo & Brick: Double Jump") and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"])),
    "Gnome Forest S Rank": lambda state: (state.has_any(["Bodyslam", "Grab", "Peppino: Dive"]) and state.has("Gustavo & Brick: Double Jump") and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"]) and state.has_any(["Superjump", "Peppino: Wallclimb"])),

#Deep-Dish 9
    "Deep-Dish 9 Complete": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]) and state.has_any("Superjump", "Peppino: Wallclimb"),
    "Deep-Dish 9 Mushroom Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]),
    "Deep-Dish 9 Cheese Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]) and state.has_any("Superjump", "Peppino: Wallclimb"),
    "Deep-Dish 9 Tomato Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]),
    "Deep-Dish 9 Sausage Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]) and state.has_any("Superjump", "Peppino: Wallclimb"),
    "Deep-Dish 9 Pineapple Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]) and state.has_any("Superjump", "Peppino: Wallclimb"),
    "Deep-Dish 9 S Rank": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]) and state.has_any("Superjump", "Peppino: Wallclimb"),

#GOLF
    "GOLF Complete": lambda state: state.has_any(["Superjump", "Bodyslam", "Peppino: Wallclimb"]),
    "GOLF Mushroom Toppin": None,
    "GOLF Cheese Toppin": None,
    "GOLF Tomato Toppin": None,
    "GOLF Sausage Toppin": None,
    "GOLF Pineapple Toppin": None,
    "GOLF S Rank": lambda state: state.has_any(["Superjump", "Bodyslam", "Peppino: Wallclimb"]),

#The Pig City
    "The Pig City Complete": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"]) and state.has("Gustavo & Brick: Double Jump") and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"])),
    "The Pig City Mushroom Toppin": None,
    "The Pig City Cheese Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"]),
    "The Pig City Tomato Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"]),
    "The Pig City Sausage Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"]) and state.has("Gustavo & Brick: Double Jump") and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"])),
    "The Pig City Pineapple Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"]) and state.has("Gustavo & Brick: Double Jump") and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"])),
    "The Pig City S Rank": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"]) and state.has("Gustavo & Brick: Double Jump") and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"]) and state.has_any(["Superjump", "Peppino: Wallclimb", "Uppercut"])),

#Peppibot Factory
    "Peppibot Factory Complete": lambda state: state.has("Peppino: Wallclimb") and state.has_any(["Bodyslam", "Grab", "Peppino: Dive"]),
    "Peppibot Factory Mushroom Toppin": lambda state: state.has_any(["Peppino: Wallclimb", "Superjump"]),
    "Peppibot Factory Cheese Toppin": lambda state: state.has("Peppino: Wallclimb"),
    "Peppibot Factory Tomato Toppin": lambda state: state.has("Peppino: Wallclimb"),
    "Peppibot Factory Sausage Toppin": lambda state: state.has("Peppino: Wallclimb"),
    "Peppibot Factory Pineapple Toppin": lambda state: state.has("Peppino: Wallclimb"),
    "Peppibot Factory S Rank": lambda state: state.has("Peppino: Wallclimb") and state.has_any(["Bodyslam", "Grab", "Peppino: Dive"]),

#Oh Shit!
    "Oh Shit! Complete": lambda state: state.has_any("Bodyslam", "Peppino: Dive", "Grab") and state.has_any(["Superjump", "Peppino: Wallclimb"]),
    "Oh Shit! Mushroom Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]),
    "Oh Shit! Cheese Toppin": lambda state: state.has_any("Bodyslam", "Peppino: Dive", "Grab") and state.has_any(["Superjump", "Peppino: Wallclimb", "Uppercut"]),
    "Oh Shit! Tomato Toppin": lambda state: state.has_any("Bodyslam", "Peppino: Dive", "Grab") and state.has_any(["Superjump", "Peppino: Wallclimb"]),
    "Oh Shit! Sausage Toppin": lambda state: state.has_any("Bodyslam", "Peppino: Dive", "Grab") and state.has_any(["Superjump", "Peppino: Wallclimb"]),
    "Oh Shit! Pineapple Toppin": lambda state: state.has_any("Bodyslam", "Peppino: Dive", "Grab") and state.has_any(["Superjump", "Peppino: Wallclimb"]),
    "Oh Shit! S Rank": lambda state: state.has_any("Bodyslam", "Peppino: Dive", "Grab") and state.has_any(["Superjump", "Peppino: Wallclimb"]),

#Freezerator
    "Freezerator Complete": lambda state: state.has("Peppino: Wallclimb") and state.has_any(["Bodyslam", "Peppino: Dive"]),
    "Freezerator Mushroom Toppin": None,
    "Freezerator Cheese Toppin": lambda state: state.has_any(["Peppino: Wallclimb", "Grab"]),
    "Freezerator Tomato Toppin": lambda state: state.has("Peppino: Wallclimb") and state.has_any(["Bodyslam", "Peppino: Dive"]),
    "Freezerator Sausage Toppin": lambda state: state.has("Peppino: Wallclimb") and state.has_any(["Bodyslam", "Peppino: Dive"]),
    "Freezerator Pineapple Toppin": lambda state: state.has("Peppino: Wallclimb") and state.has_any(["Bodyslam", "Peppino: Dive"]),
    "Freezerator S Rank": lambda state: state.has("Peppino: Wallclimb") and state.has_any(["Bodyslam", "Peppino: Dive"]),

#Pizzascare
    "Pizzascare Complete": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"]) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]),
    "Pizzascare Mushroom Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"]) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]),
    "Pizzascare Cheese Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"]) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]),
    "Pizzascare Tomato Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"]) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]),
    "Pizzascare Sausage Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"]) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]),
    "Pizzascare Pineapple Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"]) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]),
    "Pizzascare S Rank": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"]) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]),

#Don't Make a Sound
    "Don't Make a Sound Complete": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"]) and state.has_any(["Grab", "Uppercut"]),
    "Don't Make a Sound Mushroom Toppin": None,
    "Don't Make a Sound Cheese Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"]),
    "Don't Make a Sound Tomato Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"]) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]),
    "Don't Make a Sound Sausage Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"]),
    "Don't Make a Sound Pineapple Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"]) and state.has("Grab"),
    "Don't Make a Sound S Rank": lambda state: state.has("Peppino: Wallclimb") and state.has_any(["Grab", "Uppercut"]),

#WAR
    "WAR Complete": lambda state: state.has_any(["Grab", "Uppercut"]),
    "WAR Mushroom Toppin": lambda state: state.has_any(["Grab", "Uppercut"]),
    "WAR Cheese Toppin": lambda state: state.has_any(["Grab", "Uppercut"]),
    "WAR Tomato Toppin": lambda state: state.has_any(["Grab", "Uppercut"]),
    "WAR Sausage Toppin": lambda state: state.has_any(["Grab", "Uppercut"]),
    "WAR Pineapple Toppin": lambda state: state.has_any(["Grab", "Uppercut"]),
    "WAR S Rank": lambda state: state.has_any(["Grab", "Uppercut"]) and state.has_any(["Superjump, Peppino: Wallclimb"]),

#Crumbling Tower of Pizza
    "The Crumbling Tower of Pizza Complete": lambda state: (state.has_all(["Grab", "Superjump"]) or (state.has_any(["Grab", "Uppercut"]) and state.has("Peppino: Wallclimb"))) and state.has_any(["Bodyslam", "Peppino: Dive"]),
    "The Crumbling Tower of Pizza S Rank": lambda state: (state.has_all(["Grab", "Superjump"]) or (state.has_any(["Grab", "Uppercut"]) and state.has("Peppino: Wallclimb"))) and state.has_any(["Bodyslam", "Peppino: Dive"]),

#Bosses
    "Pepperman Defeated": None,
    "Pepperman S Rank": None,
    "The Vigilante Defeated": None,
    "The Vigilante S Rank": None,
    "The Noise Defeated": None,
    "The Noise S Rank": None,
    "Fake Peppino Defeated": None,
    "Fake Peppino S Rank": None,
    "Pizzaface Defeated": lambda state: state.has("Grab"),

#misc
    "Snotty Murdered": None,

#Tutorial
    "Tutorial Complete": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"]) and (state.has("Superjump") or state.has_all(["Uppercut", "Peppino: Wallclimb"])) and state.has("Grab"),
    "Tutorial Complete in under 2 minutes": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"]) and (state.has("Superjump") or state.has_all(["Uppercut", "Peppino: Wallclimb"])) and state.has("Grab"),
    "Tutorial Mushroom Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"]),
    "Tutorial Cheese Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"]) and state.has_any(["Superjump", "Peppino: Wallclimb"]),
    "Tutorial Tomato Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"]) and state.has_any(["Superjump", "Peppino: Wallclimb"]),
    "Tutorial Sausage Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"]) and (state.has("Superjump") or state.has_all(["Uppercut", "Peppino: Wallclimb"])),
    "Tutorial Pineapple Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"]) and (state.has("Superjump") or state.has_all(["Uppercut", "Peppino: Wallclimb"])) and state.has("Grab"),
}