# Write a function that checks if a given password is valid. Password validations are:
# It should be 6 - 10 (inclusive) characters long
# It should consist only of letters and digits
# It should have at least 2 digits
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
# "Password must be between 6 and 10 characters"
# "Password must consist only of letters and digits"
# "Password must have at least 2 digits"


def password_validator(password):
    is_valid = True
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False

    digit_count = 0
    for i in range(len(password)):
        if password[i].isdigit():
            digit_count += 1

        if digit_count >= 2:
            break
    if digit_count < 2:
        print("Password must have at least 2 digits")
        is_valid = False

    if is_valid:
        print("Password is valid")


my_pass = input()
password_validator(my_pass)
