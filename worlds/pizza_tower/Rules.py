from AutoWorld import World, MultiWorld
from BaseClasses import Location, Region
from .Locations import PTLocation
from .Options import PTOptions

def set_rules(world: World, multiworld: MultiWorld, options: PTOptions):
    player: int = world.player

    def must_unlock(transfo):
        return options.lock_transfo and transfo in options.lock_transfo_list


    #lots of logic checks fall under these categories
    peppino_requires_upward_mobility = lambda state: state.has_any(["Superjump", "Peppino: Wallclimb"], player)
    peppino_requires_downward_mobility = lambda state: state.has_any(["Bodyslam", "Peppino: Dive"], player)
    gustavo_requires_upward_mobility = lambda state: state.has_all(["Gustavo & Brick: Double Jump", "Gustavo & Brick: Wall Jump"], player)
    noise_requires_upward_mobility = lambda state: state.has_any(["Superjump", "Noise: Crusher"], player)
    noise_requires_downward_mobility = lambda state: state.has_any(["Bodyslam", "Noise: Tornado"], player)
    requires_any_grab = lambda state: state.has_any(["Grab", "Uppercut"], player)

    #lambda function aliases for easier reading
    requires_uppercut = lambda state: state.has("Uppercut", player)
    requires_grab = lambda state: state.has("Uppercut", player)
    requires_superjump = lambda state: state.has("Superjump", player)
    requires_taunt = lambda state: state.has("Taunt", player)
    requires_supertaunt = lambda state: state.has("Supertaunt", player)
    peppino_requires_wallclimb = lambda state: state.has("Peppino: Wallclimb", player)
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

    pt_peppino_rules_simple = {
    #John Gutter
        "John Gutter Complete": peppino_requires_upward_mobility,
        "John Gutter Mushroom Toppin": peppino_requires_upward_mobility or requires_uppercut,
        "John Gutter Cheese Toppin": peppino_requires_upward_mobility or requires_uppercut,
        "John Gutter Tomato Toppin": peppino_requires_upward_mobility or requires_uppercut,
        "John Gutter Sausage Toppin": peppino_requires_upward_mobility,
        "John Gutter Pineapple Toppin": peppino_requires_upward_mobility,

    #Pizzascape
        "Pizzascape Complete": requires_any_grab and peppino_requires_wallclimb and requires_knight,
        "Pizzascape Mushroom Toppin": None,
        "Pizzascape Cheese Toppin": None,
        "Pizzascape Tomato Toppin": requires_any_grab and requires_knight,
        "Pizzascape Sausage Toppin": requires_any_grab and requires_knight,
        "Pizzascape Pineapple Toppin": requires_any_grab and requires_knight,

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
        "Oregano Desert Complete": peppino_requires_wallclimb and requires_firemouth,
        "Oregano Desert Mushroom Toppin": peppino_requires_upward_mobility or requires_uppercut,
        "Oregano Desert Cheese Toppin": peppino_requires_upward_mobility and requires_firemouth,
        "Oregano Desert Tomato Toppin": peppino_requires_wallclimb and requires_firemouth,
        "Oregano Desert Sausage Toppin": peppino_requires_wallclimb and requires_firemouth,
        "Oregano Desert Pineapple Toppin": peppino_requires_wallclimb and requires_firemouth,

    #Wasteyard
        "Wasteyard Complete": peppino_requires_upward_mobility and requires_ghost,
        "Wasteyard Mushroom Toppin": None,
        "Wasteyard Cheese Toppin": peppino_requires_upward_mobility and requires_ghost,
        "Wasteyard Tomato Toppin": peppino_requires_upward_mobility and requires_ghost,
        "Wasteyard Sausage Toppin": peppino_requires_upward_mobility and requires_ghost,
        "Wasteyard Pineapple Toppin": peppino_requires_upward_mobility and requires_ghost,

    #Fun Farm
        "Fun Farm Complete": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_mort,
        "Fun Farm Mushroom Toppin": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or requires_uppercut) and requires_mort,
        "Fun Farm Cheese Toppin": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or requires_uppercut) and requires_mort,
        "Fun Farm Tomato Toppin": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_mort,
        "Fun Farm Sausage Toppin": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_mort,
        "Fun Farm Pineapple Toppin": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_mort,

    #Fastfood Saloon
        "Fastfood Saloon Complete": requires_superjump and requires_grab and peppino_requires_wallclimb and requires_weenie,
        "Fastfood Saloon Mushroom Toppin": requires_superjump,
        "Fastfood Saloon Cheese Toppin": requires_superjump and requires_grab and requires_weenie,
        "Fastfood Saloon Tomato Toppin": requires_superjump and peppino_requires_wallclimb and requires_grab and requires_weenie,
        "Fastfood Saloon Sausage Toppin": requires_superjump and peppino_requires_wallclimb and requires_grab and requires_weenie,
        "Fastfood Saloon Pineapple Toppin": requires_superjump and peppino_requires_wallclimb and requires_grab and requires_weenie,

    #Crust Cove
        "Crust Cove Complete": peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)) and requires_barrel,
        "Crust Cove Mushroom Toppin": peppino_requires_upward_mobility,
        "Crust Cove Cheese Toppin": peppino_requires_upward_mobility and requires_barrel,
        "Crust Cove Tomato Toppin": peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)) and requires_barrel,
        "Crust Cove Sausage Toppin": peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)) and requires_barrel,
        "Crust Cove Pineapple Toppin": peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)) and requires_barrel,

    #Gnome Forest
        "Gnome Forest Complete": peppino_requires_upward_mobility and peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,
        "Gnome Forest Mushroom Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,
        "Gnome Forest Cheese Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,
        "Gnome Forest Tomato Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,
        "Gnome Forest Sausage Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,
        "Gnome Forest Pineapple Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,

    #Deep-Dish 9
        "Deep-Dish 9 Complete": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,
        "Deep-Dish 9 Mushroom Toppin": peppino_requires_downward_mobility and (peppino_requires_upward_mobility or requires_antigrav) and requires_rocket,
        "Deep-Dish 9 Cheese Toppin": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,
        "Deep-Dish 9 Tomato Toppin": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,
        "Deep-Dish 9 Sausage Toppin": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,
        "Deep-Dish 9 Pineapple Toppin": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,

    #GOLF
        "GOLF Complete": (peppino_requires_upward_mobility or requires_uppercut) and requires_ball,
        "GOLF Mushroom Toppin": None,
        "GOLF Cheese Toppin": requires_ball,
        "GOLF Tomato Toppin": (peppino_requires_upward_mobility or requires_uppercut) and requires_ball,
        "GOLF Sausage Toppin": (peppino_requires_upward_mobility or requires_uppercut) and requires_ball,
        "GOLF Pineapple Toppin": (peppino_requires_upward_mobility or requires_uppercut) and requires_ball,

    #The Pig City
        "The Pig City Complete": peppino_requires_downward_mobility and gustavo_requires_doublejump,
        "The Pig City Mushroom Toppin": None,
        "The Pig City Cheese Toppin": peppino_requires_upward_mobility,
        "The Pig City Tomato Toppin": peppino_requires_downward_mobility,
        "The Pig City Sausage Toppin": peppino_requires_downward_mobility and gustavo_requires_upward_mobility,
        "The Pig City Pineapple Toppin": peppino_requires_downward_mobility and gustavo_requires_doublejump,

    #Peppibot Factory
        "Peppibot Factory Complete": peppino_requires_wallclimb and peppino_requires_downward_mobility and requires_pizzabox,
        "Peppibot Factory Mushroom Toppin": peppino_requires_upward_mobility,
        "Peppibot Factory Cheese Toppin": peppino_requires_wallclimb,
        "Peppibot Factory Tomato Toppin": peppino_requires_wallclimb,
        "Peppibot Factory Sausage Toppin": peppino_requires_wallclimb and requires_pizzabox,
        "Peppibot Factory Pineapple Toppin": peppino_requires_wallclimb and requires_pizzabox,

    #Oh Shit!
        "Oh Shit! Complete": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,
        "Oh Shit! Mushroom Toppin": requires_stickycheese and peppino_requires_downward_mobility,
        "Oh Shit! Cheese Toppin": requires_stickycheese and peppino_requires_downward_mobility and (peppino_requires_upward_mobility or requires_uppercut),
        "Oh Shit! Tomato Toppin": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,
        "Oh Shit! Sausage Toppin": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,
        "Oh Shit! Pineapple Toppin": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,

    #Freezerator
        "Freezerator Complete": requires_superjump and peppino_requires_downward_mobility and requires_satans,
        "Freezerator Mushroom Toppin": peppino_requires_upward_mobility,
        "Freezerator Cheese Toppin": peppino_requires_upward_mobility,
        "Freezerator Tomato Toppin": requires_superjump and peppino_requires_downward_mobility,
        "Freezerator Sausage Toppin": requires_superjump and peppino_requires_downward_mobility,
        "Freezerator Pineapple Toppin": requires_superjump and peppino_requires_downward_mobility,

    #Pizzascare
        "Pizzascare Complete": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_any_grab and requires_ball,
        "Pizzascare Mushroom Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Pizzascare Cheese Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Pizzascare Tomato Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_any_grab and requires_ball,
        "Pizzascare Sausage Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_any_grab and requires_ball,
        "Pizzascare Pineapple Toppin": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_any_grab and requires_ball,

    #Don't Make a Sound
        "Don't Make a Sound Complete": peppino_requires_wallclimb and requires_any_grab and requires_shotgun,
        "Don't Make a Sound Mushroom Toppin": None,
        "Don't Make a Sound Cheese Toppin": peppino_requires_wallclimb,
        "Don't Make a Sound Tomato Toppin": peppino_requires_wallclimb and peppino_requires_downward_mobility,
        "Don't Make a Sound Sausage Toppin": peppino_requires_wallclimb,
        "Don't Make a Sound Pineapple Toppin": peppino_requires_wallclimb and requires_any_grab and requires_shotgun,

    #WAR
        "WAR Complete": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_rocket,
        "WAR Mushroom Toppin": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility,
        "WAR Cheese Toppin": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility,
        "WAR Tomato Toppin": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "WAR Sausage Toppin": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "WAR Pineapple Toppin": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_rocket,

    #Crumbling Tower of Pizza
        "The Crumbling Tower of Pizza Complete": peppino_requires_wallclimb and requires_shotgun and requires_grab and peppino_requires_downward_mobility and requires_weenie and requires_rocket,

    #Bosses
        "Pepperman Defeated": None,
        "The Vigilante Defeated": requires_grab and requires_revolver,
        "The Noise Defeated": None,
        "Fake Peppino Defeated": None,
        "Pizzaface Defeated": requires_grab and requires_revolver,

    #misc
        "Snotty Murdered": None,
    }

    pt_peppino_tutorial_rules_simple = {
        "Tutorial Complete": peppino_requires_downward_mobility and peppino_requires_wallclimb and requires_superjump and requires_grab,
        "Tutorial Complete in under 2 minutes": peppino_requires_downward_mobility and peppino_requires_wallclimb and requires_superjump and requires_grab,
        "Tutorial Mushroom Toppin": peppino_requires_downward_mobility,
        "Tutorial Cheese Toppin": peppino_requires_downward_mobility and peppino_requires_wallclimb,
        "Tutorial Tomato Toppin": peppino_requires_downward_mobility and peppino_requires_wallclimb,
        "Tutorial Sausage Toppin": peppino_requires_downward_mobility and peppino_requires_wallclimb and requires_superjump,
        "Tutorial Pineapple Toppin": peppino_requires_downward_mobility and peppino_requires_wallclimb and requires_superjump and requires_grab,
    }

    pt_peppino_srank_rules_simple = {
        "John Gutter S Rank": peppino_requires_upward_mobility,
        "Pizzascape S Rank": requires_any_grab and peppino_requires_wallclimb and requires_knight and requires_ball,
        "Ancient Cheese S Rank": requires_any_grab and peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Bloodsauce Dungeon S Rank": peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Oregano Desert S Rank": peppino_requires_wallclimb and peppino_requires_downward_mobility and requires_firemouth,
        "Wasteyard S Rank": peppino_requires_upward_mobility and requires_ghost,
        "Fun Farm S Rank": peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_mort,
        "Fastfood Saloon S Rank": requires_superjump and peppino_requires_wallclimb and requires_grab and requires_weenie,
        "Crust Cove S Rank": requires_taunt and peppino_requires_downward_mobility and (peppino_requires_wallclimb or (requires_superjump and requires_uppercut)) and requires_barrel,
        "Gnome Forest S Rank": peppino_requires_upward_mobility and peppino_requires_downward_mobility and gustavo_requires_upward_mobility and gustavo_requires_attack,
        "Deep-Dish 9 S Rank": peppino_requires_downward_mobility and peppino_requires_upward_mobility and requires_rocket,
        "GOLF S Rank": (peppino_requires_upward_mobility or requires_uppercut) and requires_ball,
        "The Pig City S Rank": peppino_requires_downward_mobility and peppino_requires_upward_mobility and gustavo_requires_upward_mobility,
        "Peppibot Factory S Rank": peppino_requires_wallclimb and requires_any_grab and peppino_requires_downward_mobility and requires_pizzabox,
        "Oh Shit! S Rank": requires_stickycheese and peppino_requires_downward_mobility and peppino_requires_wallclimb,
        "Freezerator S Rank": requires_superjump and peppino_requires_downward_mobility and requires_satans,
        "Pizzascare S Rank": peppino_requires_wallclimb and peppino_requires_downward_mobility and requires_any_grab and requires_ball,
        "Don't Make a Sound S Rank": peppino_requires_wallclimb and requires_any_grab and requires_shotgun,
        "WAR S Rank": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_rocket,
        "The Crumbling Tower of Pizza S Rank": peppino_requires_wallclimb and requires_shotgun and requires_grab and peppino_requires_downward_mobility and requires_weenie and requires_rocket,
        "Pepperman S Rank": None,
        "The Vigilante S Rank": requires_grab and requires_revolver,
        "The Noise S Rank": None,
        "Fake Peppino S Rank": None,
    }

    pt_peppino_secret_rules_simple = { #secrets are checked when player enters; they do not have to exit
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

    pt_peppino_treasure_rules_simple = {
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
        "Chef Task: Thrill Seeker": requires_any_grab and peppino_requires_upward_mobility and peppino_requires_downward_mobility,
        "Chef Task: Volleybomb": None,
        "Chef Task: Delicacy": None,

        #Bloodsauce Dungeon
        "Chef Task: Eruption Man": peppino_requires_downward_mobility and requires_superjump,
        "Chef Task: Very Very Hot Sauce": peppino_requires_downward_mobility and peppino_requires_upward_mobility,
        "Chef Task: Unsliced Pizzaman": peppino_requires_downward_mobility and peppino_requires_upward_mobility,

        #Oregano Desert
        "Chef Task: Peppino's Rain Dance": peppino_requires_upward_mobility or requires_uppercut,
        "Chef Task: Unnecessary Violence": peppino_requires_wallclimb and requires_firemouth,
        "Chef Task: Alien Cow": peppino_requires_wallclimb and requires_firemouth,

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
        "Chef Task: Haunted Playground": 381,
        "Chef Task: Skullsplitter": 382,
        "Chef Task: Cross to Bare": 383,

        #Don't Make a Sound
        "Chef Task: Let Them Sleep": peppino_requires_wallclimb and requires_any_grab and requires_shotgun,
        "Chef Task: Jumpspared": peppino_requires_wallclimb and requires_any_grab and requires_shotgun,
        "Chef Task: And This... Is My Gun on a Stick!": peppino_requires_wallclimb and requires_any_grab and requires_shotgun,

        #WAR
        "Chef Task: Trip to the Warzone": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_rocket,
        "Chef Task: Sharpshooter": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_rocket,
        "Chef Task: Decorated Veteran": requires_any_grab and requires_shotgun and peppino_requires_upward_mobility and peppino_requires_downward_mobility and requires_rocket,

        #Floor Tasks
        "Chef Task: S Ranked #1": 390,
        "Chef Task: P Ranked #1": 391,
        "Chef Task: S Ranked #2": 392,
        "Chef Task: P Ranked #2": 393,
        "Chef Task: S Ranked #3": 394,
        "Chef Task: P Ranked #3": 395,
        "Chef Task: S Ranked #4": 396,
        "Chef Task: P Ranked #4": 397,
        "Chef Task: S Ranked #5": 398,
        "Chef Task: P Ranked #5": 399,

        #Boss Tasks
        "Chef Task: The Critic": 400,
        "Chef Task: The Ugly": 401,
        "Chef Task: Denoise": 402,
        "Chef Task: Faker": 403,
        "Chef Task: Face-Off": 404
    }

    for check in pt_rules:
        multiworld.get_location(check, player).access_rule = pt_rules[check]

    multiworld.completion_condition[player] = lambda state: state.can_reach("The Crumbling Tower of Pizza Complete", "Location", player)