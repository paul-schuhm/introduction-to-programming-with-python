"""
This program draws a triangle
of a given size, alternating characters 
on each line
"""

SIZE=20
CHAR_A='a'
CHAR_B='b'

for line in range(SIZE):
    for col in range(line):
        if(line % 2 == 0):
            # Note: print put a newline by default ("\n"), we disable this
            # setting the end parameter to an empty string
            print(CHAR_A, end="")
        else:
            print(CHAR_B, end="")
    print("") # Print a newline



