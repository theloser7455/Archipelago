from BaseClasses import Region, MultiWorld
from .Locations import PTLocation, pt_locations
from .Options import PTOptions

def create_regions(player: int, world: MultiWorld, options: PTOptions):
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
    if options.character == 0:
        tutorial_checks += [
            "Mushroom Toppin",
            "Cheese Toppin",
            "Tomato Toppin",
            "Sausage Toppin",
            "Pineapple Toppin",
        ]
    elif options.character == 2:
        tutorial_checks = []

    #create regions and add locations
    for flr in floors_list:
        tower_regions.append(Region(flr, player, world))

    if options.character != 2:
        region_tut = Region("Tutorial", player, world, None)
        for chk in tutorial_checks:
            check_name = "Tutorial " + chk
            new_location = PTLocation(player, check_name, pt_locations[check_name], region_tut)
            region_tut.locations.append(new_location)
        tower_regions.append(region_tut)

    for lvl in levels_list:
        check_region = Region(lvl, player, world, None)
        for chk in levels_checks:
            check_name = lvl + " " + chk
            new_location = PTLocation(player, check_name, pt_locations[check_name], check_region)
            check_region.locations.append(new_location)

        tower_regions.append(check_region)

    for boss in bosses_list:
        check_region = Region(boss, player, world, None)
        for chk in bosses_checks:
            check_name = boss + " " + chk
            new_location = PTLocation(player, check_name, pt_locations[check_name], check_region)
            check_region.locations.append(new_location)
        tower_regions.append(check_region)

    #odd regions
    region_pface = Region("Pizzaface", player, world, None)
    region_ctop = Region("The Crumbling Tower of Pizza", player, world, None)

    #odd locations
    region_pface.locations.append(PTLocation(player, "Pizzaface Defeated", 243, region_pface))

    region_ctop.locations.append(PTLocation(player, "The Crumbling Tower of Pizza Complete", 233, region_ctop))
    if options.srank_checks:
        region_ctop.locations.append(PTLocation(player, "The Crumbling Tower of Pizza S Rank", 234, region_ctop))
    if options.prank_checks:
        region_ctop.locations.append(PTLocation(player, "The Crumbling Tower of Pizza P Rank", 234, region_ctop))
    tower_regions[4].locations.append(PTLocation(player, "Snotty Murdered", 244, tower_regions[4]))

    #must handle chef tasks separately since they aren't common to all levels
    #weird naming here. cheftask_checks is the option bool, cheftasks_checks is the list of task names
    if options.cheftask_checks:
        for i in range(19):
            region_curr = world.get_region(levels_list[i], player)
            for ii in range(3):
                task_index = (i * 3) + ii
                task_name = cheftasks_checks[task_index]
                new_location = PTLocation(player, task_name, pt_locations[task_name], region_curr)
                region_curr.locations.append(new_location)
        for i in range(4):
            task_name = cheftasks_checks[i + 67]
            new_location = PTLocation(player, task_name, pt_locations[task_name], world.get_region(bosses_list[i], player))
            world.get_region(bosses_list[i], player).locations.append(new_location)
        loc_pface_task = PTLocation(player, "Chef Task: Face-Off", 405, region_pface)
        region_pface.locations.append(loc_pface_task)
        for i in range(5):
            curr_floor = world.get_region(floors_list[i], player)
            curr_floor.locations.append(PTLocation(player, "Chef Task: S Ranked #" + (i + 1), pt_locations["Chef Task: S Ranked #" + (i + 1)], curr_floor))
            curr_floor.locations.append(PTLocation(player, "Chef Task: P Ranked #" + (i + 1), pt_locations["Chef Task: P Ranked #" + (i + 1)], curr_floor))

    tower_regions.append(region_pface)
    tower_regions.append(region_ctop)

    world.regions += tower_regions


