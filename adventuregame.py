#Name: Louie Darke
#Student Number: 1905864

import time
import sys
import random

yes_no = ["yes", "no", "y", "n"]
directions = ["forward", "backward", "left", "right"]       #Defining some lists to use to check for valid answers to some responses
response = ""
inventory = []

def printslow(str):             #A function used to print all text with a nice looking slow printing text effect.
    for char in str:            #Uses time which was imported, and prints each character every 0.03 seconds
        time.sleep(0.03)
        sys.stdout.write(char)      #Writes each individual character on same line
        sys.stdout.flush()
    time.sleep(1)               #Waits 1 second between each line

printslow("You awaken in a strange room... No idea of how you got here. It seems as though all past memories were gone, as if you didn't exist before just now..\n")
printslow("A man with a long beard is looking at you. It startles you, but then he begins to speak..\n")
printslow("???:\n")
printslow('"Ah, you are finally awake, Er.. Remind me of your name again..?"\n>>')
name = input("")                                                                            #First variable. Your name
printslow("???:\n")
printslow('"Ah, how could I forget!"\n')
printslow(name)                             #This line is done over 3 lines here, but prints the name within the same message. Due to having no \n at the end
printslow(', I need you to complete a quest for me. Outside lies a dark forest, and within it, an entrance to a dungeon. Find the dungeon, get through it, and bring me the lost scroll of truth. It is very important."\n')
while response not in yes_no:
    printslow('"Do you accept my quest?"\n>>')
    response = input("")
    if response == "yes" or response == "y":                #First while loop to check for either yes or no being input
        printslow("???:\n")
        printslow('"Good! Now, go! There is no time to lose, ')
        printslow(name)
        printslow('! My name is Edius, if for some reason you forgot my name."\n')
        printslow(name)
        printslow(":\n")
        printslow('"..."\n')
        printslow("(Still very confused, you give a slight nervous laugh)\n")
        printslow("Edius:\n")
        printslow('"..."\n')
        printslow('"Not very talkative today, are you?"\n')
        printslow('"Alright, go on. Get out of here."\n')
    elif response == "no" or response == "n":
        printslow("???:\n")
        printslow('"What? Why not? You are the best I have for this and you are really just going to say no?"\n')
        printslow('"..."\n')
        printslow('"Fine. Get out of here. And do NOT come back. Waste of time..."\n')
        print("---------- GAME OVER -----------")
        exit()                                              #exit() function ends the program, because game over
    else:
        printslow('"What? I didnt hear you."\n')

printslow("(You stand up.)\n")
printslow("(You look around.)\n")
printslow("In front of you, is the front door of Edius' home.\n")
printslow("Behind you is the very uncomfortable looking bed you were just sitting on.\n")
printslow("To your left is Edius, and he's looking at you in confusion as you just stand there.\n")
printslow("To your right is a large bookcase.\n")
while response not in directions:
    while response != "forward":
        printslow("Which way will you go?\n>>")
        response = input("")                                            #Can choose one of the four directions and something happens depending on where they go
        if response == "forward":
            printslow("You walk towards the door of the house. Now you're just very close to this shut door.\n")
            continue
        elif response == "backward":
            printslow("(You get back on the uncomfortable bed and lie down)\n")
            printslow("Edius:\n")
            printslow('"What are you doing? Your quest is not to have a nap. You have been doing that quite enough already!"\n')
            printslow('"This is really important! Go now!"\n')
        elif response == "left":
            printslow("(You begin walking to your left, with no regard for the fact that Edius is standing right there.)\n")
            printslow("Edius:\n")
            printslow('"What the hell is wrong with you? Get back!"\n')
            printslow("(Edius pushes you back)\n")
        elif response == "right":
            if "Casting Fireballs for Beginners" in inventory:                      #Checks if the user has already been here to take the book
                printslow("You have already been here, and taken what you can. There is nothing more to take.\n")
                continue
            elif "Casting Fireballs for Beginners" not in inventory:
                printslow("You look at the bookcase, full of books. You spot an orange coloured book sticking out.\n")
                printslow("You see that the book is entitled 'Casting Fireballs for Beginners'\n")
                while response not in yes_no:
                    printslow("Take the book?\n>>")
                    response = input("")                        #If they chose to go right, toward the bookcase, they can then choose another option from here. Taking the book or not.
                    if response == "no" or response == "n":
                        printslow("You leave the book there, and move back away from the bookcase.\n")
                    elif response == "yes" or response == "y":
                        printslow("You take the book.\n")
                        printslow("It's now in your inventory.\n")
                        inventory.append("Casting Fireballs for Beginners")
                        printslow("Edius:\n")
                        printslow('"Ok, sure, just take it."\n')
                        printslow("(You walk back away from the bookcase.)\n")

