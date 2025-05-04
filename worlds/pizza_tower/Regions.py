from BaseClasses import Region, Location, MultiWorld, Entrance
from AutoWorld import World
from .Locations import PTLocation, pt_locations
from .Options import PTOptions
from Rules import set_rules
import typing

floors_list = [
    "Floor 1 Tower Lobby",
    "Floor 2 Western District",
    "Floor 3 Vacation Resort",
    "Floor 4 Slum",
    "Floor 5 Staff Only"
]

levels_list = [ #ctop handled separately
    "John Gutter",
    "Pizzascape",
    "Ancient Cheese",
    "Bloodsauce Dungeon",
    "Oregano Desert",
    "Wasteyard",
    "Fun Farm",
    "Fastfood Saloon",
    "Crust Cove",
    "Gnome Forest",
    "Deep-Dish 9",
    "GOLF",
    "The Pig City",
    "Peppibot Factory",
    "Oh Shit!",
    "Freezerator",
    "Pizzascare",
    "Don't Make a Sound",
    "WAR"
]

levels_checks = [
    "Mushroom Toppin",
    "Cheese Toppin",
    "Tomato Toppin",
    "Sausage Toppin",
    "Pineapple Toppin",
    "Complete"
]

bosses_list = [ #pizzaface is handled separately because he does not give a rank
    "Pepperman",
    "The Vigilante",
    "The Noise",
    "Fake Peppino"
]

bosses_checks = [
    "Defeated"
]

tutorial_checks = [
    "Mushroom Toppin",
    "Cheese Toppin",
    "Tomato Toppin",
    "Sausage Toppin",
    "Pineapple Toppin",
    "Complete",
    "Complete in under 2 minutes"
]

cheftasks_checks = [
    #John Gutter
    "Chef Task: John Gutted",
    "Chef Task: Primate Rage",
    "Chef Task: Let's Make This Quick",

    #Pizzascape
    "Chef Task: Shining Armor",
    "Chef Task: Spoonknight",
    "Chef Task: Spherical",

    #Ancient Cheese
    "Chef Task: Thrill Seeker",
    "Chef Task: Volleybomb",
    "Chef Task: Delicacy",

    #Bloodsauce Dungeon
    "Chef Task: Eruption Man",
    "Chef Task: Very Very Hot Sauce",
    "Chef Task: Unsliced Pizzaman",

    #Oregano Desert
    "Chef Task: Peppino's Rain Dance",
    "Chef Task: Unnecessary Violence",
    "Chef Task: Alien Cow",

    #Wasteyard
    "Chef Task: Alive and Well",
    "Chef Task: Pretend Ghost",
    "Chef Task: Ghosted",

    #Fun Farm
    "Chef Task: Good Egg",
    "Chef Task: No One Is Safe",
    "Chef Task: Cube Menace",

    #Fastfood Saloon
    "Chef Task: Royal Flush",
    "Chef Task: Non-Alcoholic",
    "Chef Task: Already Pressed",

    #Crust Cove
    "Chef Task: Demolition Expert",
    "Chef Task: Blowback",
    "Chef Task: X",

    #Gnome Forest
    "Chef Task: Bee Nice",
    "Chef Task: Bullseye",
    "Chef Task: Lumberjack",

    #Deep-Dish 9
    "Chef Task: Blast 'Em Asteroids",
    "Chef Task: Turbo Tunnel",
    "Chef Task: Man Meteor",

    #GOLF
    "Chef Task: Primo Golfer",
    "Chef Task: Helpful Burger",
    "Chef Task: Nice Shot",

    #The Pig City
    "Chef Task: Say Oink!",
    "Chef Task: Pan Fried",
    "Chef Task: Strike!",

    #Peppibot Factory
    "Chef Task: There Can Be Only One",
    "Chef Task: Whoop This!",
    "Chef Task: Unflattening",

    #Oh Shit!
    "Chef Task: Food Clan",
    "Chef Task: Can't Fool Me",
    "Chef Task: Penny Pincher",

    #Freezerator
    "Chef Task: Ice Climber",
    "Chef Task: Season's Greetings",
    "Chef Task: Frozen Nuggets",

    #Pizzascare
    "Chef Task: Haunted Playground",
    "Chef Task: Skullsplitter",
    "Chef Task: Cross to Bare",

    #Don't Make a Sound
    "Chef Task: Let Them Sleep",
    "Chef Task: Jumpspared",
    "Chef Task: And This... Is My Gun on a Stick!",

    #WAR
    "Chef Task: Trip to the Warzone",
    "Chef Task: Sharpshooter",
    "Chef Task: Decorated Veteran",

    #Floor Tasks
    "Chef Task: S Ranked #1",
    "Chef Task: P Ranked #1",
    "Chef Task: S Ranked #2",
    "Chef Task: P Ranked #2",
    "Chef Task: S Ranked #3",
    "Chef Task: P Ranked #3",
    "Chef Task: S Ranked #4",
    "Chef Task: P Ranked #4",
    "Chef Task: S Ranked #5",
    "Chef Task: P Ranked #5",

    #Boss Tasks
    "Chef Task: The Critic",
    "Chef Task: The Ugly",
    "Chef Task: Denoise",
    "Chef Task: Faker",
    "Chef Task: Face-Off"
]

