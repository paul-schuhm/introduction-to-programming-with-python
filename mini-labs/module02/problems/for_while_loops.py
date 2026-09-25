print("1.\n")
for x in range(1,11):
	print(x)


print("2.\n")
for x in range(0, 16, 2):
	print(x)

print("3.\n")
for x in range(1,9):
	print(2**x)


print("4.\n")
for x in range(1,9):
	print(1 if x % 2 != 0 else -1)

print("5.\n")
for x in range(1,9):
	print("Yes" if x % 2 != 0 else "No")

print("6.\n")
extra = 0
for x in range(1, 9):
	if(x % 2 == 0):
		result = "Yes" + extra * "s"
	else:
		result = "No" + extra * "o"
	print(f"{result}")
	extra += 1
	
	
	
