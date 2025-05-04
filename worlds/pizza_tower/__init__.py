from worlds.AutoWorld import World, WebWorld, Region
from BaseClasses import MultiWorld
from .Items import PTItem, pt_items
from .Locations import PTLocation, pt_locations
from .Options import PTOptions
from .Regions import create_regions
from .Rules import set_rules
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

    def create_item(self, item: str) -> PTItem:
        return PTItem(item, pt_items[item][1], pt_items[item][0], self.player)

    def create_regions(self):
        create_regions(self.player, self.multiworld)

    def create_items(self):
        pizza_itempool = []

        locations_to_fill = 152

        #shared moves
        pizza_itempool.append(self.create_item("Mach 4"))
        pizza_itempool.append(self.create_item("Uppercut"))
        pizza_itempool.append(self.create_item("Superjump"))
        pizza_itempool.append(self.create_item("Grab"))
        pizza_itempool.append(self.create_item("Taunt"))
        pizza_itempool.append(self.create_item("Supertaunt"))
        pizza_itempool.append(self.create_item("Bodyslam"))
        pizza_itempool.append(self.create_item("Breakdance"))

        #peppino's moves (and gus + brick)
        pizza_itempool.append(self.create_item("Peppino: Wallclimb"))
        pizza_itempool.append(self.create_item("Peppino: Dive"))
        pizza_itempool.append(self.create_item("Gustavo & Brick: Double Jump"))
        pizza_itempool.append(self.create_item("Gustavo & Brick: Rat Kick"))
        pizza_itempool.append(self.create_item("Gustavo & Brick: Walljump"))
        pizza_itempool.append(self.create_item("Gustavo: Spin Attack"))

        #add keys and toppins
        for i in range(4): pizza_itempool.append(self.create_item("Boss Key"))
        for i in range(95): pizza_itempool.append(self.create_item("Toppin"))

        #fill the rest of the pool with points. get around to putting more stuff in the pool later
        for i in range(locations_to_fill - len(pizza_itempool)): pizza_itempool.append(self.create_item("1000 Points"))

        self.multiworld.itempool += pizza_itempool

    def set_rules(self):
        set_rules(self, self.multiworld)