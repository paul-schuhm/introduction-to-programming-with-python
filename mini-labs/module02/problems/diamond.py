MAX_SIZE = 20

size_input = input("Enter the upper size of the diamond: ")
size = int(size_input)

if size > MAX_SIZE or size < 1:
    print(f"Error: The size must be between 1 and {MAX_SIZE} lines.")
else:
    # Upper half (including the middle line)
    for i in range(1, size + 1):
        spaces = " " * (size - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

    # Lower half
    for i in range(size - 1, 0, -1):
        spaces = " " * (size - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)