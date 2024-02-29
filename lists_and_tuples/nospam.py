menu = [
    ["egg", 'bacon'],
    ['egg', 'sausage', 'bacon'],
    ['egg', 'spam'],
    ['egg', 'bacon', 'spam'],
    ['egg', 'bacon', 'sausage', 'spam'],
    ['spam', 'bacon', 'sausage', 'spam'],
    ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'],
    ['spam', 'sausage', 'spam', 'bacon', 'spam', 'tomato', 'spam'],
]

# challenge to print out these lists but with spam removed
# method one - remove spam and then print list
# method two - print items in list as long as its not spam

# 1. Use reversed() not reverse
for meal in menu:
    top_ind = len(meal)-1
    for ind,item in enumerate(reversed(meal)):
        if item == 'spam':
            del meal[top_ind - ind]
    print(meal)
print(menu)

for meal in menu:
    for ind in range(len(meal) -1,-1,-1):
        if meal[ind] == 'spam':
            del meal[ind]
    print(", ".join(meal))

# 2.
for meal in menu:
    clean_meal = []
    for item in meal:
        if item != 'spam':
            clean_meal.append(item)
    print(clean_meal)

for meal in menu:
    for item in meal:
        if item != 'spam':
            print(item,end=", ")
    print()
