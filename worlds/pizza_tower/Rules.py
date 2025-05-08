from worlds.AutoWorld import World
from BaseClasses import MultiWorld
from .Options import PTOptions
from ..generic.Rules import add_rule
from math import floor

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

bosses_list = [ #pizzaface is handled separately because he does not give a rank
    "Pepperman",
    "The Vigilante",
    "The Noise",
    "Fake Peppino"
]

floors_list = [
    "Floor 1 Tower Lobby",
    "Floor 2 Western District",
    "Floor 3 Vacation Resort",
    "Floor 4 Slum",
    "Floor 5 Staff Only"
]


def level_gate_rando(world: World, is_noise: bool) -> list[str]:
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
    if is_noise:
        ok_start_levels.append("Freezerator")

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

    return rando_level_order

def boss_gate_rando(world: World, is_noise: bool) -> list[str]:
    boss_queue = [
        "Pepperman",
        "The Vigilante",
        "The Noise",
        "Fake Peppino"
    ]
    if world.options.character != 0:
        boss_queue[2] = "The Doise"
    world.random.shuffle(boss_queue)
    while boss_queue[0] == "The Vigilante": #floor 1 boss should not be vigi
        world.random.shuffle(boss_queue)
    return boss_queue

def get_secrets_list() -> list[str]:
    secrets_list = []
    for lvl in levels_list:
        for i in range(3):
            secrets_list.append(lvl + " Secret " + str(i+1))
    return secrets_list

def secret_rando(world: World) -> list[str]:
    secrets_queue = get_secrets_list()
    world.random.shuffle(secrets_queue)
    return secrets_queue

