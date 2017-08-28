# PDX Trail: Education Game Project by Jenna M. Tucker


#### Overview:
PDX Trail is an educational game designed as a parody of the beloved educational game The Oregon Trail.  The game mimics the quintessential elements of the game play and lingo to satisfy nostalgia for The Oregon Trail.  While The Oregon Trail simulates the shared historical experience of folks taking the Oregon Trail, PDX Trail simulates a shared future where ecological hardship sparks migration to the Cascades and the sprawling Portland area. Players will choose a level of difficulty for their game play, name their team members, and choose an initial inventory including food, clothes, means of carrying their inventory, basic tech, and social use items like music and books before they set out.  Success along the trail will depend on player choices and luck both. Foraging / scavenging will replace hunting as a way to subsidize inventory.


#### Specific Functionality:

User Log In:
  - User chooses a name and password
  
Gameplay Screen:
  - Character / difficulty level choices
  - Enter choice __
  - User choice determines the maximum size of inventory

Names Screen:
  - You will lead a team of four others.
  - Enter name 2-5 __
  
Pack Screen
  - list of available items by category
  - users can choose items to pack from a list 

Depart Screen
  - user blocked from departure if overpacked
  - user can choose to unpack items
  - user can go back and pack more items 

Play Screen
  - summary of days and miles traveled 
  - Play menu:  Walk on, Take some rest, Scavenge/forage, Search through packs
  - walk on: changes day count, mile count, miles to a landmark
  - randomized happenings affect inventory, single character, or multiple characters 
  - landmarks will have a unique section of story
  - finds add to inventory 
  - gives notice if characters die 
  - ends game if user character "You" dies 

#### Data Model:

User:
  - FK to Inventory to create a game

Inventory:
  - name 
  - status to end game 
  - limit to limit inventory 
  - mile_counter, day_counter, last_milestone records
  - food_warning, death, happening, landmark, find, play_message to message user 

Character:
    - name 
    - description for health score 
    - FK to inventory to link to game 
    
Item:  
  - name, description
  - FK to Inventory to create item inventory / game 
  = FK to Landmark to allow items to be lost at landmarks 
  
Landmark:
    - name 

#### Technical Components:

Python:
   - Helper functions in views.py file to support gameplay 

Javascript web interface:
  - Allows user to enter: character names, choices, plays
  - Manages Ajax calls to link database and UI 
  - Sends user to next play screen 

Django:
  - Allows user to log in 
  - Creates webpages
  - Communicates with database 

HTML / CSS:
  - Modifies what the player sees from plain text into organized gameplay menus and screens with graphics.


#### Schedule:

**First Layer:**  (Week 4, 2.5 days)       *Finished
    Python backend:
        Basic:
  - Character class
  - Item class
  - Food (Item) class
  - Inventory class
  - Place class
  - Occurrence class

Prompt choice for game play character/difficulty
        Prompt for four character names
        Instantiate characters and limited inventory
        Explain inventory.
        Display initial inventory of items that can be packed.
        Display player's inventory.
        Prompt for what items the play wants to pack or unpack.
        Block player when pack is full.
        Present game play menu.
        Add miles, reduce health, remove food for days walked.
        Generate random occurrences with loses to single characters, each character, and inventory.
        Add days and health for days rested.
        Present random finds for foraging / scavenging.
        Allow player to pack random finds and/or unpack items.


**Keep a running milestone story / game play idea sheet:           Weeks 8-10**

**Second Layer:** (approx. 2 days)
    Python backend:
        End game:
            End game when player named "you" dies.
        Landmarks:
            Set specific mile counts to trigger landmarks.
            Decide if landmarks/milestones will be a class.
            Create 3 unique landmark stories / game play menus.
            Allow interactions with inventories. Use unpack item function.
            Player choices should determine outcomes.

**Third Layer:** (approx 2 days)
    User Interface:
        Create Django project and app 
        Turn Python objects into models 
        
**Fourth Layer:** (approx 4 days)
    Translate gameplay from pure Python into Django in views.py.
    Create User model.  

**Fifth Layer:** (approx 4 days)
    Set up Ajax calls and connect user inputs and database through functions.  
    Debug game.  
    
**Sixth Layer:** (approx 1 day)
    Mimic original game aesthetic using CSS.   


#### Functionality Beyond An MVP:
  Limit inventory even during finds.  
  Allow user to choose whether to take finds.
  Allow user to drop items.  
  **Basic travel screen graphic.**
  **Build out story** 
  Link up to songs.
  Date with day counter.  Could likely use an external calendar.
  Clues/pauses to stop and forage/scavenge.
  More static graphics.
  More animations.
  Option to select a start date.
    Variable adjusted for weather that's too early or too late, too wet/cold or
    dry/hot.
  Option to adjust pace.
  Choices at forks in trail, two paths. 