from dataclasses import dataclass
from Options import DefaultOnToggle, ItemSet, Range, NamedRange, Toggle, DeathLink, Choice, PerGameCommonOptions, OptionSet, OptionGroup
from .Items import item_moveset_all, item_transfo

class ToppinCount(Range):
    """
    Number of toppins shuffled into the item pool
    """
    display_name = "Toppin Count"
    range_start = 0
    range_end = 150
    default = 95

class Floor1Door(Range):
    """
    Number of Toppins required to fight the Floor 1 Boss
    """
    display_name = "Floor 1 Boss Toppins"
    range_start = 0
    range_end = 150
    default = 10

class Floor2Door(Range):
    """
    Number of Toppins required to fight the Floor 2 Boss
    """
    display_name = "Floor 2 Boss Toppins"
    range_start = 0
    range_end = 150
    default = 15

class Floor3Door(Range):
    """
    Number of Toppins required to fight the Floor 3 Boss
    """
    display_name = "Floor 3 Boss Toppins"
    range_start = 0
    range_end = 150
    default = 20

class Floor4Door(Range):
    """
    Number of Toppins required to fight the Floor 4 Boss
    """
    display_name = "Floor 4 Boss Toppins"
    range_start = 0
    range_end = 150
    default = 20

class Floor5Door(Range):
    """
    Number of Toppins required to fight the Floor 5 Boss
    """
    display_name = "Floor 5 Boss Toppins"
    range_start = 0
    range_end = 150
    default = 21

class TreasureChecks(Toggle):
    """
    Adds the game's 19 Treasures to the pool as locations
    """
    display_name = "Treasures Award Checks"

class SecretChecks(Toggle):
    """
    Adds the game's 57 secrets to the pool as locations
    """
    display_name = "Secrets Award Checks"

class SRankChecks(DefaultOnToggle):
    """
    Adds the game's 24 S Ranks to the pool as locations
    Obtaining a P Rank in a level will also check its corresponding S Rank location
    """
    display_name = "S Ranks Award Checks"

class PRankChecks(Toggle):
    """
    Adds the game's 24 P Ranks to the pool as locations
    """
    display_name = "P Ranks Award Checks"

class ChefTaskChecks(Toggle):
    """
    Adds the game's 72 Chef Tasks (achievements) to the pool as locations
    """
    display_name = "Chef Tasks Award Checks"

class ShuffleBossKeys(DefaultOnToggle):
    """
    On: Shuffle Boss Keys into the item pool
    Off: Keep Boss Keys in their normal spots
    """
    display_name = "Shuffle Boss Keys"

class CharacterToPlay(Choice):
    """
    Choose your character!
    """
    display_name = "Character"
    option_Peppino = 0
    option_The_Noise = 1
    option_Swap = 2
    alias_Pep = 0
    alias_Noise = 1
    alias_Swap_Mode = 2
    alias_Both = 2
    default = 0

class LockMovesList(OptionSet):
    """
    Which moves should be randomized?
    """
    display_name = "Moves to Randomize"
    default = item_moveset_all

class LockTransfo(Toggle):
    """
    Locks transformations until a certain item is received
    """
    display_name = "Randomize Transfos"

class LockTransfoList(OptionSet):
    """
    Which transformations should be randomized?
    """
    display_name = "Transfos to Randomize"
    #default = **item_transfo

class RandomizeLevels(Toggle):
    """
    Shuffle level entrances around the Hub
    """
    display_name = "Shuffle Level Gates"

class RandomizeBosses(Toggle):
    """
    Shuffle bosses (except Pizzaface) between floors
    """
    display_name = "Shuffle Boss Gates"

class OpenWorld(Toggle):
    """
    Unlock all floors from the start, making more levels accessible from the start
    """
    display_name = "Open World"

class BossUnlockMode(Choice):
    """
    Toppins: Bosses are unlocked by collecting enough Toppins and paying Mr. Stick/Noisette
    All Levels: Bosses are unlocked by completing every level on the floor
    """
    display_name = "Boss Unlock Mode"
    option_Toppins = 0
    option_All_Levels = 1
    alias_Levels = 1
    default = 0

class BonusLadders(NamedRange):
    """
    Add bonus ladders to Hub to make accessing levels easier.
    Floors up to and including the selected floor number are affected.
    Set to 0 to disable bonus ladders.
    """
    display_name = "Bonus Ladders"
    range_start = 0
    range_end = 5
    default = 2
    special_range_names = { "Disabled": 0 }

class TrapPercentage(Range):
    """
    Set a percentage of how many filler items are replaced with traps here
    """
    range_start = 0
    range_end = 100
    default = 10

class EnabledTraps(ItemSet):
    """
    A trap sent to you can be any of these
    """
    verify_item_name = True
    default = [
        "Clown Trap",
        "One-Minute Timer",
        "Pizzaface",
        "Slow Trap",
        "Oktoberfest!"
    ]

class Jumpscare(Toggle):
    """
    Replace the Oktoberfest trap with a jumpscare. Not for the faint of heart!
    """
    display_name = "Replace Oktoberfest with Jumpscare"