response = ''
while 'open' not in response or 'bash' not in response or 'smash' not in response:      #Looks for certain keywords within the string. Not exact strings
    printslow("What would you like to do with this door?\n>>")                          #If the user went forward, the come to the door of the house, and can type what to do
    response = input("")                                                                #They could choose to either say they want to open it, or they could bash the door down
    if 'open' in response:              #Checks for certain word within string
        printslow("You open the door and step outside.\n")
        break
    elif 'hit' in response:
        printslow("You try hitting the door to try and get through it.\n")
        printslow("Nothing much happened.\n")
        printslow("Edius stares at you in disbelief at your inability to get through a door.\n")
    elif 'smash' in response or 'bash' in response:
        printslow("You bashed your way through the door.\n")
        printslow("Almost as if you have no time for using the doorknob.\n")
        printslow("Edius:\n")
        printslow('"What the hell? You are supposed to be my best that I have, and you just went and did that?!"\n')
        printslow('"You better come back from this alive, ')
        printslow(name)
        printslow(', becuase you are paying for that!"\n')
        break
    break

response = ''
printslow("You now find yourself outside.\n")
printslow("This place does not seem to be anything you recognise..\n")
printslow("Ahead of you, is the forest which Edius spoke of.\n")
printslow("The left of you just seems to be endless plain fields...\n")
printslow("To the right seems to be a rather steep way down to some more plain fields.\n")
printslow("Behind you, Edius' home.\n")
while response not in directions:
    while response != 'forward':
        printslow("Which way will you go?\n>>")
        response = input("")
        if response == 'forward':
            printslow("You walk towards, and into the forest.\n")
            printslow("It quickly gets dark as you enter it..\n")
        elif response == 'backward':
            printslow("Edius does not want you to return to his home unless you come back with that scroll of truth he talked about...\n")
        elif response == 'left':
            printslow("You begin walking left, away from the forest, and into very plain fields.\n")
            printslow("Feels like this field goes on forever..\n")
            printslow("It begins to make you wonder where exactly you have ended up.\n")
            printslow("All you seem to have remembered is what your name is.\n")
            printslow("Why is there nothing else except a house and a forest?")
            printslow("The further you go, the less there seems to be around you.\n")
            printslow("You head back to where you started, outside of Edius' home.\n")
        elif response == 'right':
            printslow("You walk towards the edge of a very steep way down to plain fields.\n")
            printslow("It almost looks like a cliff.\n")
            while response not in yes_no:
                printslow("Would you like to jump?\n>>")
                response = input("")                                #If they chose to go right, here is another tree of options off this one
                if response == 'yes':
                    printslow("You jumped.\n")
                    printslow("...\n")
                    printslow("Not much happened. You just jumped on the spot.\n")
                    continue
                elif response == 'no':
                    response = ''
                    while response not in yes_no:
                        printslow("Would you like to try climbing down?\n>>")
                        response = input("")
                        if response =='yes':
                            printslow("You begin to climb down the rocks of this cliff.\n")
                            printslow("The rocks you are using seem to be very loose and slippery\n")
                            printslow("You step down onto another rock\n")
                            printslow("The rock falls, and takes you with it...\n")
                            printslow("You fall to your death\n")
                            print("---------- GAME OVER -----------")
                            exit()
                        elif response == 'no':
                            printslow("You decide not to do this, as it look way to steep and unstable.\m")         #If they choose not to do this, the loop will go back to the start
                            printslow("You return back to where you were before, outside Edius' home.\m")
                            continue

printslow("You are now stood under the very tall trees of the forest.\n")
printslow("It is very hard to see, but you can see the glow of something in the distance, just a little further into the forest.\n")
response = ''
while response not in yes_no:                  #Continues to ask until a yes or no answer from the defined list is entered
    printslow("Go towards the glow?\n>>")
    response = input("")
    if response in ['no', 'n']:
        printslow("You choose not to go towards the glow.\n")
        printslow("The mysterious lone light in a dark forest you are unfamiliar with does not seem to tempt you to want to go to it.\n")
        printslow("You continue to stand in the dark forest.\n")
        while response not in directions:
            printslow("Which direction would you like to go in this dark forest?\n>>")
            response = input("")
            if response == "forward":
                printslow("Despite not wanting to investigate the glow of the light, you walk north towards the location of the glow.\n")
            elif response == "backward":
                printslow("You cannot leave the forest now! This is your quest!\n")
            elif response == "left" or response == "right":
                printslow("You walk into the darkness of the forest, away from the glowing which seemed to be your only light source under these trees.\n")
                printslow("It becomes increasingly hard to get any further, as there seems to be no real path. It also becomes even darker.\n")
                while response not in yes_no:
                    printslow("Return back to where you were?\n>>")
                    response = input("")
                    if response in ['yes', 'y']:
                        printslow("With a bit of struggle, and the feeling of wasted time, you are now back where you were, with the glow still there in front of you.\n")
                        while response not in yes_no:
                            printslow("Go towards the glow?\n>>")
                            response = input("")

