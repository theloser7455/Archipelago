from worlds.AutoWorld import World, WebWorld, Region
from .Items import PTItem, item_list
from .Locations import PTLocation, pt_locations
from .Options import PTOptions
from .Regions import create_regions
import typing

class PizzaTowerWebWorld(WebWorld):
    theme = "stone"
    #TODO: make this better when the world implementation actually gets good

class PizzaTowerWorld(World):
    """It's Pizza Time!"""
    game = "Pizza Tower"
    topology_present = False
    options_dataclass = PTOptions
    options: PTOptions

    def create_items(self):
        pizzaitempool = []

        self.multiworld.itempool += pizzaitempool