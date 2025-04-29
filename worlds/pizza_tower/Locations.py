from BaseClasses import Location

class PTLocation(Location):
    game: str = "Pizza Tower"

pt_locations = { 
#John Gutter
    "John Gutter Complete": 100,
    "John Gutter Mushroom Toppin": 101,
    "John Gutter Cheese Toppin": 102,
    "John Gutter Tomato Toppin": 103,
    "John Gutter Sausage Toppin": 104,
    "John Gutter Pineapple Toppin": 105,
    "John Gutter S Rank": 106,

#Pizzascape
    "Pizzascape Complete": 107,
    "Pizzascape Mushroom Toppin": 108,
    "Pizzascape Cheese Toppin": 109,
    "Pizzascape Tomato Toppin": 110,
    "Pizzascape Sausage Toppin": 111,
    "Pizzascape Pineapple Toppin": 112,
    "Pizzascape S Rank": 113,

#Ancient Cheese
    "Ancient Cheese Complete": 114,
    "Ancient Cheese Mushroom Toppin": 115,
    "Ancient Cheese Cheese Toppin": 116,
    "Ancient Cheese Tomato Toppin": 117,
    "Ancient Cheese Sausage Toppin": 118,
    "Ancient Cheese Pineapple Toppin": 119,
    "Ancient Cheese S Rank": 120,

#Bloodsauce Dungeon
    "Bloodsauce Dungeon Complete": 121,
    "Bloodsauce Dungeon Mushroom Toppin": 122,
    "Bloodsauce Dungeon Cheese Toppin": 123,
    "Bloodsauce Dungeon Tomato Toppin": 124,
    "Bloodsauce Dungeon Sausage Toppin": 125,
    "Bloodsauce Dungeon Pineapple Toppin": 126,
    "Bloodsauce Dungeon S Rank": 127,

#Oregano Desert
    "Oregano Desert Complete": 128,
    "Oregano Desert Mushroom Toppin": 129,
    "Oregano Desert Cheese Toppin": 130,
    "Oregano Desert Tomato Toppin": 131,
    "Oregano Desert Sausage Toppin": 132,
    "Oregano Desert Pineapple Toppin": 133,
    "Oregano Desert S Rank": 134,

#Wasteyard
    "Wasteyard Complete": 135,
    "Wasteyard Mushroom Toppin": 136,
    "Wasteyard Cheese Toppin": 137,
    "Wasteyard Tomato Toppin": 138,
    "Wasteyard Sausage Toppin": 139,
    "Wasteyard Pineapple Toppin": 140,
    "Wasteyard S Rank": 141,

#Fun Farm
    "Fun Farm Complete": 142,
    "Fun Farm Mushroom Toppin": 143,
    "Fun Farm Cheese Toppin": 144,
    "Fun Farm Tomato Toppin": 145,
    "Fun Farm Sausage Toppin": 146,
    "Fun Farm Pineapple Toppin": 147,
    "Fun Farm S Rank": 148,

#Fastfood Saloon
    "Fastfood Saloon Complete": 149,
    "Fastfood Saloon Mushroom Toppin": 150,
    "Fastfood Saloon Cheese Toppin": 151,
    "Fastfood Saloon Tomato Toppin": 152,
    "Fastfood Saloon Sausage Toppin": 153,
    "Fastfood Saloon Pineapple Toppin": 154,
    "Fastfood Saloon S Rank": 155,

#Crust Cove
    "Crust Cove Complete": 156,
    "Crust Cove Mushroom Toppin": 157,
    "Crust Cove Cheese Toppin": 158,
    "Crust Cove Tomato Toppin": 159,
    "Crust Cove Sausage Toppin": 160,
    "Crust Cove Pineapple Toppin": 161,
    "Crust Cove S Rank": 162,

#Gnome Forest
    "Gnome Forest Complete": 163,
    "Gnome Forest Mushroom Toppin": 164,
    "Gnome Forest Cheese Toppin": 165,
    "Gnome Forest Tomato Toppin": 166,
    "Gnome Forest Sausage Toppin": 167,
    "Gnome Forest Pineapple Toppin": 168,
    "Gnome Forest S Rank": 169,

#Deep-Dish 9
    "Deep-Dish 9 Complete": 170,
    "Deep-Dish 9 Mushroom Toppin": 171,
    "Deep-Dish 9 Cheese Toppin": 172,
    "Deep-Dish 9 Tomato Toppin": 173,
    "Deep-Dish 9 Sausage Toppin": 174,
    "Deep-Dish 9 Pineapple Toppin": 175,
    "Deep-Dish 9 S Rank": 176,

#GOLF
    "GOLF Complete": 177,
    "GOLF Mushroom Toppin": 178,
    "GOLF Cheese Toppin": 179,
    "GOLF Tomato Toppin": 180,
    "GOLF Sausage Toppin": 181,
    "GOLF Pineapple Toppin": 182,
    "GOLF S Rank": 183,

#The Pig City
    "The Pig City Complete": 184,
    "The Pig City Mushroom Toppin": 185,
    "The Pig City Cheese Toppin": 186,
    "The Pig City Tomato Toppin": 187,
    "The Pig City Sausage Toppin": 188,
    "The Pig City Pineapple Toppin": 189,
    "The Pig City S Rank": 190,

#Peppibot Factory
    "Peppibot Factory Complete": 191,
    "Peppibot Factory Mushroom Toppin": 192,
    "Peppibot Factory Cheese Toppin": 193,
    "Peppibot Factory Tomato Toppin": 194,
    "Peppibot Factory Sausage Toppin": 195,
    "Peppibot Factory Pineapple Toppin": 196,
    "Peppibot Factory S Rank": 197,

#Oh Shit!
    "Oh Shit! Complete": 198,
    "Oh Shit! Mushroom Toppin": 199,
    "Oh Shit! Cheese Toppin": 200,
    "Oh Shit! Tomato Toppin": 201,
    "Oh Shit! Sausage Toppin": 202,
    "Oh Shit! Pineapple Toppin": 203,
    "Oh Shit! S Rank": 204,

#Freezerator
    "Freezerator Complete": 205,
    "Freezerator Mushroom Toppin": 206,
    "Freezerator Cheese Toppin": 207,
    "Freezerator Tomato Toppin": 208,
    "Freezerator Sausage Toppin": 209,
    "Freezerator Pineapple Toppin": 210,
    "Freezerator S Rank": 211,

#Pizzascare
    "Pizzascare Complete": 212,
    "Pizzascare Mushroom Toppin": 213,
    "Pizzascare Cheese Toppin": 214,
    "Pizzascare Tomato Toppin": 215,
    "Pizzascare Sausage Toppin": 216,
    "Pizzascare Pineapple Toppin": 217,
    "Pizzascare S Rank": 218,

#Don't Make a Sound
    "Don't Make a Sound Complete": 219,
    "Don't Make a Sound Mushroom Toppin": 220,
    "Don't Make a Sound Cheese Toppin": 221,
    "Don't Make a Sound Tomato Toppin": 222,
    "Don't Make a Sound Sausage Toppin": 223,
    "Don't Make a Sound Pineapple Toppin": 224,
    "Don't Make a Sound S Rank": 225,

#WAR
    "WAR Complete": 226,
    "WAR Mushroom Toppin": 227,
    "WAR Cheese Toppin": 228,
    "WAR Tomato Toppin": 229,
    "WAR Sausage Toppin": 230,
    "WAR Pineapple Toppin": 231,
    "WAR S Rank": 232,

#Crumbling Tower of Pizza
    "The Crumbling Tower of Pizza Complete": 233,
    "The Crumbling Tower of Pizza S Rank": 234,

#Bosses
    "Pepperman Defeated": 235,
    "Pepperman S Rank": 236,
    "The Vigilante Defeated": 237,
    "The Vigilante S Rank": 238,
    "The Noise Defeated": 239,
    "The Noise S Rank": 240,
    "Fake Peppino Defeated": 241,
    "Fake Peppino S Rank": 242,
    "Pizzaface Defeated": 243,

#misc
    "Snotty Murdered": 244,

#Tutorial
    "Tutorial Complete": 245,
    "Tutorial Complete in under 2 minutes": 246,
    "Tutorial Mushroom Toppin": 247,
    "Tutorial Cheese Toppin": 248,
    "Tutorial Tomato Toppin": 249,
    "Tutorial Sausage Toppin": 250,
    "Tutorial Pineapple Toppin": 251,
}