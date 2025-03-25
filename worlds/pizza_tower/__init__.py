from worlds.AutoWorld import World, WebWorld
from .Items import PTItem, item_list
from .Locations import PTLocation, locations_data_list
from .Options import PTOptions
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
    item_name_to_id = item_list
    location_name_to_id = {locations_data_list[i]: i for i in location_data_list}