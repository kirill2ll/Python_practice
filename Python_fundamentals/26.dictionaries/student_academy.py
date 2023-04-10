# Write a program that keeps the information about students and their grades.
# On the first line, you will receive an integer number representing the next pair of rows. On the next lines, you will be receiving each student's name and their grade.
# Keep track of all grades for each student and keep only the students with an average grade higher than or equal to 4.50.
# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.


number_of_lines = int(input())
academy_total_grades = {}
academy_total_grades_count = {}

for i in range(number_of_lines):
    name = input()
    grade = float(input())

    if name not in academy_total_grades.keys():
        academy_total_grades[name] = 0
        academy_total_grades_count[name] = 0
    academy_total_grades[name] += grade
    academy_total_grades_count[name] += 1

for name, grade in academy_total_grades.items():
    average_grade = academy_total_grades[name]/academy_total_grades_count[name]
    if average_grade >= 4.5:
        print(f"{name} -> {average_grade:.2f}")