printslow("You walk towards this glowing light.\n")                                         #When the loop is successfully ended, the game progresses.
printslow("It's an orb of some kind, just sitting there on a very damaged table.\n")
printslow("You are unsure of what it is, but it provides a very good light source.\n")
printslow("You take the orb, and it is now in your inventory.\n")
printslow("You decide to keep a hold of it, so you can now see where you're going.\n")
printslow("-------\n")
printslow("Further on, past this damaged table, you see some kind of entrance which goes downward.\n")
response = ''
while response not in yes_no:                              #Setting respone variable back to nothing, in case of previous entries of valid strings, which would make it skip a loop
    printslow("Would you like to try entering?\n>>")
    response = input("")
    if response in ['yes', 'y']:
        printslow('You proceed toward this entrance and walk down some very cracked looking stone brick stairs.\n')
    elif response in ['no', 'n']:
        printslow("You decide you would rather not go there in case it's really dangerous.\n")
        printslow("You gaze at your new light emitting orb, and wonder if you are even going to be successful on this quest, as you can't seem to find any trace of something that could be the dungeon.\n")

printslow("You come to a set of large shut wooden doors.\n")
printslow("The doors have square holes where you could see into the dungeon.\n")
printslow("But it seems pitch black\n")
while 'open' not in response:
    printslow("What would you like to do?\n>>")
    response = input("")
    if 'open' in response:
        printslow("You decide to just try and open up the doors to get in.\n")
        printslow("With some power behind it, you get them open.\n")
        printslow("It seems as though no one has been here in decades\n")
    elif 'orb' in response or 'light' in response:                              #Check for more keywords within the string instead of exact string
        printslow("You put the orb in the hole so that you can see into what could be past the doors.\n")
        printslow("There isn't much too see..\n")
        printslow("...\n")
        printslow("You swear you just saw something move..\n")

printslow("???:\n")
printslow('"Intruder..."\n')
printslow('"You must leave."\n')
printslow("...\n")
printslow("The creature comes out of the darkness and reveals itself.\n")
printslow("It's a skeleton with glowing green eyes, holding a sword.\n")
while response not in ['run', 'fight']:
    printslow("Would you like to run or fight?\n>>")
    response = input("")
    if response == 'run':
        printslow("You attempt to turn back and run.\n")
        printslow("The skeleton is surprisingly fast, and knocks you to the ground.\n")
        printslow("You try to get up but now the skeleton has you held down firmly.\n")
        printslow("Skeleton:\n")
        printslow('"You.... should not have come here..."\n')
        printslow("The skeleton stabs you straight through the heart\n")
        printslow("It dealt 100 Damage.\n")
        print("---------- GAME OVER -----------\n")
        exit()
    elif response == 'fight':
        enemy_health = 300                              #Defining two health integer variables
        health = 100
        printslow("You initiate a fight with the skeleton\n")
        printslow("You draw your sword\n")
        attack= ''
        while attack not in ['strike', 'fireball']:             #Attacks to choose from
            while enemy_health > 0:
                while health > 0:                       #While neither enemy not player has 0 health or less
                    printslow("Enemy Skeleton has ")
                    printslow(str(enemy_health))                #Print out the integer variable as a string. Gave error using this function otherwise
                    printslow(" HP.\n")
                    printslow("You have ")
                    printslow(str(health))
                    printslow(" HP.\n")
                    printslow("What attack will you use? (Strike) (Fireball)\n>>")
                    attack = input("")
                    if attack == 'strike':
                        printslow("You strike the skeleton with your sword.\n")
                        damage = random.randint(30, 100)                    #Takes away random amount of health from enemy between 30 to 100
                        enemy_health = enemy_health - damage
                        printslow("You dealt ")
                        printslow(str(damage))
                        printslow(" Damage to the Enemy Skeleton.\n")
                        if enemy_health > 0:
                            printslow("The Enemy Skeleton swings its sword at you.\n")          #As long as the skeleton is not at 0 or less health, attack player
                            printslow("It hit you and dealt ")
                            hostile_damage = random.randint(10, 20)
                            health = health - hostile_damage                #Takes away random amount of health from player between 10 to 20. Player has less health
                            printslow(str(hostile_damage))
                            printslow(" Damage to you.\n")
                        elif enemy_health <= 0:
                            printslow("You have successfully defeated the Enemy Skeleton with ")
                            printslow(str(health))                                                      #When enemy skeleton has 0 or less health, congratulate player and move on
                            printslow(" HP left.\n")
                            break
                    elif attack == 'fireball':
                        if "Casting Fireballs for Beginners" in inventory:                              #Check that player picked up book at start of the game, or they cannot use this
                            printslow("You use your new found power from the spell book, and cast a sizeable fireball.\n")
                            printslow("You throw it directly into the chest of the skeleton.\n")
                            damage = random.randint(100, 160)
                            enemy_health = enemy_health - damage                #Take away random amount of health from enemy between 100 to 160
                            printslow("You dealt ")
                            printslow(str(damage))
                            printslow(" Damage to the Enemy Skeleton.\n")
                            if enemy_health > 0:
                                printslow("The Enemy Skeleton swings its sword at you.\n")
                                printslow("It hit you and dealt ")
                                hostile_damage = random.randint(10, 20)
                                health = health - hostile_damage
                                printslow(str(hostile_damage))
                                printslow(" Damage to you.\n")
                            elif enemy_health <= 0:
                                printslow("You have successfully defeated the Enemy Skeleton with ")
                                printslow(str(health))
                                printslow(" HP left.\n")
                                break
                        elif "Casting Fireballs for Beginners" not in inventory:                #Check for the book not being there, and deny access to attack
                            printslow("You do not have the knowledge of how to do this.\n")
                            printslow("Perhaps you missed something earlier..?\n")
                    if health <= 0:
                        printslow("You have been defeated by the Enemy Skeleton.\n")
                        print("---------- GAME OVER -----------\n")                     #End the game if player reaches 0 or less health
                        exit()

