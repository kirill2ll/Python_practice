# Write a program that processes information about a race. On the first line you will be given list of participants separated by ", ". On the next few lines until you receive a line "end of race" you will be given some info which will be some alphanumeric characters. In between them you could have some extra characters which you should ignore. For example: "G!32e%o7r#32g$235@!2e". The letters are the name of the person and the sum of the digits is the distance he ran. So here we have George who ran 29 km. Store the information about the person only if the list of racers contains the name of the person. If you receive the same person more than once just add the distance to his old distance. At the end print the top 3 racers ordered by distance in descending in the format:
# "1st place: {first racer}
# 2nd place: {second racer}
# 3rd place: {third racer}"
import re

racers = input().split(", ")
racers_dict = {}

pattern_name = r"([a-zA-Z])"
pattern_numbers = r"([0-9])"

while True:

    line = input()

    if line == "end of race":
        break

    name_list = re.findall(pattern_name, line)
    km_list = re.findall(pattern_numbers, line)

    name = "".join(name_list)
    if name in racers:
        if name not in racers_dict.keys():
            racers_dict[name] = 0
        racers_dict[name] += sum([int(km) for km in km_list])



sort_by_values = sorted(racers_dict.items(), key=lambda x:-x[1])


print(f"1st place: {sort_by_values[0][0]}")
print(f"2nd place: {sort_by_values[1][0]}")
print(f"3rd place: {sort_by_values[2][0]}")

