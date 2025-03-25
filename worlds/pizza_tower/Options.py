from dataclasses import dataclass
from Options import Range, Toggle, DeathLink, Choice, PerGameCommonOptions, OptionSet, OptionGroup
from .Items import item_moveset_all, item_transfo

class ToppinCount(Range):
    """
    How many toppins should be shuffled into the item pool?
    """
    display_name = "Toppin Count"
    range_start = 5
    range_end = 150
    default = 95

class Floor1Door(Range):
    """
    How many toppins are required to unlock the Floor 1 boss door?
    """
    display_name = "Floor 1 Boss Toppins"
    range_start = 0
    range_end = 30
    default = 10

class Floor2Door(Range):
    """
    How many toppins are required to unlock the Floor 2 boss door?
    """
    display_name = "Floor 2 Boss Toppins"
    range_start = 0
    range_end = 30
    default = 15

class Floor3Door(Range):
    """
    How many toppins are required to unlock the Floor 3 boss door?
    """
    display_name = "Floor 3 Boss Toppins"
    range_start = 0
    range_end = 30
    default = 20

class Floor4Door(Range):
    """
    How many toppins are required to unlock the Floor 4 boss door?
    """
    display_name = "Floor 4 Boss Toppins"
    range_start = 0
    range_end = 30
    default = 20

class Floor5Door(Range):
    """
    How many toppins are required to unlock the Floor 5 boss door?
    """
    display_name = "Floor 5 Boss Toppins"
    range_start = 0
    range_end = 30
    default = 21

class PRankChecks(Toggle):
    """
    Should some items require P Ranks to unlock? This will add 24 checks to the pool.
    """
    display_name = "P Ranks Award Checks"

class ChefTaskChecks(Toggle):
    """
    Should some items require Chef Tasks to unlock? This will add 72 checks to the pool.
    """
    display_name = "Chef Tasks Award Checks"

class ClothesChecks(Toggle):
    """
    Should some items require Clothes to unlock? This will add between 19 and 22 checks to the pool, depending on the character played.

    Bear in mind that some Clothes require significant effort to unlock!
    """
    display_name = "Clothes Award Checks"

class CharacterToPlay(Choice):
    """
    Which character will you be playing?
    """
    display_name = "Character"
    option_peppino = 0
    option_noise = 1
    option_swap = 2
    alias_pep = 0
    default = 0

class LockMoves(Toggle):
    """
    Should most of your moves be locked until a corresponding item is picked up?
    """
    display_name = "Randomize Moves"

class LockMovesList(OptionSet):
    """
    Which moves should be randomized?
    """
    display_name = "Moves to Randomize"
    default = item_moveset_all

class LockTransfo(Toggle):
    """
    Should transformations be locked until a corresponding item is picked up?
    """
    display_name = "Randomize Transfos"

class LockTransfoList(OptionSet):
    """
    Which transformations should be randomized?
    """
    display_name = "Transfos to Randomize"
    default = **item_transfo

class UnlockMode(Toggle):
    """
    Should checks tied to collectibles (like toppins or Tower Secret Treasures) be unlocked immediately when touched?

    Intended to be used with move/transfo randomization. If disabled, collectibles will only award checks when brought to the end of the level.
    """
    display_name = "Collectibles Give Checks On Touch"

class RandomizeLevels(Toggle):
    """
    Should level entrances be shuffled around the hub?
    """
    display_name = "Shuffle Level Gates"

class RandomizeBosses(Toggle):
    """
    Should boss gates be shuffled between each other?

    This will not affect Pizzaface's boss gate.
    """
    display_name = "Shuffle Boss Gates"

pt_option_groups = [
    OptionGroup("General Options", [
        CharacterToPlay,
        RandomizeLevels,
        RandomizeBosses,
        UnlockMode,
    ]),
    OptionGroup("Toppin Options", [
        ToppinCount,
        Floor1Door,
        Floor2Door,
        Floor3Door,
        Floor4Door,
        Floor5Door,
    ]),
    OptionGroup("Moveset Options", [
        LockMoves,
        LockMovesList,
        LockTransfo,
        LockTransfoList,
    ]),
    OptionGroup("Extra Checks", [
        PRankChecks,
        ChefTaskChecks,
        ClothesChecks,
    ])
]

@dataclass
class PTOptions(PerGameCommonOptions):
    toppin_count: ToppinCount
    floor_1_boss_cost: Floor1Door
    floor_2_boss_cost: Floor2Door
    floor_3_boss_cost: Floor3Door
    floor_4_boss_cost: Floor4Door
    floor_5_boss_cost: Floor5Door
    p_rank_checks: PRankChecks
    chef_task_checks: ChefTaskChecks
    clothes_checks: ClothesChecks
    character_to_play: CharacterToPlay
    lock_moves: LockMoves
    lock_moves_list: LockMovesList
    lock_transfo: LockTransfo
    lock_transfo_list: LockTransfoList
    unlock_mode: UnlockMode
    shuffle_levels: RandomizeLevels
    shuffle_bosses: RandomizeBosses
    death_link: DeathLink