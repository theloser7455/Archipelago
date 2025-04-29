from AutoWorld import World, MultiWorld
from BaseClasses import Location, Region
from .Locations import PTLocation

def set_rules(world: World, multiworld: MultiWorld):
    player: int = world.player

    pt_rules = {
    #John Gutter
        "John Gutter Complete": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"], player)),
        "John Gutter Mushroom Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb", "Uppercut", "Grab"], player)),
        "John Gutter Cheese Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb", "Uppercut", "Grab"], player)),
        "John Gutter Tomato Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb", "Uppercut", "Grab"], player)),
        "John Gutter Sausage Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"], player)),
        "John Gutter Pineapple Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"], player)),
        "John Gutter S Rank": lambda state: (state.has("Peppino: Wallclimb", player)),

    #Pizzascape
        "Pizzascape Complete": lambda state: (state.has_any(["Grab", "Uppercut"], player) and state.has(["Peppino: Wallclimb"], player)),
        "Pizzascape Mushroom Toppin": None,
        "Pizzascape Cheese Toppin": None,
        "Pizzascape Tomato Toppin": lambda state: (state.has_any(["Grab", "Uppercut"], player)),
        "Pizzascape Sausage Toppin": lambda state: (state.has_any(["Grab", "Uppercut"], player)),
        "Pizzascape Pineapple Toppin": lambda state: (state.has_any(["Grab", "Uppercut"], player)),
        "Pizzascape S Rank": lambda state: (state.has_any(["Grab", "Uppercut"], player) and state.has(["Peppino: Wallclimb"], player)),

    #Ancient Cheese
        "Ancient Cheese Complete": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Bodyslam", "Peppino: Dive"], player)),
        "Ancient Cheese Mushroom Toppin": None,
        "Ancient Cheese Cheese Toppin": None,
        "Ancient Cheese Tomato Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "Ancient Cheese Sausage Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Bodyslam", "Peppino: Dive"], player)),
        "Ancient Cheese Pineapple Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Bodyslam", "Peppino: Dive"], player)),
        "Ancient Cheese S Rank": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Bodyslam", "Peppino: Dive"], player)),

    #Bloodsauce Dungeon
        "Bloodsauce Dungeon Complete": lambda state: ((state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player)) and state.has_any(["Superjump", "Peppino: Wallclimb"], player)),
        "Bloodsauce Dungeon Mushroom Toppin": None,
        "Bloodsauce Dungeon Cheese Toppin": None,
        "Bloodsauce Dungeon Tomato Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player)),
        "Bloodsauce Dungeon Sausage Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player)),
        "Bloodsauce Dungeon Pineapple Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player)),
        "Bloodsauce Dungeon S Rank": lambda state: ((state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player)) and state.has_any(["Superjump", "Peppino: Wallclimb"], player)),

    #Oregano Desert
        "Oregano Desert Complete": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"], player or state.has_all(["Grab", "Uppercut"], player))),
        "Oregano Desert Mushroom Toppin": lambda state: (state.has_any(["Uppercut", "Superjump", "Peppino: Wallclimb"], player)),
        "Oregano Desert Cheese Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"], player or state.has_all(["Grab", "Uppercut"], player))),
        "Oregano Desert Tomato Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"], player or state.has_all(["Grab", "Uppercut"], player))),
        "Oregano Desert Sausage Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"], player or state.has_all(["Grab", "Uppercut"], player))),
        "Oregano Desert Pineapple Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"], player or state.has_all(["Grab", "Uppercut"], player))),
        "Oregano Desert S Rank": lambda state: ((state.has_any(["Superjump", "Peppino: Wallclimb"], player or state.has_all(["Grab", "Uppercut"], player))) and state.has_any(["Bodyslam", "Peppino: Dive"], player)),

    #Wasteyard
        "Wasteyard Complete": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"], player)),
        "Wasteyard Mushroom Toppin": None,
        "Wasteyard Cheese Toppin": None,
        "Wasteyard Tomato Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"], player)),
        "Wasteyard Sausage Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"], player)),
        "Wasteyard Pineapple Toppin": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"], player)),
        "Wasteyard S Rank": lambda state: (state.has_any(["Superjump", "Peppino: Wallclimb"], player)),

    #Fun Farm
        "Fun Farm Complete": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"], player) and (state.has_any(["Superjump", "Peppino: Wallclimb"], player))),
        "Fun Farm Mushroom Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"], player) and state.has_any(["Superjump", "Peppino: Wallclimb", "Uppercut"], player)),
        "Fun Farm Cheese Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"], player) and state.has_any(["Superjump", "Peppino: Wallclimb", "Uppercut"], player)),
        "Fun Farm Tomato Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"], player) and (state.has_any(["Superjump", "Peppino: Wallclimb"], player) or state.has_all("Grab", "Uppercut", player))),
        "Fun Farm Sausage Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"], player) and (state.has_any(["Superjump", "Peppino: Wallclimb"], player) or state.has_all("Grab", "Uppercut", player))),
        "Fun Farm Pineapple Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"], player) and (state.has_any(["Superjump", "Peppino: Wallclimb"], player))),
        "Fun Farm S Rank": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"], player) and (state.has_any(["Superjump", "Peppino: Wallclimb"], player))),

    #Fastfood Saloon
        "Fastfood Saloon Complete": lambda state: state.has("Grab", player) and (state.has_all(["Superjump", "Peppino: Dive"], player) or state.has("Peppino: Wallclimb", player)),
        "Fastfood Saloon Mushroom Toppin": lambda state: state.has("Superjump", player),
        "Fastfood Saloon Cheese Toppin": lambda state: state.has_all(["Superjump", "Grab"], player),
        "Fastfood Saloon Tomato Toppin": lambda state: state.has("Grab", player) and (state.has_all(["Superjump", "Peppino: Dive"], player) or state.has("Peppino: Wallclimb", player)),
        "Fastfood Saloon Sausage Toppin": lambda state: state.has("Grab", player) and (state.has_all(["Superjump", "Peppino: Dive"], player) or state.has("Peppino: Wallclimb", player)),
        "Fastfood Saloon Pineapple Toppin": lambda state: state.has("Grab", player) and (state.has_all(["Superjump", "Peppino: Dive"], player) or state.has("Peppino: Wallclimb", player)),
        "Fastfood Saloon S Rank": lambda state: state.has("Grab", player) and (state.has_all(["Superjump", "Peppino: Dive"], player) or state.has("Peppino: Wallclimb", player)),

    #Crust Cove
        "Crust Cove Complete": lambda state: state.has(["Peppino: Wallclimb"], player),
        "Crust Cove Mushroom Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "Crust Cove Cheese Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "Crust Cove Tomato Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "Crust Cove Sausage Toppin": lambda state: state.has("Peppino: Wallclimb", player),
        "Crust Cove Pineapple Toppin": lambda state: state.has("Peppino: Wallclimb", player),
        "Crust Cove S Rank": lambda state: state.has_all(["Peppino: Wallclimb", "Taunt"], player),

    #Gnome Forest
        "Gnome Forest Complete": lambda state: (state.has_any(["Bodyslam", "Grab", "Peppino: Dive"], player) and state.has("Gustavo & Brick: Double Jump", player) and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"], player) and state.has_any(["Superjump", "Peppino: Wallclimb"], player)),
        "Gnome Forest Mushroom Toppin": lambda state: (state.has_any(["Bodyslam", "Grab", "Peppino: Dive"], player) and state.has("Gustavo & Brick: Double Jump", player) and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"], player)),
        "Gnome Forest Cheese Toppin": lambda state: (state.has_any(["Bodyslam", "Grab", "Peppino: Dive"], player) and state.has("Gustavo & Brick: Double Jump", player) and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"], player)),
        "Gnome Forest Tomato Toppin": lambda state: (state.has_any(["Bodyslam", "Grab", "Peppino: Dive"], player) and state.has("Gustavo & Brick: Double Jump", player) and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"], player)),
        "Gnome Forest Sausage Toppin": lambda state: (state.has_any(["Bodyslam", "Grab", "Peppino: Dive"], player) and state.has("Gustavo & Brick: Double Jump", player) and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"], player)),
        "Gnome Forest Pineapple Toppin": lambda state: (state.has_any(["Bodyslam", "Grab", "Peppino: Dive"], player) and state.has("Gustavo & Brick: Double Jump", player) and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"], player)),
        "Gnome Forest S Rank": lambda state: (state.has_any(["Bodyslam", "Grab", "Peppino: Dive"], player) and state.has("Gustavo & Brick: Double Jump", player) and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"], player) and state.has_any(["Superjump", "Peppino: Wallclimb"], player)),

    #Deep-Dish 9
        "Deep-Dish 9 Complete": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player) and state.has_any(["Superjump", "Peppino: Wallclimb"]),
        "Deep-Dish 9 Mushroom Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),
        "Deep-Dish 9 Cheese Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player) and state.has_any(["Superjump", "Peppino: Wallclimb"]),
        "Deep-Dish 9 Tomato Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),
        "Deep-Dish 9 Sausage Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player) and state.has_any(["Superjump", "Peppino: Wallclimb"]),
        "Deep-Dish 9 Pineapple Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player) and state.has_any(["Superjump", "Peppino: Wallclimb"]),
        "Deep-Dish 9 S Rank": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player) and state.has_any(["Superjump", "Peppino: Wallclimb"]),

    #GOLF
        "GOLF Complete": lambda state: state.has_any(["Superjump", "Bodyslam", "Peppino: Wallclimb"], player),
        "GOLF Mushroom Toppin": None,
        "GOLF Cheese Toppin": None,
        "GOLF Tomato Toppin": None,
        "GOLF Sausage Toppin": None,
        "GOLF Pineapple Toppin": None,
        "GOLF S Rank": lambda state: state.has_any(["Superjump", "Bodyslam", "Peppino: Wallclimb"], player),

    #The Pig City
        "The Pig City Complete": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"], player) and state.has("Gustavo & Brick: Double Jump", player) and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"], player)),
        "The Pig City Mushroom Toppin": None,
        "The Pig City Cheese Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "The Pig City Tomato Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"], player),
        "The Pig City Sausage Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"], player) and state.has("Gustavo & Brick: Double Jump", player) and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"], player)),
        "The Pig City Pineapple Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"], player) and state.has("Gustavo & Brick: Double Jump", player) and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"], player)),
        "The Pig City S Rank": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"], player) and state.has("Gustavo & Brick: Double Jump", player) and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"], player) and state.has_any(["Superjump", "Peppino: Wallclimb", "Uppercut"], player)),

    #Peppibot Factory
        "Peppibot Factory Complete": lambda state: state.has("Peppino: Wallclimb", player) and state.has_any(["Bodyslam", "Grab", "Peppino: Dive"], player),
        "Peppibot Factory Mushroom Toppin": lambda state: state.has_any(["Peppino: Wallclimb", "Superjump"], player),
        "Peppibot Factory Cheese Toppin": lambda state: state.has("Peppino: Wallclimb", player),
        "Peppibot Factory Tomato Toppin": lambda state: state.has("Peppino: Wallclimb", player),
        "Peppibot Factory Sausage Toppin": lambda state: state.has("Peppino: Wallclimb", player),
        "Peppibot Factory Pineapple Toppin": lambda state: state.has("Peppino: Wallclimb", player),
        "Peppibot Factory S Rank": lambda state: state.has("Peppino: Wallclimb", player) and state.has_any(["Bodyslam", "Grab", "Peppino: Dive"], player),

    #Oh Shit!
        "Oh Shit! Complete": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]) and state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "Oh Shit! Mushroom Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),
        "Oh Shit! Cheese Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]) and state.has_any(["Superjump", "Peppino: Wallclimb", "Uppercut"], player),
        "Oh Shit! Tomato Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]) and state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "Oh Shit! Sausage Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]) and state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "Oh Shit! Pineapple Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]) and state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "Oh Shit! S Rank": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]) and state.has_any(["Superjump", "Peppino: Wallclimb"], player),

    #Freezerator
        "Freezerator Complete": lambda state: state.has("Peppino: Wallclimb", player) and state.has_any(["Bodyslam", "Peppino: Dive"], player),
        "Freezerator Mushroom Toppin": None,
        "Freezerator Cheese Toppin": lambda state: state.has_any(["Peppino: Wallclimb", "Grab"], player),
        "Freezerator Tomato Toppin": lambda state: state.has("Peppino: Wallclimb", player) and state.has_any(["Bodyslam", "Peppino: Dive"], player),
        "Freezerator Sausage Toppin": lambda state: state.has("Peppino: Wallclimb", player) and state.has_any(["Bodyslam", "Peppino: Dive"], player),
        "Freezerator Pineapple Toppin": lambda state: state.has("Peppino: Wallclimb", player) and state.has_any(["Bodyslam", "Peppino: Dive"], player),
        "Freezerator S Rank": lambda state: state.has("Peppino: Wallclimb", player) and state.has_any(["Bodyslam", "Peppino: Dive"], player),

    #Pizzascare
        "Pizzascare Complete": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),
        "Pizzascare Mushroom Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),
        "Pizzascare Cheese Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),
        "Pizzascare Tomato Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),
        "Pizzascare Sausage Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),
        "Pizzascare Pineapple Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),
        "Pizzascare S Rank": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),

    #Don't Make a Sound
        "Don't Make a Sound Complete": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Grab", "Uppercut"], player),
        "Don't Make a Sound Mushroom Toppin": None,
        "Don't Make a Sound Cheese Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "Don't Make a Sound Tomato Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),
        "Don't Make a Sound Sausage Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "Don't Make a Sound Pineapple Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has("Grab", player),
        "Don't Make a Sound S Rank": lambda state: state.has("Peppino: Wallclimb", player) and state.has_any(["Grab", "Uppercut"], player),

    #WAR
        "WAR Complete": lambda state: state.has_any(["Grab", "Uppercut"], player),
        "WAR Mushroom Toppin": lambda state: state.has_any(["Grab", "Uppercut"], player),
        "WAR Cheese Toppin": lambda state: state.has_any(["Grab", "Uppercut"], player),
        "WAR Tomato Toppin": lambda state: state.has_any(["Grab", "Uppercut"], player),
        "WAR Sausage Toppin": lambda state: state.has_any(["Grab", "Uppercut"], player),
        "WAR Pineapple Toppin": lambda state: state.has_any(["Grab", "Uppercut"], player),
        "WAR S Rank": lambda state: state.has_any(["Grab", "Uppercut"], player) and state.has_any(["Superjump, Peppino: Wallclimb"], player),

    #Crumbling Tower of Pizza
        "The Crumbling Tower of Pizza Complete": lambda state: (state.has_all(["Grab", "Superjump"], player) or (state.has_any(["Grab", "Uppercut"], player) and state.has("Peppino: Wallclimb", player))) and state.has_any(["Bodyslam", "Peppino: Dive"], player),
        "The Crumbling Tower of Pizza S Rank": lambda state: (state.has_all(["Grab", "Superjump"], player) or (state.has_any(["Grab", "Uppercut"], player) and state.has("Peppino: Wallclimb", player))) and state.has_any(["Bodyslam", "Peppino: Dive"], player),

    #Bosses
        "Pepperman Defeated": None,
        "Pepperman S Rank": None,
        "The Vigilante Defeated": lambda state: state.has("Grab", player),
        "The Vigilante S Rank": lambda state: state.has("Grab", player),
        "The Noise Defeated": None,
        "The Noise S Rank": None,
        "Fake Peppino Defeated": None,
        "Fake Peppino S Rank": None,
        "Pizzaface Defeated": lambda state: state.has("Grab", player),

    #misc
        "Snotty Murdered": None,

    #Tutorial
        "Tutorial Complete": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"], player) and (state.has("Superjump", player) or state.has_all(["Uppercut", "Peppino: Wallclimb"], player)) and state.has("Grab", player),
        "Tutorial Complete in under 2 minutes": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"], player) and (state.has("Superjump", player) or state.has_all(["Uppercut", "Peppino: Wallclimb"], player)) and state.has("Grab", player),
        "Tutorial Mushroom Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"], player),
        "Tutorial Cheese Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"], player) and state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "Tutorial Tomato Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"], player) and state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "Tutorial Sausage Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"], player) and (state.has("Superjump", player) or state.has_all(["Uppercut", "Peppino: Wallclimb"], player)),
        "Tutorial Pineapple Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"], player) and (state.has("Superjump", player) or state.has_all(["Uppercut", "Peppino: Wallclimb"], player)) and state.has("Grab", player),
    }

    for check in pt_rules:
        multiworld.get_location(check, player).access_rule = pt_rules[check]

    multiworld.completion_condition[player] = lambda state: state.can_reach("The Crumbling Tower of Pizza Complete", "Location", player)