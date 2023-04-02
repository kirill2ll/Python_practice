# Write a program that keeps the information about courses. Each course has a name and registered students.
# You will be receiving a course name and a student name until you receive the command "end".
# You should register each user into the corresponding course. If the given course does not exist, add it.
# When you receive the command "end", print the courses with their names and total registered users. For each course, print the registered users.

courses = {}

while True:
    current_line = input().split(" : ")

    if current_line[0] == "end":
        break

    course = current_line[0]
    name = current_line[1]

    if course not in courses.keys():
        courses[course] = []

    courses[course].append(name)

for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")
        