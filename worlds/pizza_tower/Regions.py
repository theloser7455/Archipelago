from BaseClasses import Region, Location, MultiWorld, Entrance
from AutoWorld import World
from .Locations import PTLocation, pt_locations
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
    "Complete",
    "S Rank"
]

bosses_list = [ #pizzaface is handled separately because he does not give a rank
    "Pepperman",
    "The Vigilante",
    "The Noise",
    "Fake Peppino"
]

bosses_checks = [
    "Defeated",
    "S Rank"
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

def create_regions(player: int, world: MultiWorld):
    tower_regions: list[Region] = []

    tower_regions.append(Region("Menu", player, world, None))

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

    world.regions += tower_regions

    #get connected!tm
    world.get_region("Menu", player).connect(world.get_region("Floor 1 Tower Lobby", player))

    #connect floors to each other
    for i in range(4):
        world.get_region(floors_list[i], player).connect(world.get_region(floors_list[i+1], player))

    #connect floors to levels
    world.get_region("Floor 1 Tower Lobby", player).connect(world.get_region("Tutorial", player))
    for i in range(len(levels_list)):
        world.get_region(floors_list[i//4], player).connect(world.get_region(levels_list[i], player))

    #connect floors to bosses
    for i in range(4):
        world.get_region(floors_list[i], player).connect(world.get_region(bosses_list[i], player))
    world.get_region("Floor 5 Staff Only", player).connect(world.get_region("Pizzaface", player))

    world.get_region("Pizzaface", player).connect(world.get_region("The Crumbling Tower of Pizza", player))