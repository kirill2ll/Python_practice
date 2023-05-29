row, col = map(int, input().split())

#generate abc
abc = []
for i in range(0, 26):
    abc.append(chr(97+i))

for r in range(row):
    for c in range(col):
        cur_palindrome = abc[r] + abc[c+r] + abc[r]
        print(cur_palindrome, end=" ")

    print()