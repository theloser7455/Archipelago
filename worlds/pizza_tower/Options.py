from dataclasses import dataclass
from Options import DefaultOnToggle, Range, NamedRange, Toggle, Choice, PerGameCommonOptions, OptionSet, OptionGroup, DeathLink
from .Items import pt_items

class ToppinCount(Range):
    """
    Number of toppins shuffled into the item pool.
    
    May be less than expected if the item pool is too small.
    """
    display_name = "Toppin Count"
    range_start = 0
    range_end = 150
    default = 95

class Floor1Door(Range):
    """
    Percentage of Toppins required to fight the Floor 1 Boss.
    """
    display_name = "Floor 1 Boss Toppins"
    range_start = 0
    range_end = 100
    default = 11

class Floor2Door(Range):
    """
    Percentage of Toppins required to fight the Floor 2 Boss.
    """
    display_name = "Floor 2 Boss Toppins"
    range_start = 0
    range_end = 100
    default = 27

class Floor3Door(Range):
    """
    Percentage of Toppins required to fight the Floor 3 Boss.
    """
    display_name = "Floor 3 Boss Toppins"
    range_start = 0
    range_end = 100
    default = 48

class Floor4Door(Range):
    """
    Percentage of Toppins required to fight the Floor 4 Boss.
    """
    display_name = "Floor 4 Boss Toppins"
    range_start = 0
    range_end = 100
    default = 69

class Floor5Door(Range):
    """
    Percentage of Toppins required to fight the Floor 5 Boss.
    """
    display_name = "Floor 5 Boss Toppins"
    range_start = 0
    range_end = 100
    default = 91

class TreasureChecks(DefaultOnToggle):
    """
    Adds the game's 19 Treasures to the pool as locations.
    """
    display_name = "Treasures Award Checks"

class SecretChecks(DefaultOnToggle):
    """
    Adds the game's 57 Secrets to the pool as locations.
    """
    display_name = "Secrets Award Checks"

class SRankChecks(Toggle):
    """
    Adds the game's 24 S Ranks to the pool as locations.

    Obtaining a P Rank in a level will also check its corresponding S Rank location.
    """
    display_name = "S Ranks Award Checks"

class PRankChecks(Toggle):
    """
    Adds the game's 24 P Ranks to the pool as locations.
    """
    display_name = "P Ranks Award Checks"

class ChefTaskChecks(Toggle):
    """
    Adds the game's 72 Chef Tasks (achievements) to the pool as locations.
    """
    display_name = "Chef Tasks Award Checks"

