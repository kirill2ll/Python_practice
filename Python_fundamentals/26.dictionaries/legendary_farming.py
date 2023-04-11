# You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough. However, it's a tedious process, and it requires quite a bit of farming. The possible items are:
# "Shadowmourne" - requires 250 Shards
# "Valanyr" - requires 250 Fragments
# "Dragonwrath" - requires 250 Motes
# "Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk.
# You will be given lines of input in the format:
# "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Keep track of the key materials - the first one that reaches 250, wins the race. At that point, you have to print that the corresponding legendary item is obtained.
# In the end, print the remaining shards, fragments, motes in the format:
# "shards: {number_of_shards}
# fragments: {number_of_fragments}
# motes: {number_of_motes}"
# Finally, print the collected junk items in the order of appearance.



materials = {"shards": 0, "fragments": 0, "motes": 0}
is_achieved = False
special_materials = ["shards", "fragments", "motes"]


def check_is_achieved(materials, material):
    if materials[material] >= 250:
        if material == "shards":
            print("Shadowmourne obtained!")

        elif material == "fragments":
            print("Valanyr obtained!")

        elif material == "motes":
            print("Dragonwrath obtained!")

        materials[material] -= 250
        return True, materials

    return False, materials


while is_achieved != True:
    current_line = input().split()

    for i in range(0, len(current_line), 2):
        material = current_line[i+1].lower()
        quantity = int(current_line[i])

        if material not in materials.keys():
            materials[material] = 0

        materials[material] += quantity

        if material in special_materials:
            is_achieved, materials = check_is_achieved(materials, material)
            if(is_achieved):
                break


for material, quantity in materials.items():
    print(f"{material}: {quantity}")