def create_regions(player: int, world: MultiWorld, options: PTOptions):
    #defining the rules here cuz doing it in another file is yucky
    def must_unlock(transfo):
        return options.lock_transfo and transfo in options.lock_transfo_list


    #lots of logic checks fall under these categories
    peppino_requires_upward_mobility = lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player)
    peppino_requires_downward_mobility = lambda state: state.has_any(["Bodyslam", "Peppino: Dive"], player)
    gustavo_requires_upward_mobility = lambda state: state.has("Gustavo & Brick: Double Jump", player) and state.has_any(["Gustavo & Brick: Rat Kick", "Gustavo & Brick: Wall Jump", "Gustavo: Spin Attack"], player)
    noise_requires_upward_mobility = lambda state: state.has_any(["Superjump", "Noise: Crusher"], player)
    noise_requires_downward_mobility = lambda state: state.has_any(["Bodyslam", "Noise: Tornado"], player)
    requires_any_grab = lambda state: state.has_any(["Grab", "Uppercut"], player)

    #lambda function aliases for easier reading
    requires_uppercut = lambda state: state.has("Uppercut", player)
    requires_grab = lambda state: state.has("Grab", player)
    requires_superjump = lambda state: state.has("Superjump", player)
    requires_taunt = lambda state: state.has("Taunt", player)
    requires_supertaunt = lambda state: state.has("Supertaunt", player)
    peppino_requires_wallclimb = lambda state: state.has("Peppino: Wallclimb", player)
    peppino_requires_dive = lambda state: state.has("Peppino: Dive", player)
    gustavo_requires_doublejump = lambda state: state.has("Gustavo & Brick: Double Jump", player)
    gustavo_requires_attack = lambda state: state.has_any(["Gustavo & Brick: Rat Kick", "Gustavo: Spin Attack"], player)
    gustavo_requires_kick = lambda state: state.has("Gustavo & Brick: Rat Kick", player)

    requires_ball = lambda state: state.has("Ball", player) or not must_unlock("Ball")
    requires_knight = lambda state: state.has("Knight", player) or not must_unlock("Knight")
    requires_firemouth = lambda state: state.has("Firemouth", player) or not must_unlock("Firemouth")
    requires_ghost = lambda state: state.has("Ghost", player) or not must_unlock("Ghost")
    requires_mort = lambda state: state.has("Mort", player) or not must_unlock("Mort")
    requires_weenie = lambda state: state.has("Weenie", player) or not must_unlock("Weenie")
    requires_barrel = lambda state: state.has("Barrel", player) or not must_unlock("Barrel")
    requires_antigrav = lambda state: state.has("Anti-Grav Bubble", player) or not must_unlock("Anti-Grav Bubble")
    requires_rocket = lambda state: state.has("Rocket", player) or not must_unlock("Rocket")
    requires_pizzabox = lambda state: state.has("Pizzabox", player) or not must_unlock("Pizzabox")
    requires_stickycheese = lambda state: state.has("Sticky Cheese", player) or not must_unlock("Sticky Cheese")
    requires_satans = lambda state: state.has("Satan's Choice", player) or not must_unlock("Satan's Choice")
    requires_shotgun = lambda state: state.has("Shotgun", player) or not must_unlock("Shotgun")
    requires_revolver = lambda state: state.has("Revolver", player) or not must_unlock("Revolver")

    peppino_level_access_rule_by_index = {
        # indices correspond to gate locations in-game
        # comments indicate which levels are usually there in vanilla
        # may be overridden by bonus ladders
        # only counts from floor entrance to level gate; floor access rules are assumed
        0: None, #John Gutter
        1: None, #Pizzascape
        2: peppino_requires_upward_mobility, #Ancient Cheese
        3: peppino_requires_upward_mobility, #Bloodsauce Dungeon
        4: None, #Oregano Desert
        5: None, #Wasteyard
        6: None, #Fun Farm
        7: None, #Fastfood Saloon; can get down but cannot get back up without upward mobility or bonus ladder
        8: None, #Crust Cove
        9: peppino_requires_upward_mobility or requires_uppercut, #Gnome Forest
        10: peppino_requires_upward_mobility or requires_antigrav, #Deep-Dish 9
        11: peppino_requires_upward_mobility, #GOLF
        12: None, #The Pig City
        13: None, #Peppibot Factory; can get down but not up
        14: None, #Oh Shit!; can get down but not up
        15: peppino_requires_upward_mobility, #Freezer
        16: peppino_requires_upward_mobility, #Pizzascare
        17: peppino_requires_upward_mobility, #DMAS
        18: requires_superjump, #WAR
    }

    peppino_boss_access_rule_by_index = {
        0: None, #Pepperman
        1: None, #Vigilante
        2: peppino_requires_upward_mobility or requires_uppercut, #Noise
        3: peppino_requires_upward_mobility #Fake Pep
    }

    pt_peppino_rules = { #access rules within levels, which do not change
    #John Gutter
        "John Gutter Complete": peppino_requires_upward_mobility,
        "John Gutter Mushroom Toppin": peppino_requires_upward_mobility or requires_uppercut or requires_grab or peppino_requires_downward_mobility,
        "John Gutter Cheese Toppin": peppino_requires_upward_mobility or requires_uppercut or requires_grab or peppino_requires_downward_mobility,
        "John Gutter Tomato Toppin": peppino_requires_upward_mobility or requires_uppercut or requires_grab or peppino_requires_downward_mobility,
        "John Gutter Sausage Toppin": peppino_requires_upward_mobility,
        "John Gutter Pineapple Toppin": peppino_requires_upward_mobility,

    #Pizzascape
        "Pizzascape Complete": requires_any_grab and (peppino_requires_wallclimb or (requires_superjump and requires_grab) or requires_uppercut) and requires_knight,
        "Pizzascape Mushroom Toppin": None,
        "Pizzascape Cheese Toppin": None,
        "Pizzascape Tomato Toppin": requires_any_grab and requires_knight,
        "Pizzascape Sausage Toppin": requires_any_grab and requires_knight,
        "Pizzascape Pineapple Toppin": requires_any_grab and requires_knight,

    #Ancient Cheese
        "Ancient Cheese Complete": requires_any_grab and peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Ancient Cheese Mushroom Toppin": None,
        "Ancient Cheese Cheese Toppin": requires_any_grab,
        "Ancient Cheese Tomato Toppin": requires_any_grab and (peppino_requires_upward_mobility or requires_uppercut),
        "Ancient Cheese Sausage Toppin": requires_any_grab and (peppino_requires_upward_mobility or requires_uppercut) and peppino_requires_downward_mobility,
        "Ancient Cheese Pineapple Toppin": requires_any_grab and (peppino_requires_upward_mobility or requires_uppercut) and peppino_requires_downward_mobility,

    #Bloodsauce Dungeon
        "Bloodsauce Dungeon Complete": peppino_requires_downward_mobility and peppino_requires_upward_mobility,
        "Bloodsauce Dungeon Mushroom Toppin": None,
        "Bloodsauce Dungeon Cheese Toppin": None,
        "Bloodsauce Dungeon Tomato Toppin": peppino_requires_downward_mobility,
        "Bloodsauce Dungeon Sausage Toppin": peppino_requires_downward_mobility,
        "Bloodsauce Dungeon Pineapple Toppin": peppino_requires_downward_mobility,

    #Oregano Desert
        "Oregano Desert Complete": (peppino_requires_wallclimb or (requires_superjump and requires_grab) or (requires_uppercut and requires_grab)) and requires_firemouth,
        "Oregano Desert Mushroom Toppin": peppino_requires_upward_mobility or requires_uppercut,
        "Oregano Desert Cheese Toppin": (peppino_requires_upward_mobility or (requires_uppercut and requires_grab)) and requires_firemouth,
        "Oregano Desert Tomato Toppin": (peppino_requires_wallclimb or (requires_superjump and requires_grab) or (requires_uppercut and requires_grab)) and requires_firemouth,
        "Oregano Desert Sausage Toppin": (peppino_requires_wallclimb or (requires_superjump and requires_grab) or (requires_uppercut and requires_grab)) and requires_firemouth,
        "Oregano Desert Pineapple Toppin": (peppino_requires_wallclimb or (requires_superjump and requires_grab) or (requires_uppercut and requires_grab)) and requires_firemouth,

    #Wasteyard
        "Wasteyard Complete": peppino_requires_upward_mobility and requires_ghost,
        "Wasteyard Mushroom Toppin": None,
        "Wasteyard Cheese Toppin": requires_ghost,
        "Wasteyard Tomato Toppin": (peppino_requires_upward_mobility or requires_uppercut) and requires_ghost,
        "Wasteyard Sausage Toppin": (peppino_requires_upward_mobility or requires_uppercut) and requires_ghost,
        "Wasteyard Pineapple Toppin": (peppino_requires_upward_mobility or requires_uppercut) and requires_ghost,

    #Fun Farm
        "Fun Farm Complete": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or (requires_uppercut and requires_grab)) and requires_mort,
        "Fun Farm Mushroom Toppin": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or requires_uppercut) and requires_mort,
        "Fun Farm Cheese Toppin": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or requires_uppercut) and requires_mort,
        "Fun Farm Tomato Toppin": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or (requires_uppercut and requires_grab)) and requires_mort,
        "Fun Farm Sausage Toppin": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or (requires_uppercut and requires_grab)) and requires_mort,
        "Fun Farm Pineapple Toppin": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or (requires_uppercut and requires_grab)) and requires_mort,

    #Fastfood Saloon
        "Fastfood Saloon Complete": ((requires_superjump and peppino_requires_dive) or peppino_requires_wallclimb) and requires_grab and requires_weenie,
        "Fastfood Saloon Mushroom Toppin": peppino_requires_upward_mobility,
        "Fastfood Saloon Cheese Toppin": peppino_requires_upward_mobility and requires_grab and requires_weenie,
        "Fastfood Saloon Tomato Toppin": ((requires_superjump and peppino_requires_dive) or peppino_requires_wallclimb) and requires_grab and requires_weenie,
        "Fastfood Saloon Sausage Toppin": ((requires_superjump and peppino_requires_dive) or peppino_requires_wallclimb) and requires_grab and requires_weenie,
        "Fastfood Saloon Pineapple Toppin": ((requires_superjump and peppino_requires_dive) or peppino_requires_wallclimb) and requires_grab and requires_weenie,

    #Crust Cove
        "Crust Cove Complete": peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)) and requires_barrel,
        "Crust Cove Mushroom Toppin": peppino_requires_upward_mobility,
        "Crust Cove Cheese Toppin": peppino_requires_upward_mobility and requires_barrel,
        "Crust Cove Tomato Toppin": peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)) and requires_barrel,
        "Crust Cove Sausage Toppin": peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)) and requires_barrel,
        "Crust Cove Pineapple Toppin": peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)) and requires_barrel,

    #Gnome Forest
        "Gnome Forest Complete": peppino_requires_upward_mobility and peppino_requires_downward_mobility and gustavo_requires_upward_mobility,
        "Gnome Forest Mushroom Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility,
        "Gnome Forest Cheese Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility,
        "Gnome Forest Tomato Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility,
        "Gnome Forest Sausage Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility,
        "Gnome Forest Pineapple Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility,

    #Deep-Dish 9
        "Deep-Dish 9 Complete": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,
        "Deep-Dish 9 Mushroom Toppin": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or requires_antigrav) and requires_rocket,
        "Deep-Dish 9 Cheese Toppin": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,
        "Deep-Dish 9 Tomato Toppin": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or (requires_antigrav and requires_uppercut)) and requires_rocket,
        "Deep-Dish 9 Sausage Toppin": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,
        "Deep-Dish 9 Pineapple Toppin": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,

    #GOLF
        "GOLF Complete": (peppino_requires_upward_mobility or requires_uppercut or peppino_requires_downward_mobility) and requires_ball,
        "GOLF Mushroom Toppin": None,
        "GOLF Cheese Toppin": requires_ball,
        "GOLF Tomato Toppin": requires_ball,
        "GOLF Sausage Toppin": requires_ball,
        "GOLF Pineapple Toppin": requires_ball,

    #The Pig City
        "The Pig City Complete": peppino_requires_downward_mobility and gustavo_requires_doublejump,
        "The Pig City Mushroom Toppin": None,
        "The Pig City Cheese Toppin": peppino_requires_upward_mobility,
        "The Pig City Tomato Toppin": peppino_requires_downward_mobility,
        "The Pig City Sausage Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility,
        "The Pig City Pineapple Toppin": peppino_requires_downward_mobility and gustavo_requires_doublejump,

    #Peppibot Factory
        "Peppibot Factory Complete": (requires_superjump and requires_uppercut) or (peppino_requires_wallclimb and (requires_grab or requires_uppercut)) and peppino_requires_downward_mobility and requires_pizzabox,
        "Peppibot Factory Mushroom Toppin": requires_superjump or (peppino_requires_wallclimb and (requires_grab or requires_uppercut)),
        "Peppibot Factory Cheese Toppin": (requires_superjump and requires_uppercut) or (peppino_requires_wallclimb and (requires_grab or requires_uppercut)),
        "Peppibot Factory Tomato Toppin": (requires_superjump and requires_uppercut) or (peppino_requires_wallclimb and (requires_grab or requires_uppercut)),
        "Peppibot Factory Sausage Toppin": (requires_superjump and requires_uppercut) or (peppino_requires_wallclimb and (requires_grab or requires_uppercut)) and requires_pizzabox,
        "Peppibot Factory Pineapple Toppin": (requires_superjump and requires_uppercut) or (peppino_requires_wallclimb and (requires_grab or requires_uppercut)) and requires_pizzabox,

    #Oh Shit!
        "Oh Shit! Complete": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,
        "Oh Shit! Mushroom Toppin": requires_stickycheese and peppino_requires_downward_mobility,
        "Oh Shit! Cheese Toppin": requires_stickycheese and peppino_requires_downward_mobility and (peppino_requires_upward_mobility or requires_uppercut),
        "Oh Shit! Tomato Toppin": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,
        "Oh Shit! Sausage Toppin": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,
        "Oh Shit! Pineapple Toppin": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,

    #Freezerator
        "Freezerator Complete": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_satans,
        "Freezerator Mushroom Toppin": None,
        "Freezerator Cheese Toppin": peppino_requires_upward_mobility or requires_uppercut,
        "Freezerator Tomato Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Freezerator Sausage Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Freezerator Pineapple Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility,

    #Pizzascare
        "Pizzascare Complete": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_ball,
        "Pizzascare Mushroom Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Pizzascare Cheese Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Pizzascare Tomato Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_ball,
        "Pizzascare Sausage Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_ball,
        "Pizzascare Pineapple Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_ball,

    #Don't Make a Sound
        "Don't Make a Sound Complete": (peppino_requires_wallclimb or (requires_superjump and peppino_requires_dive)) and requires_any_grab and requires_shotgun,
        "Don't Make a Sound Mushroom Toppin": None,
        "Don't Make a Sound Cheese Toppin": peppino_requires_upward_mobility,
        "Don't Make a Sound Tomato Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Don't Make a Sound Sausage Toppin": peppino_requires_upward_mobility,
        "Don't Make a Sound Pineapple Toppin": (peppino_requires_wallclimb or (requires_superjump and peppino_requires_dive)) and requires_any_grab and requires_shotgun,

    #WAR
        "WAR Complete": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_rocket,
        "WAR Mushroom Toppin": requires_any_grab and requires_shotgun and (peppino_requires_downward_mobility or peppino_requires_upward_mobility),
        "WAR Cheese Toppin": requires_any_grab and requires_shotgun and (peppino_requires_downward_mobility or peppino_requires_upward_mobility) and requires_rocket,
        "WAR Tomato Toppin": requires_any_grab and requires_shotgun and peppino_requires_downward_mobility and requires_rocket,
        "WAR Sausage Toppin": requires_any_grab and requires_shotgun and peppino_requires_downward_mobility and requires_rocket,
        "WAR Pineapple Toppin": requires_any_grab and requires_shotgun and peppino_requires_downward_mobility and requires_rocket,

    #Crumbling Tower of Pizza
        "The Crumbling Tower of Pizza Complete": peppino_requires_upward_mobility and requires_shotgun and requires_grab and peppino_requires_downward_mobility and requires_weenie and requires_rocket,

    #Bosses
        "Pepperman Defeated": None,
        "The Vigilante Defeated": requires_grab and requires_revolver,
        "The Noise Defeated": None,
        "Fake Peppino Defeated": None,
        "Pizzaface Defeated": requires_grab and requires_revolver,

    #misc
        "Snotty Murdered": None,
    }

    pt_peppino_tutorial_rules = {
        "Tutorial Complete": peppino_requires_downward_mobility and (requires_superjump or requires_uppercut) and requires_grab,
        "Tutorial Complete in under 2 minutes": peppino_requires_downward_mobility and (requires_superjump or requires_uppercut) and requires_grab,
        "Tutorial Mushroom Toppin": peppino_requires_downward_mobility,
        "Tutorial Cheese Toppin": peppino_requires_downward_mobility and peppino_requires_upward_mobility,
        "Tutorial Tomato Toppin": peppino_requires_downward_mobility and peppino_requires_upward_mobility,
        "Tutorial Sausage Toppin": peppino_requires_downward_mobility and (requires_superjump or requires_uppercut),
        "Tutorial Pineapple Toppin": peppino_requires_downward_mobility and (requires_superjump or requires_uppercut) and requires_grab,
    }

    pt_peppino_secret_rules = { #secrets are checked when player enters; they do not have to exit
        #John Gutter
        "John Gutter Secret 1": peppino_requires_upward_mobility or requires_uppercut,
        "John Gutter Secret 2": peppino_requires_upward_mobility,
        "John Gutter Secret 3": peppino_requires_upward_mobility,

        #Pizzascape
        "Pizzascape Secret 1": requires_any_grab and requires_knight,
        "Pizzascape Secret 2": requires_any_grab and requires_knight,
        "Pizzascape Secret 3": requires_any_grab and peppino_requires_upward_mobility and requires_knight,

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
        "Oregano Desert Secret 2": peppino_requires_wallclimb and requires_firemouth,
        "Oregano Desert Secret 3": peppino_requires_wallclimb and requires_firemouth,

        #Wasteyard
        "Wasteyard Secret 1": peppino_requires_upward_mobility,
        "Wasteyard Secret 2": peppino_requires_upward_mobility and requires_ghost,
        "Wasteyard Secret 3": peppino_requires_upward_mobility and requires_ghost,

        #Fun Farm
        "Fun Farm Secret 1": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_mort,
        "Fun Farm Secret 2": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_mort,
        "Fun Farm Secret 3": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_mort,

        "Fastfood Saloon Secret 1": requires_superjump and peppino_requires_wallclimb and requires_grab and requires_weenie,
        "Fastfood Saloon Secret 2": requires_superjump and peppino_requires_wallclimb and requires_grab and requires_weenie,
        "Fastfood Saloon Secret 3": requires_superjump and peppino_requires_wallclimb and requires_grab and requires_weenie,

        "Crust Cove Secret 1": peppino_requires_upward_mobility and requires_barrel,
        "Crust Cove Secret 2": peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)) and requires_barrel,
        "Crust Cove Secret 3": requires_taunt and peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)) and requires_barrel,

        "Gnome Forest Secret 1": peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,
        "Gnome Forest Secret 2": peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,
        "Gnome Forest Secret 3": peppino_requires_upward_mobility and peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,

        "Deep-Dish 9 Secret 1": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or requires_antigrav) and requires_rocket,
        "Deep-Dish 9 Secret 2": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_rocket and requires_antigrav,
        "Deep-Dish 9 Secret 3": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,

        "GOLF Secret 1": requires_ball,
        "GOLF Secret 2": (peppino_requires_upward_mobility or requires_uppercut) and requires_ball,
        "GOLF Secret 3": (peppino_requires_upward_mobility or requires_uppercut) and requires_ball,

        "The Pig City Secret 1": None,
        "The Pig City Secret 2": peppino_requires_downward_mobility and gustavo_requires_upward_mobility,
        "The Pig City Secret 3": peppino_requires_downward_mobility and gustavo_requires_doublejump,

        "Peppibot Factory Secret 1": peppino_requires_upward_mobility,
        "Peppibot Factory Secret 2": peppino_requires_wallclimb,
        "Peppibot Factory Secret 3": peppino_requires_wallclimb and peppino_requires_downward_mobility and requires_pizzabox,

        "Oh Shit! Secret 1": requires_stickycheese and peppino_requires_downward_mobility,
        "Oh Shit! Secret 2": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,
        "Oh Shit! Secret 3": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,

        "Freezerator Secret 1": requires_superjump and peppino_requires_downward_mobility,
        "Freezerator Secret 2": requires_superjump and peppino_requires_downward_mobility,
        "Freezerator Secret 3": requires_superjump and peppino_requires_downward_mobility and requires_satans,

        "Pizzascare Secret 1": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_any_grab and requires_ball,
        "Pizzascare Secret 2": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_any_grab and requires_ball,
        "Pizzascare Secret 3": requires_superjump and peppino_requires_downward_mobility and requires_any_grab and requires_ball,

        "Don't Make a Sound Secret 1": None,
        "Don't Make a Sound Secret 2": peppino_requires_wallclimb,
        "Don't Make a Sound Secret 3": peppino_requires_wallclimb,

        "WAR Secret 1": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility,
        "WAR Secret 2": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility,
        "WAR Secret 3": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility,
    }

    pt_peppino_treasure_rules = {
        "John Gutter Treasure": peppino_requires_upward_mobility,
        "Pizzascape Treasure": requires_any_grab and peppino_requires_upward_mobility and requires_knight,
        "Ancient Cheese Treasure": requires_any_grab and peppino_requires_upward_mobility,
        "Bloodsauce Dungeon Treasure": peppino_requires_downward_mobility and peppino_requires_upward_mobility,
        "Oregano Desert Treasure": peppino_requires_wallclimb and requires_firemouth,
        "Wasteyard Treasure": peppino_requires_upward_mobility and requires_ghost,
        "Fun Farm Treasure": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_mort,
        "Crust Cove Treasure": peppino_requires_upward_mobility and requires_barrel,
        "Gnome Forest Treasure": peppino_requires_upward_mobility and peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,
        "Deep-Dish 9 Treasure": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,
        "GOLF Treasure": (peppino_requires_upward_mobility or requires_uppercut) and requires_ball,
        "The Pig City Treasure": peppino_requires_downward_mobility and gustavo_requires_doublejump,
        "Peppibot Factory Treasure": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_pizzabox,
        "Oh Shit! Treasure": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,
        "Freezerator Treasure": requires_superjump and peppino_requires_downward_mobility and requires_satans,
        "Pizzascare Treasure": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_any_grab and requires_ball,
        "Don't Make a Sound Treasure": peppino_requires_wallclimb and requires_any_grab and requires_shotgun,
        "WAR Treasure": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_rocket
    }
    
    pt_peppino_extra_rules = {
        #these rules make sure the player can collect things not already
        #covered by checks, like lap 2 and completing secrets
        #these will then be anded with rules for reaching secrets, treasure,
        #toppins, and level completion, even though not all are strictly required
        #these will be recycled for p rank rules
        "John Gutter Extra": peppino_requires_wallclimb, #secret 2 requires wallclimb only
        "Pizzascape Extra": requires_ball, #secret 3 requires ball
        "Ancient Cheese Extra": None,
        "Bloodsauce Dungeon Extra": peppino_requires_wallclimb, #secret 2 requires wallclimb; lava boost gets you high enough but does not break blocks
        "Oregano Desert Extra": requires_superjump, #secret 3 requires superjump
        "Wasteyard Extra": peppino_requires_wallclimb or requires_uppercut, #secret 3 requires wallclimb or highjump
        "Fun Farm Extra": peppino_requires_upward_mobility, #secret 3 requires superjump or wallclimb
        "Fastfood Saloon Extra": peppino_requires_wallclimb, #secret 2 requires wallclimb
        "Crust Cove Extra": requires_taunt, #secret 3 requires taunt (parry)
        "Gnome Forest Extra": None,
        "Deep-Dish 9 Extra": requires_antigrav, #secret 1 requires antigrav bubble
        "GOLF Extra": None, #seriously considering forcing golf to always be at the start
        "The Pig City Extra": (requires_uppercut or peppino_requires_upward_mobility), #secret 1 requires a little bit of height
        "Peppibot Factory Extra": requires_any_grab, #secret 2 has a bomb to grab
        "Oh Shit! Extra": None,
        "Freezerator Extra": None, #lap 2 removes satan's choice but to no effect on the access rules
        "Pizzascare Extra": peppino_requires_wallclimb, #secret 2 and maybe secret 1 require wallclimb
        "Don't Make a Sound Extra": peppino_requires_wallclimb, #secret 2 requires wallclimb
        "WAR Extra": peppino_requires_upward_mobility, #lap 2 removes shotgun so double shot cheese is no longer possible
        "The Crumbling Tower of Pizza Extra": None, #no special stuff
        "Pepperman Extra": None,
        "The Vigilante Extra": None,
        "The Noise Extra": None,
        "Fake Peppino Extra": None,
    }

    pt_cheftasks = {
        #John Gutter
        "Chef Task: John Gutted": peppino_requires_upward_mobility,
        "Chef Task: Primate Rage": peppino_requires_upward_mobility,
        "Chef Task: Let's Make This Quick": peppino_requires_upward_mobility,

        #Pizzascape
        "Chef Task: Shining Armor": requires_any_grab and requires_knight,
        "Chef Task: Spoonknight": requires_taunt,
        "Chef Task: Spherical": requires_any_grab and requires_knight,

        #Ancient Cheese
        "Chef Task: Thrill Seeker": pt_peppino_rules["Ancient Cheese Complete"],
        "Chef Task: Volleybomb": None,
        "Chef Task: Delicacy": None,

        #Bloodsauce Dungeon
        "Chef Task: Eruption Man": peppino_requires_downward_mobility and requires_superjump,
        "Chef Task: Very Very Hot Sauce": pt_peppino_rules["Bloodsauce Dungeon Complete"],
        "Chef Task: Unsliced Pizzaman": pt_peppino_rules["Bloodsauce Dungeon Complete"],

        #Oregano Desert
        "Chef Task: Peppino's Rain Dance": peppino_requires_upward_mobility or requires_uppercut,
        "Chef Task: Unnecessary Violence": peppino_requires_wallclimb and requires_firemouth,
        "Chef Task: Alien Cow": pt_peppino_rules["Oregano Desert Complete"],

        #Wasteyard
        "Chef Task: Alive and Well": peppino_requires_upward_mobility and requires_ghost,
        "Chef Task: Pretend Ghost": peppino_requires_upward_mobility and requires_ghost,
        "Chef Task: Ghosted": peppino_requires_upward_mobility and requires_ghost,

        #Fun Farm
        "Chef Task: Good Egg": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_mort,
        "Chef Task: No One Is Safe": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_mort and requires_supertaunt,
        "Chef Task: Cube Menace": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or requires_uppercut) and requires_mort,

        #Fastfood Saloon
        "Chef Task: Royal Flush": requires_superjump and requires_grab and peppino_requires_wallclimb and requires_weenie,
        "Chef Task: Non-Alcoholic": requires_superjump and requires_grab and peppino_requires_wallclimb and requires_weenie,
        "Chef Task: Already Pressed": requires_superjump and requires_grab and peppino_requires_wallclimb and requires_weenie,

        #Crust Cove
        "Chef Task: Demolition Expert": peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)) and requires_barrel,
        "Chef Task: Blowback": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_taunt,
        "Chef Task: X": peppino_requires_upward_mobility and peppino_requires_downward_mobility,

        #Gnome Forest
        "Chef Task: Bee Nice": requires_taunt,
        "Chef Task: Bullseye": requires_taunt,
        "Chef Task: Lumberjack": peppino_requires_upward_mobility and peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,

        #Deep-Dish 9
        "Chef Task: Blast 'Em Asteroids": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,
        "Chef Task: Turbo Tunnel": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket and requires_antigrav,
        "Chef Task: Man Meteor": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,

        #GOLF
        "Chef Task: Primo Golfer": (peppino_requires_upward_mobility or requires_uppercut) and requires_ball,
        "Chef Task: Helpful Burger": (peppino_requires_upward_mobility or requires_uppercut) and requires_ball,
        "Chef Task: Nice Shot": (peppino_requires_upward_mobility or requires_uppercut) and requires_ball,

        #The Pig City
        "Chef Task: Say Oink!": peppino_requires_downward_mobility and gustavo_requires_doublejump and requires_taunt,
        "Chef Task: Pan Fried": peppino_requires_downward_mobility and requires_superjump,
        "Chef Task: Strike!": peppino_requires_downward_mobility and gustavo_requires_doublejump and gustavo_requires_kick,

        #Peppibot Factory
        "Chef Task: There Can Be Only One": peppino_requires_wallclimb and peppino_requires_downward_mobility and requires_pizzabox,
        "Chef Task: Whoop This!": peppino_requires_upward_mobility,
        "Chef Task: Unflattening": peppino_requires_wallclimb and requires_pizzabox,

        #Oh Shit!
        "Chef Task: Food Clan": requires_stickycheese and peppino_requires_downward_mobility and (peppino_requires_upward_mobility or requires_uppercut),
        "Chef Task: Can't Fool Me": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,
        "Chef Task: Penny Pincher": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,

        #Freezerator
        "Chef Task: Ice Climber": requires_superjump and peppino_requires_downward_mobility and requires_satans,
        "Chef Task: Season's Greetings": requires_superjump and peppino_requires_downward_mobility and requires_satans and requires_grab,
        "Chef Task: Frozen Nuggets": requires_superjump and peppino_requires_downward_mobility and requires_satans,

        #Pizzascare
        "Chef Task: Haunted Playground": pt_peppino_rules["Pizzascare Complete"],
        "Chef Task: Skullsplitter": pt_peppino_rules["Pizzascare Complete"],
        "Chef Task: Cross to Bare": pt_peppino_rules["Pizzascare Secret 3"],

        #Don't Make a Sound
        "Chef Task: Let Them Sleep": peppino_requires_wallclimb and requires_any_grab and requires_shotgun,
        "Chef Task: Jumpspared": peppino_requires_wallclimb and requires_any_grab and requires_shotgun,
        "Chef Task: And This... Is My Gun on a Stick!": peppino_requires_wallclimb and requires_any_grab and requires_shotgun,

        #WAR
        "Chef Task: Trip to the Warzone": pt_peppino_rules["WAR Complete"],
        "Chef Task: Sharpshooter": pt_peppino_rules["WAR Complete"],
        "Chef Task: Decorated Veteran": pt_peppino_rules["WAR Complete"],

        #Floor Tasks will be generated later

        #Boss Tasks
        "Chef Task: The Critic": pt_peppino_rules["Pepperman Defeated"],
        "Chef Task: The Ugly": pt_peppino_rules["The Vigilante Defeated"],
        "Chef Task: Denoise": pt_peppino_rules["The Noise Defeated"],
        "Chef Task: Faker": pt_peppino_rules["Fake Peppino Defeated"],
        "Chef Task: Face-Off": pt_peppino_rules["Pizzaface Defeated"]
    }

    def get_s_rank(level_name): #huge fuckoff return statement for calculating s and p rank rules
        return pt_peppino_rules[level_name + " Complete"] and pt_peppino_rules[level_name + " Mushroom Toppin"] and pt_peppino_rules[level_name + " Cheese Toppin"] and pt_peppino_rules[level_name + " Tomato Toppin"] and pt_peppino_rules[level_name + " Sausage Toppin"] and pt_peppino_rules[level_name + " Pineapple Toppin"] and pt_peppino_secret_rules[level_name + " Secret 1"] and pt_peppino_secret_rules[level_name + " Secret 2"] and pt_peppino_secret_rules[level_name + " Secret 3"] and pt_peppino_treasure_rules[level_name + " Treasure"] and pt_peppino_extra_rules[level_name + " Extra"]
    
    pt_peppino_srank_rules = {
        "John Gutter S Rank": get_s_rank("John Gutter"),
        "Pizzascape S Rank": get_s_rank("Pizzascape"),
        "Ancient Cheese S Rank": get_s_rank("Ancient Cheese"),
        "Bloodsauce Dungeon S Rank": get_s_rank("Bloodsauce Dungeon"),
        "Oregano Desert S Rank": get_s_rank("Oregano Desert"),
        "Wasteyard S Rank": get_s_rank("Wasteyard"),
        "Fun Farm S Rank": get_s_rank("Fun Farm"),
        "Fastfood Saloon S Rank": get_s_rank("Fastfood Saloon"),
        "Crust Cove S Rank": get_s_rank("Crust Cove"),
        "Gnome Forest S Rank": get_s_rank("Gnome Forest"),
        "Deep-Dish 9 S Rank": get_s_rank("Deep-Dish 9"),
        "GOLF S Rank": get_s_rank("GOLF"),
        "The Pig City S Rank": get_s_rank("The Pig City"),
        "Peppibot Factory S Rank": get_s_rank("Peppibot Factory"),
        "Oh Shit! S Rank": get_s_rank("Oh Shit!"),
        "Freezerator S Rank": get_s_rank("Freezerator"),
        "Pizzascare S Rank": get_s_rank("Pizzascare"),
        "Don't Make a Sound S Rank": get_s_rank("Don't Make a Sound"),
        "WAR S Rank": get_s_rank("WAR"),
        "Pepperman S Rank": None,
        "The Vigilante S Rank": pt_peppino_rules["The Vigilante Defeated"],
        "The Noise S Rank": None,
        "Fake Peppino S Rank": None,
        "The Crumbling Tower of Pizza S Rank": pt_peppino_rules["The Crumbling Tower of Pizza Complete"],
    }

    pt_peppino_prank_rules = {
        "John Gutter P Rank": pt_peppino_srank_rules["John Gutter S Rank"],
        "Pizzascape P Rank": pt_peppino_srank_rules["Pizzascape S Rank"],
        "Ancient Cheese P Rank": pt_peppino_srank_rules["Ancient Cheese S Rank"],
        "Bloodsauce Dungeon P Rank": pt_peppino_srank_rules["Bloodsauce Dungeon S Rank"],
        "Oregano Desert P Rank": pt_peppino_srank_rules["Oregano Desert S Rank"],
        "Wasteyard P Rank": pt_peppino_srank_rules["Wasteyard S Rank"],
        "Fun Farm P Rank": pt_peppino_srank_rules["Fun Farm S Rank"],
        "Fastfood Saloon P Rank": pt_peppino_srank_rules["Fastfood Saloon S Rank"],
        "Crust Cove P Rank": pt_peppino_srank_rules["Crust Cove S Rank"],
        "Gnome Forest P Rank": pt_peppino_srank_rules["Gnome Forest S Rank"],
        "Deep-Dish 9 P Rank": pt_peppino_srank_rules["Deep-Dish 9 S Rank"],
        "GOLF P Rank": pt_peppino_srank_rules["GOLF S Rank"],
        "The Pig City P Rank": pt_peppino_srank_rules["The Pig City S Rank"],
        "Peppibot Factory P Rank": pt_peppino_srank_rules["Peppibot Factory S Rank"],
        "Oh Shit! P Rank": pt_peppino_srank_rules["Oh Shit! S Rank"],
        "Freezerator P Rank": pt_peppino_srank_rules["Freezerator S Rank"],
        "Pizzascare P Rank": pt_peppino_srank_rules["Pizzascare S Rank"],
        "Don't Make a Sound P Rank": pt_peppino_srank_rules["Don't Make a Sound S Rank"],
        "WAR P Rank": pt_peppino_srank_rules["WAR S Rank"],
        "Pepperman P Rank": None,
        "The Vigilante P Rank": pt_peppino_srank_rules["The Vigilante S Rank"],
        "The Noise P Rank": None,
        "Fake Peppino P Rank": None,
        "The Crumbling Tower of Pizza P Rank": pt_peppino_srank_rules["The Crumbling Tower of Pizza S Rank"],
    }

    check_type_to_dict = {
        "Complete": pt_peppino_rules,
        "Mushroom Toppin": pt_peppino_rules,
        "Cheese Toppin": pt_peppino_rules,
        "Tomato Toppin": pt_peppino_rules,
        "Sausage Toppin": pt_peppino_rules,
        "Pineapple Toppin": pt_peppino_rules,
        "Treasure": pt_peppino_treasure_rules,
        "Secret 1": pt_peppino_secret_rules,
        "Secret 2": pt_peppino_secret_rules,
        "Secret 3": pt_peppino_secret_rules,
        "S Rank": pt_peppino_srank_rules,
        "P Rank": pt_peppino_prank_rules
    }
    

    tower_regions: list[Region] = []

    tower_regions.append(Region("Menu", player, world, None))

    #extra mf checks!!!!!
    if options.secret_checks:
        levels_checks += ["Secret 1", "Secret 2", "Secret 3"]
    if options.treasure_checks:
        levels_checks.append("Treasure")
    if options.srank_checks:
        levels_checks.append("S Rank")
        bosses_checks.append("S Rank")
    if options.prank_checks:
        levels_checks.append("P Rank")
        bosses_checks.append("P Rank")

    #create regions and add locations
    for flr in floors_list:
        tower_regions.append(Region(flr, player, world))

    region_tut = Region("Tutorial", player, world)
    for chk in tutorial_checks:
        check_name = "Tutorial " + chk
        new_location = PTLocation(player, check_name, pt_locations[check_name], region_tut)
        new_location.access_rule = pt_peppino_tutorial_rules[check_name]
        region_tut.locations.append(new_location)
    tower_regions.append(region_tut)

    for lvl in levels_list:
        check_region = Region(lvl, player, world, None)
        for chk in levels_checks:
            check_name = lvl + " " + chk
            new_location = PTLocation(player, check_name, pt_locations[check_name], check_region)
            new_location.access_rule = check_type_to_dict[chk][check_name]
            check_region.locations.append(new_location)

        tower_regions.append(check_region)

    for boss in bosses_list:
        check_region = Region(boss, player, world, None)
        for chk in bosses_checks:
            check_name = lvl + " " + chk
            new_location = PTLocation(player, check_name, pt_locations[check_name], check_region)
            new_location.access_rule = check_type_to_dict[chk][check_name]
            check_region.locations.append(new_location)
        tower_regions.append(check_region)

    #odd regions
    region_pface = Region("Pizzaface", player, world)
    region_ctop = Region("The Crumbling Tower of Pizza", player, world)

    #odd locations
    region_pface.locations.append(PTLocation(player, "Pizzaface Defeated", 243, region_pface))
    world.get_location("Pizzaface Defeated", player).access_rule = pt_peppino_rules["Pizzaface Defeated"]

    region_ctop.locations.append(PTLocation(player, "The Crumbling Tower of Pizza Complete", 233, region_ctop))
    world.get_location("The Crumbling Tower of Pizza Complete", player).access_rule = pt_peppino_rules["The Crumbling Tower of Pizza Complete"]
    if options.srank_checks:
        region_ctop.locations.append(PTLocation(player, "The Crumbling Tower of Pizza S Rank", 234, region_ctop))
        world.get_location("The Crumbling Tower of Pizza S Rank", player).access_rule = pt_peppino_rules["The Crumbling Tower of Pizza S Rank"]
    if options.prank_checks:
        region_ctop.locations.append(PTLocation(player, "The Crumbling Tower of Pizza P Rank", 234, region_ctop))
        world.get_location("The Crumbling Tower of Pizza P Rank", player).access_rule = pt_peppino_rules["The Crumbling Tower of Pizza S Rank"]
    tower_regions[4].locations.append(PTLocation(player, "Snotty Murdered", 244, tower_regions[4]))
    world.get_location("Snotty Murdered", player).access_rule = None

    #must handle chef tasks separately since they aren't common to all levels
    #weird naming here. cheftask_checks is the option bool, cheftasks_checks is the list of task names
    if options.cheftask_checks:
        for i in range(19):
            region_curr = world.get_region(levels_list[i], player)
            for ii in range(3):
                task_index = (i * 3) + ii
                task_name = cheftasks_checks[task_index]
                region_curr.locations.append(PTLocation(player, task_name, pt_locations[task_name], region_curr))
        for i in range(4):
            task_name = cheftasks_checks[i + 67]
            world.get_region(bosses_list[i], player).locations.append(PTLocation(player, task_name, pt_locations[task_name], world.get_region(bosses_list[i], player)))
        region_pface.locations.append(PTLocation(player, "Chef Task: Face-Off", 405, region_pface))
        for i in range(5):
            curr_floor = world.get_region(floors_list[i], player)
            curr_floor.locations.append(PTLocation(player, "Chef Task: S Ranked #" + (i + 1), pt_locations["Chef Task: S Ranked #" + (i + 1)], curr_floor))
            curr_floor.locations.append(PTLocation(player, "Chef Task: P Ranked #" + (i + 1), pt_locations["Chef Task: P Ranked #" + (i + 1)], curr_floor))

    tower_regions.append(region_pface)
    tower_regions.append(region_ctop)

    world.regions += tower_regions
    
    randomized_list = level_gate_rando(world)
    if options.randomize_levels:
        level_queue = randomized_list[0]
    else:
        level_queue = levels_list
    if options.randomize_bosses:
        boss_queue = randomized_list[1]
    else:
        boss_queue = bosses_list

    world.get_region("Menu", player).connect(world.get_region("Floor 1 Tower Lobby", player), "Menu to Floor 1 Tower Lobby")
    world.get_region("Floor 1 Tower Lobby", player).connect(world.get_region("Tutorial", player), "Floor 1 Tower Lobby to Tutorial")
    for i in range(4):
        curr_floor_name = floors_list[i]
        curr_floor = world.get_region(curr_floor_name, player)
        if options.cheftask_checks:
            world.get_location("Chef Task: S Ranked #" + (i + 1), player).access_rule = pt_peppino_srank_rules[level_queue[0]] and pt_peppino_srank_rules[level_queue[1]] and pt_peppino_srank_rules[level_queue[2]] and pt_peppino_srank_rules[level_queue[3]]
            world.get_location("Chef Task: P Ranked #" + (i + 1), player).access_rule = pt_peppino_srank_rules[level_queue[0]] and pt_peppino_srank_rules[level_queue[1]] and pt_peppino_srank_rules[level_queue[2]] and pt_peppino_srank_rules[level_queue[3]]
        for i in range(4):
            curr_level_name = level_queue.pop(0)
            curr_level = world.get_region(curr_level_name, player)
            curr_floor.connect(curr_level, curr_floor_name + " to " + curr_level_name)
    if options.cheftask_checks:
        world.get_location("Chef Task: S Ranked #5", player).access_rule = pt_peppino_srank_rules[level_queue[0]] and pt_peppino_srank_rules[level_queue[1]] and pt_peppino_srank_rules[level_queue[2]]
        world.get_location("Chef Task: P Ranked #5", player).access_rule = pt_peppino_srank_rules[level_queue[0]] and pt_peppino_srank_rules[level_queue[1]] and pt_peppino_srank_rules[level_queue[2]]
    for i in range(3):
        curr_level_name = level_queue.pop(0)
        curr_level = world.get_region(curr_level_name, player)
        world.get_region("Floor 5 Staff Only", player).connect(curr_level, "Floor 5 Staff Only to " + curr_level_name)
    for i in range(4):
        curr_floor_name = floors_list[i]
        curr_boss_name = boss_queue.pop(0)
        world.get_region(curr_floor_name, player).connect(world.get_region(curr_boss_name, player), curr_floor_name + " to " + curr_boss_name)
    #connect floors to each other
    for i in range(4):
        curr_floor_name = floors_list[i]
        next_floor_name = floors_list[i+1]
        world.get_region(curr_floor_name, player).connect(world.get_region(next_floor_name, player), curr_floor_name + " to " + next_floor_name)
    world.get_region("Floor 5 Staff Only", player).connect(world.get_region("Pizzaface", player), "Floor 5 Staff Only to Pizzaface")
    world.get_region("Pizzaface", player).connect(world.get_region("The Crumbling Tower of Pizza", player), "Pizzaface to The Crumbling Tower of Pizza")


