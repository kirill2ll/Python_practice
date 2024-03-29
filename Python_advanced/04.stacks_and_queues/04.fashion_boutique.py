# You own a fashion boutique and receive a delivery of a huge box of clothes, represented as a sequence of integers. On the following line, you will be given an integer representing the capacity for one rack in your store.
# You must arrange the clothes in the store and use the racks to hang up every piece of clothing. You start from the last piece of clothing on the top of the pile to the first one at the bottom. Use a stack for this purpose. Each piece of clothing has its value (an integer). You must sum their values while you take them out of the box:
# •	If the sum becomes equal to the capacity of the current rack, you must take a new one for the next clothes (if there are any left in the box).
# •	If the sum becomes greater than the capacity, do not hang the piece of clothing on the current rack. Take a new rack and then hang it up.
# In the end, print how many racks you have used to hang up the clothes.



from collections import deque

clothes = deque(map(int, input().split()))
rack = int(input())
number_of_racks = 1
current_rack = 0

while len(clothes) > 0:
    current_cloth = clothes.pop()
    current_rack += current_cloth

    if current_rack > rack:
        number_of_racks += 1
        current_rack = current_cloth
    elif current_rack == rack and len(clothes) > 0:
        number_of_racks += 1
        current_rack = 0

print(number_of_racks)