def set_rules(multiworld: MultiWorld, world: World, options: PTOptions, toppins: int):
    def must_unlock(transfo):
        return options.lock_transfo and transfo in options.lock_transfo_list


    #lots of logic checks fall under these categories
    peppino_requires_upward_mobility = lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], world.player)
    peppino_requires_downward_mobility = lambda state: state.has("Bodyslam", world.player)
    gustavo_requires_upward_mobility = lambda state: state.has("Gustavo & Brick: Double Jump", world.player) and state.has_any(["Gustavo & Brick: Rat Kick", "Gustavo & Brick: Wall Jump", "Gustavo: Spin Attack"], world.player)
    noise_requires_big_upward_mobility = lambda state: state.has_any(["Superjump", "Noise: Crusher"], world.player)
    noise_requires_upward_mobility = lambda state: state.has_any(["Superjump", "Noise: Crusher", "Uppercut", "Noise: Wallbounce"], world.player)
    noise_requires_downward_mobility = lambda state: state.has_any(["Bodyslam", "Noise: Tornado", "Noise: Crusher"], world.player)
    noise_requires_bomb = lambda state: state.has("Noise: Bomb", world.player)
    requires_any_grab = lambda state: state.has_any(["Grab", "Uppercut"], world.player)

    #lambda function aliases for easier reading
    requires_uppercut = lambda state: state.has("Uppercut", world.player)
    requires_grab = lambda state: state.has("Grab", world.player)
    requires_superjump = lambda state: state.has("Superjump", world.player)
    requires_taunt = lambda state: state.has("Taunt", world.player)
    requires_supertaunt = lambda state: state.has("Supertaunt", world.player)
    requires_bodyslam = lambda state: state.has("Bodyslam", world.player)
    peppino_requires_wallclimb = lambda state: state.has("Peppino: Wallclimb", world.player)
    peppino_requires_dive = lambda state: state.has("Peppino: Dive", world.player)
    gustavo_requires_doublejump = lambda state: state.has("Gustavo & Brick: Double Jump", world.player)
    gustavo_requires_attack = lambda state: state.has_any(["Gustavo & Brick: Rat Kick", "Gustavo: Spin Attack"], world.player)
    gustavo_requires_kick = lambda state: state.has("Gustavo & Brick: Rat Kick", world.player)
    noise_requires_crusher = lambda state: state.has("Noise: Crusher", world.player)
    noise_requires_wallbounce = lambda state: state.has("Noise: Wallbounce", world.player)
    noise_requires_tornado = lambda state: state.has("Noise: Tornado", world.player)

    requires_ball = lambda state: state.has("Ball", world.player) or not must_unlock("Ball")
    requires_knight = lambda state: state.has("Knight", world.player) or not must_unlock("Knight")
    requires_firemouth = lambda state: state.has("Firemouth", world.player) or not must_unlock("Firemouth")
    requires_ghost = lambda state: state.has("Ghost", world.player) or not must_unlock("Ghost")
    requires_mort = lambda state: state.has("Mort", world.player) or not must_unlock("Mort")
    requires_weenie = lambda state: state.has("Weenie", world.player) or not must_unlock("Weenie")
    requires_barrel = lambda state: state.has("Barrel", world.player) or not must_unlock("Barrel")
    requires_antigrav = lambda state: state.has("Anti-Grav Bubble", world.player) or not must_unlock("Anti-Grav Bubble")
    requires_rocket = lambda state: state.has("Rocket", world.player) or not must_unlock("Rocket")
    requires_pizzabox = lambda state: state.has("Pizzabox", world.player) or not must_unlock("Pizzabox")
    requires_stickycheese = lambda state: state.has("Sticky Cheese", world.player) or not must_unlock("Sticky Cheese")
    requires_satans = lambda state: state.has("Satan's Choice", world.player) or not must_unlock("Satan's Choice")
    requires_shotgun = lambda state: state.has("Shotgun", world.player) or not must_unlock("Shotgun")
    requires_revolver = lambda state: state.has("Revolver", world.player) or not must_unlock("Revolver")

    requires_none = lambda state: True

    peppino_level_access_rules = {
        # indices correspond to gate locations in-game
        # comments indicate which levels are usually there in vanilla
        # may be overridden by bonus ladders
        # only counts from floor entrance to level gate; floor access rules are assumed
        "John Gutter": requires_none,
        "Pizzascape": requires_none,
        "Ancient Cheese": peppino_requires_upward_mobility,
        "Bloodsauce Dungeon": peppino_requires_upward_mobility,
        "Oregano Desert": requires_none,
        "Wasteyard": requires_none,
        "Fun Farm": requires_none,
        "Fastfood Saloon": requires_none,
        "Crust Cove": requires_none, #Crust Cove
        "Gnome Forest": peppino_requires_upward_mobility or requires_uppercut, 
        "Deep-Dish 9": peppino_requires_upward_mobility or requires_antigrav,
        "GOLF": peppino_requires_upward_mobility, 
        "The Pig City": requires_none, 
        "Peppibot Factory": requires_none, 
        "Oh Shit!": requires_none, 
        "Freezerator": peppino_requires_upward_mobility,
        "Pizzascare": peppino_requires_upward_mobility,
        "Don't Make a Sound": peppino_requires_upward_mobility, 
        "WAR": requires_superjump,
    }

    peppino_boss_access_rules = {
        "Pepperman": requires_none,
        "The Vigilante": requires_none,
        "The Noise": peppino_requires_upward_mobility or requires_uppercut,
        "The Doise": peppino_requires_upward_mobility or requires_uppercut,
        "Fake Peppino": peppino_requires_upward_mobility
    }

    peppino_next_floor_access_rules = [
        peppino_requires_upward_mobility,
        requires_none,
        peppino_requires_upward_mobility or requires_uppercut,
        requires_none
    ]

    pt_peppino_rules = { #access rules within levels, which do not change
    #John Gutter
        "John Gutter Complete": peppino_requires_upward_mobility,
        "John Gutter Mushroom Toppin": peppino_requires_upward_mobility or requires_uppercut or requires_grab or peppino_requires_downward_mobility,
        "John Gutter Cheese Toppin": peppino_requires_upward_mobility or requires_uppercut or requires_grab or peppino_requires_downward_mobility,
        "John Gutter Tomato Toppin": peppino_requires_upward_mobility or requires_uppercut or requires_grab or peppino_requires_downward_mobility,
        "John Gutter Sausage Toppin": peppino_requires_upward_mobility,
        "John Gutter Pineapple Toppin": peppino_requires_upward_mobility,
        "John Gutter Secret 1": peppino_requires_upward_mobility or requires_uppercut or requires_grab or peppino_requires_downward_mobility,
        "John Gutter Secret 2": peppino_requires_upward_mobility,
        "John Gutter Secret 3": peppino_requires_upward_mobility,
        "John Gutter Treasure": peppino_requires_upward_mobility,
        "Chef Task: John Gutted": peppino_requires_upward_mobility,
        "Chef Task: Primate Rage": peppino_requires_upward_mobility,
        "Chef Task: Let's Make This Quick": peppino_requires_upward_mobility,

    #Pizzascape
        "Pizzascape Complete": requires_any_grab and (peppino_requires_wallclimb or (requires_superjump and requires_grab) or requires_uppercut) and requires_knight,
        "Pizzascape Mushroom Toppin": requires_none,
        "Pizzascape Cheese Toppin": requires_none,
        "Pizzascape Tomato Toppin": requires_any_grab and requires_knight,
        "Pizzascape Sausage Toppin": requires_any_grab and requires_knight,
        "Pizzascape Pineapple Toppin": requires_any_grab and requires_knight,
        "Pizzascape Secret 1": requires_any_grab and requires_knight,
        "Pizzascape Secret 2": requires_any_grab and requires_knight,
        "Pizzascape Secret 3": requires_any_grab and peppino_requires_upward_mobility and requires_knight,
        "Pizzascape Treasure": requires_any_grab and peppino_requires_upward_mobility and requires_knight,
        "Chef Task: Shining Armor": requires_any_grab and requires_knight,
        "Chef Task: Spoonknight": requires_taunt,
        "Chef Task: Spherical": requires_any_grab and requires_knight,

    #Ancient Cheese
        "Ancient Cheese Complete": requires_any_grab and peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Ancient Cheese Mushroom Toppin": requires_none,
        "Ancient Cheese Cheese Toppin": requires_any_grab,
        "Ancient Cheese Tomato Toppin": requires_any_grab and (peppino_requires_upward_mobility or requires_uppercut),
        "Ancient Cheese Sausage Toppin": requires_any_grab and (peppino_requires_upward_mobility or requires_uppercut) and peppino_requires_downward_mobility,
        "Ancient Cheese Pineapple Toppin": requires_any_grab and (peppino_requires_upward_mobility or requires_uppercut) and peppino_requires_downward_mobility,
        "Ancient Cheese Secret 1": requires_none,
        "Ancient Cheese Secret 2": requires_any_grab and peppino_requires_upward_mobility,
        "Ancient Cheese Secret 3": requires_any_grab and peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Ancient Cheese Treasure": requires_any_grab and peppino_requires_upward_mobility,
        "Chef Task: Thrill Seeker": requires_any_grab and peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Chef Task: Volleybomb": requires_none,
        "Chef Task: Delicacy": requires_none,

    #Bloodsauce Dungeon
        "Bloodsauce Dungeon Complete": peppino_requires_downward_mobility and peppino_requires_upward_mobility,
        "Bloodsauce Dungeon Mushroom Toppin": requires_none,
        "Bloodsauce Dungeon Cheese Toppin": requires_none,
        "Bloodsauce Dungeon Tomato Toppin": peppino_requires_downward_mobility,
        "Bloodsauce Dungeon Sausage Toppin": peppino_requires_downward_mobility,
        "Bloodsauce Dungeon Pineapple Toppin": peppino_requires_downward_mobility,
        "Bloodsauce Dungeon Secret 1": requires_none,
        "Bloodsauce Dungeon Secret 2": requires_superjump and peppino_requires_downward_mobility,
        "Bloodsauce Dungeon Secret 3": peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Bloodsauce Dungeon Treasure": peppino_requires_downward_mobility and peppino_requires_upward_mobility,
        "Chef Task: Eruption Man": peppino_requires_downward_mobility and requires_superjump,
        "Chef Task: Very Very Hot Sauce": peppino_requires_downward_mobility and peppino_requires_upward_mobility,
        "Chef Task: Unsliced Pizzaman": peppino_requires_downward_mobility and peppino_requires_upward_mobility,

    #Oregano Desert
        "Oregano Desert Complete": (peppino_requires_wallclimb or (requires_superjump and requires_grab) or (requires_uppercut and requires_grab)) and requires_firemouth,
        "Oregano Desert Mushroom Toppin": peppino_requires_upward_mobility or requires_uppercut,
        "Oregano Desert Cheese Toppin": (peppino_requires_upward_mobility or (requires_uppercut and requires_grab)) and requires_firemouth,
        "Oregano Desert Tomato Toppin": (peppino_requires_wallclimb or (requires_superjump and requires_grab) or (requires_uppercut and requires_grab)) and requires_firemouth,
        "Oregano Desert Sausage Toppin": (peppino_requires_wallclimb or (requires_superjump and requires_grab) or (requires_uppercut and requires_grab)) and requires_firemouth,
        "Oregano Desert Pineapple Toppin": (peppino_requires_wallclimb or (requires_superjump and requires_grab) or (requires_uppercut and requires_grab)) and requires_firemouth,
        "Oregano Desert Secret 1": peppino_requires_upward_mobility,
        "Oregano Desert Secret 2": peppino_requires_wallclimb and requires_firemouth,
        "Oregano Desert Secret 3": peppino_requires_wallclimb and requires_firemouth,
        "Oregano Desert Treasure": peppino_requires_wallclimb and requires_firemouth,
        "Chef Task: Peppino's Rain Dance": peppino_requires_upward_mobility or requires_uppercut,
        "Chef Task: Unnecessary Violence": peppino_requires_wallclimb and requires_firemouth,
        "Chef Task: Alien Cow": (peppino_requires_wallclimb or (requires_superjump and requires_grab) or (requires_uppercut and requires_grab)) and requires_firemouth,

    #Wasteyard
        "Wasteyard Complete": peppino_requires_upward_mobility and requires_ghost,
        "Wasteyard Mushroom Toppin": requires_none,
        "Wasteyard Cheese Toppin": requires_ghost,
        "Wasteyard Tomato Toppin": (peppino_requires_upward_mobility or requires_uppercut) and requires_ghost,
        "Wasteyard Sausage Toppin": (peppino_requires_upward_mobility or requires_uppercut) and requires_ghost,
        "Wasteyard Pineapple Toppin": (peppino_requires_upward_mobility or requires_uppercut) and requires_ghost,
        "Wasteyard Secret 1": peppino_requires_upward_mobility,
        "Wasteyard Secret 2": peppino_requires_upward_mobility and requires_ghost,
        "Wasteyard Secret 3": peppino_requires_upward_mobility and requires_ghost,
        "Wasteyard Treasure": peppino_requires_upward_mobility and requires_ghost,
        "Chef Task: Alive and Well": peppino_requires_upward_mobility and requires_ghost,
        "Chef Task: Pretend Ghost": peppino_requires_upward_mobility and requires_ghost,
        "Chef Task: Ghosted": peppino_requires_upward_mobility and requires_ghost,

    #Fun Farm
        "Fun Farm Complete": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or (requires_uppercut and requires_grab)) and requires_mort,
        "Fun Farm Mushroom Toppin": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or requires_uppercut) and requires_mort,
        "Fun Farm Cheese Toppin": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or requires_uppercut) and requires_mort,
        "Fun Farm Tomato Toppin": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or (requires_uppercut and requires_grab)) and requires_mort,
        "Fun Farm Sausage Toppin": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or (requires_uppercut and requires_grab)) and requires_mort,
        "Fun Farm Pineapple Toppin": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or (requires_uppercut and requires_grab)) and requires_mort,
        "Fun Farm Secret 1": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_mort,
        "Fun Farm Secret 2": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_mort,
        "Fun Farm Secret 3": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_mort,
        "Fun Farm Treasure": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_mort,
        "Chef Task: Good Egg": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_mort,
        "Chef Task: No One Is Safe": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_mort and requires_supertaunt,
        "Chef Task: Cube Menace": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or requires_uppercut) and requires_mort,

    #Fastfood Saloon
        "Fastfood Saloon Complete": ((requires_superjump and peppino_requires_dive) or peppino_requires_wallclimb) and requires_grab and requires_weenie,
        "Fastfood Saloon Mushroom Toppin": peppino_requires_upward_mobility,
        "Fastfood Saloon Cheese Toppin": peppino_requires_upward_mobility and requires_grab and requires_weenie,
        "Fastfood Saloon Tomato Toppin": ((requires_superjump and peppino_requires_dive) or peppino_requires_wallclimb) and requires_grab and requires_weenie,
        "Fastfood Saloon Sausage Toppin": ((requires_superjump and peppino_requires_dive) or peppino_requires_wallclimb) and requires_grab and requires_weenie,
        "Fastfood Saloon Pineapple Toppin": ((requires_superjump and peppino_requires_dive) or peppino_requires_wallclimb) and requires_grab and requires_weenie,
        "Fastfood Saloon Secret 1": requires_superjump and peppino_requires_wallclimb and requires_grab and requires_weenie,
        "Fastfood Saloon Secret 2": requires_superjump and peppino_requires_wallclimb and requires_grab and requires_weenie,
        "Fastfood Saloon Secret 3": requires_superjump and peppino_requires_wallclimb and requires_grab and requires_weenie,
	    "Fastfood Saloon Treasure": ((requires_superjump and peppino_requires_dive) or peppino_requires_wallclimb) and requires_grab and requires_weenie,
        "Chef Task: Royal Flush": requires_superjump and requires_grab and peppino_requires_wallclimb and requires_weenie,
        "Chef Task: Non-Alcoholic": requires_superjump and requires_grab and peppino_requires_wallclimb and requires_weenie,
        "Chef Task: Already Pressed": requires_superjump and requires_grab and peppino_requires_wallclimb and requires_weenie,

    #Crust Cove
        "Crust Cove Complete": peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)) and requires_barrel,
        "Crust Cove Mushroom Toppin": peppino_requires_upward_mobility,
        "Crust Cove Cheese Toppin": peppino_requires_upward_mobility and requires_barrel,
        "Crust Cove Tomato Toppin": peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)) and requires_barrel,
        "Crust Cove Sausage Toppin": peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)) and requires_barrel,
        "Crust Cove Pineapple Toppin": peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)) and requires_barrel,
        "Crust Cove Secret 1": peppino_requires_upward_mobility and requires_barrel,
        "Crust Cove Secret 2": peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)) and requires_barrel,
        "Crust Cove Secret 3": requires_taunt and peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)) and requires_barrel,
        "Crust Cove Treasure": peppino_requires_upward_mobility and requires_barrel,
        "Chef Task: Demolition Expert": peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)) and requires_barrel,
        "Chef Task: Blowback": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_taunt,
        "Chef Task: X": peppino_requires_upward_mobility and peppino_requires_downward_mobility,

    #Gnome Forest
        "Gnome Forest Complete": peppino_requires_upward_mobility and peppino_requires_downward_mobility and gustavo_requires_upward_mobility,
        "Gnome Forest Mushroom Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility,
        "Gnome Forest Cheese Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility,
        "Gnome Forest Tomato Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility,
        "Gnome Forest Sausage Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility,
        "Gnome Forest Pineapple Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility,
        "Gnome Forest Secret 1": peppino_requires_downward_mobility and gustavo_requires_upward_mobility,
        "Gnome Forest Secret 2": peppino_requires_downward_mobility and gustavo_requires_upward_mobility,
        "Gnome Forest Secret 3": peppino_requires_upward_mobility and peppino_requires_downward_mobility and gustavo_requires_upward_mobility,
        "Gnome Forest Treasure": peppino_requires_upward_mobility and peppino_requires_downward_mobility and gustavo_requires_upward_mobility,
        "Chef Task: Bee Nice": requires_taunt,
        "Chef Task: Bullseye": requires_taunt,
        "Chef Task: Lumberjack": peppino_requires_upward_mobility and peppino_requires_downward_mobility and gustavo_requires_upward_mobility,

    #Deep-Dish 9
        "Deep-Dish 9 Complete": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,
        "Deep-Dish 9 Mushroom Toppin": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or requires_antigrav) and requires_rocket,
        "Deep-Dish 9 Cheese Toppin": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,
        "Deep-Dish 9 Tomato Toppin": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or (requires_antigrav and requires_uppercut)) and requires_rocket,
        "Deep-Dish 9 Sausage Toppin": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,
        "Deep-Dish 9 Pineapple Toppin": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,
        "Deep-Dish 9 Secret 1": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or requires_antigrav) and requires_rocket,
        "Deep-Dish 9 Secret 2": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_rocket and requires_antigrav,
        "Deep-Dish 9 Secret 3": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,
        "Deep-Dish 9 Treasure": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,
        "Chef Task: Blast 'Em Asteroids": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,
        "Chef Task: Turbo Tunnel": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,
        "Chef Task: Man Meteor": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,

    #GOLF
        "GOLF Complete": (peppino_requires_upward_mobility or requires_uppercut or peppino_requires_downward_mobility) and requires_ball,
        "GOLF Mushroom Toppin": requires_none,
        "GOLF Cheese Toppin": requires_ball,
        "GOLF Tomato Toppin": requires_ball,
        "GOLF Sausage Toppin": requires_ball,
        "GOLF Pineapple Toppin": requires_ball,
        "GOLF Secret 1": requires_ball,
        "GOLF Secret 2": (peppino_requires_upward_mobility or requires_uppercut) and requires_ball,
        "GOLF Secret 3": (peppino_requires_upward_mobility or requires_uppercut) and requires_ball,
        "GOLF Treasure": (peppino_requires_upward_mobility or requires_uppercut) and requires_ball,
        "Chef Task: Primo Golfer": (peppino_requires_upward_mobility or requires_uppercut) and requires_ball,
        "Chef Task: Helpful Burger": (peppino_requires_upward_mobility or requires_uppercut) and requires_ball,
        "Chef Task: Nice Shot": (peppino_requires_upward_mobility or requires_uppercut) and requires_ball,

    #The Pig City
        "The Pig City Complete": peppino_requires_downward_mobility and gustavo_requires_doublejump,
        "The Pig City Mushroom Toppin": requires_none,
        "The Pig City Cheese Toppin": peppino_requires_upward_mobility,
        "The Pig City Tomato Toppin": peppino_requires_downward_mobility,
        "The Pig City Sausage Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility,
        "The Pig City Pineapple Toppin": peppino_requires_downward_mobility and gustavo_requires_doublejump,
        "The Pig City Secret 1": requires_none,
        "The Pig City Secret 2": peppino_requires_downward_mobility and gustavo_requires_upward_mobility,
        "The Pig City Secret 3": peppino_requires_downward_mobility and gustavo_requires_doublejump,
        "The Pig City Treasure": peppino_requires_downward_mobility and gustavo_requires_doublejump,
        "Chef Task: Say Oink!": peppino_requires_downward_mobility and gustavo_requires_doublejump and requires_taunt,
        "Chef Task: Pan Fried": peppino_requires_downward_mobility and peppino_requires_upward_mobility,
        "Chef Task: Strike!": peppino_requires_downward_mobility and gustavo_requires_doublejump and gustavo_requires_kick,

    #Peppibot Factory
        "Peppibot Factory Complete": (requires_superjump and requires_uppercut) or (peppino_requires_wallclimb and (requires_grab or requires_uppercut)) and peppino_requires_downward_mobility and requires_pizzabox,
        "Peppibot Factory Mushroom Toppin": requires_superjump or (peppino_requires_wallclimb and (requires_grab or requires_uppercut)),
        "Peppibot Factory Cheese Toppin": (requires_superjump and requires_uppercut) or (peppino_requires_wallclimb and (requires_grab or requires_uppercut)),
        "Peppibot Factory Tomato Toppin": (requires_superjump and requires_uppercut) or (peppino_requires_wallclimb and (requires_grab or requires_uppercut)),
        "Peppibot Factory Sausage Toppin": (requires_superjump and requires_uppercut) or (peppino_requires_wallclimb and (requires_grab or requires_uppercut)) and requires_pizzabox,
        "Peppibot Factory Pineapple Toppin": (requires_superjump and requires_uppercut) or (peppino_requires_wallclimb and (requires_grab or requires_uppercut)) and requires_pizzabox,
        "Peppibot Factory Secret 1": peppino_requires_upward_mobility,
        "Peppibot Factory Secret 2": peppino_requires_wallclimb,
        "Peppibot Factory Secret 3": peppino_requires_wallclimb and peppino_requires_downward_mobility and requires_pizzabox,
        "Peppibot Factory Treasure": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_pizzabox,
        "Chef Task: There Can Be Only One": peppino_requires_wallclimb and peppino_requires_downward_mobility and requires_pizzabox,
        "Chef Task: Whoop This!": peppino_requires_upward_mobility,
        "Chef Task: Unflattening": peppino_requires_wallclimb and peppino_requires_downward_mobility and requires_pizzabox,

    #Oh Shit!
        "Oh Shit! Complete": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,
        "Oh Shit! Mushroom Toppin": requires_stickycheese and peppino_requires_downward_mobility,
        "Oh Shit! Cheese Toppin": requires_stickycheese and peppino_requires_downward_mobility and (peppino_requires_upward_mobility or requires_uppercut),
        "Oh Shit! Tomato Toppin": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,
        "Oh Shit! Sausage Toppin": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,
        "Oh Shit! Pineapple Toppin": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,
        "Oh Shit! Secret 1": requires_stickycheese and peppino_requires_downward_mobility,
        "Oh Shit! Secret 2": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,
        "Oh Shit! Secret 3": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,
        "Oh Shit! Treasure": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,
        "Chef Task: Food Clan": requires_stickycheese and peppino_requires_downward_mobility and (peppino_requires_upward_mobility or requires_uppercut),
        "Chef Task: Can't Fool Me": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,
        "Chef Task: Penny Pincher": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,

    #Freezerator
        "Freezerator Complete": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_satans,
        "Freezerator Mushroom Toppin": requires_none,
        "Freezerator Cheese Toppin": peppino_requires_upward_mobility or requires_uppercut,
        "Freezerator Tomato Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Freezerator Sausage Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Freezerator Pineapple Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Freezerator Secret 1": requires_superjump and peppino_requires_downward_mobility,
        "Freezerator Secret 2": requires_superjump and peppino_requires_downward_mobility,
        "Freezerator Secret 3": requires_superjump and peppino_requires_downward_mobility and requires_satans,
        "Freezerator Treasure": requires_superjump and peppino_requires_downward_mobility and requires_satans,
        "Chef Task: Ice Climber": requires_superjump and peppino_requires_downward_mobility and requires_satans,
        "Chef Task: Season's Greetings": requires_superjump and peppino_requires_downward_mobility and requires_satans and requires_grab,
        "Chef Task: Frozen Nuggets": requires_superjump and peppino_requires_downward_mobility and requires_satans,

    #Pizzascare
        "Pizzascare Complete": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_ball,
        "Pizzascare Mushroom Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Pizzascare Cheese Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Pizzascare Tomato Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_ball,
        "Pizzascare Sausage Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_ball,
        "Pizzascare Pineapple Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_ball,
        "Pizzascare Secret 1": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_ball,
        "Pizzascare Secret 2": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_ball,
        "Pizzascare Secret 3": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_ball,
        "Pizzascare Treasure": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_ball,
        "Chef Task: Haunted Playground": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_ball,
        "Chef Task: Skullsplitter": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_ball,
        "Chef Task: Cross to Bare": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_ball,

    #Don't Make a Sound
        "Don't Make a Sound Complete": (peppino_requires_wallclimb or (requires_superjump and peppino_requires_dive)) and requires_any_grab and requires_shotgun,
        "Don't Make a Sound Mushroom Toppin": requires_none,
        "Don't Make a Sound Cheese Toppin": peppino_requires_upward_mobility,
        "Don't Make a Sound Tomato Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Don't Make a Sound Sausage Toppin": peppino_requires_upward_mobility,
        "Don't Make a Sound Pineapple Toppin": (peppino_requires_wallclimb or (requires_superjump and peppino_requires_dive)) and requires_any_grab and requires_shotgun,
        "Don't Make a Sound Secret 1": requires_none,
        "Don't Make a Sound Secret 2": peppino_requires_wallclimb,
        "Don't Make a Sound Secret 3": peppino_requires_wallclimb,
        "Don't Make a Sound Treasure": peppino_requires_wallclimb and requires_any_grab and requires_shotgun,
        "Chef Task: Let Them Sleep": peppino_requires_wallclimb and requires_any_grab and requires_shotgun,
        "Chef Task: Jumpspared": peppino_requires_wallclimb and requires_any_grab and requires_shotgun,
        "Chef Task: And This... Is My Gun on a Stick!": peppino_requires_wallclimb and requires_any_grab and requires_shotgun,

    #WAR
        "WAR Complete": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_rocket,
        "WAR Mushroom Toppin": requires_any_grab and requires_shotgun and (peppino_requires_downward_mobility or peppino_requires_upward_mobility),
        "WAR Cheese Toppin": requires_any_grab and requires_shotgun and (peppino_requires_downward_mobility or peppino_requires_upward_mobility) and requires_rocket,
        "WAR Tomato Toppin": requires_any_grab and requires_shotgun and peppino_requires_downward_mobility and requires_rocket,
        "WAR Sausage Toppin": requires_any_grab and requires_shotgun and peppino_requires_downward_mobility and requires_rocket,
        "WAR Pineapple Toppin": requires_any_grab and requires_shotgun and peppino_requires_downward_mobility and requires_rocket,
        "WAR Secret 1": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility,
        "WAR Secret 2": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility,
        "WAR Secret 3": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility,
        "WAR Treasure": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_rocket,
        "Chef Task: Trip to the Warzone": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_rocket,
        "Chef Task: Sharpshooter": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_rocket,
        "Chef Task: Decorated Veteran": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_rocket,

    #Crumbling Tower of Pizza
        "The Crumbling Tower of Pizza Complete": peppino_requires_upward_mobility and requires_shotgun and requires_grab and peppino_requires_downward_mobility and requires_weenie and requires_rocket,
        "The Crumbling Tower of Pizza S Rank": peppino_requires_upward_mobility and requires_shotgun and requires_grab and peppino_requires_downward_mobility and requires_weenie and requires_rocket,
        "The Crumbling Tower of Pizza P Rank": peppino_requires_upward_mobility and requires_shotgun and requires_grab and peppino_requires_downward_mobility and requires_weenie and requires_rocket,

    #Pepperman
        "Pepperman Defeated": requires_none,
        "Chef Task: The Critic": requires_none,
        "Pepperman S Rank": requires_none,
        "Pepperman P Rank": requires_none,

    #Vigilante
        "The Vigilante Defeated": requires_grab and requires_revolver,
        "Chef Task: The Ugly": requires_grab and requires_revolver,
        "The Vigilante S Rank": requires_grab and requires_revolver,
        "The Vigilante P Rank": requires_grab and requires_revolver,

    #Noise
        "The Noise Defeated": requires_none,
        "Chef Task: Denoise": requires_none,
        "The Noise S Rank": requires_none,
        "The Noise P Rank": requires_none,

    #Fake Pep
        "Fake Peppino Defeated": requires_none,
        "Chef Task: Faker": requires_none,
        "Fake Peppino S Rank": requires_none,
        "Fake Peppino P Rank": requires_none,

    #Pizzaface
        "Pizzaface Defeated": requires_grab and requires_revolver,
        "Chef Task: Face-Off": requires_grab and requires_revolver,

    #Tutorial
        "Tutorial Complete": peppino_requires_downward_mobility and (requires_superjump or requires_uppercut) and requires_grab,
        "Tutorial Complete in under 2 minutes": peppino_requires_downward_mobility and (requires_superjump or requires_uppercut) and requires_grab,
        "Tutorial Mushroom Toppin": peppino_requires_downward_mobility,
        "Tutorial Cheese Toppin": peppino_requires_downward_mobility and peppino_requires_upward_mobility,
        "Tutorial Tomato Toppin": peppino_requires_downward_mobility and peppino_requires_upward_mobility,
        "Tutorial Sausage Toppin": peppino_requires_downward_mobility and (requires_superjump or requires_uppercut),
        "Tutorial Pineapple Toppin": peppino_requires_downward_mobility and (requires_superjump or requires_uppercut) and requires_grab,

    #misc
        "Snotty Murdered": requires_none,

    #for swap mode
        "The Doise Defeated": requires_none,
        "Chef Task: Denoise": requires_none,
        "The Doise S Rank": requires_none,
        "The Doise P Rank": requires_none,
    }

    pt_peppino_extra_rules = { #internal rules for rando purposes; do not correspond to real checks
	    "John Gutter Secret 1 Passed": requires_none,
        "John Gutter Secret 2 Passed": peppino_requires_wallclimb,
        "John Gutter Secret 3 Passed": peppino_requires_upward_mobility,

        "Pizzascape Secret 1 Passed": requires_none,
        "Pizzascape Secret 2 Passed": requires_any_grab and requires_knight,
        "Pizzascape Secret 3 Passed": requires_ball,

        "Ancient Cheese Secret 1 Passed": requires_none,
        "Ancient Cheese Secret 2 Passed": requires_any_grab,
        "Ancient Cheese Secret 3 Passed": peppino_requires_upward_mobility,

        "Bloodsauce Dungeon Secret 1 Passed": peppino_requires_upward_mobility,
        "Bloodsauce Dungeon Secret 2 Passed": peppino_requires_wallclimb,
        "Bloodsauce Dungeon Secret 3 Passed": requires_none,

        "Oregano Desert Secret 1 Passed": peppino_requires_downward_mobility,
        "Oregano Desert Secret 2 Passed": requires_firemouth,
        "Oregano Desert Secret 3 Passed": requires_superjump,

        "Wasteyard Secret 1 Passed": requires_none,
        "Wasteyard Secret 2 Passed": requires_ghost,
        "Wasteyard Secret 3 Passed": peppino_requires_wallclimb or requires_uppercut,

        "Fun Farm Secret 1 Passed": requires_none,
        "Fun Farm Secret 2 Passed": requires_mort,
        "Fun Farm Secret 3 Passed": peppino_requires_upward_mobility,

        "Fastfood Saloon Secret 1 Passed": peppino_requires_upward_mobility,
        "Fastfood Saloon Secret 2 Passed": peppino_requires_wallclimb,
        "Fastfood Saloon Secret 3 Passed": peppino_requires_upward_mobility,

        "Crust Cove Secret 1 Passed": requires_barrel,
        "Crust Cove Secret 2 Passed": peppino_requires_upward_mobility,
        "Crust Cove Secret 3 Passed": requires_taunt,

        "Gnome Forest Secret 1 Passed": gustavo_requires_doublejump,
        "Gnome Forest Secret 2 Passed": gustavo_requires_doublejump,
        "Gnome Forest Secret 3 Passed": peppino_requires_upward_mobility,

        "Deep-Dish 9 Secret 1 Passed": requires_antigrav,
        "Deep-Dish 9 Secret 2 Passed": requires_rocket,
        "Deep-Dish 9 Secret 3 Passed": peppino_requires_downward_mobility,

        "GOLF Secret 1 Passed": requires_none,
        "GOLF Secret 2 Passed": requires_ball,
        "GOLF Secret 3 Passed": requires_none,

        "The Pig City Secret 1 Passed": (requires_uppercut or peppino_requires_upward_mobility),
        "The Pig City Secret 2 Passed": gustavo_requires_doublejump,
        "The Pig City Secret 3 Passed": requires_none,

        "Peppibot Factory Secret 1 Passed": requires_none,
        "Peppibot Factory Secret 2 Passed": requires_any_grab,
        "Peppibot Factory Secret 3 Passed": requires_pizzabox,

        "Oh Shit! Secret 1 Passed": requires_none,
        "Oh Shit! Secret 2 Passed": requires_none,
        "Oh Shit! Secret 3 Passed": requires_none,

        "Freezerator Secret 1 Passed": requires_none,
        "Freezerator Secret 2 Passed": requires_none,
        "Freezerator Secret 3 Passed": requires_none,

        "Pizzascare Secret 1 Passed": requires_ball and peppino_requires_upward_mobility,
        "Pizzascare Secret 2 Passed": peppino_requires_wallclimb,
        "Pizzascare Secret 3 Passed": peppino_requires_upward_mobility,

        "Don't Make a Sound Secret 1 Passed": requires_none,
        "Don't Make a Sound Secret 2 Passed": peppino_requires_wallclimb,
        "Don't Make a Sound Secret 3 Passed": peppino_requires_upward_mobility,

        "WAR Secret 1 Passed": requires_none,
        "WAR Secret 2 Passed": peppino_requires_upward_mobility,
        "WAR Secret 3 Passed": requires_none,
    }

    noise_level_access_rules = {
        "John Gutter": requires_none,
        "Pizzascape": requires_none,
        "Ancient Cheese": noise_requires_upward_mobility,
        "Bloodsauce Dungeon": noise_requires_upward_mobility,
        "Oregano Desert": requires_none,
        "Wasteyard": requires_none,
        "Fun Farm": requires_none,
        "Fastfood Saloon": requires_none,
        "Crust Cove": requires_none, #Crust Cove
        "Gnome Forest": noise_requires_upward_mobility, 
        "Deep-Dish 9": noise_requires_big_upward_mobility or requires_antigrav,
        "GOLF": noise_requires_upward_mobility, 
        "The Pig City": requires_none, 
        "Peppibot Factory": requires_none, 
        "Oh Shit!": requires_none, 
        "Freezerator": noise_requires_upward_mobility,
        "Pizzascare": noise_requires_upward_mobility,
        "Don't Make a Sound": noise_requires_upward_mobility, 
        "WAR": noise_requires_big_upward_mobility,
    }

    noise_boss_access_rules = {
        "Pepperman": requires_none,
        "The Vigilante": requires_none,
        "The Doise": noise_requires_upward_mobility,
        "Fake Peppino": noise_requires_upward_mobility
    }

    noise_next_floor_access_rules = [
        noise_requires_upward_mobility,
        requires_none,
        noise_requires_upward_mobility,
        requires_none
    ]

    pt_noise_rules = { #access rules within levels, which do not change
    #John Gutter
        "John Gutter Complete": noise_requires_upward_mobility,
        "John Gutter Mushroom Toppin": noise_requires_upward_mobility or requires_grab or requires_bodyslam,
        "John Gutter Cheese Toppin": noise_requires_upward_mobility or requires_grab or requires_bodyslam,
        "John Gutter Tomato Toppin": noise_requires_upward_mobility or requires_grab or requires_bodyslam,
        "John Gutter Sausage Toppin": noise_requires_upward_mobility,
        "John Gutter Pineapple Toppin": noise_requires_upward_mobility,
        "John Gutter Secret 1": noise_requires_upward_mobility or requires_grab or requires_bodyslam,
        "John Gutter Secret 2": noise_requires_upward_mobility,
        "John Gutter Secret 3": noise_requires_upward_mobility,
        "John Gutter Treasure": noise_requires_upward_mobility,
        "Chef Task: John Gutted": noise_requires_upward_mobility,
        "Chef Task: Primate Rage": noise_requires_upward_mobility,
        "Chef Task: Let's Make This Quick": noise_requires_upward_mobility,

    #Pizzascape
        "Pizzascape Complete": requires_any_grab and noise_requires_upward_mobility and requires_knight,
        "Pizzascape Mushroom Toppin": requires_none,
        "Pizzascape Cheese Toppin": requires_none,
        "Pizzascape Tomato Toppin": requires_any_grab and requires_knight,
        "Pizzascape Sausage Toppin": requires_any_grab and requires_knight,
        "Pizzascape Pineapple Toppin": requires_any_grab and requires_knight,
        "Pizzascape Secret 1": requires_any_grab and requires_knight,
        "Pizzascape Secret 2": requires_any_grab and requires_knight,
        "Pizzascape Secret 3": requires_any_grab and noise_requires_upward_mobility and requires_knight,
        "Pizzascape Treasure": requires_any_grab and noise_requires_upward_mobility and requires_knight,
        "Chef Task: Shining Armor": requires_any_grab and requires_knight,
        "Chef Task: Spoonknight": requires_taunt,
        "Chef Task: Spherical": requires_any_grab and requires_knight,

    #Ancient Cheese
        "Ancient Cheese Complete": requires_any_grab and noise_requires_upward_mobility and noise_requires_downward_mobility,
        "Ancient Cheese Mushroom Toppin": requires_none,
        "Ancient Cheese Cheese Toppin": requires_any_grab,
        "Ancient Cheese Tomato Toppin": requires_any_grab and noise_requires_upward_mobility and noise_requires_downward_mobility, #noise can't use bombs to reach tomato cuz he's too slow
        "Ancient Cheese Sausage Toppin": requires_any_grab and noise_requires_upward_mobility and noise_requires_downward_mobility,
        "Ancient Cheese Pineapple Toppin": requires_any_grab and noise_requires_upward_mobility and noise_requires_downward_mobility,
        "Ancient Cheese Secret 1": requires_none,
        "Ancient Cheese Secret 2": requires_any_grab and noise_requires_upward_mobility,
        "Ancient Cheese Secret 3": requires_any_grab and noise_requires_upward_mobility and noise_requires_downward_mobility,
        "Ancient Cheese Treasure": requires_any_grab and noise_requires_upward_mobility,
        "Chef Task: Thrill Seeker": requires_any_grab and noise_requires_upward_mobility and noise_requires_downward_mobility,
        "Chef Task: Volleybomb": requires_none,
        "Chef Task: Delicacy": requires_none,

    #Bloodsauce Dungeon
        "Bloodsauce Dungeon Complete": noise_requires_downward_mobility and noise_requires_upward_mobility,
        "Bloodsauce Dungeon Mushroom Toppin": requires_none,
        "Bloodsauce Dungeon Cheese Toppin": requires_none,
        "Bloodsauce Dungeon Tomato Toppin": noise_requires_downward_mobility,
        "Bloodsauce Dungeon Sausage Toppin": noise_requires_downward_mobility,
        "Bloodsauce Dungeon Pineapple Toppin": noise_requires_downward_mobility,
        "Bloodsauce Dungeon Secret 1": requires_none,
        "Bloodsauce Dungeon Secret 2": requires_superjump and noise_requires_downward_mobility,
        "Bloodsauce Dungeon Secret 3": noise_requires_upward_mobility and noise_requires_downward_mobility,
        "Bloodsauce Dungeon Treasure": noise_requires_downward_mobility and noise_requires_upward_mobility,
        "Chef Task: Eruption Man": noise_requires_downward_mobility and requires_superjump,
        "Chef Task: Very Very Hot Sauce": noise_requires_downward_mobility and noise_requires_upward_mobility,
        "Chef Task: Unsliced Pizzaman": noise_requires_downward_mobility and noise_requires_upward_mobility,

    #Oregano Desert
        "Oregano Desert Complete": noise_requires_upward_mobility and requires_firemouth,
        "Oregano Desert Mushroom Toppin": noise_requires_upward_mobility,
        "Oregano Desert Cheese Toppin": noise_requires_upward_mobility and requires_firemouth,
        "Oregano Desert Tomato Toppin": noise_requires_upward_mobility and requires_firemouth,
        "Oregano Desert Sausage Toppin": noise_requires_upward_mobility and requires_firemouth,
        "Oregano Desert Pineapple Toppin": noise_requires_upward_mobility and requires_firemouth,
        "Oregano Desert Secret 1": noise_requires_crusher or noise_requires_wallbounce or requires_superjump,
        "Oregano Desert Secret 2": noise_requires_upward_mobility and requires_firemouth,
        "Oregano Desert Secret 3": noise_requires_upward_mobility and requires_firemouth,
        "Oregano Desert Treasure": noise_requires_upward_mobility and requires_firemouth,
        "Chef Task: Peppino's Rain Dance": noise_requires_upward_mobility,
        "Chef Task: Unnecessary Violence": noise_requires_upward_mobility and requires_firemouth,
        "Chef Task: Alien Cow": noise_requires_upward_mobility and requires_firemouth,

    #Wasteyard
        "Wasteyard Complete": noise_requires_upward_mobility and requires_ghost,
        "Wasteyard Mushroom Toppin": requires_none,
        "Wasteyard Cheese Toppin": requires_ghost,
        "Wasteyard Tomato Toppin": noise_requires_upward_mobility and requires_ghost,
        "Wasteyard Sausage Toppin": noise_requires_upward_mobility and requires_ghost,
        "Wasteyard Pineapple Toppin": noise_requires_upward_mobility and requires_ghost,
        "Wasteyard Secret 1": noise_requires_upward_mobility,
        "Wasteyard Secret 2": noise_requires_upward_mobility and requires_ghost,
        "Wasteyard Secret 3": noise_requires_upward_mobility and requires_ghost,
        "Wasteyard Treasure": noise_requires_upward_mobility and requires_ghost,
        "Chef Task: Alive and Well": noise_requires_upward_mobility and requires_ghost,
        "Chef Task: Pretend Ghost": noise_requires_upward_mobility and requires_ghost,
        "Chef Task: Ghosted": noise_requires_upward_mobility and requires_ghost,

    #Fun Farm
        "Fun Farm Complete": noise_requires_downward_mobility and noise_requires_upward_mobility and requires_mort,
        "Fun Farm Mushroom Toppin": noise_requires_downward_mobility and noise_requires_upward_mobility and requires_mort,
        "Fun Farm Cheese Toppin": noise_requires_downward_mobility and noise_requires_upward_mobility and requires_mort,
        "Fun Farm Tomato Toppin": noise_requires_downward_mobility and noise_requires_upward_mobility and requires_mort,
        "Fun Farm Sausage Toppin": noise_requires_downward_mobility and noise_requires_upward_mobility and requires_mort,
        "Fun Farm Pineapple Toppin": (noise_requires_crusher or requires_bodyslam) and noise_requires_upward_mobility and requires_mort,
        "Fun Farm Secret 1": noise_requires_downward_mobility and noise_requires_upward_mobility and requires_mort,
        "Fun Farm Secret 2": noise_requires_downward_mobility and noise_requires_upward_mobility and requires_mort,
        "Fun Farm Secret 3": noise_requires_downward_mobility and noise_requires_upward_mobility and requires_mort,
        "Fun Farm Treasure": noise_requires_downward_mobility and noise_requires_upward_mobility and requires_mort,
        "Chef Task: Good Egg": noise_requires_upward_mobility and noise_requires_downward_mobility and requires_mort,
        "Chef Task: No One Is Safe": noise_requires_upward_mobility and noise_requires_downward_mobility and requires_mort and requires_supertaunt,
        "Chef Task: Cube Menace": noise_requires_downward_mobility and noise_requires_upward_mobility and requires_mort and requires_mort,

    #Fastfood Saloon
        "Fastfood Saloon Complete": noise_requires_upward_mobility and requires_grab and requires_weenie,
        "Fastfood Saloon Mushroom Toppin": noise_requires_upward_mobility,
        "Fastfood Saloon Cheese Toppin": noise_requires_upward_mobility and requires_grab and requires_weenie,
        "Fastfood Saloon Tomato Toppin": noise_requires_upward_mobility and requires_grab and requires_weenie,
        "Fastfood Saloon Sausage Toppin": noise_requires_upward_mobility and requires_grab and requires_weenie,
        "Fastfood Saloon Pineapple Toppin": noise_requires_upward_mobility and requires_grab and requires_weenie,
        "Fastfood Saloon Secret 1": noise_requires_upward_mobility and requires_grab and requires_weenie,
        "Fastfood Saloon Secret 2": noise_requires_upward_mobility and requires_grab and requires_weenie,
        "Fastfood Saloon Secret 3": noise_requires_upward_mobility and requires_grab and requires_weenie,
	    "Fastfood Saloon Treasure": noise_requires_upward_mobility and requires_grab and requires_weenie,
        "Chef Task: Royal Flush": noise_requires_upward_mobility and requires_grab and requires_weenie,
        "Chef Task: Non-Alcoholic": noise_requires_upward_mobility and requires_grab and requires_weenie,
        "Chef Task: Already Pressed": noise_requires_upward_mobility and requires_grab and requires_weenie,

    #Crust Cove
        "Crust Cove Complete": noise_requires_big_upward_mobility and requires_barrel and noise_requires_downward_mobility,
        "Crust Cove Mushroom Toppin": noise_requires_big_upward_mobility,
        "Crust Cove Cheese Toppin": noise_requires_big_upward_mobility and requires_barrel,
        "Crust Cove Tomato Toppin": noise_requires_big_upward_mobility and requires_barrel and noise_requires_downward_mobility,
        "Crust Cove Sausage Toppin": noise_requires_big_upward_mobility and requires_barrel and noise_requires_downward_mobility,
        "Crust Cove Pineapple Toppin": noise_requires_big_upward_mobility and requires_barrel and noise_requires_downward_mobility,
        "Crust Cove Secret 1": noise_requires_upward_mobility and requires_barrel,
        "Crust Cove Secret 2": noise_requires_big_upward_mobility and requires_barrel and noise_requires_downward_mobility,
        "Crust Cove Secret 3": requires_taunt and noise_requires_big_upward_mobility and requires_barrel and noise_requires_downward_mobility,
        "Crust Cove Treasure": noise_requires_upward_mobility and requires_barrel,
        "Chef Task: Demolition Expert": noise_requires_big_upward_mobility and requires_barrel and noise_requires_downward_mobility,
        "Chef Task: Blowback": noise_requires_upward_mobility and noise_requires_downward_mobility and requires_taunt,
        "Chef Task: X": noise_requires_upward_mobility and noise_requires_downward_mobility,

    #Gnome Forest
        "Gnome Forest Complete": (requires_bodyslam or noise_requires_crusher) and noise_requires_upward_mobility,
        "Gnome Forest Mushroom Toppin": (requires_bodyslam or noise_requires_crusher) and noise_requires_upward_mobility,
        "Gnome Forest Cheese Toppin": (requires_bodyslam or noise_requires_crusher) and noise_requires_upward_mobility,
        "Gnome Forest Tomato Toppin": (requires_bodyslam or noise_requires_crusher) and noise_requires_upward_mobility,
        "Gnome Forest Sausage Toppin": (requires_bodyslam or noise_requires_crusher) and noise_requires_upward_mobility,
        "Gnome Forest Pineapple Toppin": (requires_bodyslam or noise_requires_crusher) and noise_requires_upward_mobility,
        "Gnome Forest Secret 1": (requires_bodyslam or noise_requires_crusher) and noise_requires_upward_mobility,
        "Gnome Forest Secret 2": (requires_bodyslam or noise_requires_crusher) and noise_requires_upward_mobility,
        "Gnome Forest Secret 3": (requires_bodyslam or noise_requires_crusher) and noise_requires_upward_mobility,
        "Gnome Forest Treasure": (requires_bodyslam or noise_requires_crusher) and noise_requires_upward_mobility,
        "Chef Task: Bee Nice": requires_taunt,
        "Chef Task: Bullseye": requires_taunt,
        "Chef Task: Lumberjack": (requires_bodyslam or noise_requires_crusher) and noise_requires_upward_mobility,

    #Deep-Dish 9
        "Deep-Dish 9 Complete": noise_requires_downward_mobility and noise_requires_upward_mobility and requires_rocket,
        "Deep-Dish 9 Mushroom Toppin": requires_rocket and (noise_requires_big_upward_mobility or requires_antigrav) and noise_requires_downward_mobility,
        "Deep-Dish 9 Cheese Toppin": requires_rocket and (noise_requires_big_upward_mobility or requires_antigrav) and noise_requires_downward_mobility,
        "Deep-Dish 9 Tomato Toppin": requires_rocket and (noise_requires_big_upward_mobility or requires_antigrav) and noise_requires_downward_mobility,
        "Deep-Dish 9 Sausage Toppin": requires_rocket and (noise_requires_big_upward_mobility or requires_uppercut) and (noise_requires_big_upward_mobility or requires_antigrav) and noise_requires_downward_mobility,
        "Deep-Dish 9 Pineapple Toppin": requires_rocket and (noise_requires_big_upward_mobility or requires_uppercut) and (noise_requires_big_upward_mobility or requires_antigrav) and noise_requires_downward_mobility,
        "Deep-Dish 9 Secret 1": requires_rocket and (noise_requires_big_upward_mobility or requires_antigrav) and noise_requires_downward_mobility,
        "Deep-Dish 9 Secret 2": requires_rocket and (noise_requires_big_upward_mobility or requires_uppercut) and (noise_requires_big_upward_mobility or requires_antigrav) and noise_requires_downward_mobility,
        "Deep-Dish 9 Secret 3": noise_requires_downward_mobility and noise_requires_upward_mobility and requires_rocket,
        "Deep-Dish 9 Treasure": noise_requires_downward_mobility and noise_requires_upward_mobility and requires_rocket,
        "Chef Task: Blast 'Em Asteroids": noise_requires_downward_mobility and noise_requires_upward_mobility and requires_rocket,
        "Chef Task: Turbo Tunnel": requires_rocket and (noise_requires_big_upward_mobility or requires_uppercut) and (noise_requires_big_upward_mobility or requires_antigrav) and noise_requires_downward_mobility,
        "Chef Task: Man Meteor": requires_bodyslam and noise_requires_upward_mobility and requires_rocket,

    #GOLF
        "GOLF Complete": (noise_requires_upward_mobility or requires_bodyslam) and requires_ball,
        "GOLF Mushroom Toppin": requires_none,
        "GOLF Cheese Toppin": requires_ball,
        "GOLF Tomato Toppin": requires_ball,
        "GOLF Sausage Toppin": requires_ball,
        "GOLF Pineapple Toppin": requires_ball,
        "GOLF Secret 1": requires_ball,
        "GOLF Secret 2": requires_ball,
        "GOLF Secret 3": requires_ball,
        "GOLF Treasure": requires_ball,
        "Chef Task: Primo Golfer": requires_ball,
        "Chef Task: Helpful Burger": requires_ball,
        "Chef Task: Nice Shot": requires_ball,

    #The Pig City
        "The Pig City Complete": noise_requires_downward_mobility and gustavo_requires_doublejump,
        "The Pig City Mushroom Toppin": requires_none,
        "The Pig City Cheese Toppin": noise_requires_upward_mobility,
        "The Pig City Tomato Toppin": noise_requires_crusher or requires_bodyslam,
        "The Pig City Sausage Toppin": noise_requires_downward_mobility and noise_requires_upward_mobility,
        "The Pig City Pineapple Toppin": noise_requires_downward_mobility and noise_requires_upward_mobility,
        "The Pig City Secret 1": requires_none,
        "The Pig City Secret 2": noise_requires_downward_mobility and noise_requires_upward_mobility,
        "The Pig City Secret 3": noise_requires_downward_mobility and noise_requires_upward_mobility,
        "The Pig City Treasure": noise_requires_downward_mobility and noise_requires_upward_mobility,
        "Chef Task: Say Oink!": noise_requires_downward_mobility and noise_requires_upward_mobility and requires_taunt,
        "Chef Task: Pan Fried": noise_requires_downward_mobility and (noise_requires_big_upward_mobility or requires_uppercut),
        "Chef Task: Strike!": noise_requires_downward_mobility and noise_requires_upward_mobility,

    #Peppibot Factory
        "Peppibot Factory Complete": (noise_requires_big_upward_mobility or requires_uppercut),
        "Peppibot Factory Mushroom Toppin": noise_requires_big_upward_mobility or requires_uppercut,
        "Peppibot Factory Cheese Toppin": noise_requires_big_upward_mobility or requires_uppercut,
        "Peppibot Factory Tomato Toppin": noise_requires_big_upward_mobility or requires_uppercut,
        "Peppibot Factory Sausage Toppin": (noise_requires_big_upward_mobility or requires_uppercut) and requires_pizzabox,
        "Peppibot Factory Pineapple Toppin": (noise_requires_big_upward_mobility or requires_uppercut) and requires_pizzabox,
        "Peppibot Factory Secret 1": noise_requires_big_upward_mobility or requires_uppercut,
        "Peppibot Factory Secret 2": noise_requires_big_upward_mobility or requires_uppercut,
        "Peppibot Factory Secret 3": (noise_requires_big_upward_mobility or requires_uppercut) and requires_pizzabox and noise_requires_downward_mobility,
        "Peppibot Factory Treasure": (noise_requires_big_upward_mobility or requires_uppercut) and requires_pizzabox and noise_requires_downward_mobility,
        "Chef Task: There Can Be Only One": (noise_requires_big_upward_mobility or requires_uppercut) and requires_pizzabox and noise_requires_downward_mobility,
        "Chef Task: Whoop This!": noise_requires_upward_mobility,
        "Chef Task: Unflattening": (noise_requires_big_upward_mobility or requires_uppercut) and requires_pizzabox and noise_requires_downward_mobility,

    #Oh Shit!
        "Oh Shit! Complete": requires_stickycheese and noise_requires_downward_mobility and noise_requires_upward_mobility,
        "Oh Shit! Mushroom Toppin": requires_stickycheese and noise_requires_downward_mobility,
        "Oh Shit! Cheese Toppin": requires_stickycheese and noise_requires_downward_mobility and noise_requires_upward_mobility,
        "Oh Shit! Tomato Toppin": requires_stickycheese and noise_requires_downward_mobility and noise_requires_upward_mobility,
        "Oh Shit! Sausage Toppin": requires_stickycheese and noise_requires_downward_mobility and noise_requires_upward_mobility,
        "Oh Shit! Pineapple Toppin": requires_stickycheese and noise_requires_downward_mobility and noise_requires_upward_mobility,
        "Oh Shit! Secret 1": requires_stickycheese and noise_requires_downward_mobility,
        "Oh Shit! Secret 2": requires_stickycheese and noise_requires_downward_mobility and noise_requires_upward_mobility,
        "Oh Shit! Secret 3": requires_stickycheese and noise_requires_downward_mobility and noise_requires_upward_mobility,
        "Oh Shit! Treasure": requires_stickycheese and noise_requires_downward_mobility and noise_requires_upward_mobility,
        "Chef Task: Food Clan": requires_stickycheese and noise_requires_downward_mobility and (noise_requires_upward_mobility or requires_uppercut),
        "Chef Task: Can't Fool Me": requires_stickycheese and noise_requires_downward_mobility and noise_requires_upward_mobility,
        "Chef Task: Penny Pincher": requires_stickycheese and noise_requires_downward_mobility and noise_requires_upward_mobility,

    #Freezerator
        "Freezerator Complete": requires_satans,
        "Freezerator Mushroom Toppin": requires_none,
        "Freezerator Cheese Toppin": noise_requires_upward_mobility or requires_satans,
        "Freezerator Tomato Toppin": (noise_requires_upward_mobility and noise_requires_downward_mobility) or requires_satans,
        "Freezerator Sausage Toppin": (noise_requires_big_upward_mobility and noise_requires_downward_mobility) or requires_satans,
        "Freezerator Pineapple Toppin": (noise_requires_big_upward_mobility and noise_requires_downward_mobility) or requires_satans,
        "Freezerator Secret 1": noise_requires_upward_mobility and noise_requires_downward_mobility,
        "Freezerator Secret 2": (noise_requires_big_upward_mobility and noise_requires_downward_mobility) or requires_satans,
        "Freezerator Secret 3": requires_satans,
        "Freezerator Treasure": requires_satans,
        "Chef Task: Ice Climber": requires_satans,
        "Chef Task: Season's Greetings": requires_satans and requires_grab,
        "Chef Task: Frozen Nuggets": requires_satans,

    #Pizzascare
        "Pizzascare Complete": noise_requires_upward_mobility and noise_requires_downward_mobility and requires_ball,
        "Pizzascare Mushroom Toppin": noise_requires_upward_mobility and noise_requires_downward_mobility,
        "Pizzascare Cheese Toppin": noise_requires_upward_mobility and noise_requires_downward_mobility,
        "Pizzascare Tomato Toppin": noise_requires_upward_mobility and noise_requires_downward_mobility and requires_ball,
        "Pizzascare Sausage Toppin": noise_requires_upward_mobility and noise_requires_downward_mobility and requires_ball,
        "Pizzascare Pineapple Toppin": noise_requires_upward_mobility and noise_requires_downward_mobility and requires_ball,
        "Pizzascare Secret 1": noise_requires_upward_mobility and noise_requires_downward_mobility and requires_ball,
        "Pizzascare Secret 2": noise_requires_upward_mobility and noise_requires_downward_mobility and requires_ball,
        "Pizzascare Secret 3": noise_requires_upward_mobility and noise_requires_downward_mobility and requires_ball,
        "Pizzascare Treasure": noise_requires_upward_mobility and noise_requires_downward_mobility and requires_ball,
        "Chef Task: Haunted Playground": noise_requires_upward_mobility and noise_requires_downward_mobility and requires_ball,
        "Chef Task: Skullsplitter": noise_requires_upward_mobility and noise_requires_downward_mobility and requires_ball,
        "Chef Task: Cross to Bare": noise_requires_upward_mobility and noise_requires_downward_mobility and requires_ball,

    #Don't Make a Sound
        "Don't Make a Sound Complete": noise_requires_big_upward_mobility and requires_any_grab and requires_shotgun,
        "Don't Make a Sound Mushroom Toppin": requires_none,
        "Don't Make a Sound Cheese Toppin": noise_requires_upward_mobility,
        "Don't Make a Sound Tomato Toppin": noise_requires_big_upward_mobility and noise_requires_downward_mobility,
        "Don't Make a Sound Sausage Toppin": noise_requires_big_upward_mobility,
        "Don't Make a Sound Pineapple Toppin": noise_requires_big_upward_mobility and requires_any_grab and requires_shotgun,
        "Don't Make a Sound Secret 1": requires_none,
        "Don't Make a Sound Secret 2": noise_requires_upward_mobility,
        "Don't Make a Sound Secret 3": noise_requires_big_upward_mobility,
        "Don't Make a Sound Treasure": noise_requires_big_upward_mobility and requires_any_grab and requires_shotgun,
        "Chef Task: Let Them Sleep": noise_requires_big_upward_mobility and requires_any_grab and requires_shotgun,
        "Chef Task: Jumpspared": noise_requires_big_upward_mobility and requires_any_grab and requires_shotgun,
        "Chef Task: And This... Is My Gun on a Stick!": noise_requires_big_upward_mobility and requires_any_grab and requires_shotgun,

    #WAR
        "WAR Complete": requires_any_grab and requires_shotgun and noise_requires_upward_mobility and noise_requires_downward_mobility and requires_rocket,
        "WAR Mushroom Toppin": requires_any_grab and requires_shotgun and (noise_requires_downward_mobility or (noise_requires_big_upward_mobility or noise_requires_wallbounce)),
        "WAR Cheese Toppin": requires_any_grab and requires_shotgun and (requires_bodyslam or noise_requires_crusher or (noise_requires_tornado and (noise_requires_big_upward_mobility or noise_requires_wallbounce))) and requires_rocket,
        "WAR Tomato Toppin": requires_any_grab and requires_shotgun and (requires_bodyslam or noise_requires_crusher or (noise_requires_tornado and (noise_requires_big_upward_mobility or noise_requires_wallbounce))) and requires_rocket,
        "WAR Sausage Toppin": requires_any_grab and requires_shotgun and (requires_bodyslam or noise_requires_crusher or (noise_requires_tornado and (noise_requires_big_upward_mobility or noise_requires_wallbounce))) and requires_rocket,
        "WAR Pineapple Toppin": requires_any_grab and requires_shotgun and (requires_bodyslam or noise_requires_crusher or (noise_requires_tornado and (noise_requires_big_upward_mobility or noise_requires_wallbounce))) and requires_rocket,
        "WAR Secret 1": requires_any_grab and requires_shotgun and (requires_bodyslam or noise_requires_crusher or (noise_requires_tornado and (noise_requires_big_upward_mobility or noise_requires_wallbounce))) and requires_rocket,
        "WAR Secret 2": requires_any_grab and requires_shotgun and (requires_bodyslam or noise_requires_crusher or (noise_requires_tornado and (noise_requires_big_upward_mobility or noise_requires_wallbounce))) and requires_rocket,
        "WAR Secret 3": requires_any_grab and requires_shotgun and (requires_bodyslam or noise_requires_crusher or (noise_requires_tornado and (noise_requires_big_upward_mobility or noise_requires_wallbounce))) and requires_rocket,
        "WAR Treasure": requires_any_grab and requires_shotgun and (requires_bodyslam or noise_requires_crusher or (noise_requires_tornado and noise_requires_big_upward_mobility)) and requires_rocket,
        "Chef Task: Trip to the Warzone": requires_any_grab and requires_shotgun and noise_requires_upward_mobility and noise_requires_downward_mobility and requires_rocket,
        "Chef Task: Sharpshooter": requires_any_grab and requires_shotgun and noise_requires_upward_mobility and noise_requires_downward_mobility and requires_rocket,
        "Chef Task: Decorated Veteran": requires_any_grab and requires_shotgun and noise_requires_upward_mobility and noise_requires_downward_mobility and requires_rocket,

    #Crumbling Tower of Pizza
        "The Crumbling Tower of Pizza Complete": noise_requires_big_upward_mobility and requires_shotgun and requires_grab and noise_requires_downward_mobility and requires_weenie and requires_rocket,
        "The Crumbling Tower of Pizza S Rank": noise_requires_big_upward_mobility and requires_shotgun and requires_grab and noise_requires_downward_mobility and requires_weenie and requires_rocket,
        "The Crumbling Tower of Pizza P Rank": noise_requires_big_upward_mobility and requires_shotgun and requires_grab and noise_requires_downward_mobility and requires_weenie and requires_rocket,

    #Pepperman
        "Pepperman Defeated": requires_none,
        "Chef Task: The Critic": requires_none,
        "Pepperman S Rank": requires_none,
        "Pepperman P Rank": requires_none,

    #Vigilante
        "The Vigilante Defeated": noise_requires_bomb,
        "Chef Task: The Ugly": noise_requires_bomb,
        "The Vigilante S Rank": noise_requires_bomb,
        "The Vigilante P Rank": noise_requires_bomb,

    #Noise
        "The Doise Defeated": requires_none,
        "Chef Task: Denoise": requires_none,
        "The Doise S Rank": requires_none,
        "The Doise P Rank": requires_none,

    #Fake Pep
        "Fake Peppino Defeated": requires_none,
        "Chef Task: Faker": requires_none,
        "Fake Peppino S Rank": requires_none,
        "Fake Peppino P Rank": requires_none,

    #Pizzaface
        "Pizzaface Defeated": noise_requires_bomb,
        "Chef Task: Face-Off": noise_requires_bomb,

    #Tutorial
        "Tutorial Complete": (noise_requires_big_upward_mobility or noise_requires_tornado) and noise_requires_upward_mobility and noise_requires_downward_mobility,
        "Tutorial Complete in under 2 minutes": (noise_requires_big_upward_mobility or noise_requires_tornado) and noise_requires_upward_mobility and noise_requires_downward_mobility,

    #misc
        "Snotty Murdered": requires_none,
    }

    pt_noise_extra_rules = { #internal rules for rando purposes; do not correspond to real checks
	    "John Gutter Secret 1 Passed": requires_none,
        "John Gutter Secret 2 Passed": noise_requires_upward_mobility,
        "John Gutter Secret 3 Passed": noise_requires_upward_mobility,

        "Pizzascape Secret 1 Passed": requires_none,
        "Pizzascape Secret 2 Passed": requires_any_grab and requires_knight,
        "Pizzascape Secret 3 Passed": requires_ball,

        "Ancient Cheese Secret 1 Passed": requires_none,
        "Ancient Cheese Secret 2 Passed": requires_any_grab,
        "Ancient Cheese Secret 3 Passed": noise_requires_upward_mobility,

        "Bloodsauce Dungeon Secret 1 Passed": noise_requires_upward_mobility,
        "Bloodsauce Dungeon Secret 2 Passed": noise_requires_crusher or noise_requires_wallbounce or requires_uppercut,
        "Bloodsauce Dungeon Secret 3 Passed": requires_none,

        "Oregano Desert Secret 1 Passed": noise_requires_downward_mobility,
        "Oregano Desert Secret 2 Passed": requires_firemouth,
        "Oregano Desert Secret 3 Passed": noise_requires_crusher or noise_requires_big_upward_mobility,

        "Wasteyard Secret 1 Passed": requires_none,
        "Wasteyard Secret 2 Passed": requires_ghost,
        "Wasteyard Secret 3 Passed": noise_requires_upward_mobility and requires_ghost,

        "Fun Farm Secret 1 Passed": requires_none,
        "Fun Farm Secret 2 Passed": requires_mort,
        "Fun Farm Secret 3 Passed": noise_requires_upward_mobility,

        "Fastfood Saloon Secret 1 Passed": noise_requires_upward_mobility,
        "Fastfood Saloon Secret 2 Passed": (noise_requires_crusher or noise_requires_wallbounce or requires_uppercut),
        "Fastfood Saloon Secret 3 Passed": noise_requires_downward_mobility,

        "Crust Cove Secret 1 Passed": requires_barrel,
        "Crust Cove Secret 2 Passed": noise_requires_upward_mobility,
        "Crust Cove Secret 3 Passed": requires_taunt,

        "Gnome Forest Secret 1 Passed": noise_requires_big_upward_mobility or requires_uppercut,
        "Gnome Forest Secret 2 Passed": noise_requires_big_upward_mobility or requires_uppercut,
        "Gnome Forest Secret 3 Passed": noise_requires_big_upward_mobility or noise_requires_wallbounce,

        "Deep-Dish 9 Secret 1 Passed": requires_antigrav or noise_requires_big_upward_mobility or requires_uppercut,
        "Deep-Dish 9 Secret 2 Passed": requires_rocket or noise_requires_crusher,
        "Deep-Dish 9 Secret 3 Passed": (requires_bodyslam or noise_requires_crusher) and (requires_antigrav or noise_requires_upward_mobility),

        "GOLF Secret 1 Passed": requires_none,
        "GOLF Secret 2 Passed": requires_ball,
        "GOLF Secret 3 Passed": requires_none,

        "The Pig City Secret 1 Passed": noise_requires_upward_mobility,
        "The Pig City Secret 2 Passed": noise_requires_upward_mobility,
        "The Pig City Secret 3 Passed": requires_none,

        "Peppibot Factory Secret 1 Passed": requires_none,
        "Peppibot Factory Secret 2 Passed": requires_any_grab,
        "Peppibot Factory Secret 3 Passed": requires_pizzabox,

        "Oh Shit! Secret 1 Passed": requires_none,
        "Oh Shit! Secret 2 Passed": requires_none,
        "Oh Shit! Secret 3 Passed": requires_none,

        "Freezerator Secret 1 Passed": requires_none,
        "Freezerator Secret 2 Passed": requires_none,
        "Freezerator Secret 3 Passed": requires_none,

        "Pizzascare Secret 1 Passed": requires_ball and noise_requires_upward_mobility,
        "Pizzascare Secret 2 Passed": noise_requires_upward_mobility,
        "Pizzascare Secret 3 Passed": noise_requires_upward_mobility,

        "Don't Make a Sound Secret 1 Passed": requires_none,
        "Don't Make a Sound Secret 2 Passed": noise_requires_upward_mobility,
        "Don't Make a Sound Secret 3 Passed": noise_requires_upward_mobility,

        "WAR Secret 1 Passed": requires_none,
        "WAR Secret 2 Passed": noise_requires_upward_mobility,
        "WAR Secret 3 Passed": requires_none,
    }

    pt_swap_rules = { #for swap-specific rules

    }

    def get_s_rank_rule(lvl: str, character: int):
        if character == 0:
            new_rule = (pt_peppino_rules[lvl + " Mushroom Toppin"] and pt_peppino_rules[lvl + " Cheese Toppin"] and pt_peppino_rules[lvl + " Tomato Toppin"] and pt_peppino_rules[lvl + " Sausage Toppin"] and pt_peppino_rules[lvl + " Pineapple Toppin"] and pt_peppino_rules[lvl + " Complete"] and pt_peppino_rules[lvl + " Treasure"] and pt_peppino_rules[lvl + " Secret 1"] and pt_peppino_rules[lvl + " Secret 2"] and pt_peppino_rules[lvl + " Secret 3"] and pt_peppino_extra_rules[secrets_map[lvl + " Secret 1"] + " Passed"] and pt_peppino_extra_rules[secrets_map[lvl + " Secret 2"] + " Passed"] and pt_peppino_extra_rules[secrets_map[lvl + " Secret 3"] + " Passed"])
        elif character == 1:
            new_rule = pt_noise_rules[lvl + " Mushroom Toppin"] and pt_noise_rules[lvl + " Cheese Toppin"] and pt_noise_rules[lvl + " Tomato Toppin"] and pt_noise_rules[lvl + " Sausage Toppin"] and pt_noise_rules[lvl + " Pineapple Toppin"] and pt_noise_rules[lvl + " Complete"] and pt_noise_rules[lvl + " Treasure"] and pt_noise_rules[lvl + " Secret 1"] and pt_noise_rules[lvl + " Secret 2"] and pt_noise_rules[lvl + " Secret 3"] and pt_noise_extra_rules[secrets_map[lvl + " Secret 1"] + " Passed"] and pt_noise_extra_rules[secrets_map[lvl + " Secret 2"] + " Passed"] and pt_noise_extra_rules[secrets_map[lvl + " Secret 3"] + " Passed"]
        else:
            new_rule = (pt_peppino_rules[lvl + " Mushroom Toppin"] and pt_peppino_rules[lvl + " Cheese Toppin"] and pt_peppino_rules[lvl + " Tomato Toppin"] and pt_peppino_rules[lvl + " Sausage Toppin"] and pt_peppino_rules[lvl + " Pineapple Toppin"] and pt_peppino_rules[lvl + " Complete"] and pt_peppino_rules[lvl + " Treasure"] and pt_peppino_rules[lvl + " Secret 1"] and pt_peppino_rules[lvl + " Secret 2"] and pt_peppino_rules[lvl + " Secret 3"] and pt_peppino_extra_rules[secrets_map[lvl + " Secret 1"] + " Passed"] and pt_peppino_extra_rules[secrets_map[lvl + " Secret 2"] + " Passed"] and pt_peppino_extra_rules[secrets_map[lvl + " Secret 3"] + " Passed"]) or (pt_noise_rules[lvl + " Mushroom Toppin"] and pt_noise_rules[lvl + " Cheese Toppin"] and pt_noise_rules[lvl + " Tomato Toppin"] and pt_noise_rules[lvl + " Sausage Toppin"] and pt_noise_rules[lvl + " Pineapple Toppin"] and pt_noise_rules[lvl + " Complete"] and pt_noise_rules[lvl + " Treasure"] and pt_noise_rules[lvl + " Secret 1"] and pt_noise_rules[lvl + " Secret 2"] and pt_noise_rules[lvl + " Secret 3"] and pt_noise_extra_rules[secrets_map[lvl + " Secret 1"] + " Passed"] and pt_noise_extra_rules[secrets_map[lvl + " Secret 2"] + " Passed"] and pt_noise_extra_rules[secrets_map[lvl + " Secret 3"] + " Passed"])
        return new_rule

    secrets_list = get_secrets_list() 
    if options.randomize_levels:
        levels_map = dict(zip(levels_list, level_gate_rando(world, options.character != 0)))
    else:
        levels_map = dict(zip(levels_list, levels_list))

    if options.randomize_bosses:
        bosses_map = dict(zip(bosses_list, boss_gate_rando(world, options.character != 0)))
    else:
        bosses_map = dict(zip(bosses_list, bosses_list))

    if options.randomize_secrets:
        secrets_map = dict(zip(secrets_list, secret_rando(world)))
    else:
        secrets_map = dict(zip(secrets_list, secrets_list))

    world.level_map = levels_map
    world.boss_map = bosses_map
    world.secret_map = secrets_map

    #connect regions
    multiworld.get_region("Menu", world.player).connect(multiworld.get_region("Floor 1 Tower Lobby", world.player), "Menu to Floor 1 Tower Lobby")
    for i in range(4):
        multiworld.get_region(floors_list[i], world.player).connect(multiworld.get_region(floors_list[i+1], world.player), floors_list[i] + " to " + floors_list[i+1])
    
    multiworld.get_region("Floor 5 Staff Only", world.player).connect(multiworld.get_region("Pizzaface", world.player), "Floor 5 Staff Only to Pizzaface")
    multiworld.get_region("Pizzaface", world.player).connect(multiworld.get_region("The Crumbling Tower of Pizza", world.player), "Pizzaface to The Crumbling Tower of Pizza")

    for i in range(4):
        for ii in range(4):
            level_name = levels_map[levels_list[(4*i)+ii]]
            multiworld.get_region(floors_list[i], world.player).connect(multiworld.get_region(levels_map[level_name], world.player), floors_list[i] + " to " + levels_map[level_name])
        multiworld.get_region(floors_list[i], world.player).connect(multiworld.get_region(bosses_map[bosses_list[i]], world.player), floors_list[i] + " to " + bosses_map[bosses_list[i]])

    for i in range(3):
        level_name = levels_map[levels_list[i + 16]]
        multiworld.get_region("Floor 5 Staff Only", world.player).connect(multiworld.get_region("Floor 5 Staff Only", world.player), "Floor 5 Staff Only to " + levels_map[level_name])

    #set rules
    for location in multiworld.get_locations(world.player):
        if (("S Rank" in location.name) or ("P Rank" in location.name)) and (location.parent_region.name not in bosses_list):
            location.access_rule = get_s_rank_rule(location.parent_region.name, options.character)
        else:
            if options.character == 0: location.access_rule = pt_peppino_rules[location.name]
            elif options.character == 1: location.access_rule = pt_noise_rules[location.name]
            else: location.access_rule = pt_peppino_rules[location.name] or pt_noise_rules[location.name]

    def get_toppin_prop(perc: int):
        return floor(toppins * (perc / 100))

    #toppin requirements for bosses
    multiworld.get_entrance("Floor 1 Tower Lobby to " + bosses_map["Pepperman"], world.player).access_rule = lambda state: state.has("Toppin", world.player, get_toppin_prop(options.floor_1_cost))
    multiworld.get_entrance("Floor 2 Western District to " + bosses_map["The Vigilante"], world.player).access_rule = lambda state: state.has("Toppin", world.player, get_toppin_prop(options.floor_2_cost))
    multiworld.get_entrance("Floor 3 Vacation Resort to " + bosses_map[bosses_list[2]], world.player).access_rule = lambda state: state.has("Toppin", world.player, get_toppin_prop(options.floor_3_cost)) #the noise or the doise, depending on character played
    multiworld.get_entrance("Floor 4 Slum to " + bosses_map["Fake Peppino"], world.player).access_rule = lambda state: state.has("Toppin", world.player, get_toppin_prop(options.floor_4_cost))
    multiworld.get_entrance("Floor 5 Staff Only to Pizzaface", world.player).access_rule = lambda state: state.has("Toppin", world.player, get_toppin_prop(options.floor_5_cost))

    #boss key requirements for floors
    if not options.open_world:
        multiworld.get_entrance("Floor 1 Tower Lobby to Floor 2 Western District", world.player).access_rule = lambda state: state.has("Boss Key", world.player, 1)
        multiworld.get_entrance("Floor 2 Western District to Floor 3 Vacation Resort", world.player).access_rule = lambda state: state.has("Boss Key", world.player, 2)
        multiworld.get_entrance("Floor 3 Vacation Resort to Floor 4 Slum", world.player).access_rule = lambda state: state.has("Boss Key", world.player, 3)
        multiworld.get_entrance("Floor 4 Slum to Floor 5 Staff Only", world.player).access_rule = lambda state: state.has("Boss Key", world.player, 4)

    #access rules for floors
    for i in range(4): 
        if options.bonus_ladders < (i+1):
            if options.character == 0:
                add_rule(multiworld.get_entrance(floors_list[i] + " to " + floors_list[i+1], world.player), peppino_next_floor_access_rules[i])
            elif options.character == 1:
                add_rule(multiworld.get_entrance(floors_list[i] + " to " + floors_list[i+1], world.player), noise_next_floor_access_rules[i])
            elif options.character == 2:
                add_rule(multiworld.get_entrance(floors_list[i] + " to " + floors_list[i+1], world.player), peppino_next_floor_access_rules[i] or noise_next_floor_access_rules[i])

    #access rules for levels
    for i in range(4):
        if options.bonus_ladders < (i+1):
            for ii in range(4):
                level_name = levels_map[levels_list[(4*i)+ii]]
                if options.character == 0: multiworld.get_entrance(floors_list[i] + " to " + level_name, world.player).access_rule = peppino_level_access_rules[levels_list[(4*i)+ii]]
                elif options.character == 1: multiworld.get_entrance(floors_list[i] + " to " + level_name, world.player).access_rule = noise_level_access_rules[levels_list[(4*i)+ii]]
                elif options.character == 2: multiworld.get_entrance(floors_list[i] + " to " + level_name, world.player).access_rule = peppino_level_access_rules[levels_list[(4*i)+ii]] or noise_level_access_rules[levels_list[(4*i)+ii]]
    for i in range(3):
        if options.bonus_ladders < 5:
            level_name = levels_map[levels_list[i+16]]
            if options.character == 0: multiworld.get_entrance("Floor 5 Staff Only to " + level_name, world.player).access_rule = peppino_level_access_rules[levels_list[i+16]]
            elif options.character == 1: multiworld.get_entrance("Floor 5 Staff Only to " + level_name, world.player).access_rule = noise_level_access_rules[levels_list[i+16]]
            elif options.character == 2: multiworld.get_entrance("Floor 5 Staff Only to " + level_name, world.player).access_rule = peppino_level_access_rules[levels_list[i+16]] or noise_level_access_rules[levels_list[i+16]]

    #access rules for bosses
    for i in range(4):
        if options.bonus_ladders < (i+1):
            if options.character == 0: add_rule(multiworld.get_entrance(floors_list[i] + " to " + bosses_map[bosses_list[i]], world.player), peppino_boss_access_rules[bosses_list[i]])
            elif options.character == 1: add_rule(multiworld.get_entrance(floors_list[i] + " to " + bosses_map[bosses_list[i]], world.player), noise_boss_access_rules[bosses_list[i]])
            elif options.character == 1: add_rule(multiworld.get_entrance(floors_list[i] + " to " + bosses_map[bosses_list[i]], world.player), peppino_boss_access_rules[bosses_list[i]] or noise_boss_access_rules[bosses_list[i]])
    #...and pizzaface
    if options.bonus_ladders < 5:
        if options.character == 0: add_rule(multiworld.get_entrance("Floor 5 Staff Only to Pizzaface", world.player), requires_superjump)
        else: add_rule(multiworld.get_entrance("Floor 5 Staff Only to Pizzaface", world.player), noise_requires_big_upward_mobility)