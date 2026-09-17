names = ["Lamport", "Von Neumann", "Abelson", "Van Rossum", "Ritchie", "Thompson"]

# 1. Iterate over the names collection
for name in names:
	# print(name)
	print(name.center(50, '-'))

# 2. Sort names alphabetically
names.sort()

for name in names:
	# print(name)
	print(name)

# 3. Find the index of "Van Rossum" in the SORTED LIST!
index = names.index("Van Rossum")
print(index)

# 4. Remove the last element and store it in last_item
print(names.pop())
print(names, len(names))

# 5. Remove all elements from the list
names.clear()
print(names, len(names))


