# This program procedurally generates band names based on a simple template "The {adjective} {noun}"
import random

def find_adjectives():
    adjectives = ["green", "fearless", "angry", "lunar", "beautiful", "silent", "dark", "last", "first", "crazy", "terrible", "terrifying", "dark", "sunny", "lost", "big", "legit", "silent"]
    return adjectives

def find_nouns():
    nouns = ["cat", "car", "guitar", "human", "hole", "adventurer", "star", "bird", "rocker", "businessman", "dog", "project" , "forest", "city", "humans", "body", "floor"]
    return nouns

def generate_bandnames(quantity, adjectives, nouns):
    if quantity <= 0: return None
    bandnames = []
    for i in range(quantity):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        bandname = f"The {adjective.capitalize()} {noun.capitalize()}"
        bandnames.append(bandname)
    return bandnames

def main():
    bandnames = generate_bandnames(10, find_adjectives(), find_nouns())
    for bandname in bandnames:
        print(bandname)

#Starting point of the program
main()
