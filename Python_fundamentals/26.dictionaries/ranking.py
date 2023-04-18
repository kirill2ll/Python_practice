# Here comes the final and the most interesting part – the Final ranking of the candidate-interns. The final ranking is determined by the points of the interview tasks and by the points from the exams in SoftUni. Here is your final task. You will receive some lines of input in the format "{contest}:{password for contest}" until you receive "end of contests". Save that data because you will need it later. After that you will receive other type of inputs in format "{contest}=>{password}=>{username}=>{points}" until you receive "end of submissions". Here is what you need to do.
# Check if the contest is valid (It is considered valid if you received it in the first type of input)
# Check if the password is correct for the given contest
# If the contest and the password is valid, save the user with the contest they take part in (a user can take part in many contests) and the points the user has in the given contest. If you receive the same contest and the same user update the points only if the new ones are more than the older ones.
# In the end, you should print the info for the user with the most points (total points for all contents they participated in) in the format "Best candidate is {user} with total {total_points} points.". After that print all students ordered by their names. For each user print each contest with the points in descending order. See the examples.

def read_contests(contests):
    while True:
        current_input = input()
        if current_input == "end of contests":
            break

        course = current_input.split(":")[0]
        password = current_input.split(":")[1]

        contests[course] = password

    return contests


def course_is_valid(course, password):
    if course in contests.keys():
        if contests[course] == password:
            return True

    return False


def read_submissions(submissions):
    while True:
        current_input = input().split("=>")
        if current_input[0] == "end of submissions":
            break

        course = current_input[0]
        password = current_input[1]

        if (course_is_valid(course, password)):
            student_name = current_input[2]
            points = int(current_input[3])

            if student_name not in all_stats.keys():
                all_stats[student_name] = {}
            if course not in all_stats[student_name]:
                all_stats[student_name][course] = 0
            if points > all_stats[student_name][course]:
                all_stats[student_name][course] = points

    return all_stats

#dictionary in dictionary
all_stats = {}

contests = {}

contests = read_contests(contests)

all_stats = read_submissions(all_stats)

#sorted(all_stats)


def find_best_student(all_stats):
    best_student = None
    best_points = 0

    for names, courses in all_stats.items():
        current_points = 0

        for course, points in courses.items():
            current_points += points

        if current_points > best_points:
            best_points = current_points
            best_student = names


    return  best_student, best_points


best_student, best_points = find_best_student(all_stats)

print(f"Best candidate is {best_student} with total {best_points} points.")
print("Ranking:")
for name, dict in sorted(all_stats.items()):

    sorted_dict = sorted(dict.items(), key=lambda x:-x[1])

    print(name)
    for course, points in sorted_dict:
        print(f"#  {course} -> {points}")



