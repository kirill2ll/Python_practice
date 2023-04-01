# Write a program that reads N lines of strings and extracts the name and the age of a given person:
# The person's name will be surrounded by "@" and "|" in the format "@{name}|".
# The person's age will be surrounded by "#" and "*" in the format "#{age}*".
# Example: "Hello my name is @Peter| and I am #20* years old."
# For each found name-age pair, print a line in the following format "{name} is {age} years old."

number_of_lines = int(input())

for i in range(number_of_lines):
    current_line = input()
    name = ""
    age = ""

    append_name = False
    append_age = False

    for ch in current_line:
        if ch == "@":
            append_name = True

        elif ch == "|":
            append_name = False

        elif ch == "#":
            append_age = True

        elif ch == "*":
            append_age = False

        if append_name:
            name += ch
        if append_age:
            age += ch


    print(f"{name[1:]} is {age[1:]} years old.")
