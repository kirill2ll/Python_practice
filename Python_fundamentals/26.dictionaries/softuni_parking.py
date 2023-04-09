# SoftUni just got a new fancy parking lot. It even has online parking validation, except the online service doesn't work. It can only receive users' data, but it doesn't know what to do with it. Good thing you're on the dev team and know how to fix it, right?
# Write a program, which validates a parking place - users can register to enter the park and unregister to leave.
# The program receives 2 types of commands:
# "register {username} {license_plate_number}":
# The system only supports one car per user at the moment, so if a user tries to register another license plate using the same username, the system should print:
# "ERROR: already registered with plate number {license_plate_number}"
# If the check above passes successfully, the user should be registered, so the system should print:
#  "{username} registered {license_plate_number} successfully"
# "unregister {username}":
# If the user is not present in the database, the system should print:
# "ERROR: user {username} not found"
# If the check above passes successfully, the system should print:
# "{username} unregistered successfully"
# After you execute all of the commands, print all the currently registered users and their license plates in the format:
# "{username} => {license_plate_number}"
# Input
# First line: n - number of commands - integer
# Next n lines: commands in one of the two possible formats:
# Register: "register {username} {license_plate_number}"
# Unregister: "unregister {username}"
# The input will always be valid, and you do not need to check it explicitly.

def check_parking(command, name, license_plate):
    if command == "register":
        if name not in parking.keys():
            parking[name] = license_plate
            print(f"{name} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")

    else:
        if name not in parking.keys():
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            parking.pop(name)


number_of_lines = int(input())
parking = {}

for i in range(number_of_lines):
    current_line = input().split()

    command = current_line[0]
    name = current_line[1]
    license_plate = None

    #for unregister command the license_plate doesn't exist
    if len(current_line) == 3:
        license_plate = current_line[2]

    check_parking(command, name, license_plate)

for username, license_plate_number in parking.items():
    print(f"{username} => {license_plate_number}")