printslow("Exhausted, you sit for a moment, next to your orb.\n")
printslow("You shine the orb around, and notice three different ways to go.\n")
printslow("To your left, your right and straight ahead, there are three different dark looking rooms.\n")
while response not in ['left', 'right', 'forward']:
    response = ''
    printslow("Which of these ways will you look in? (Forward/Left/Right)\n>>")              #More directions to choose
    response = input("")
    if response == 'left':
        printslow("You decide to go into the room on the left.\n")
        printslow("The room is dark so you shine your orb.\n")
        printslow("There doesn't seem to be much around except some rocks and a completely boarded up doorway.\n")
        printslow("You return back to where you were.\n")
        response = ''
        continue
    elif response == 'forward':
        response2 = ''
        printslow("You enter the room straight ahead of you.\n")
        printslow("There is a chest.\n")
        reward = random.randint(50, 150)                    #Give player random amount of coins from this chest
        while response2 not in yes_no:
            printslow("Would you like to open it?\n>>")
            response2 = input("")
            if response2 in ['yes', 'y']:
                printslow("You open the chest slowly.\n")
                printslow("It is very old.\n")
                printslow("Inside you find a few gold coins\n")
                printslow("You now have ")
                printslow(str(reward))
                printslow(" Gold Coins in your inventory\n")
                printslow("You close the chest, and look around. There is nothing more of note in this room.\n")        #Tree of options
                printslow("You return back out of this room\n")
                response = ''
                break
            continue
            if response2 in ['no', 'n']:
                printslow("You decide not to open this chest, in fear that it could be something dangerous, or a trick.\n")
                printslow("You look around, and there seems to be nothing more of note in this room.\n")
                printslow("You return back out of this room\n")
                response = ''
                break
            continue
    elif response == 'right':
        response3 = ''
        printslow("You enter the room on the right.\n")
        printslow("You shine your orb around and it just seems like another pretty empty room with not much going on.\n")
        printslow("You then notice to your right, there is a very tight looking way into another room\n")
        printslow("There is something glowing in there.\n")
        while response3 not in yes_no:
            printslow("You can probably just about fit through. Would you like to enter the room?\n>>")
            response3 = input("")
            if response3 in ['yes', 'y']:                #Break out of loop and move if player says yes
                break
            if response3 in ['no', 'n']:
                printslow("You decide not to enter the room, and instead return back, in front of the three rooms to go in.\n")
                response3 = ''
                break
            continue

printslow("You manage to just about squeeze through this narrow way into this next room.\n")
printslow("The source of the glow becomes clear...\n")
printslow("It was the scroll of truth!\n")
printslow("You wonder how such a thing even gives off any light.\n")
printslow("Nonetheless, you take it anyway.\n")
printslow("---------\n")
printslow("-- Edius' Home --\n")
printslow("Edius:\n")
printslow('"Well done, ')
printslow(name)
printslow('! This is going to make some big changes."\n')
printslow('"This scroll contains knowledge which would be dangerous for most to know about."\n')
printslow('"But a wizard such as myself requires this knowledge."\n')
printslow('"Now, go and get out of here! I have business to attend to. And just be ready for me to call on you again."\n')
printslow('"I may require more of your services in future.."\n')
printslow('--- The End ---\n')
printslow('Congratulations, you have won the game.')                #Congratulate player, and game ends
exit()
