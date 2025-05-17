from worlds.AutoWorld import World, WebWorld
from .Items import PTItem, pt_items
from .Locations import PTLocation, pt_locations
from .Options import PTOptions, pt_option_groups, pt_option_presets
from .Regions import create_regions
from .Rules import set_rules
from math import floor

def internal_from_external(name: str):
    aliases = {
        "John Gutter": "entrance",
        "Pizzascape": "medieval",
        "Ancient Cheese": "ruin",
        "Bloodsauce Dungeon": "dungeon",
        "Oregano Desert": "badland",
        "Wasteyard": "graveyard",
        "Fun Farm": "farm",
        "Fastfood Saloon": "saloon",
        "Crust Cove": "plage",
        "Gnome Forest": "forest",
        "Deep-Dish 9": "space",
        "GOLF": "minigolf",
        "The Pig City": "street",
        "Peppibot Factory": "industrial",
        "Oh Shit!": "sewer",
        "Freezerator": "freezer",
        "Pizzascare": "chateau",
        "Don't Make A Sound": "kidsparty",
        "WAR": "war",
        "Pepperman": "boss_pepperman",
        "The Vigilante": "boss_vigilante",
        "The Noise": "boss_noise",
        "The Doise": "boss_noise",
        "Fake Peppino": "boss_fakepep"
    }
    if "Secret 1" in name:
        return aliases[name.replace(" Secret 1", "")] + "1"
    if "Secret 2" in name:
        return aliases[name.replace(" Secret 2", "")] + "2"
    if "Secret 3" in name:
        return aliases[name.replace(" Secret 3", "")] + "3"
    return aliases[name]

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

        #disable for now; unlocking laps is kind of annoying
        #pizza_itempool.append(self.create_item("Lap 2 Portals"))

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
            pizza_itempool.append(self.create_item("Gustavo & Brick: Double Jump"))
            pizza_itempool.append(self.create_item("Gustavo & Brick: Rat Kick"))
            pizza_itempool.append(self.create_item("Gustavo: Spin Attack"))

        #noise's moves
        if self.options.character != 0:
            pizza_itempool.append(self.create_item("Noise: Wallbounce"))
            pizza_itempool.append(self.create_item("Noise: Tornado"))
            pizza_itempool.append(self.create_item("Noise: Crusher"))
            pizza_itempool.append(self.create_item("Noise: Bomb"))
        
        #add keys
        if not self.options.open_world:
            if self.options.shuffle_boss_keys:
                for i in range(4): pizza_itempool.append(self.create_item("Boss Key"))
            else:
                self.multiworld.get_location("Pepperman Defeated", self.player).place_locked_item(self.create_item("Boss Key"))
                self.multiworld.get_location("The Vigilante Defeated", self.player).place_locked_item(self.create_item("Boss Key"))
                if self.options.character == 0: self.multiworld.get_location("The Noise Defeated", self.player).place_locked_item(self.create_item("Boss Key"))
                else: self.multiworld.get_location("The Doise Defeated", self.player).place_locked_item(self.create_item("Boss Key"))
                self.multiworld.get_location("Fake Peppino Defeated", self.player).place_locked_item(self.create_item("Boss Key"))
        
        #add toppins, if we can
        if self.options.toppin_count > (locations_to_fill - len(pizza_itempool)):
            self.toppin_number = (locations_to_fill - len(pizza_itempool))
            for i in range(locations_to_fill - len(pizza_itempool)): pizza_itempool.append(self.create_item("Toppin"))
        else:
            self.toppin_number = self.options.toppin_count
            for i in range(self.options.toppin_count): pizza_itempool.append(self.create_item("Toppin"))
        
        #add filler
        for i in range(floor((locations_to_fill - len(pizza_itempool)) * (self.options.trap_percentage * 0.01))):
            roll_item = self.random.randint(0, 100)
            if (roll_item <= 10):
                pizza_itempool.append(self.create_item("Pizzaface"))
            elif (roll_item <= 20):
                pizza_itempool.append(self.create_item("Timer Trap"))
            elif (roll_item <= 40):
                if self.options.jumpscare:
                    pizza_itempool.append(self.create_item("Jumpscare"))
                else:
                    pizza_itempool.append(self.create_item("Oktoberfest!"))
            else:
                pizza_itempool.append(self.create_item("Clown Trap"))
        for i in range(locations_to_fill - len(pizza_itempool)):
            roll_item = self.random.randint(0, 100)
            if (roll_item <= 2):
                pizza_itempool.append(self.create_item("Permanent 100 Points"))
            elif (roll_item <= 12):
                pizza_itempool.append(self.create_item("Permanent 50 Points"))
            elif (roll_item <= 22):
                pizza_itempool.append(self.create_item("Pizza Shield"))
            elif (roll_item <= 42):
                pizza_itempool.append(self.create_item("Cross Buff"))
            elif (roll_item <= 70):
                pizza_itempool.append(self.create_item("500 Points"))
            else:
                pizza_itempool.append(self.create_item("Permanent 10 Points"))

        self.multiworld.itempool += pizza_itempool

    def set_rules(self):
        set_rules(self.multiworld, self, self.options, self.toppin_number)
        self.multiworld.completion_condition[self.player] = lambda state: state.can_reach("The Crumbling Tower of Pizza Complete", "Location", self.player)

    def fill_slot_data(self):
        return {
            "floor_1_toppins": floor((self.toppin_number / 100) * self.options.floor_1_cost),
            "floor_2_toppins": floor((self.toppin_number / 100) * self.options.floor_2_cost),
            "floor_3_toppins": floor((self.toppin_number / 100) * self.options.floor_3_cost),
            "floor_4_toppins": floor((self.toppin_number / 100) * self.options.floor_4_cost),
            "floor_5_toppins": floor((self.toppin_number / 100) * self.options.floor_5_cost),
            "rando_levels": {internal_from_external(level): internal_from_external(self.level_map[level]) for level in self.level_map},
            "rando_bosses": {internal_from_external(boss): internal_from_external(self.boss_map[boss]) for boss in self.boss_map},
            "rando_secrets": {internal_from_external(sec): internal_from_external(self.secret_map[sec]) for sec in self.secret_map},
            "open_world": bool(self.options.open_world),
            "bonus_ladders": int(self.options.bonus_ladders)
        }