class ShuffleBossKeys(Toggle):
    """
    On: Shuffle Boss Keys into the item pool.

    Off: Keep Boss Keys in their normal spots.
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

class RandomizeLevels(Toggle):
    """
    Shuffle level entrances around the Hub.
    """
    display_name = "Shuffle Level Gates"

class RandomizeBosses(Toggle):
    """
    Shuffle bosses (except Pizzaface) between floors.
    """
    display_name = "Shuffle Boss Gates"

class RandomizeSecrets(Toggle):
    """
    Shuffle Secrets between levels.
    """
    display_name = "Shuffle Secrets"

class OpenWorld(Toggle):
    """
    Unlock all floors immediately, making more levels accessible from the start.

    If active, boss keys will be removed from the item pool.
    """
    display_name = "Open World"

class BonusLadders(NamedRange):
    """
    Add bonus ladders to Hub to make accessing levels easier.

    Floors up to and including the selected floor number are affected.

    Set to 0 to disable bonus ladders.
    """
    display_name = "Bonus Ladders"
    range_start = 0
    range_end = 5
    default = 3
    special_range_names = { "disabled": 0 }

class TrapPercentage(Range):
    """
    Set a percentage of how many filler items are replaced with traps here.
    """
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 10

class EnabledTraps(OptionSet):
    """
    A trap sent to you can be any of these.
    """
    display_name = "Enabled Traps"
    verify_item_name = True
    default = [
        "Clown Trap",
        "Timer Trap",
        "Pizzaface",
        "Granny Trap",
        "Oktoberfest!"
    ]

class Jumpscare(Toggle):
    """
    Replace the Oktoberfest trap with a jumpscare. Not for the faint of heart!

    Does not change the functionality of the trap.
    """
    display_name = "Replace Oktoberfest with Jumpscare"

class FairlyRandom(DefaultOnToggle):
    """
    On: The first two levels will have at least two accessible locations each, and the first boss will not require a grab to defeat.

    Off: The first two levels and first boss can be anything.

    Only applies when Shuffle Level Gates and/or Shuffle Boss Gates are enabled.
    """
    display_name = "Fairly Random"

class LogicDifficulty(Choice):
    """
    Determines how strict the randomizer logic will be, and as a result, how difficult your run may be.

    Normal: Stricter logic for new players or those looking for a quick, simple run. The randomizer will never expect you to do anything too technical or creative.

    Expert: Relaxed logic for those looking for a challenge. The randomizer may expect you to use obscure mechanics or perform precise tricks.
    """
    display_name = "Difficulty"
    option_Normal = 0
    option_Expert = 1
    default = 0

class RandomizeMoves(DefaultOnToggle):
    """
    Determines whether your moves will even be randomized. If disabled, only Toppins, Boss Keys, and filler will appear in the item pool.
    """
    display_name = "Randomize Moves"

class MovesToRandomize(OptionSet):
    """
    Any move indicated here will be shuffled into the item pool. Any move not indicated here will be useable from the start.
    """
    display_name = "Randomize These Moves"
    default = [
        "Mach 4",
        "Uppercut",
        "Superjump",
        "Grab",
        "Taunt",
        "Supertaunt",
        "Bodyslam",
        "Breakdance",
        "Wallclimb",
        "Double Jump",
        "Rat Kick",
        "Spin Attack",
        "Wallbounce",
        "Tornado",
        "Crusher",
        "Bomb"
    ]

class ClothingFiller(Toggle):
    """
    Determines whether outfits will be shuffled into the item pool.
    """
    display_name = "Shuffle Clothes"

pt_option_groups = [
    OptionGroup("General Options", [
        CharacterToPlay,
        LogicDifficulty,
        OpenWorld,
        BonusLadders
    ]),
    OptionGroup("Boss Options", [
        ToppinCount,
        Floor1Door,
        Floor2Door,
        Floor3Door,
        Floor4Door,
        Floor5Door,
        ShuffleBossKeys
    ]),
    OptionGroup("Extra Checks", [
        TreasureChecks,
        SecretChecks,
        SRankChecks,
        PRankChecks,
        ChefTaskChecks
    ]),
    OptionGroup("Traps", [
        EnabledTraps,
        TrapPercentage,
        Jumpscare
    ]),
    OptionGroup("Randomization Options", [
        RandomizeLevels,
        RandomizeBosses,
        RandomizeSecrets,
        RandomizeMoves,
        MovesToRandomize,
        FairlyRandom
    ])
]

@dataclass
class PTOptions(PerGameCommonOptions):
    character: CharacterToPlay
    toppin_count: ToppinCount
    floor_1_cost: Floor1Door
    floor_2_cost: Floor2Door
    floor_3_cost: Floor3Door
    floor_4_cost: Floor4Door
    floor_5_cost: Floor5Door
    treasure_checks: TreasureChecks
    secret_checks: SecretChecks
    srank_checks: SRankChecks
    prank_checks: PRankChecks
    cheftask_checks: ChefTaskChecks
    shuffle_boss_keys: ShuffleBossKeys
    randomize_levels: RandomizeLevels
    randomize_bosses: RandomizeBosses
    randomize_secrets: RandomizeSecrets
    open_world: OpenWorld
    bonus_ladders: BonusLadders
    trap_percentage: TrapPercentage
    #enabled_traps: EnabledTraps # not implemented
    jumpscare: Jumpscare
    fairly_random: FairlyRandom
    difficulty: LogicDifficulty
    do_move_rando: RandomizeMoves
    move_rando_list: MovesToRandomize
    death_link: DeathLink
    clothing_filler: ClothingFiller

#presets - feel free to suggest more

toppin_hunt = {
    "toppin_count": 100,
    "floor_1_cost": 0,
    "floor_2_cost": 0,
    "floor_3_cost": 0,
    "floor_4_cost": 0,
    "floor_5_cost": 100,
    "open_world": True,
    "bonus_ladders": 5,
    "fairly_random": False
}

pt_option_presets = {
    "Toppin Hunt": toppin_hunt
}