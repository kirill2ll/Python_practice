# Judge statistics on the last Programing Fundamentals exam were not working correctly, so you have the task of taking all the submissions and analyzing them properly. You should collect all the submissions and print the final results and statistics about each language in which the participants submitted their solutions.
# You will be receiving lines in the following format: "{username}-{language}-{points}" until you receive "exam finished". You should store each username and their submissions and points. If a student has two or more submissions for the same language, save only his maximum points.
# You can receive a command to ban a user for cheating in the following format: "{username}-banned". In that case, you should remove the user from the contest but preserve his submissions in the total count of submissions for each language.




submissions = {}
results = {}

while True:
    current_line = input().split("-")

    if current_line[0] == "exam finished":
        break

    user_name = current_line[0]
    language = current_line[1]

    if language != "banned":
        score = int(current_line[2])

        if user_name not in results.keys():
            results[user_name] = score

        if results[user_name] < score:
            results[user_name] = score

        if language not in submissions.keys():
            submissions[language] = 0
        submissions[language] += 1

    else:
        #banned
        results.pop(user_name)

#printing
print("Results:")
for user_name, points in results.items():
    print(f"{user_name} | {points}")

print("Submissions:")
for course, submission in submissions.items():
    print(f"{course} - {submission}")

