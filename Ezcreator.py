import tkinter as tk
from tkinter import ttk
import os

def add_settings_to_file():
    champion_selection = champion_combobox.get()
    level_selection = level_combobox.get()
    position_selection = position_combobox.get()
    item1_selection = item1_combobox.get()
    item2_selection = item2_combobox.get()
    item3_selection = item3_combobox.get()
    final_comp_state = "True," if final_comp_var.get() else "False,"

    # reset item selection dropdowns
    item1_combobox.set('')
    item2_combobox.set('')
    item3_combobox.set('')
    
    # Get the directory of the Python script
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Create the full path to the file
    file_path = os.path.join(dir_path, "settings.txt")

    # Write the settings to the file
    with open(file_path, "a") as f:
        f.write('"{}": {{\n'.format(champion_selection))
        f.write('\t"board_position": {},\n'.format(position_selection))
        f.write('\t"items": ["{}", "{}", "{}"],\n'.format(item1_selection, item2_selection, item3_selection))
        f.write('\t"level": {},\n'.format(level_selection))
        f.write('\t"final_comp": {}\n'.format(str(final_comp_state).lower()))
        f.write('},\n\n')

# create the main window
root = tk.Tk()
root.title("EasyComp 0.1")

# create the champion selection dropdown
champion_label = tk.Label(root, text="Champion")
champion_label.grid(column=0, row=0, padx=10, pady=10)
champion_combobox = tk.ttk.Combobox(root, values=["Alistar", "Annie", "Aphelios", "Ashe", "AurelionSol", "Belveth", "Blitzcrank", "Camille", "Chogath", "Draven", "Ekko", "Ezreal", "Fiddlesticks", "Fiora", "Galio", "Gangplank", "Janna", "Jax", "Jinx", "Kaisa", "Kayle", "Leblanc", "LeeSin", "Leona", "Lulu", "Lux", "Malphite", "MissFortune", "Mordekaiser", "Nasus", "Nilah", "Nunu", "Poppy", "Rammus", "Rell", "Renekton", "Riven", "Samira", "Sejuani", "Senna", "Sett", "Sivir", "Sona", "Soraka", "Sylas", "Syndra", "Taliyah", "Talon", "Urgot", "Vayne", "Velkoz", "Vi", "Viego", "Wukong", "Yasuo", "Yuumi", "Zac", "Zed", "Zoe",])
champion_combobox.grid(column=1, row=0)

# create the level selection dropdown
level_label = tk.Label(root, text="Level")
level_label.grid(column=0, row=1, padx=10, pady=10)
level_combobox = tk.ttk.Combobox(root, values=["1", "2", "3"])
level_combobox.grid(column=1, row=1)

# create the position selection dropdown
position_label = tk.Label(root, text="Board position")
position_label.grid(column=0, row=2, padx=10, pady=10)

positions = [" {}".format(i+0) for i in range(28)]

position_combobox = tk.ttk.Combobox(root, values=positions)
position_combobox.grid(column=1, row=2)

# create the item selection dropdown
item1_label = tk.Label(root, text="Item")
item1_label.grid(column=0, row=4, padx=10, pady=10)
item1_combobox = tk.ttk.Combobox(root, values=["BFSword", "ChainVest", "GiantsBelt", "NeedlesslyLargeRod",
                            "NegatronCloak", "SparringGloves", "Spatula", "TearoftheGoddess",
                            "ArchangelsStaff", "RenegadeEmblem", "Guardbreaker", "Bloodthirster",
                            "BlueBuff", "BrambleVest", "MascotEmblem", "ChaliceofPower",
                            "Deathblade", "HeartEmblem", "DragonsClaw", "EdgeofNight",
                            "FrozenHeart", "GargoyleStoneplate", "GiantSlayer", "HandofJustice",
                            "HextechGunblade", "InfinityEdge", "IonicSpark", "JeweledGauntlet",
                            "LastWhisper", "LocketoftheIronSolari", "AnimaEmblem", "ADMINEmblem",
                            "Morellonomicon", "Quicksilver", "RabadonsDeathcap", "OxForceEmblem",
                            "RapidFirecannon", "Redemption", "RunaansHurricane", "DuelistEmblem",
                            "ShroudofStillness", "SpearofShojin", "StatikkShiv", "SunfireCape",
                            "TacticiansCrown", "ThiefsGloves", "TitansResolve", "WarmogsArmor",
                            "ZekesHerald", "Zephyr", "ZzRotPortal", "RecurveBow",
                            "LaserCorpsEmblem", "GuinsoosRageblade"])
