# Write a Python program that accepts a sequence of comma-separated numbers
# from the user and generates a list and a tuple of those numbers

user_input = input("Enter a sequence of comma-separated numbers: ")

# Simplest version (integers only and triming)
numbers=[]

# Naive.
for item in user_input.split(','):
    value = item.strip()
    if value:
        if "." in value:
            numbers.append(float(value)) #value is a string!
        else:
            numbers.append(int(value))

# More compact
# for item in user_input.split(','):
#     value = item.strip()
#     if value:
#         numbers.append(float(value)) if "." in value else numbers.append(int(value)) #short if/else notation

# print("List:", numbers)
# print("Tuple:", tuple(numbers))

# == More advanced and idiomatic version, using list comprehension syntax

# Handle extra spaces, float numbers and extra white spaces and empty numbers
# 
# numbers_list = [
#     float(item.strip()) if "." in item else int(item.strip()) 
#     for item in user_input.split(',')
#     if item.strip()
# ]

# print("List:", numbers_list)
# print("Tuple:", tuple(numbers_list))

