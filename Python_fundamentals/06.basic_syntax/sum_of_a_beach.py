#Beaches are filled with sand, water, fish, and sun. Given a string, calculate how many times the words "Sand", "Water", "Fish", and "Sun" appear (case insensitive).



# first solution:

# word = input().lower()
# sun_arr = word.split("sun")
# sand_arr = word.split("sand")
# fish_arr = word.split("fish")
# water_arr = word.split("water")
#
# sum_of_words = len(sun_arr) + len(sand_arr) + len(fish_arr) + len(water_arr) - 4
#
# print(sum_of_words)

#======================
# 2nd solution:

word = input().lower()

words = ["sun", "sand", "fish", "water"]
sum_of_words = 0

for each_word in words:
    arr = word.split(each_word)
    sum_of_words += len(arr) - 1

print(sum_of_words)
