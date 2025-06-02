# Pizza Tower Randomizer Setup Guide

## Required Software
- [Pizza Tower](https://store.steampowered.com/app/2231450/Pizza_Tower/) (obviously)
- One of the following:
    - [Pizza Oven](https://gamebanana.com/tools/12625), a Pizza Tower mod manager
    - [Delta Patcher](https://github.com/marco-calautti/DeltaPatcher), or some other way to apply `.xdelta` patches

## Optional Software
- [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases/tag/0.6.1), for its text client, if you want to be able to use commands like !hint or see your friends' progress

## Installation

First, let's get the mod installed.

### I'm using Pizza Oven!
1. Install and set up Pizza Oven according to its "Setup" section on its Gamebanana page.
2. Head on over to the [Archipelago mod page](https://gamebanana.com/mods/598236), scroll down to the most recent release, and click "Pizza Oven 1-Click Install".
3. On the prompt that appears in Pizza Oven, click "Yes".
4. Once the mod installs, click on the mod in Pizza Oven and then click "Launch".

### I'm using Delta Patcher!
1. Head on over to the [Archipelago mod page](https://gamebanana.com/mods/598236), scroll down to the most recent release, and click "Manual Download".
2. Open Delta Patcher. You'll need to give it two files:
    - The first file, "Original file", will be Pizza Tower's `data.win`. This can be found by right-clicking Pizza Tower in your Steam library, then clicking on Manage -> Browse local files.
    - The second file, "XDelta patch", will be the `.xdelta` file in the `.zip` folder you downloaded earlier. Extract it and place it into the "XDelta patch" field.
3. Click "Apply patch". If everything went as expected, you'll get a pop-up saying "Patch successfully applied!", and launching Pizza Tower from Steam will open it with the Archipelago mod installed.

## Joining a MultiWorld

After opening the game and selecting the file on the main menu (don't forget to select the character that you chose in your YAML!), input the required information on the next screen:
- Your slot name, which you wrote into your yaml
- The room's password
- The room's address and port, as indicated in the Multiworld room. It'll look something like archipelago.gg:38281

If all the info is correct, the game will start a new save file automatically. This save file can be returned to later if you connect to the same room.