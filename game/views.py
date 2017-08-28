from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .models import Item, Inventory, Character, Landmark
from authentication.models import User
from django.http import JsonResponse
from random import randrange, choice, randint

"""

From play screen 3) Scavenge / forage: 
    check limit 
    ability to drop items
    abililty to choose 

Put limit of 5 characters.  

"""

place_list = {
    "camp":
        {"description": "a camp",
         "find_name": "food",
         "find_description": "a day's food",
         },
    "hotel":
        {"description": "a hotel",
         "find_name": "Bible",
         "find_description": "a Gideon Bible"
         },
    "pack":
        {"description": "a pack",
         "find_name": "cd",
         "find_description": "a cd"
         }
}

landmarks = {"Oregon Border":
                 {
                     "story": "You have reached the Oregon Border.  You accidentally make camp on private property owned by a separatist religous group.",
                     "key": "Bible",
                     "gain": "food",
                     "loss": "food",
                     "story_loss": "The group asks for a tithe of your food stores.  You lose one day's food.",
                     "story_gain": "After finding a Bible in your packs, the group allows you to rest on their land and offers you a gift of food to help you on your way."
                     },
             "Eugene":
                 {"story": "You have reached Eugene.  You run into another party of campers.  They have fallen on especially hard times.",
                  "key": "Bible",
                  "gain": "cd",
                  "loss": "food",
                  "story_loss": "You give them one day's food.",
                  "story_gain": "They give you a cd from a stash they found scavening in an abandoned trailer, since the full load is too heavy to carry."
                  },
             "Salem":
                 {"story": "You have reached Salem.  A homesteader lets your party stay on their land and taps a keg of homebrew.",
                  "key": "Bible",
                  "gain": "book",
                  "loss": "food",
                  "story_loss": "You lose a day's food throwing up.",
                  "story_gain": "You are given a book on identifying edible wild mushrooms.",
                  },
             }

item_list = {'food': 'A parcel containing a day\'s food rations for your team.',
             'Bible': 'A Gideon Bible',
             'solar panel': 'A portable solar charging panel',
             }

# """This helper function creates the initial inventory in packing view. """
#
#
# def create_initial_inventory():
#     initial_inv = Inventory.objects.create(name="initial_inv")
#     items = []
#     for x in beginning_inventory.keys():
#         items.append(x)
#     for x in range(len(beginning_inventory)):
#         if items[x] != "food":
#             name = Item.objects.create(name=items[x], description=beginning_inventory[items[x]], inventory=initial_inv)
#         if items[x] == "food":
#             y = 0
#             while y < 5:
#                 name = Item.objects.create(name=items[x], description=beginning_inventory[items[x]],
#                                            inventory=initial_inv)
#                 y += 1
#     return initial_inv

"""This helper function creates all the place inventories and found items in play view."""


def create_place_inventories(place_inventory):
    places = place_list.keys()
    for place in places:
        find = Item.objects.create(name=place, description=place_list[place],
                                   inventory=place_inventory)


def landmark_outcomes(name, player_inventory):
    milestone = landmarks[name]
    ldmk = Landmark.objects.create(name=name)
    find = Item.objects.create(name=milestone["gain"], description=milestone["gain"], landmark=ldmk, inventory=None)
    has_key = None
    for item in player_inventory.items.all():
        if item.name == milestone["key"]:
            has_key = True
            break
        else:
            has_key = False
    if has_key == True:
        find.landmark = None
        find.inventory = player_inventory
        find.save()
        player_inventory.play_message = milestone["story_gain"]
    if has_key == False:
        for item in player_inventory.items.all():
            if item.name == milestone["loss"]:
                item.inventory = None
                item.save()
                break
        player_inventory.play_message = milestone["story_loss"]


def gameplay(request):
    return render(request, 'game/gameplay.html', {})


