from AutoWorld import World, MultiWorld
from BaseClasses import Location, Region
from .Locations import PTLocation
from .Options import PTOptions

def set_rules(world: World, multiworld: MultiWorld):
    player: int = world.player

    #lots of logic checks fall under these categories
    peppino_requires_upward_mobility = lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player)
    peppino_requires_downward_mobility = lambda state: state.has_any(["Bodyslam", "Peppino: Dive"], player)
    noise_requires_upward_mobility = lambda state: state.has_any(["Superjump", "Noise: Crusher"], player)
    noise_requires_downward_mobility = lambda state: state.has_any(["Bodyslam", "Noise: Tornado"], player)
    requires_any_grab = lambda state: state.has_any(["Grab", "Uppercut"], player)

    #lambda function aliases for easier reading
    requires_uppercut = lambda state: state.has("Uppercut", player)
    requires_grab = lambda state: state.has("Uppercut", player)
    requires_superjump = lambda state: state.has("Superjump", player)
    requires_taunt = lambda state: state.has("Taunt", player)
    peppino_requires_wallclimb = lambda state: state.has("Peppino: Wallclimb", player)
    gustavo_requires_upward_mobility = lambda state: state.has_all(["Gustavo & Brick: Double Jump", "Gustavo & Brick: Wall Jump"], player)
    gustavo_requires_attack = lambda state: state.has_any(["Gustavo & Brick: Rat Kick", "Gustavo: Spin Attack"], player)

    pt_peppino_rules = {
    #John Gutter
        "John Gutter Complete": peppino_requires_upward_mobility,
        "John Gutter Mushroom Toppin": peppino_requires_upward_mobility or requires_uppercut,
        "John Gutter Cheese Toppin": peppino_requires_upward_mobility or requires_uppercut,
        "John Gutter Tomato Toppin": peppino_requires_upward_mobility or requires_uppercut,
        "John Gutter Sausage Toppin": peppino_requires_upward_mobility,
        "John Gutter Pineapple Toppin": peppino_requires_upward_mobility,

    #Pizzascape
        "Pizzascape Complete": requires_any_grab and peppino_requires_wallclimb,
        "Pizzascape Mushroom Toppin": None,
        "Pizzascape Cheese Toppin": None,
        "Pizzascape Tomato Toppin": requires_any_grab,
        "Pizzascape Sausage Toppin": requires_any_grab,
        "Pizzascape Pineapple Toppin": requires_any_grab,

    #Ancient Cheese
        "Ancient Cheese Complete": requires_any_grab and peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Ancient Cheese Mushroom Toppin": None,
        "Ancient Cheese Cheese Toppin": requires_any_grab,
        "Ancient Cheese Tomato Toppin": requires_any_grab and peppino_requires_upward_mobility,
        "Ancient Cheese Sausage Toppin": requires_any_grab and peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Ancient Cheese Pineapple Toppin": requires_any_grab and peppino_requires_upward_mobility and peppino_requires_downward_mobility,

    #Bloodsauce Dungeon
        "Bloodsauce Dungeon Complete": peppino_requires_downward_mobility and peppino_requires_upward_mobility,
        "Bloodsauce Dungeon Mushroom Toppin": None,
        "Bloodsauce Dungeon Cheese Toppin": None,
        "Bloodsauce Dungeon Tomato Toppin": peppino_requires_downward_mobility,
        "Bloodsauce Dungeon Sausage Toppin": peppino_requires_downward_mobility,
        "Bloodsauce Dungeon Pineapple Toppin": peppino_requires_downward_mobility,

    #Oregano Desert
        "Oregano Desert Complete": peppino_requires_wallclimb,
        "Oregano Desert Mushroom Toppin": peppino_requires_upward_mobility or requires_uppercut,
        "Oregano Desert Cheese Toppin": peppino_requires_upward_mobility,
        "Oregano Desert Tomato Toppin": peppino_requires_wallclimb,
        "Oregano Desert Sausage Toppin": peppino_requires_wallclimb,
        "Oregano Desert Pineapple Toppin": peppino_requires_wallclimb,

    #Wasteyard
        "Wasteyard Complete": peppino_requires_upward_mobility,
        "Wasteyard Mushroom Toppin": None,
        "Wasteyard Cheese Toppin": peppino_requires_upward_mobility,
        "Wasteyard Tomato Toppin": peppino_requires_upward_mobility,
        "Wasteyard Sausage Toppin": peppino_requires_upward_mobility,
        "Wasteyard Pineapple Toppin": peppino_requires_upward_mobility,

    #Fun Farm
        "Fun Farm Complete": peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Fun Farm Mushroom Toppin": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or requires_uppercut),
        "Fun Farm Cheese Toppin": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or requires_uppercut),
        "Fun Farm Tomato Toppin": peppino_requires_downward_mobility and peppino_requires_upward_mobility,
        "Fun Farm Sausage Toppin": peppino_requires_downward_mobility and peppino_requires_upward_mobility,
        "Fun Farm Pineapple Toppin": peppino_requires_downward_mobility and peppino_requires_upward_mobility,

    #Fastfood Saloon
        "Fastfood Saloon Complete": lambda state: state.has("Grab", player) and (state.has_all(["Superjump", "Peppino: Dive"], player) or state.has("Peppino: Wallclimb", player)),
        "Fastfood Saloon Mushroom Toppin": requires_superjump,
        "Fastfood Saloon Cheese Toppin": requires_superjump and requires_grab,
        "Fastfood Saloon Tomato Toppin": requires_superjump and peppino_requires_wallclimb and requires_grab,
        "Fastfood Saloon Sausage Toppin": requires_superjump and peppino_requires_wallclimb and requires_grab,
        "Fastfood Saloon Pineapple Toppin": requires_superjump and peppino_requires_wallclimb and requires_grab,

    #Crust Cove
        "Crust Cove Complete": peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)),
        "Crust Cove Mushroom Toppin": peppino_requires_upward_mobility,
        "Crust Cove Cheese Toppin": peppino_requires_upward_mobility,
        "Crust Cove Tomato Toppin": peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)),
        "Crust Cove Sausage Toppin": peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)),
        "Crust Cove Pineapple Toppin": peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)),

    #Gnome Forest
        "Gnome Forest Complete": peppino_requires_upward_mobility and peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,
        "Gnome Forest Mushroom Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,
        "Gnome Forest Cheese Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,
        "Gnome Forest Tomato Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,
        "Gnome Forest Sausage Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,
        "Gnome Forest Pineapple Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,

    #Deep-Dish 9
        "Deep-Dish 9 Complete": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player) and state.has_any(["Superjump", "Peppino: Wallclimb"]),
        "Deep-Dish 9 Mushroom Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),
        "Deep-Dish 9 Cheese Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player) and state.has_any(["Superjump", "Peppino: Wallclimb"]),
        "Deep-Dish 9 Tomato Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),
        "Deep-Dish 9 Sausage Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player) and state.has_any(["Superjump", "Peppino: Wallclimb"]),
        "Deep-Dish 9 Pineapple Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player) and state.has_any(["Superjump", "Peppino: Wallclimb"]),

    #GOLF
        "GOLF Complete": lambda state: state.has_any(["Superjump", "Bodyslam", "Peppino: Wallclimb", "Uppercut"], player),
        "GOLF Mushroom Toppin": None,
        "GOLF Cheese Toppin": None,
        "GOLF Tomato Toppin": None,
        "GOLF Sausage Toppin": None,
        "GOLF Pineapple Toppin": None,

    #The Pig City
        "The Pig City Complete": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"], player) and state.has("Gustavo & Brick: Double Jump", player) and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"], player)),
        "The Pig City Mushroom Toppin": None,
        "The Pig City Cheese Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "The Pig City Tomato Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"], player),
        "The Pig City Sausage Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"], player) and state.has("Gustavo & Brick: Double Jump", player) and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"], player)),
        "The Pig City Pineapple Toppin": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"], player) and state.has("Gustavo & Brick: Double Jump", player) and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"], player)),

    #Peppibot Factory
        "Peppibot Factory Complete": lambda state: state.has("Peppino: Wallclimb", player) and state.has_any(["Bodyslam", "Grab", "Peppino: Dive"], player),
        "Peppibot Factory Mushroom Toppin": lambda state: state.has_any(["Peppino: Wallclimb", "Superjump"], player),
        "Peppibot Factory Cheese Toppin": lambda state: state.has("Peppino: Wallclimb", player),
        "Peppibot Factory Tomato Toppin": lambda state: state.has("Peppino: Wallclimb", player),
        "Peppibot Factory Sausage Toppin": lambda state: state.has("Peppino: Wallclimb", player),
        "Peppibot Factory Pineapple Toppin": lambda state: state.has("Peppino: Wallclimb", player),

    #Oh Shit!
        "Oh Shit! Complete": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]) and state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "Oh Shit! Mushroom Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),
        "Oh Shit! Cheese Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]) and state.has_any(["Superjump", "Peppino: Wallclimb", "Uppercut"], player),
        "Oh Shit! Tomato Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]) and state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "Oh Shit! Sausage Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]) and state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "Oh Shit! Pineapple Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]) and state.has_any(["Superjump", "Peppino: Wallclimb"], player),

    #Freezerator
        "Freezerator Complete": lambda state: state.has("Peppino: Wallclimb", player) and state.has_any(["Bodyslam", "Peppino: Dive"], player),
        "Freezerator Mushroom Toppin": None,
        "Freezerator Cheese Toppin": lambda state: state.has_any(["Peppino: Wallclimb", "Grab"], player),
        "Freezerator Tomato Toppin": lambda state: state.has("Peppino: Wallclimb", player) and state.has_any(["Bodyslam", "Peppino: Dive"], player),
        "Freezerator Sausage Toppin": lambda state: state.has("Peppino: Wallclimb", player) and state.has_any(["Bodyslam", "Peppino: Dive"], player),
        "Freezerator Pineapple Toppin": lambda state: state.has("Peppino: Wallclimb", player) and state.has_any(["Bodyslam", "Peppino: Dive"], player),

    #Pizzascare
        "Pizzascare Complete": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),
        "Pizzascare Mushroom Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),
        "Pizzascare Cheese Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),
        "Pizzascare Tomato Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),
        "Pizzascare Sausage Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),
        "Pizzascare Pineapple Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),

    #Don't Make a Sound
        "Don't Make a Sound Complete": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Grab", "Uppercut"], player),
        "Don't Make a Sound Mushroom Toppin": None,
        "Don't Make a Sound Cheese Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "Don't Make a Sound Tomato Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),
        "Don't Make a Sound Sausage Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "Don't Make a Sound Pineapple Toppin": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has("Grab", player),

    #WAR
        "WAR Complete": lambda state: state.has_any(["Grab", "Uppercut"], player),
        "WAR Mushroom Toppin": lambda state: state.has_any(["Grab", "Uppercut"], player),
        "WAR Cheese Toppin": lambda state: state.has_any(["Grab", "Uppercut"], player),
        "WAR Tomato Toppin": lambda state: state.has_any(["Grab", "Uppercut"], player),
        "WAR Sausage Toppin": lambda state: state.has_any(["Grab", "Uppercut"], player),
        "WAR Pineapple Toppin": lambda state: state.has_any(["Grab", "Uppercut"], player),

    #Crumbling Tower of Pizza
        "The Crumbling Tower of Pizza Complete": lambda state: (state.has_all(["Grab", "Superjump"], player) or (state.has_any(["Grab", "Uppercut"], player) and state.has("Peppino: Wallclimb", player))) and state.has_any(["Bodyslam", "Peppino: Dive"], player),

    #Bosses
        "Pepperman Defeated": None,
        "The Vigilante Defeated": lambda state: state.has("Grab", player),
        "The Noise Defeated": None,
        "Fake Peppino Defeated": None,
        "Pizzaface Defeated": lambda state: state.has("Grab", player),

    #misc
        "Snotty Murdered": None,
    }

    pt_peppino_tutorial_rules = {
        "Tutorial Complete": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"], player) and (state.has("Superjump", player) or state.has_all(["Uppercut", "Peppino: Wallclimb"], player)) and state.has("Grab", player),
        "Tutorial Complete in under 2 minutes": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"], player) and (state.has("Superjump", player) or state.has_all(["Uppercut", "Peppino: Wallclimb"], player)) and state.has("Grab", player),
        "Tutorial Mushroom Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"], player),
        "Tutorial Cheese Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"], player) and state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "Tutorial Tomato Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"], player) and state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "Tutorial Sausage Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"], player) and (state.has("Superjump", player) or state.has_all(["Uppercut", "Peppino: Wallclimb"], player)),
        "Tutorial Pineapple Toppin": lambda state: state.has_any(["Bodyslam", "Peppino: Dive"], player) and (state.has("Superjump", player) or state.has_all(["Uppercut", "Peppino: Wallclimb"], player)) and state.has("Grab", player),
    }

    pt_peppino_srank_rules = {
        "John Gutter S Rank": peppino_requires_upward_mobility,
        "Pizzascape S Rank": requires_any_grab and peppino_requires_wallclimb,
        "Ancient Cheese S Rank": requires_any_grab and peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Bloodsauce Dungeon S Rank": peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Oregano Desert S Rank": peppino_requires_wallclimb and peppino_requires_downward_mobility,
        "Wasteyard S Rank": peppino_requires_upward_mobility,
        "Fun Farm S Rank": peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Fastfood Saloon S Rank": requires_superjump and peppino_requires_wallclimb and requires_grab,
        "Crust Cove S Rank": requires_taunt and peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)),
        "Gnome Forest S Rank": peppino_requires_upward_mobility and peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,
        "Deep-Dish 9 S Rank": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player) and state.has_any(["Superjump", "Peppino: Wallclimb"]),
        "GOLF S Rank": lambda state: state.has_any(["Superjump", "Bodyslam", "Peppino: Wallclimb", "Uppercut"], player),
        "The Pig City S Rank": lambda state: (state.has_any(["Bodyslam", "Peppino: Dive"], player) and state.has("Gustavo & Brick: Double Jump", player) and state.has_any(["Gustavo: Spin Attack", "Gustavo & Brick: Rat Kick", "Gustavo & Brick: Walljump"], player) and state.has_any(["Superjump", "Peppino: Wallclimb", "Uppercut"], player)),
        "Peppibot Factory S Rank": lambda state: state.has("Peppino: Wallclimb", player) and state.has_any(["Bodyslam", "Grab", "Peppino: Dive"], player),
        "Oh Shit! S Rank": lambda state: state.has_any(["Bodyslam", "Peppino: Dive", "Grab"]) and state.has_any(["Superjump", "Peppino: Wallclimb"], player),
        "Freezerator S Rank": lambda state: state.has("Peppino: Wallclimb", player) and state.has_any(["Bodyslam", "Peppino: Dive"], player),
        "Pizzascare S Rank": lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player) and state.has_any(["Bodyslam", "Peppino: Dive", "Grab"], player),
        "Don't Make a Sound S Rank": lambda state: state.has("Peppino: Wallclimb", player) and state.has_any(["Grab", "Uppercut"], player),
        "WAR S Rank": lambda state: state.has_any(["Grab", "Uppercut"], player) and state.has_any(["Superjump, Peppino: Wallclimb"], player),
        "The Crumbling Tower of Pizza S Rank": lambda state: (state.has_all(["Grab", "Superjump"], player) or (state.has_any(["Grab", "Uppercut"], player) and state.has("Peppino: Wallclimb", player))) and state.has_any(["Bodyslam", "Peppino: Dive"], player),
        "Pepperman S Rank": None,
        "The Vigilante S Rank": lambda state: state.has("Grab", player),
        "The Noise S Rank": None,
        "Fake Peppino S Rank": None,
    }

    pt_peppino_secret_rules = { #secrets are checked when player enters; they do not have to exit
        #John Gutter
        "John Gutter Secret 1": peppino_requires_upward_mobility or requires_uppercut,
        "John Gutter Secret 2": peppino_requires_upward_mobility,
        "John Gutter Secret 3": peppino_requires_upward_mobility,

        #Pizzascape
        "Pizzascape Secret 1": requires_any_grab,
        "Pizzascape Secret 2": requires_any_grab,
        "Pizzascape Secret 3": requires_any_grab and peppino_requires_upward_mobility,
        #Ancient Cheese
        "Ancient Cheese Secret 1": None,
        "Ancient Cheese Secret 2": requires_any_grab and peppino_requires_upward_mobility,
        "Ancient Cheese Secret 3": requires_any_grab and peppino_requires_upward_mobility and peppino_requires_downward_mobility,

        #Bloodsauce Dungeon
        "Bloodsauce Dungeon Secret 1": None,
        "Bloodsauce Dungeon Secret 2": requires_superjump and peppino_requires_downward_mobility,
        "Bloodsauce Dungeon Secret 3": peppino_requires_upward_mobility and peppino_requires_downward_mobility,

        #Oregano Desert
        "Oregano Desert Secret 1": peppino_requires_upward_mobility,
        "Oregano Desert Secret 2": peppino_requires_wallclimb,
        "Oregano Desert Secret 3": peppino_requires_wallclimb,

        #Wasteyard
        "Wasteyard Secret 1": peppino_requires_upward_mobility,
        "Wasteyard Secret 2": peppino_requires_upward_mobility,
        "Wasteyard Secret 3": peppino_requires_upward_mobility,

        #Fun Farm
        "Fun Farm Secret 1": peppino_requires_downward_mobility and peppino_requires_upward_mobility,
        "Fun Farm Secret 2": peppino_requires_downward_mobility and peppino_requires_upward_mobility,
        "Fun Farm Secret 3": peppino_requires_downward_mobility and peppino_requires_upward_mobility,

        "Fastfood Saloon Secret 1": requires_superjump and peppino_requires_wallclimb and requires_grab,
        "Fastfood Saloon Secret 2": requires_superjump and peppino_requires_wallclimb and requires_grab,
        "Fastfood Saloon Secret 3": requires_superjump and peppino_requires_wallclimb and requires_grab,

        "Crust Cove Secret 1": peppino_requires_upward_mobility,
        "Crust Cove Secret 2": peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)),
        "Crust Cove Secret 3": requires_taunt and peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)),

        "Gnome Forest Secret 1": peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,
        "Gnome Forest Secret 2": peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,
        "Gnome Forest Secret 3": peppino_requires_upward_mobility and peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,
    }

    pt_peppino_treasure_rules = {
        "John Gutter Treasure": peppino_requires_upward_mobility,
        "Pizzascape Treasure": requires_any_grab and peppino_requires_upward_mobility,
        "Ancient Cheese Treasure": requires_any_grab and peppino_requires_upward_mobility,
        "Bloodsauce Dungeon Treasure": peppino_requires_downward_mobility and peppino_requires_upward_mobility,
        "Oregano Desert Treasure": peppino_requires_wallclimb,
        "Wasteyard Treasure": peppino_requires_upward_mobility,
        "Fun Farm Treasure": peppino_requires_downward_mobility and peppino_requires_upward_mobility,
        "Crust Cove Treasure": peppino_requires_upward_mobility,
        "Gnome Forest Treasure": peppino_requires_upward_mobility and peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,
    }

    for check in pt_rules:
        multiworld.get_location(check, player).access_rule = pt_rules[check]

    multiworld.completion_condition[player] = lambda state: state.can_reach("The Crumbling Tower of Pizza Complete", "Location", player)