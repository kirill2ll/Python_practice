# You will be given a sequence of strings, each on a new line until you receive the "stop" command. Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity. Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# "{resource} -> {quantity}"

all_resources = {}

while True:
    source = input()
    if source == "stop":
        break

    quantity = int(input())

    if source not in all_resources.keys():
        all_resources[source] = 0

    all_resources[source] += quantity


for resource, quantity in all_resources.items():
    print(f"{resource} -> {quantity}")