item1_combobox.grid(column=1, row=4)

# create the item selection dropdown
item2_label = tk.Label(root, text="Item")
item2_label.grid(column=2, row=4, padx=10, pady=10)
item2_combobox = tk.ttk.Combobox(root, values=["BFSword", "ChainVest", "GiantsBelt", "NeedlesslyLargeRod",
                            "NegatronCloak", "SparringGloves", "Spatula", "TearoftheGoddess",
                            "ArchangelsStaff", "RenegadeEmblem", "Guardbreaker", "Bloodthirster",
                            "BlueBuff", "BrambleVest", "MascotEmblem", "ChaliceofPower",
                            "Deathblade", "HeartEmblem", "DragonsClaw", "EdgeofNight",
                            "FrozenHeart", "GargoyleStoneplate", "GiantSlayer", "HandofJustice",
                            "HextechGunblade", "InfinityEdge", "IonicSpark", "JeweledGauntlet",
                            "LastWhisper", "LocketoftheIronSolari", "AnimaEmblem", "ADMINEmblem",
                            "Morellonomicon", "Quicksilver", "RabadonsDeathcap", "OxForceEmblem",
                            "RapidFirecannon", "Redemption", "RunaansHurricane", "DuelistEmblem",
                            "ShroudofStillness", "SpearofShojin", "StatikkShiv", "SunfireCape",
                            "TacticiansCrown", "ThiefsGloves", "TitansResolve", "WarmogsArmor",
                            "ZekesHerald", "Zephyr", "ZzRotPortal", "RecurveBow",
                            "LaserCorpsEmblem", "GuinsoosRageblade"])
item2_combobox.grid(column=2, row=4)

item3_label = tk.Label(root, text="Item")
item3_label.grid(column=3, row=4, padx=10, pady=10)
item3_combobox = tk.ttk.Combobox(root, values=["BFSword", "ChainVest", "GiantsBelt", "NeedlesslyLargeRod",
                            "NegatronCloak", "SparringGloves", "Spatula", "TearoftheGoddess",
                            "ArchangelsStaff", "RenegadeEmblem", "Guardbreaker", "Bloodthirster",
                            "BlueBuff", "BrambleVest", "MascotEmblem", "ChaliceofPower",
                            "Deathblade", "HeartEmblem", "DragonsClaw", "EdgeofNight",
                            "FrozenHeart", "GargoyleStoneplate", "GiantSlayer", "HandofJustice",
                            "HextechGunblade", "InfinityEdge", "IonicSpark", "JeweledGauntlet",
                            "LastWhisper", "LocketoftheIronSolari", "AnimaEmblem", "ADMINEmblem",
                            "Morellonomicon", "Quicksilver", "RabadonsDeathcap", "OxForceEmblem",
                            "RapidFirecannon", "Redemption", "RunaansHurricane", "DuelistEmblem",
                            "ShroudofStillness", "SpearofShojin", "StatikkShiv", "SunfireCape",
                            "TacticiansCrown", "ThiefsGloves", "TitansResolve", "WarmogsArmor",
                            "ZekesHerald", "Zephyr", "ZzRotPortal", "RecurveBow",
                            "LaserCorpsEmblem", "GuinsoosRageblade"])
item3_combobox.grid(column=3, row=4)

# create the final comp checkbox
final_comp_label = tk.Label(root, text="Final Comp")
final_comp_label.grid(column=0, row=5, padx=10, pady=10)
final_comp_var = tk.BooleanVar()
final_comp_checkbutton = tk.Checkbutton(root, variable=final_comp_var)
final_comp_checkbutton.grid(column=1, row=5)

# create the add button
add_button = tk.Button(root, text="Add", command=add_settings_to_file)
add_button.grid(column=0, row=6, columnspan=2, pady=10)

root.mainloop()
