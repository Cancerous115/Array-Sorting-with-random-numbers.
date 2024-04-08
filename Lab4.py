
nights = int(input("Number of nights:"))
p = int(input("Number of people:"))
# used '\n' to space out each string
r = int(input("(1) - Two Queen Beds" + '\n'
 "(2) - One King Bed" + '\n'
 "(3) - Queen Suite" + '\n'
"(4) - King Suit" + '\n'
"Select Type:"))
#function for our room cost per night
def function_roomCost(r,nights):
    ro = r * nights
    return ro
# if statement giving each room selection a integer value
if r == 1:
    r = 375
elif r == 2:
    r = 350
elif r == 3:
    r = 525
else:
    r = 475



b = int(input("How many Brunches:"))
d = int(input("How many Dinners:"))
#formula for our meal cost and a mealCost function
def function_mealCost(meal,meald):
    m = meal + meald
    return m
meal = b * 25 + d * 75
meald = meal * 0.15



# Giving each excursion a integer value, only if true (Y or y)
#Created funciton for our excursion cost
def function_excursionCost(pic, s, g,bo):
    x = pic + s + g + bo
    return x
pic = input("Picnic?:")
if pic == 'y' or pic == 'Y':
    pic = 50
else:
    pic =0
s = input("Snorkeling?:")
if s == 'y' or s == 'Y':
    s = 25 * p
else:
    s = 0
g = input("Guided Hike?:")
if g == 'y' or g == 'Y':
    g = 17 * p
else:
    g = 0
bo = input("Boat Dinner?:")
if bo == 'y' or bo == 'Y':
    bo = 200
else:
    bo =0


totalCost = function_excursionCost(pic,s,g,bo) + function_roomCost(r,nights) + function_mealCost(meal,meald)

# print each total amount for cost))
print("room cost:$", function_roomCost(r,nights))
print("meal cost:$", function_mealCost(meal,meald))
print("excursion cost:$", function_excursionCost(pic,s,g,bo))

print("Total cost:$", totalCost)