from BaseClasses import Location

class PTLocation(Location):
    game: str = "Pizza Tower"

pt_locations = { 
    #basics

#John Gutter
    "John Gutter Complete": 100,
    "John Gutter Mushroom Toppin": 101,
    "John Gutter Cheese Toppin": 102,
    "John Gutter Tomato Toppin": 103,
    "John Gutter Sausage Toppin": 104,
    "John Gutter Pineapple Toppin": 105,

#Pizzascape
    "Pizzascape Complete": 107,
    "Pizzascape Mushroom Toppin": 108,
    "Pizzascape Cheese Toppin": 109,
    "Pizzascape Tomato Toppin": 110,
    "Pizzascape Sausage Toppin": 111,
    "Pizzascape Pineapple Toppin": 112,

#Ancient Cheese
    "Ancient Cheese Complete": 114,
    "Ancient Cheese Mushroom Toppin": 115,
    "Ancient Cheese Cheese Toppin": 116,
    "Ancient Cheese Tomato Toppin": 117,
    "Ancient Cheese Sausage Toppin": 118,
    "Ancient Cheese Pineapple Toppin": 119,

#Bloodsauce Dungeon
    "Bloodsauce Dungeon Complete": 121,
    "Bloodsauce Dungeon Mushroom Toppin": 122,
    "Bloodsauce Dungeon Cheese Toppin": 123,
    "Bloodsauce Dungeon Tomato Toppin": 124,
    "Bloodsauce Dungeon Sausage Toppin": 125,
    "Bloodsauce Dungeon Pineapple Toppin": 126,

#Oregano Desert
    "Oregano Desert Complete": 128,
    "Oregano Desert Mushroom Toppin": 129,
    "Oregano Desert Cheese Toppin": 130,
    "Oregano Desert Tomato Toppin": 131,
    "Oregano Desert Sausage Toppin": 132,
    "Oregano Desert Pineapple Toppin": 133,

#Wasteyard
    "Wasteyard Complete": 135,
    "Wasteyard Mushroom Toppin": 136,
    "Wasteyard Cheese Toppin": 137,
    "Wasteyard Tomato Toppin": 138,
    "Wasteyard Sausage Toppin": 139,
    "Wasteyard Pineapple Toppin": 140,

#Fun Farm
    "Fun Farm Complete": 142,
    "Fun Farm Mushroom Toppin": 143,
    "Fun Farm Cheese Toppin": 144,
    "Fun Farm Tomato Toppin": 145,
    "Fun Farm Sausage Toppin": 146,
    "Fun Farm Pineapple Toppin": 147,

#Fastfood Saloon
    "Fastfood Saloon Complete": 149,
    "Fastfood Saloon Mushroom Toppin": 150,
    "Fastfood Saloon Cheese Toppin": 151,
    "Fastfood Saloon Tomato Toppin": 152,
    "Fastfood Saloon Sausage Toppin": 153,
    "Fastfood Saloon Pineapple Toppin": 154,

#Crust Cove
    "Crust Cove Complete": 156,
    "Crust Cove Mushroom Toppin": 157,
    "Crust Cove Cheese Toppin": 158,
    "Crust Cove Tomato Toppin": 159,
    "Crust Cove Sausage Toppin": 160,
    "Crust Cove Pineapple Toppin": 161,

#Gnome Forest
    "Gnome Forest Complete": 163,
    "Gnome Forest Mushroom Toppin": 164,
    "Gnome Forest Cheese Toppin": 165,
    "Gnome Forest Tomato Toppin": 166,
    "Gnome Forest Sausage Toppin": 167,
    "Gnome Forest Pineapple Toppin": 168,

#Deep-Dish 9
    "Deep-Dish 9 Complete": 170,
    "Deep-Dish 9 Mushroom Toppin": 171,
    "Deep-Dish 9 Cheese Toppin": 172,
    "Deep-Dish 9 Tomato Toppin": 173,
    "Deep-Dish 9 Sausage Toppin": 174,
    "Deep-Dish 9 Pineapple Toppin": 175,

#GOLF
    "GOLF Complete": 177,
    "GOLF Mushroom Toppin": 178,
    "GOLF Cheese Toppin": 179,
    "GOLF Tomato Toppin": 180,
    "GOLF Sausage Toppin": 181,
    "GOLF Pineapple Toppin": 182,

#The Pig City
    "The Pig City Complete": 184,
    "The Pig City Mushroom Toppin": 185,
    "The Pig City Cheese Toppin": 186,
    "The Pig City Tomato Toppin": 187,
    "The Pig City Sausage Toppin": 188,
    "The Pig City Pineapple Toppin": 189,

#Peppibot Factory
    "Peppibot Factory Complete": 191,
    "Peppibot Factory Mushroom Toppin": 192,
    "Peppibot Factory Cheese Toppin": 193,
    "Peppibot Factory Tomato Toppin": 194,
    "Peppibot Factory Sausage Toppin": 195,
    "Peppibot Factory Pineapple Toppin": 196,

#Oh Shit!
    "Oh Shit! Complete": 198,
    "Oh Shit! Mushroom Toppin": 199,
    "Oh Shit! Cheese Toppin": 200,
    "Oh Shit! Tomato Toppin": 201,
    "Oh Shit! Sausage Toppin": 202,
    "Oh Shit! Pineapple Toppin": 203,

#Freezerator
    "Freezerator Complete": 205,
    "Freezerator Mushroom Toppin": 206,
    "Freezerator Cheese Toppin": 207,
    "Freezerator Tomato Toppin": 208,
    "Freezerator Sausage Toppin": 209,
    "Freezerator Pineapple Toppin": 210,

#Pizzascare
    "Pizzascare Complete": 212,
    "Pizzascare Mushroom Toppin": 213,
    "Pizzascare Cheese Toppin": 214,
    "Pizzascare Tomato Toppin": 215,
    "Pizzascare Sausage Toppin": 216,
    "Pizzascare Pineapple Toppin": 217,

#Don't Make a Sound
    "Don't Make a Sound Complete": 219,
    "Don't Make a Sound Mushroom Toppin": 220,
    "Don't Make a Sound Cheese Toppin": 221,
    "Don't Make a Sound Tomato Toppin": 222,
    "Don't Make a Sound Sausage Toppin": 223,
    "Don't Make a Sound Pineapple Toppin": 224,

#WAR
    "WAR Complete": 226,
    "WAR Mushroom Toppin": 227,
    "WAR Cheese Toppin": 228,
    "WAR Tomato Toppin": 229,
    "WAR Sausage Toppin": 230,
    "WAR Pineapple Toppin": 231,

#Crumbling Tower of Pizza
    "The Crumbling Tower of Pizza Complete": 233,

#Bosses
    "Pepperman Defeated": 235,
    "The Vigilante Defeated": 237,
    "The Noise Defeated": 239,
    "Fake Peppino Defeated": 241,
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
    
    #s ranks

    #Levels
    "John Gutter S Rank": 106,
    "Pizzascape S Rank": 113,
    "Ancient Cheese S Rank": 120,
    "Bloodsauce Dungeon S Rank": 127,
    "Oregano Desert S Rank": 134,
    "Wasteyard S Rank": 141,
    "Fun Farm S Rank": 148,
    "Fastfood Saloon S Rank": 155,
    "Crust Cove S Rank": 162,
    "Gnome Forest S Rank": 169,
    "Deep-Dish 9 S Rank": 176,
    "GOLF S Rank": 183,
    "The Pig City S Rank": 190,
    "Peppibot Factory S Rank": 197,
    "Oh Shit! S Rank": 204,
    "Freezerator S Rank": 211,
    "Pizzascare S Rank": 218,
    "Don't Make a Sound S Rank": 225,
    "WAR S Rank": 232,
    "The Crumbling Tower of Pizza S Rank": 234,

    #Bosses
    "Pepperman S Rank": 236,
    "The Vigilante S Rank": 238,
    "The Noise S Rank": 240,
    "Fake Peppino S Rank": 242,

    #secrets 

    #John Gutter
    "John Gutter Secret 1": 252,
    "John Gutter Secret 2": 253,
    "John Gutter Secret 3": 254,

    #Pizzascape
    "Pizzascape Secret 1": 255,
    "Pizzascape Secret 2": 256,
    "Pizzascape Secret 3": 257,

    #Ancient Cheese
    "Ancient Cheese Secret 1": 258,
    "Ancient Cheese Secret 2": 259,
    "Ancient Cheese Secret 3": 260,

    #Bloodsauce Dungeon
    "Bloodsauce Dungeon Secret 1": 261,
    "Bloodsauce Dungeon Secret 2": 262,
    "Bloodsauce Dungeon Secret 3": 263,

    #Oregano Desert
    "Oregano Desert Secret 1": 264,
    "Oregano Desert Secret 2": 265,
    "Oregano Desert Secret 3": 266,

    #Wasteyard
    "Wasteyard Secret 1": 267,
    "Wasteyard Secret 2": 268,
    "Wasteyard Secret 3": 269,

    #Fun Farm
    "Fun Farm Secret 1": 270,
    "Fun Farm Secret 2": 271,
    "Fun Farm Secret 3": 272,

    #Fastfood Saloon
    "Fastfood Saloon Secret 1": 273,
    "Fastfood Saloon Secret 2": 274,
    "Fastfood Saloon Secret 3": 275,

    #Crust Cove
    "Crust Cove Secret 1": 276,
    "Crust Cove Secret 2": 277,
    "Crust Cove Secret 3": 278,

    #Gnome Forest
    "Gnome Forest Secret 1": 279,
    "Gnome Forest Secret 2": 280,
    "Gnome Forest Secret 3": 281,

    #Deep-Dish 9
    "Deep-Dish 9 Secret 1": 282,
    "Deep-Dish 9 Secret 2": 283,
    "Deep-Dish 9 Secret 3": 284,

    #GOLF
    "GOLF Secret 1": 285,
    "GOLF Secret 2": 286,
    "GOLF Secret 3": 287,

    #The Pig City
    "The Pig City Secret 1": 288,
    "The Pig City Secret 2": 289,
    "The Pig City Secret 3": 290,

    #Peppibot Factory
    "The Pig City Secret 1": 291,
    "The Pig City Secret 2": 292,
    "The Pig City Secret 3": 293,

    #Oh Shit!
    "Oh Shit! Secret 1": 294,
    "Oh Shit! Secret 2": 295,
    "Oh Shit! Secret 3": 296,

    #Freezerator
    "Freezerator Secret 1": 297,
    "Freezerator Secret 2": 298,
    "Freezerator Secret 3": 299,

    #Pizzascare
    "Pizzascare Secret 1": 300,
    "Pizzascare Secret 2": 301,
    "Pizzascare Secret 3": 302,

    #Don't Make a Sound
    "Don't Make a Sound Secret 1": 303,
    "Don't Make a Sound Secret 2": 304,
    "Don't Make a Sound Secret 3": 305,

    #WAR
    "WAR Secret 1": 306,
    "WAR Secret 2": 307,
    "WAR Secret 3": 308,

    #p ranks

    #Levels
    "John Gutter P Rank": 309,
    "Pizzascape P Rank": 310,
    "Ancient Cheese P Rank": 311,
    "Bloodsauce Dungeon P Rank": 312,
    "Oregano Desert P Rank": 313,
    "Wasteyard P Rank": 314,
    "Fun Farm P Rank": 315,
    "Fastfood Saloon P Rank": 316,
    "Crust Cove P Rank": 317,
    "Gnome Forest P Rank": 318,
    "Deep-Dish 9 P Rank": 319,
    "GOLF P Rank": 320,
    "The Pig City P Rank": 321,
    "Peppibot Factory P Rank": 322,
    "Oh Shit! P Rank": 323,
    "Freezerator P Rank": 324,
    "Pizzascare P Rank": 325,
    "Don't Make a Sound P Rank": 326,
    "WAR P Rank": 327,
    "The Crumbling Tower of Pizza P Rank": 328,

    #Bosses
    "Pepperman P Rank": 329,
    "The Vigilante P Rank": 330,
    "The Noise P Rank": 331,
    "Fake Peppino P Rank": 332,

    #cheftasks

    #John Gutter
    "Chef Task: John Gutted": 333,
    "Chef Task: Primate Rage": 334,
    "Chef Task: Let's Make This Quick": 335,

    #Pizzascape
    "Chef Task: Shining Armor": 336,
    "Chef Task: Spoonknight": 337,
    "Chef Task: Spherical": 338,

    #Ancient Cheese
    "Chef Task: Thrill Seeker": 339,
    "Chef Task: Volleybomb": 340,
    "Chef Task: Delicacy": 341,

    #Bloodsauce Dungeon
    "Chef Task: Eruption Man": 342,
    "Chef Task: Very Very Hot Sauce": 343,
    "Chef Task: Unsliced Pizzaman": 344,

    #Oregano Desert
    "Chef Task: Peppino's Rain Dance": 345,
    "Chef Task: Unnecessary Violence": 346,
    "Chef Task: Alien Cow": 347,

    #Wasteyard
    "Chef Task: Alive and Well": 348,
    "Chef Task: Pretend Ghost": 349,
    "Chef Task: Ghosted": 350,

    #Fun Farm
    "Chef Task: Good Egg": 351,
    "Chef Task: No One Is Safe": 352,
    "Chef Task: Cube Menace": 353,

    #Fastfood Saloon
    "Chef Task: Royal Flush": 354,
    "Chef Task: Non-Alcoholic": 355,
    "Chef Task: Already Pressed": 356,

    #Crust Cove
    "Chef Task: Demolition Expert": 357,
    "Chef Task: Blowback": 358,
    "Chef Task: X": 359,

    #Gnome Forest
    "Chef Task: Bee Nice": 360,
    "Chef Task: Bullseye": 361,
    "Chef Task: Lumberjack": 362,

    #Deep-Dish 9
    "Chef Task: Blast 'Em Asteroids": 363,
    "Chef Task: Turbo Tunnel": 364,
    "Chef Task: Man Meteor": 365,

    #GOLF
    "Chef Task: Primo Golfer": 366,
    "Chef Task: Helpful Burger": 367,
    "Chef Task: Nice Shot": 368,

    #The Pig City
    "Chef Task: Say Oink!": 369,
    "Chef Task: Pan Fried": 370,
    "Chef Task: Strike!": 371,

    #Peppibot Factory
    "Chef Task: There Can Be Only One": 372,
    "Chef Task: Whoop This!": 373,
    "Chef Task: Unflattening": 374,

    #Oh Shit!
    "Chef Task: Food Clan": 375,
    "Chef Task: Can't Fool Me": 376,
    "Chef Task: Penny Pincher": 377,

    #Freezerator
    "Chef Task: Ice Climber": 378,
    "Chef Task: Season's Greetings": 379,
    "Chef Task: Frozen Nuggets": 380,

    #Pizzascare
    "Chef Task: Haunted Playground": 381,
    "Chef Task: Skullsplitter": 382,
    "Chef Task: Cross to Bare": 383,

    #Don't Make a Sound
    "Chef Task: Let Them Sleep": 384,
    "Chef Task: Jumpspared": 385,
    "Chef Task: And This... Is My Gun on a Stick!": 386,

    #WAR
    "Chef Task: Trip to the Warzone": 387,
    "Chef Task: Sharpshooter": 388,
    "Chef Task: Decorated Veteran": 389,

    #Floor Tasks
    "Chef Task: S Ranked #1": 390,
    "Chef Task: P Ranked #1": 391,
    "Chef Task: S Ranked #2": 392,
    "Chef Task: P Ranked #2": 393,
    "Chef Task: S Ranked #3": 394,
    "Chef Task: P Ranked #3": 395,
    "Chef Task: S Ranked #4": 396,
    "Chef Task: P Ranked #4": 397,
    "Chef Task: S Ranked #5": 398,
    "Chef Task: P Ranked #5": 399,

    #Boss Tasks
    "Chef Task: The Critic": 400,
    "Chef Task: The Ugly": 401,
    "Chef Task: Denoise": 402,
    "Chef Task: Faker": 403,
    "Chef Task: Face-Off": 404,

    #treasures
    "John Gutter Treasure": 405,
    "Pizzascape Treasure": 406,
    "Ancient Cheese Treasure": 407,
    "Bloodsauce Dungeon Treasure": 408,
    "Oregano Desert Treasure": 409,
    "Wasteyard Treasure": 410,
    "Fun Farm Treasure": 411,
    "Fastfood Saloon Treasure": 412,
    "Crust Cove Treasure": 413,
    "Gnome Forest Treasure": 414,
    "Deep-Dish 9 Treasure": 415,
    "GOLF Treasure": 416,
    "The Pig City Treasure": 417,
    "Peppibot Factory Treasure": 418,
    "Oh Shit! Treasure": 419,
    "Freezerator Treasure": 420,
    "Pizzascare Treasure": 421,
    "Don't Make a Sound Treasure": 422,
    "WAR Treasure": 423
}