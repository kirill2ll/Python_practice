# Write a program that keeps the information about companies and their employees.
# You will be receiving company names and an employees' id until you receive the command "End" command. Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.


companies = {}

while True:
    current_line = input().split(" -> ")

    if current_line[0] == "End":
        break

    company = current_line[0]
    id = current_line[1]

    if company not in companies.keys():
        companies[company] = []

    if id not in companies[company]:
        companies[company].append(id)

for company, ids in companies.items():
    print(company)
    for id in ids:
        print(f"-- {id}")

