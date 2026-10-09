"""
(This is just a multiline comment, ignored by the interpreter)

We have a list of cats described by 1) a name 2) a color
We want to know:
1. the names of black cats only
2. the names of black or orange cats
"""

# Start of the program

# Data
cats = [
        {
            "name": "Lylyth",
            "color": "black"
            },
        {
            "name": "Puik-Puik",
            "color": "grey"
            },
        {
            "name": "Mimoune",
            "color": "orange"
            },
        {
            "name": "Le petit chat",
            "color": "black"
            },
        ]

# Find all black cats

# Our selection initialized to an empty list
selected = []

for cat in cats:
    if(cat['color'] == 'black'):
        #If the cat is black, add its name to our black cat list
        selected.append(cat['name'])

print("Here are the black cats:")
for cat in selected:
    print(cat)

# Find all black OR orange cats. Let's reset our selection:
selected = []

for cat in cats:
    if(cat['color'] == 'black' or cat['color'] == 'orange'):
        selected.append(cat['name'])

print("Here are the black or orange cats:")
for cat in selected:
    print(cat)

"""
Notice how we are repeating ourselves here! Same code is used again and again.
Maybe we should write a procedure/function to select cats based on their colors.
"""
def select_cats(cats, colors):
    "Return a list of cat that are at least one of the colors"
    selection = []
    for cat in cats:
        if cat['color'] in colors:
            selection.append(cat['name'])
    return selection


# Now we can use this function, again and again, for different use cases!

selection = select_cats(cats, ['black', 'orange'])
print(selection)

selection = select_cats(cats, ['black'])
print(selection)

selection = select_cats(cats, ['grey'])
print(selection)
