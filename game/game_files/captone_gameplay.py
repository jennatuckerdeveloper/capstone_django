from random import randrange, choice, randint

from .python_capstone import Character, Item, Food, Inventory, Place, Occurrence, Landmark

"""
Game play:
"""

print("Welcome to PDX Trail!")

#Add a try / except.  You can choose an incorrect key and not get an inventory.

difficulty = input(   """
                            You will lead a team of five to Portland.
                            Do you want to be:
                            1.  A homesteader with a packing lama.  
                            2.  A former tech worker with lots of camping gear.
                            3.  A confident person with scavenged gear.  
                            """)

"""
Limits inventory and sets difficulty level.  
Includes 5 spaces for characters.  
"""

if difficulty == "1":
    player_inventory = Inventory(19)
elif difficulty == "2":
    player_inventory = Inventory(15)
elif difficulty == "3":
    player_inventory = Inventory(11)

print("You will lead your team.")
name1 = Character("You")
name2 = Character(input("Choose a second character name: "))
name3 = Character(input("Choose a third character name: "))
name4 = Character(input("Choose a fourth character name: "))
name5 = Character(input("Choose a fifth character name: "))

print("\n")

"""
Instantiates an inventory for the player.
Loads the 5 characters into the inventory.
"""

player_inventory.get_item(name1)
player_inventory.get_item(name2)
player_inventory.get_item(name3)
player_inventory.get_item(name4)
player_inventory.get_item(name5)


"""
Creates an initial inventory to use in loading player inventory.
"""

print("Before you head out, you have to decide what to bring. \n")

initial_inventory = Inventory()
food = Food()
cd = Item("cd", "a cd")
energy = Item("solar panel", "a solar panel")

food_stores = 0
while food_stores <= 10:
    food = Food()
    initial_inventory.get_item(food)
    food_stores += 1

initial_inventory.get_item(energy)
initial_inventory.get_item(cd)

print("You have the following stores to choose from: ")
initial_inventory.list_inventory()
print("\n")


while True:
    print("Your pack has: ")
    for i in player_inventory.inventory:
        if i.type != "character":
            print(i)
    try:
        item = input("What do you want to pack? \nEnter 2 to unpack an item. \nEnter item or 'ready' to depart: ")
        player_inventory.pack_item(initial_inventory, item)
    except ValueError:
        continue
    if item == "2":
        try:
            item = input("What do you want to unpack? ")
            initial_inventory.pack_item(player_inventory, item)
        except ValueError:
            continue
    if item == "ready":
        ready = input("Are you ready to depart? y/n? ")
        if ready == "n":
            continue
        if ready == "y":
            break

mile_counter = 0
day_counter = 0
last_milestone = "start"

while True:
    try:
        play = input("""
                What do you want to do? 
                1) Walk on.
                2) Take some rest.
                3) Scavenge / forage nearby area.
                4) Search through packs.  
                5) Look at the map.
                6) Quit 
              
            """)
    except ValueError:
        continue

    if play == "1":
        try:
            mile_counter += randint(12, 22)
        except:
            import pdb; pdb.set_trace()
        day_counter += 1
        print("{} days on the trail.  {} miles covered.".format(day_counter, mile_counter))
        for i in player_inventory.inventory:
            if i.type == "character":
                i.description -= 5


        for x in player_inventory.inventory:
            if x.type == "food":
                player_inventory.inventory.remove(x)
                break

        else:
            print("You have run out of food.")
            for i in player_inventory.inventory:
                if i.type == "character":
                    i.description -= 20
                    print(i)

        if any(x.type == "character" for x in player_inventory.inventory):
            temp = []
            for i in player_inventory.inventory:
                if i.type == "character":
                    temp.append(i)
            for i in temp:
                if i.description <= 0:
                    if i.name != "You":
                        print("{} has died of hunger and exhaustion.".format(i.name))
                        player_inventory.inventory.remove(i)
                        player_inventory.limit -= 1
                    if i.name == "You":
                        print("You have died of hunger and exhaustion.")
                        quit()

        # if not any(x.type == "character" for x in player_inventory.inventory):
        #         print("Your team has died.")
        #         quit()

        luck = randint(1, 20)

        if luck == 1:
            happening = Occurrence(player_inventory)
            happening.theft()

        if luck == 2:
            happening = Occurrence(player_inventory)
            happening.depression()

        if luck == 3:
            happening = Occurrence(player_inventory)
            happening.rain()

        milestones = [[50, "Salem"], [37, "Eugene"], [23, "Oregon Border"], [0, "start"]]

        for x in range(len(milestones) - 1):
            if mile_counter >= milestones[x][0] and last_milestone == milestones[x + 1][1]:
                ms = Landmark(milestones[x][1], player_inventory)
                ms.arrive()
                last_milestone = milestones[x][1]
            # Will likely error at the end of the game without another line of code.

    elif play == "2":
        days = input("How many days do you want to rest? ")
        day_counter += int(days)
        for i in player_inventory.inventory:
            if i.type == "character":
                if i.description < 100:
                    i.description += (20 * int(days))
                if i.description > 100:
                    i.description = 100

    elif play == "3":
        places = ["camp", "hotel", "pack"]
        #The places list matches the places list in the Place class.
        find = Place(choice(places))
        print(find)

        decision = input("Do you want to take what you found? ")
        if decision == "y":
             player_inventory.pack_item(find.inventory, find.finds)
        else:
            continue

        #How can I limit the number of time this can be done in a row?

    elif play == "4":
        player_inventory.list_inventory()

    elif play == "5":
        pass
        #map goes last along with other graphics

    elif play == "6":
         quit()


# noinspection PyUnreachableCode

"""



"""