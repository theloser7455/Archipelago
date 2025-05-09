from worlds.AutoWorld import World, WebWorld
from .Items import PTItem, pt_items
from .Locations import PTLocation, pt_locations
from .Options import PTOptions, pt_option_groups, pt_option_presets
from .Regions import create_regions
from .Rules import set_rules

class PizzaTowerWebWorld(WebWorld):
    theme = "stone"
    option_groups = pt_option_groups
    option_presets = pt_option_presets

class PizzaTowerWorld(World):
    """It's Pizza Time!"""
    game = "Pizza Tower"
    topology_present = False
    options_dataclass = PTOptions
    options: PTOptions
    webworld = PizzaTowerWebWorld

    toppin_number: int

    level_map: dict[str, str]
    boss_map: dict[str, str]
    secret_map: dict[str, str]

    item_name_to_id = {name: data[0] for name, data in pt_items.items()}
    location_name_to_id = pt_locations

    def create_item(self, item: str) -> PTItem:
        return PTItem(item, pt_items[item][1], pt_items[item][0], self.player)

    def create_regions(self):
        create_regions(self.player, self.multiworld, self.options)

    def create_items(self):
        pizza_itempool = []

        locations_to_fill = 121
        if self.options.secret_checks: locations_to_fill += 57
        if self.options.treasure_checks: locations_to_fill += 19
        if self.options.srank_checks: locations_to_fill += 24
        if self.options.prank_checks: locations_to_fill += 24
        if self.options.cheftask_checks: locations_to_fill += 72
        if self.options.character == 0:
            locations_to_fill += 7 #2 tutorial checks and its 5 toppins
        elif self.options.character == 1:
            locations_to_fill += 2 #no toppins in noise tutorial
        #no tutorial in swap mode, so no tutorial checks

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
        if self.options.character != 1:
            pizza_itempool.append(self.create_item("Peppino: Wallclimb"))
            pizza_itempool.append(self.create_item("Peppino: Dive"))
            pizza_itempool.append(self.create_item("Gustavo & Brick: Double Jump"))
            pizza_itempool.append(self.create_item("Gustavo & Brick: Rat Kick"))
            pizza_itempool.append(self.create_item("Gustavo & Brick: Wall Jump"))
            pizza_itempool.append(self.create_item("Gustavo: Spin Attack"))

        #noise's moves
        if self.options.character != 0:
            pizza_itempool.append(self.create_item("Noise: Wallbounce"))
            pizza_itempool.append(self.create_item("Noise: Tornado"))
            pizza_itempool.append(self.create_item("Noise: Crusher"))
        
        #add keys
        if not self.options.open_world:
            if self.options.shuffle_boss_keys:
                for i in range(4): pizza_itempool.append(self.create_item("Boss Key"))
            else:
                self.multiworld.get_location("Pepperman Defeated").place_locked_item(self.create_item("Boss Key"))
                self.multiworld.get_location("The Vigilante Defeated").place_locked_item(self.create_item("Boss Key"))
                if self.options.character == 0: self.multiworld.get_location("The Noise Defeated").place_locked_item(self.create_item("Boss Key"))
                else: self.multiworld.get_location("The Doise Defeated").place_locked_item(self.create_item("Boss Key"))
                self.multiworld.get_location("Fake Peppino Defeated").place_locked_item(self.create_item("Boss Key"))
        
        #add toppins, if we can
        if self.options.toppin_count > (locations_to_fill - len(pizza_itempool)):
            self.toppin_number = (locations_to_fill - len(pizza_itempool))
            for i in range(locations_to_fill - len(pizza_itempool)): pizza_itempool.append(self.create_item("Toppin"))
        else:
            self.toppin_number = self.options.toppin_count
            for i in range(self.options.toppin_count): pizza_itempool.append(self.create_item("Toppin"))
        
        #fill the rest of the pool with points. get around to putting more stuff in the pool later
        for i in range(locations_to_fill - len(pizza_itempool)): pizza_itempool.append(self.create_item("1000 Points"))

        self.multiworld.itempool += pizza_itempool

    def set_rules(self):
        set_rules(self.multiworld, self, self.options, self.toppin_number)
        self.multiworld.completion_condition[self.player] = lambda state: state.can_reach("The Crumbling Tower of Pizza Complete", "Location", self.player)