from BaseClasses import Region, Location, MultiWorld, Entrance
from AutoWorld import World
from .Locations import PTLocation, pt_locations
from .Options import PTOptions
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
        region_tut.locations.append(PTLocation(player, check_name, pt_locations[check_name], region_tut))
    tower_regions.append(region_tut)

    for lvl in levels_list:
        check_region = Region(lvl, player, world, None)
        for chk in levels_checks:
            check_name = lvl + " " + chk
            check_region.locations.append(PTLocation(player, check_name, pt_locations[check_name], check_region))
        tower_regions.append(check_region)

    for boss in bosses_list:
        check_region = Region(boss, player, world, None)
        for chk in bosses_checks:
            check_name = lvl + " " + chk
            check_region.locations.append(PTLocation(player, check_name, pt_locations[check_name], check_region))
        tower_regions.append(check_region)

    #odd regions
    region_pface = Region("Pizzaface", player, world)
    region_ctop = Region("The Crumbling Tower of Pizza", player, world)

    #odd locations
    region_pface.locations.append(PTLocation(player, "Pizzaface Defeated", 243, region_pface))
    region_ctop.locations.append(PTLocation(player, "The Crumbling Tower of Pizza Complete", 233, region_ctop))
    region_ctop.locations.append(PTLocation(player, "The Crumbling Tower of Pizza S Rank", 234, region_ctop))
    tower_regions[4].locations.append(PTLocation(player, "Snotty Murdered", 244, tower_regions[4]))

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
            curr_floor.locations.append(PTLocation(player, "Chef Task: S Ranked #" + i, pt_locations["Chef Task: S Ranked #" + i], curr_floor))
            curr_floor.locations.append(PTLocation(player, "Chef Task: P Ranked #" + i, pt_locations["Chef Task: P Ranked #" + i], curr_floor))

    tower_regions.append(region_pface)
    tower_regions.append(region_ctop)

    world.regions += tower_regions

    #connect floors to each other
    for i in range(4):
        world.get_region(floors_list[i], player).connect(world.get_region(floors_list[i+1], player), rule=(lambda state: state.has("Boss Key", i)))

def connect_regions(world: World, multiworld: MultiWorld, player: int, options: PTOptions):
    world.get_region("Menu", player).connect(world.get_region("Floor 1 Tower Lobby", player))

def level_gate_rando(world: World, multiworld: MultiWorld):
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

    return rando_level_order