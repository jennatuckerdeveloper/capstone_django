"""

7 classes form the foundation for PDX Trail:
    Character
    Item
    Food(Item)
    Inventory
    Place
    Occurrence
    Landmark

"""

from random import randrange

"""
Creates characters each with their own names and health scores (descriptions).
"""

class Character:


    """
    Characters begin with a health score (description) of 100.
    """

    def __init__(self, name, description=100):
        self.name = name
        self.description = description
        self.type = "character"

    """
    The __str__ function prints a readable description of characters' health status.
    """

    def __str__(self):
        if self.name == "You":
            if 0 < self.description <= 25:
                return "{} are in poor health.".format(self.name)
            elif 26 <= self.description <= 50:
                return "{} are in fair health.".format(self.name)
            elif 51 <= self.description <= 75:
                return "{} are in decent health.".format(self.name)
            elif 76 <= self.description <= 100:
                return "{} are in good health.".format(self.name)
        else:
            if 0 < self.description <= 25:
                return "{} is in poor health.".format(self.name)
            elif 26 <= self.description <= 50:
                return "{} is in fair health.".format(self.name)
            elif 51 <= self.description <= 75:
                return "{} is in decent health.".format(self.name)
            elif 76 <= self.description <= 100:
                return "{} is in good health.".format(self.name)

    """
    The __repr__ function shows characters printed in a list as their names.
    """

    def __repr__(self):
        return str(self.name)

        # The character is not yet removed from the player inventory.


"""
The Item class creates Items with unique names and descriptions and a default type.
"""

class Item:
    def __init__(self, name, description, type="item"):
        self.name = name
        self.description = description
        self.type = type

    """
    Prints a readable version of the Item's name: description.  
    """
    def __str__(self):
        return "{}: {}".format(self.name, self.description)

    """
    Prints the item's name when the Item is printed in a list.  
    """
    def __repr__(self):
        return str(self.name)
        # return self.__str__()

"""
Food Items have a default name, description, and type.  
"""
class Food(Item):
    def __init__(self):
        super().__init__(name="Food", description="A day's food for your group.", type="food")

"""
An Inventory has an inventory list and a limit to the number of Items it can hold.
"""

class Inventory:
    def __init__(self, limit=None):
        self.inventory = []
        self.limit = limit

    """
    The get_item function takes an Item or returns a message if the Inventory is full.
    """
    def get_item(self, item):
        if self.limit is not None:
            if len(self.inventory) <= self.limit:
                self.inventory.append(item)
            elif len(self.inventory) > self.limit:
                print("You don't have enough room. ")
        else:
            self.inventory.append(item)

    """
    The pack_item function moves an Item from one Inventory to another.  
    """
    def pack_item(self, source, item):
        for x in source.inventory:
            if x.name == item:
                self.get_item(x)
                source.inventory.remove(x)
                break

    """
    The list_inventory function prints each Item in the Inventory.  
    """
    def list_inventory(self):
        for each in self.inventory:
            print(each)

"""

"""
class Place:
    def __init__(self, name, inventory=Inventory()):
        places = {"camp": "a camp", "hotel": "a hotel", "pack": "a pack"}
        finds = {"camp": Food(), "hotel": Item("bible", "a Gideon Bible"), "pack": Item("cd", "a cd")}
        self.inventory = inventory
        self.name = name
        self.description = places[name]
        self.finds = finds[name]
        self.inventory.get_item(self.finds)

    def __str__(self):
        return "You come across a {} and find: \n{}".format(self.description, self.finds.description)


class Occurrence:
    def __init__(self, supplies):
        self.supplies = supplies

    def theft(self):
        loss = []
        luck = randrange(1, 3)
        while luck > 0:
            for x in self.supplies.inventory:
                if x.type != "character":
                    if luck > 0:
                        loss.append(x)
                        self.supplies.inventory.remove(x)
                    luck -= 1
        print("A thief comes in the night and steals the following: ")
        for i in loss:
            print("{}".format(i))

    def depression(self):
        for x in self.supplies.inventory:
            if x.type == "character":
                if x.name == "You":
                    print("{} are depressed".format(x.name))
                    x.description -= 15
                else:
                    print("{} is depressed.".format(x.name))
                    x.description -= 15
                break

    def rain(self):
        print("A cold rain comes.")
        for x in self.supplies.inventory:
            if x.type == "character":
                x.description -= 10


class Landmark:
    def __init__(self, name, supplies):
        self.name = name
        self.supplies = supplies

        landmarks = {"Oregon Border":
                         {"story": "You make camp on ",
                          "pack": "food",
                          "gain": Food(),
                          "loss": Food(),
                          "story_loss": "You lose one day's food.",
                          "story_gain": "After finding the Bible in your packs, the group allows you to rest on their land and offers you a gift of food to help you on your way."
                          },
                     "Eugene":
                         {"story": "You have reached Eugene.",
                          "pack": "",
                          "gain": Item("cd", "a cd"),
                          "loss": Food(),
                          "story_loss": "You lose one day's food.",
                          "story_gain": "You receive a CD.",
                          },
                     "Salem":
                         {"story": "You have reached Salem.",
                          "pack": "",
                          "gain": Item("book", "a book"),
                          "loss": Food(),
                          "story_loss": "You lose a day's food.",
                          "story_gain": "You receive a book.",
                          },
                     }
        self.story = landmarks[name]["story"]
        self.gain = landmarks[name]["gain"]
        self.loss = landmarks[name]["loss"]
        self.story_loss = landmarks[name]["story_loss"]
        self.story_gain = landmarks[name]["story_gain"]
        self.pack = landmarks[name]['pack']

    def outcome(self):
        """ The outcome function checks a character's inventory for the key associated with a Landmark
        Whehther the key is present in the inventory then calls a loss or a gain to the inventory.
        Do I need three functions to affect inventories, characters, etc like with luck?
        """
        have = []
        for x in self.supplies.inventory:
            if x.type == self.pack:
                have.append(x)

        if len(have) > 0:
            self.supplies.get_item(self.gain)
            print(self.story_gain)

        else:
            try:
                self.supplies.inventory.remove(self.loss)
                print(self.story_loss)
            except ValueError:
                pass

    def arrive(self):
        print(self.story)
        self.outcome()