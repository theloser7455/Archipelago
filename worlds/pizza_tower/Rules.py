from AutoWorld import World, MultiWorld
from BaseClasses import Location, Region
from .Locations import PTLocation
from .Options import PTOptions

def set_rules(world: World, multiworld: MultiWorld, player: int, options: PTOptions):
    multiworld.completion_condition[player] = lambda state: state.can_reach("The Crumbling Tower of Pizza Complete", "Location", player)