def gameplay_entry(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        choice = request.POST.get("choice", None)
        limit = 0
        if choice == str(1):
            limit = 15
        if choice == str(2):
            limit = 10
        if choice == str(3):
            limit = 5
        inv = Inventory(name="player_inv", limit=limit)
        inv.save()
        user.game = inv
        user.save()
        return JsonResponse({'message': 'success',
                             'choice': choice
                             })
    return JsonResponse({'message': 'fail'})


# This needs a try/except to ensure it's one of these three.

def names(request):
    return render(request, 'game/names.html', {})


def names_entry(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        inv = user.game
        Character.objects.create(name="You", inventory=inv)
        Character.objects.create(name=request.POST.get('choice2', None), inventory=inv)
        Character.objects.create(name=request.POST.get('choice3', None), inventory=inv)
        Character.objects.create(name=request.POST.get('choice4', None), inventory=inv)
        Character.objects.create(name=request.POST.get('choice5', None), inventory=inv)
        user.save()
        inv.save()
        return JsonResponse({'message': 'success'})
    return JsonResponse({'message': 'fail'})


def show_game(request):
    user = User.objects.get(username=request.user.username)
    return render(request, 'pages/show_game.html', {'user': user})


# What is this function for?  Testing?



"""
The first version of packing and packing_entry created an initial inventory and changed inv to player inv.
"""


def packing(request):
    """
    This second version of the function needs a dictionary to print out the names of the items.
    """

    user = User.objects.get(username=request.user.username)
    player_inventory = user.game

    return render(request, 'game/packing.html', {'packed': player_inventory.items.all()})


def packing_entry(request):
    """
    This second version of the view function will need a dictionary to fill out descriptions.
    This or the next two functions need to set limit on player_inventory items.
    """
    if request.method == 'POST':

        user = User.objects.get(username=request.user.username)
        player_inventory = user.game
        to_pack = request.POST.get('choice', None)
        item_list_names = item_list.keys()
        for item in item_list_names:
            if to_pack == item:
                Item.objects.create(name=item, description=item_list[item], inventory=player_inventory)
        print(player_inventory)
        packed = []
        for i in player_inventory.items.all():
            packed.append(i.name)

        return JsonResponse({'message': 'success', 'packed': packed})
    return JsonResponse({'message': 'fail'})


def depart(request):
    user = User.objects.get(username=request.user.username)
    player_inventory = user.game
    limit = player_inventory.limit

    return render(request, 'game/depart.html', {"limit": limit, 'packed': player_inventory.items.all()})

    # The form on this page needs to allow the user to:
    #  remove items from the pack and return them to initial_inv.


def depart_entry(request):
    user = User.objects.get(username=request.user.username)
    player_inventory = user.game
    limit = player_inventory.limit

    if request.method == 'POST':
        print(player_inventory.items.all())
        unpack = request.POST.get("unpack", None)
        print(unpack)
        for i in player_inventory.items.all():
            if i.name == unpack:
                i.inventory = None
                i.save()
                break
        packed = []
        for i in player_inventory.items.all():
            packed.append(i.name)

        return JsonResponse({'message': 'success', 'packed': packed, 'limit': limit})
    return JsonResponse({'message': 'fail'})


def depart_check(request):
    if request.method == 'POST':

        user = User.objects.get(username=request.user.username)
        player_inventory = user.game
        limit = player_inventory.limit
        packed_items = []
        for i in player_inventory.items.all():
            packed_items.append(i.name)
        packed = len(packed_items)

        return JsonResponse({'message': 'success', 'limit': limit, 'packed': packed})
    return JsonResponse({'message': 'fail'})


def play(request):
    """This one is the heart of the game.
    Template:
        display mile_counter and day_counter (Do they need to be in the database to show in template?
        User needs to be able to:
            Walk
            Random events
            Forage / Scavenge (places)
            Landmarks
        This needs to allow the user to die / lose the game.
        This needs to allow the user to win.
    """

    user = User.objects.get(username=request.user.username)
    player_inventory = user.game

    if player_inventory.status == "active":

        place_inventory = Inventory.objects.create(name="place_inv")
        create_place_inventories(place_inventory)

        user = User.objects.get(username=request.user.username)
        player_inventory = user.game
        mile_counter = player_inventory.mile_counter
        day_counter = player_inventory.day_counter

        return render(request, 'game/play.html', {
            "mile_counter": mile_counter,
            "day_counter": day_counter,
        })
    elif player_inventory.status == "win":
        return render(request, 'game/win.html', {})

    elif player_inventory.status == "dead":
        return HttpResponseRedirect("/game/gameplay/")


def play_entry(request):
    user = User.objects.get(username=request.user.username)
    player_inventory = user.game

    if player_inventory.status == "active":

        player_inventory.play_message = ""
        player_inventory.food_warning = ""
        player_inventory.death = ""
        player_inventory.happening = ""
        player_inventory.landmark = ""
        player_inventory.find = ""
        player_inventory.save()

        characters = []
        for i in player_inventory.characters.all():
            characters.append(i.name + " : " + i.describe())

        packs = []
        for i in player_inventory.items.all():
            packs.append(i.name + " : " + i.description)

        """
        The day_counter and mile_counter track each play and a day's food is lost.  
        """

        if request.method == 'POST':
            if request.POST.get("move", None) == str(1):
                player_inventory.mile_counter += randint(12, 22)
                player_inventory.day_counter += 1
                player_inventory.save()

                for i in player_inventory.characters.all():
                    i.description -= 5
                    i.save()

                for i in player_inventory.items.all():
                    if i.name == "food":
                        i.inventory = None
                        i.save()
                        break
                else:
                    player_inventory.food_warning = "You have run out of food."
                    player_inventory.save()
                    for i in player_inventory.characters.all():
                        i.description -= 20
                        i.save()

                deaths = []
                for i in player_inventory.characters.all():
                    if i.description <= 0:
                        deaths.append(i)
                print(deaths)
                if len(deaths) > 0:
                    person = choice(deaths)
                    if person.name != "You":
                        person.inventory = None
                        person.save()
                        player_inventory.death = "{} has died of hunger and exhaustion.".format(person.name)
                        player_inventory.save()
                        deaths.remove(person)
                    if person.name == "You":
                        person.inventory = None
                        person.save()
                        player_inventory.death = "You have died of melancholy."
                        player_inventory.save()
                        deaths.remove(person)
                        player_inventory.status = "dead"
                        player_inventory.save()
                    for i in deaths:
                        i.description = 5
                        i.save()
                        print(i)

                if player_inventory.status != "dead":

                    """ The luck portion of play function creates random losses to inventory or individual or group health."""
                    luck = randint(1, 5)

                    if luck == 1:
                        player_inventory.theft()
                        player_inventory.save()

                    if luck == 2:
                        player_inventory.depression()
                        player_inventory.save()

                    if luck == 3:
                        player_inventory.rain()
                        player_inventory.save()

                    """ The landmark section of the play function creates a unique storyline based on player inv."""

                    milestones = [[100, "Salem"], [60, "Eugene"], [30, "Oregon Border"], [0, "start"]]

                    for x in range(len(milestones) - 1):
                        if player_inventory.mile_counter >= milestones[x][0] and player_inventory.last_milestone == \
                                milestones[x + 1][1]:
                            ms = Landmark(milestones[x][1], player_inventory)
                            player_inventory.landmark = (landmarks[milestones[x][1]]["story"])
                            player_inventory.save()
                            print(player_inventory.landmark)
                            player_inventory.last_milestone = milestones[x][1]
                            player_inventory.save()
                            landmark_outcomes(milestones[x][1], player_inventory)

                    if player_inventory.mile_counter > 160:
                        player_inventory.play_message = "You have reached the Portland metro area!"
                        player_inventory.status = "win"
                        player_inventory.save()

            if request.POST.get("move", None) == str(2):
                player_inventory.day_counter += 1
                player_inventory.save()
                for i in player_inventory.characters.all():
                    if i.description <= 100:
                        i.description += 20
                        i.save()
                    if i.description > 100:
                        i.description = 100
                        i.save()

            if request.POST.get("move", None) == str(3):
                places = []
                for i in place_list.keys():
                    places.append(i)
                find = choice(places)
                player_inventory.find = (
                "You find " + place_list[find]["description"] + " with " + place_list[find]["find_description"] + ".")
                player_inventory.save()
                gain = Item.objects.create(name=place_list[find]["find_name"], inventory=player_inventory)

                # Add decision
                # Add ability to unpack item

            return JsonResponse({
                'message': 'success',
                "mile_counter": player_inventory.mile_counter,
                "day_counter": player_inventory.day_counter,
                "play_message": player_inventory.play_message,
                "food_warning": player_inventory.food_warning,
                "death": player_inventory.death,
                "happening": player_inventory.happening,
                "find": player_inventory.find,
                "landmark": player_inventory.landmark,
                "status": player_inventory.status,
                "characters": characters,
                "packs": packs,
            })

    else:
        return JsonResponse({'message': 'fail', "status": player_inventory.status})


def win(request):
    return render(request, 'game/win.html', {})
