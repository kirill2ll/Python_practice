# Write a function that, depending on the first line of the input, reads one of the following strings: "int", "real", or "string".
# If the data type is an int, multiply the number by 2.
# If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
# If the data type is a string, surround the input with "$".
# Print the result on the console.



def data_manipulation(type_of_data, data):
    if type_of_data == "string":
        return f"${data}$"
    elif type_of_data == "int":
        return int(data) * 2
    elif type_of_data == "real":
        return f"{(float(data) * 1.5):.2f}"

type_of_data = input()
data = input()

print(data_manipulation(type_of_data, data))