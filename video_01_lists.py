from csv import DictReader

# read a list of dictionaries from a CSV file
def get_list_of_dicts_from_csv(filename):
    with open(filename) as csvfile:
        return list(dict(row) for row in DictReader(csvfile))

foods = get_list_of_dicts_from_csv("foods.csv")

# Write some helper functions
def get_article(noun):
    "Returns the appropriate article (a or an) for a noun"
    if food['name'][0] in ['a', 'e', 'i', 'o', 'u']:
        return "An"
    else:
        return "A"

def describe(food):
    "Returns a string describing a food"
    a = get_article(food['name'])
    return "{} {} is {} and {}.".format(a, food['name'], food['color'], food['texture'])

# Iterate through a list
print("FOOD DESCRIPTIONS")
for food in foods:
    print(describe(food))

# Transform (map) a list
def i_like(food):
    "Returns True or False, depending on whether I like the food"
    return food['texture'] == 'crisp'

def reaction(food):
    "Returns a string with my reaction to the food"
    if i_like(food):
        return "I love it."
    else:
        return "I find it revolting."
    
def review(food):
    "Returns a string decribing the food and my reaction to it"
    return describe(food) + " " + reaction(food)

reactions = []
for food in foods:
    reactions.append(review(food))

# Another way to do the same thing
reactions = [review(food) for food in foods]

print()
print("FOOD REVIEWS")
for r in reactions:
    print(r)

# Filter a list
foods_i_like = []
for food in foods:
    if i_like(food):
        foods_i_like.append(food)

# Another way to do the same thing
foods_i_like = [food for food in foods if i_like(food)]

print()
print("FOODS I LIKE")
for food in foods_i_like:
    print(describe(food))

print()
print("REVIEWS OF FOODS I LIKE")
for review in [review(food) for food in foods if i_like(food)]:
    print(review)