def level_gate_rando(world: World):
    #replace john gutter and pizzascape with any of these levels
    ok_start_levels = [ 
        "Pizzascape",
        "Ancient Cheese",
        "Bloodsauce Dungeon",
        "Wasteyard",
        "GOLF",
        "The Pig City",
        "Don't Make a Sound"
    ]

    #copies of level and boss lists to be shuffled
    level_queue = [
        "John Gutter",
        "Pizzascape",
        "Ancient Cheese",
        "Bloodsauce Dungeon",
        "Oregano Desert",
        "Wasteyard",
        "Fun Farm",
        "Fastfood Saloon",
        "Crust Cove",
        "Gnome Forest",
        "Deep-Dish 9",
        "GOLF",
        "The Pig City",
        "Peppibot Factory",
        "Oh Shit!",
        "Freezerator",
        "Pizzascare",
        "Don't Make a Sound",
        "WAR"
    ]

    boss_queue = bosses_list

    rando_level_order = []

    #place two levels from ok_start_levels at the beginning of the rando level order
    for i in range(2):
        rando_level = ok_start_levels[world.random.randrange(len(ok_start_levels) - 1)]
        rando_level_order.append(rando_level)
        ok_start_levels.remove(rando_level)
        level_queue.remove(rando_level)
    
    #don't care where the leftover levels go
    world.random.shuffle(level_queue)
    rando_level_order += level_queue
    world.random.shuffle(boss_queue)
    while (boss_queue[0] == "The Vigilante"): #first boss should not be the vigilante
        world.random.shuffle(boss_queue)

    return rando_level_order, boss_queue