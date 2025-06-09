from worlds.AutoWorld import World, WebWorld
from BaseClasses import Tutorial
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

    setup_en = Tutorial(
        "MultiWorld Setup Guide",
        "A guide to setting up Pizza Tower for Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Skizzers"]
    )

class PizzaTowerWorld(World):
    """
    Down-on-his-luck pizza chef Peppino Spaghetti and his restaurant are threatened by a sentient floating pizza... and this time
    all of his abilities are gone, too! Climb up and bring down the Pizza Tower to save your restaurant in this cheesy, saucy,
    Wario Land 4-inspired platformer!
    """
    game = "Pizza Tower"
    topology_present = True
    options_dataclass = PTOptions
    options: PTOptions
    webworld = PizzaTowerWebWorld

    toppin_number: int
    starting_moves: int

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

        if not self.options.shuffle_boss_keys and not self.options.open_world:
            locations_to_fill -= 4
        #disable for now; unlocking laps is kind of annoying
        #pizza_itempool.append(self.create_item("Lap 2 Portals"))

        #define moves per character
        shared_moves = [
            "Mach 4",
            "Uppercut",
            "Superjump",
            "Grab",
            "Taunt",
            "Supertaunt",
            "Bodyslam",
            "Breakdance"
        ]
        pep_moves = [
            "Wallclimb",
            "Double Jump",
            "Rat Kick",
            "none", #placeholder for missing move
            "Spin Attack"
        ]
        noise_moves = [
            "Wallbounce",
            "Tornado",
            "Crusher",
            "Bomb"
        ]
        total_moves = shared_moves + pep_moves + noise_moves

        if self.options.do_move_rando:
            for move in self.options.move_rando_list:
                if self.options.character != 1 and (move in pep_moves or move in shared_moves):
                    pizza_itempool.append(self.create_item(move))
                elif self.options.character != 0 and (move in noise_moves or move in shared_moves):
                    pizza_itempool.append(self.create_item(move))
        
        self.starting_moves = 0
        for i in range(len(total_moves)):
            self.starting_moves = self.starting_moves << 1
            if total_moves[i] not in self.options.move_rando_list or not self.options.do_move_rando:
                self.starting_moves |= 1
        
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
        one_percent_trap = (locations_to_fill - len(pizza_itempool)) * (int(self.options.trap_percentage) / 100) / 100
        for i in range(floor(one_percent_trap * 10)):
            pizza_itempool.append(self.create_item("Ghost Trap"))
        for i in range(floor(one_percent_trap * 10)):
            pizza_itempool.append(self.create_item("Timer Trap"))
        for i in range(floor(one_percent_trap * 20)):
            if self.options.jumpscare:
                pizza_itempool.append(self.create_item("Jumpscare"))
            else:
                pizza_itempool.append(self.create_item("Oktoberfest!"))
        for i in range(floor(one_percent_trap * 20)):
            pizza_itempool.append(self.create_item("Granny Trap"))
        for i in range(floor(one_percent_trap * 20)):
            pizza_itempool.append(self.create_item("Fake Santa Trap"))
        for i in range(floor(one_percent_trap * 20)):
            pizza_itempool.append(self.create_item("Clown Trap"))
        
        one_percent_filler = (locations_to_fill - len(pizza_itempool)) / 100
        for i in range(floor(one_percent_filler * 3)):
            pizza_itempool.append(self.create_item("Permanent 100 Points"))
        for i in range(floor(one_percent_filler * 7)):
            pizza_itempool.append(self.create_item("Permanent 50 Points"))
        for i in range(floor(one_percent_filler * 20)):
            pizza_itempool.append(self.create_item("Cross Buff"))
        for i in range(floor(one_percent_filler * 10)):
            pizza_itempool.append(self.create_item("Pizza Shield"))
        for i in range(floor(one_percent_filler * 5)):
            pizza_itempool.append(self.create_item("Nothing"))
        for i in range(floor(one_percent_filler * 40)):
            pizza_itempool.append(self.create_item("Permanent 10 Points"))
        for i in range(locations_to_fill - len(pizza_itempool)):
            pizza_itempool.append(self.create_item("Primo Burg"))

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
            "bonus_ladders": int(self.options.bonus_ladders),
            "character": int(self.options.character.value),
            "death_link": bool(self.options.death_link),
            "starting_moves": int(self.starting_moves),
            "treasure_checks": bool(self.options.treasure_checks),
            "srank_checks": bool(self.options.srank_checks),
            "prank_checks": bool(self.options.prank_checks),
            "cheftask_checks": bool(self.options.cheftask_checks),
            "difficulty": bool(self.options.difficulty)
        }