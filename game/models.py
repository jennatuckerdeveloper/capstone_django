from django.db import models
from random import randrange, choice
from authentication.models import User

class Character(models.Model):

    name = models.CharField(max_length=100)
    description = models.IntegerField(default=100)
    inventory = models.ForeignKey("Inventory", related_name="characters", blank=True, null=True)

    """
    The __str__ function prints a readable description of characters' health status.
    """

    def describe(self):
        return self.__str__()

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

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    inventory = models.ForeignKey("Inventory", related_name="items", blank=True, null=True)
    landmark = models.ForeignKey("Landmark", related_name="landmark", blank=True, null=True)

    """
    Prints a readable version of the Item's name: description.  
    """
    def __str__(self):
        return "{}: {}".format(self.name, self.description)

    """
    Prints the item's name when the Item is printed in a list.  
    """
    def __repr__(self):
        return self.name
        # return self.__str__()

"""
An Inventory has an inventory list and a limit to the number of Items it can hold.
"""

#This one needs a lot of work

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=200, default="active")
    limit = models.IntegerField(blank=True, null=True)

    day_counter = models.IntegerField(default=0)
    mile_counter = models.IntegerField(default=0)
    last_milestone = models.CharField(max_length=200, default="start")

    food_warning = models.CharField(max_length=500, default="", blank=True, null=True)
    death = models.TextField(max_length=5000, default="", blank=True, null=True)
    happening = models.CharField(max_length=500, default="", blank=True, null=True)
    landmark = models.CharField(max_length=500, default="", blank=True, null=True)
    find = models.CharField(max_length=500, default="", blank=True, null=True)
    play_message = models.CharField(max_length=500, default="", blank=True, null=True)

    def __str__(self):
        return "{}: {}".format(self.name, self.items.all())

    def __repr__(self):
        return self.name
        # return self.__str__()

    """
    The list_inventory function prints each Item in the Inventory.  
    Kept for testing.  Should be unncessary after Django refactoring.
    """

    def list_inventory(self):
        for each in self.items.all():
            print(each)

    def theft(self):
        print("Theft triggered")
        luck = randrange(1, 3)
        loss = []
        for x in self.items.all():
            if luck > 0:
                loss.append(x)
                luck -= 1
        # print('after loop luck: {}'.format(luck))
        message = "A thief comes in the night and steals the follow items: "
        details = []
        for x in loss:
            x.inventory = None
            x.save()
            details.append(x.name)
        for x in details:
            message = message + "(" + x + ") "
            self.happening = message
        self.save()


    def depression(self):
        print("Depression triggered.")
        people = []
        for x in self.characters.all():
            people.append(x.name)
        person = choice(people)
        depressed = self.characters.filter(name=person)
        for i in depressed:
            if i.name == "You":
                self.happening = "{} are depressed.".format(i.name)
                self.save()
                if i.description >= 20:
                    i.description -= 15
                    i.save()
                else:
                    i.description = 5
                    i.save()
            else:
                self.happening = "{} is depressed.".format(i.name)
                self.save()
                if i.description >= 20:
                    i.description -= 15
                    i.save()
                else:
                    i.description = 5
                    i.save()

    def rain(self):
        print("Rain triggered.")
        message = "A cold rain comes."
        self.happening = message
        self.save()
        for x in self.characters.all():
            x.description -= 10

#Place are Inventories of Items with unique names.
# If the user chooses to take Items from the inventory, the Item's inventory = changes.

class Landmark(models.Model):
    name = models.CharField(max_length=100)

    """
    Landmarks will be systematically generated.  
    The will have a name based on the place.
    Items will be systematically generated and connected to Landmarks by FK.
    """
