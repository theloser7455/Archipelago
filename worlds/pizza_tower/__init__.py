from worlds.AutoWorld import World, WebWorld
from BaseClasses import Tutorial
from .Items import PTItem, pt_items, get_item_from_category, pt_item_groups
from .Locations import PTLocation, pt_locations, pt_location_groups
from .Options import PTOptions, pt_option_groups, pt_option_presets
from .Regions import create_regions
from .Rules import set_rules
from math import floor
from typing import Any

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

def external_from_internal(name: str):
    aliases = {
        "entrance" : "John Gutter",
        "medieval" : "Pizzascape",
        "ruin" : "Ancient Cheese",
        "dungeon" : "Bloodsauce Dungeon",
        "badland" : "Oregano Desert",
        "graveyard" : "Wasteyard",
        "farm" : "Fun Farm",
        "saloon" : "Fastfood Saloon",
        "plage" : "Crust Cove",
        "forest" : "Gnome Forest",
        "space" : "Deep-Dish 9",
        "minigolf" : "GOLF",
        "street" : "The Pig City",
        "industrial" : "Peppibot Factory",
        "sewer" : "Oh Shit!",
        "freezer" : "Freezerator",
        "chateau" : "Pizzascare",
        "kidsparty" : "Don't Make A Sound",
        "war" : "WAR",
        "boss_pepperman" : "Pepperman",
        "boss_vigilante" : "The Vigilante",
        "boss_noise" : "The Noise",
        "boss_fakepep" : "Fake Peppino"
    }
    if "1" in name:
        return aliases[name.replace("1", "")] + " Secret 1"
    if "2" in name:
        return aliases[name.replace("2", "")] + " Secret 2"
    if "3" in name:
        return aliases[name.replace("3", "")] + " Secret 3"
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
    pumpkin_number: int

    level_map: dict[str, str]
    boss_map: dict[str, str]
    secret_map: dict[str, str]

    item_name_to_id = {name: data[1] for name, data in pt_items.items()}
    location_name_to_id = pt_locations

    item_name_groups = pt_item_groups # not extremely important for this world but it's here for completeness
    location_name_groups = pt_location_groups

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]: #UT support function that causes a re-generation
        return slot_data #we don't need to do any modification to the slot data, so just return it

            #"rando_levels": {internal_from_external(level): internal_from_external(self.level_map[level]) for level in self.level_map},
            #"rando_bosses": {internal_from_external(boss): internal_from_external(self.boss_map[boss]) for boss in self.boss_map},
            #"rando_secrets": {internal_from_external(sec): internal_from_external(self.secret_map[sec]) for sec in self.secret_map},

    def generate_early(self):
        re_gen_passthrough = getattr(self.multiworld,"re_gen_passthrough",{})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            slot_data = re_gen_passthrough[self.game]
            self.level_map = {external_from_internal(level): external_from_internal(slot_data["rando_levels"][level]) for level in slot_data["rando_levels"]}
            self.boss_map = {external_from_internal(boss): external_from_internal(slot_data["rando_bosses"][boss]) for boss in slot_data["rando_bosses"]}
            self.secret_map = {external_from_internal(sec): external_from_internal(slot_data["rando_secrets"][sec]) for sec in slot_data["rando_secrets"]}
            if self.options.character != 0:
                self.boss_map = {(k if k != "The Noise" else "The Doise"):(v if v != "The Noise" else "The Doise") for k,v in self.boss_map.items()}
        else:
            self.level_map = {}
            self.boss_map = {}
            self.secret_map = {}

    def create_item(self, item: str) -> PTItem:
        return PTItem(item, pt_items[item][2], pt_items[item][1], self.player)

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
        if self.options.pumpkin_checks:
            locations_to_fill += 30
            if self.options.cheftask_checks: locations_to_fill += 2 #tricky treat chef tasks
        if self.options.character == 0:
            locations_to_fill += 7 #2 tutorial checks and its 5 toppins
        elif self.options.character == 1:
            locations_to_fill += 2 #no toppins in noise tutorial
        #no tutorial in swap mode, so no tutorial checks

        if not self.options.shuffle_boss_keys and not self.options.open_world:
            locations_to_fill -= 4
        if self.options.shuffle_lap2:
            pizza_itempool.append(self.create_item("Lap 2 Portals"))

        pep_moves = get_item_from_category("Moves Peppino")
        noise_moves = get_item_from_category("Moves Noise")
        shared_moves = get_item_from_category("Moves Shared")
        if self.options.do_move_rando:
            for move in self.options.move_rando_list:
                if self.options.character != 1 and (move in pep_moves or move in shared_moves):
                    pizza_itempool.append(self.create_item(move))
                elif self.options.character != 0 and (move in noise_moves or move in shared_moves):
                    pizza_itempool.append(self.create_item(move))
        
        total_moves = shared_moves + pep_moves + noise_moves
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

        #add pumpkins, if we can
        if self.options.pumpkin_checks:
            for i in range(self.options.pumpkin_count):
                if locations_to_fill <= len(pizza_itempool):
                    break
                pizza_itempool.append(self.create_item("Pumpkin"))
                self.pumpkin_number = i+1
        
        #add clothes, if there's room
        if self.options.clothing_filler:
            total_clothes = get_item_from_category("Clothes Shared")
            if self.options.character != 1:
                total_clothes += get_item_from_category("Clothes Peppino")
            if self.options.character != 0:
                total_clothes += get_item_from_category("Clothes Noise")
            
            for clothing in total_clothes:
                if locations_to_fill <= len(pizza_itempool):
                    break
                pizza_itempool.append(self.create_item(clothing))

        #add traps
        one_percent_trap = (locations_to_fill - len(pizza_itempool)) * (int(self.options.trap_percentage) / 100) / 100
        total_trapweights = 0
        for trapweight in self.options.trap_weights:
            total_trapweights += self.options.trap_weights[trapweight]
        trapweight_mult = 100 / total_trapweights
        for trap in get_item_from_category("Trap"):
            get_trapweight = trap
            if (trap == "Oktoberfest!" and self.options.jumpscare) or (trap == "Jumpscare" and not self.options.jumpscare):
                continue
            if trap == "Jumpscare":
                get_trapweight = "Oktoberfest!"
            for i in range(floor(one_percent_trap * (self.options.trap_weights[get_trapweight] * trapweight_mult))):
                pizza_itempool.append(self.create_item(trap))
        
        #add filler
        one_percent_filler = (locations_to_fill - len(pizza_itempool)) / 100
        total_fillerweights = 0
        for fillerweight in self.options.filler_weights:
            total_fillerweights += self.options.filler_weights[fillerweight]
        fillerweight_mult = 100 / total_fillerweights
        for filler in get_item_from_category("Filler"):
            for i in range(floor(one_percent_filler * (self.options.filler_weights[filler] * fillerweight_mult))):
                pizza_itempool.append(self.create_item(filler))
        
        #if there's still slots left over from rounding fill them with primo burgs
        for i in range(locations_to_fill - len(pizza_itempool)):
            pizza_itempool.append(self.create_item("Primo Burg"))

        self.multiworld.itempool += pizza_itempool

    def set_rules(self):
        set_rules(self.multiworld, self, self.options, self.toppin_number, self.pumpkin_number)
        self.multiworld.completion_condition[self.player] = lambda state: state.can_reach("The Crumbling Tower of Pizza Complete", "Location", self.player)

    def get_filler_item_name(self) -> str:
        weighted_filler = []
        for filler in get_item_from_category("Filler"):
            for i in range(self.options.filler_weights[filler]):
                weighted_filler.append(filler)
        
        return self.random.choice(weighted_filler)

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
            "difficulty": bool(self.options.difficulty),
            "palette_filler": bool(self.options.clothing_filler),
            "secret_checks": bool(self.options.secret_checks),
            "shuffle_lap2": bool(self.options.shuffle_lap2),
            "pumpkin_checks": bool(self.options.pumpkin_checks),
            "pumpkin_count": floor(self.pumpkin_number * (self.options.tricky_treat_cost / 100))
        }