
import random
#Player stats
deff = 0
atk = 1
health = 100
shield = 50
inv = []
equip = []
max_inv = 10
#Bag Setup
bags_inv = ("Drooma", "Pointard", "Food", "Sword", "Wits", "Ring",
             "Bubble Fruit")
max_bags = 5
items = random.randint(1, max_bags)
bags = []
for i in range (items):
    bags.append (random.choice(bags_inv))
#This is where you pick what items you want and use them
if inv:
    print(inv)
else:
    print("You have nothing, you left it all at the campsite")
    input("Visit local tavern to restock")
    for items in bags:
        inv.append(items)

for items in inv:
    if items == "healing potion":
        health += 50
        inv.remove("healing potion")
    if items == ("Bubble Fruit"):
        health += 70
        inv.remove("Bubble Fruit")

for items in inv:
    if i == "Shield":
        print("You put on a shield")
        deff += 50
        equip.append("Shield")
        inv.remove("Shield")
    if i == "Ring":
        print("You showed the ring to survive")
        deff += 25
        inv.remove("Ring")

for items in inv:
    if i == "Poniard":
        print("You pulled out your poniard")
        deff += 30
        inv.remove("Poniard")
    if i == "Sword":
        print("You pulled out your sword")
        deff += 25
        inv.remove("Sword")
    if i == "Orantium":
        print("You pulled your orantium out")
        deff +=20
        inv.remove("Orantium")
    if i == "Wits":
        print("You used your wits")
        deff += 50
        inv.remove("Wits")

print(health)
print(equip)
print(inv)
#You have to run away from your campsite and have to leave items behind. This allows you to pick what you lose.
max_bags = 15
items = random.randint(1,max_bags)
bags = []
for i in range (items):
    bags.append(random.choice( bags_inv))

input ("Press enter to open chest")
for i in bags:
    inv.append(i)

if len(inv) > max_inv:
    x =  len(inv) - max_inv
    print(inv)
    print("You need to remove " +str(x)+" items")
    while x > 0:
        item = input("What item do you want to remove")
        inv.remove(item)
        x -=1
    print(inv)






