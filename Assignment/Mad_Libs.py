#  Step 1: Get user input
name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
food = input("Enter a food: ")

# Step 2: Create the story
story = f"""
One day, {name} went to {place} for a picnic. 
There they saw a {adjective} {animal} trying to {verb} a basket of {food}. 
It was the funniest thing {name} had ever seen!
"""

# Step 3: Print the story
print("\n--- Your Mad Libs Story ---")
print(story)
