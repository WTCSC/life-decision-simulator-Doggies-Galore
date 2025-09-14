#No dependencies needed!
#Init, imports, and helper functions
import sys
import time
import datetime
#Pay no attention to these variables
houseburned=False
homeless=False
dogmonopoly=False
starttime=datetime.datetime.now()
def slow_print(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
#Start of the "Afternoon" Scenes. Ran out of time to add more scenes.

#Normal Afternoon
def afternoonNormal():
    slow_print("\nIt's now the afternoon. After a bizarre morning, you find yourself reflecting on your life choices. What do you do now?")
    slow_print("1. Take your dog for a walk to clear your mind.")
    slow_print("2. Call a friend to talk about what happened.")
    choice = input("Enter 1 or 2: ")
    if choice == '1':
        slow_print("\nYou take your dog for a walk. He catches a squirel in his vision, and in his haste, trips you almost immediately, causing you to fall and sprain your ankle. It's impressive that you keep trusting him. In the end, you go home and enjoy a quiet evening.")
        endtime=datetime.datetime.now()
        elapsed=endtime-starttime
        slow_print("\n ENDING 13 - WALK - Time taken: "+str(elapsed))
    elif choice == '2':
        slow_print("\nYou call a friend to talk about what happened. They don't believe you, and think you're making it up. You feel isolated and misunderstood. Therapy might help.")
        endtime=datetime.datetime.now()
        elapsed=endtime-starttime
        slow_print("\n ENDING 14 - THERAPY - Time taken: "+str(elapsed))
    else:
        slow_print("\nInvalid choice. You just stand there, lost in thought. The end.")
        endtime=datetime.datetime.now()
        elapsed=endtime=starttime
        slow_print("\n ENDING 15 - LOST - Time taken: "+str(elapsed))

#You monster
def afternonRegret():
    slow_print("\nStill shaken up, you try to forget the morning and move on. What do you do now?")
    slow_print("1. Forget the morning.")
    slow_print("2. Talk to your partner about what happened.")
    choice = input("Enter 1 or 2: ")
    if choice == '1':
        slow_print("\nYou try to forget the morning, but the guilt lingers. You and what's left of your dog live a quiet life, but the memory of the dog-soup haunts you.")
        endtime=datetime.datetime.now()
        elapsed=endtime-starttime
        slow_print("\n ENDING 4 - GUILT - Time taken: "+str(elapsed))
    elif choice == '2':
        slow_print("\nYou talk to your partner about what happened. They are horrified. Turns out, they're not your partner anymore. They leave you, and you are left alone.")
        endtime=datetime.datetime.now()
        elapsed=endtime-starttime
        slow_print("\n ENDING 5 - ALONE - Time taken: "+str(elapsed))
    else:
        slow_print("\nInvalid choice. You just stand there.")
        endtime=datetime.datetime.now()
        elapsed=endtime=starttime
        slow_print("\n ENDING 6 - TRUAMA - Time taken: "+str(elapsed))

#If your dog burned down your house and dipped
def afternoonHomeless():
    slow_print("\nYou now find yourself homeless, with your dog nowhere to be found. What do you do now?")
    slow_print("1. Find a second job to move to an appartment.")
    slow_print("2. Ask your partner if you can stay over.")
    choice = input("Enter 1 or 2: ")
    if choice == '1':
        slow_print("\nGreat news! Dog™ is hiring! You end up taking the job, and you start working for your own dog. Congratulations. Your dog burned down your house, dipped after commiting arson, and now you're working for him.")
        endtime=datetime.datetime.now()
        elapsed=endtime=starttime
        slow_print("\n ENDING 9 - MONOPOLY - Time taken: "+str(elapsed))
    elif choice == '2':
        slow_print("\nYour partner agrees to let you stay over, but only if the dog can come too. No matter how hard you try, you can't seem to get rid of him.")
        slow_print("Congratulations. Your dog burned down your house, dipped after commiting arson, and now you're stuck with him.")
        endtime=datetime.datetime.now()
        elapsed=endtime=starttime
        slow_print("\n ENDING 10 - TRAPPED - Time taken: "+str(elapsed))
    else:
        slow_print("\nInvalid choice. You just stand there, homeless and alone. The end.")
        endtime=datetime.datetime.now()
        elapsed=endtime=starttime
        slow_print("\n ENDING 11 - HOMELESS - Time taken: "+str(elapsed))

#If you try to rebuild your house
def afternoonRebuild():
    slow_print("\nYou decide to rebuild the house, but without proper tools and materials, it's a lost cause. Whtat do you do now?")
    slow_print("1. Give up. Call your dog to see if you can live with him in the wild.")
    slow_print("2. Pay people to help you rebuild.")
    choice = input("Enter 1 or 2: ")
    if choice == '1':
        slow_print("\nHe says 'abbbsoluttely! Just make sure you agree to my Terms and I'll get you moved in!'")
        slow_print("\n You wonder what terms a dog could possibly have, but you agree anyway. He invites you into his mansion (that he's had for years!?) and tells you to get to work. Congratulations. Your dog burned down your house, dipped after commiting arson, and has just enslaved you.")
        endtime=datetime.datetime.now()
        elapsed=endtime-starttime
        slow_print("\n ENDING 1 - SLAVE TO THE DOG - Time taken: "+str(elapsed))
    elif choice == '2':
        slow_print("\nYou pay people to help you rebuild, but you run out of money quickly. Congratulations. Your dog burned down your house, dipped after commiting arson, and now you're broke.")
        endtime=datetime.datetime.now()
        elapsed=endtime-starttime
        slow_print("\n ENDING 2 - BROKE - Time taken: "+str(elapsed))
    else:
        slow_print("\nInvalid choice. You just stand there. Your dog is in the wild, your house is gone, and you're stuck with a husk of a house. The end.")
        endtime=datetime.datetime.now()
        elapsed=endtime-starttime
        slow_print("\n ENDING 3 - GONE - Time taken: "+str(elapsed))

#Start of the Program- "Morning" Scene
def main():
    slow_print("Good morning! You wake up in your house. Your dog is looking at you like you're starving him. What do you do?")
    slow_print("1. Explain to him that the GP part of CSGP is programing bland text based adventure games.")
    slow_print("2. Feed him.")
    slow_print("3. Go back to sleep.")
    choice = input("Enter 1, 2, or 3: ")
    if choice == '1':
        slow_print("\nHe stands up, says 'Ah- 'tis such a tragedy. What has our life come to. We were supposed to be learning Ghidra and IDA, and breaking stuff.'")
        slow_print("His CPU is not space-hardened, and has inadequate cooling. The SiP isn't able to downclock because he's so overwhelmed, so his enclosure starts melting.")
        slow_print("Look at what you've done, you monster. You turned your dog into dog-soup.")
        slow_print("\nWhat do you do now?")
        slow_print("1. Try to evaporate him to put him out of his misery")
        slow_print("2. Cry and question your life choices.")
        slow_print("3. Put him in a dog-shaped mould and place him in the fridge.")
        choice = input("Enter 1, 2, or 3: ")
        if choice == '1':
            slow_print("\nYou try to evaporate him, but now your kitchen smells like burnt dog. You try to forget the whole incident, but the smell lingers.")
            afternonRegret()
        elif choice == '2':
            slow_print("\nYou cry. The dog-soup bubbles in sympathy. Therapy might help.")
            afternonRegret()
        elif choice == '3':
            slow_print("\nYou now have a dog-shaped popsicle. It's weird, but at least he's cool now.")
            afternonRegret()
        else:
            slow_print("\nInvalid choice. The dog-soup evaporates on its own, leaving a lingering smell of regret. The end.")
    elif choice == '2':
        slow_print("\nYou and your dog go downstairs. In a twist of fate, your dog runs in front of you, tripping you, and causing multiple minor injuries.")
        slow_print("Unfortunately, dogs have under-developed empathy skills, so he's still dead-set on eating. What do you do?")
        slow_print("1. Give into his demands, feed him while bleeding")
        slow_print("2. Call emergency services")
        slow_print("3. Press charges.")
        choice = input("Enter 1, 2, or 3: ")
        if choice == '1':
            slow_print("\nYou feed him while bleeding. He is satisfied. You, however, need a bandage. At least the dog's happy. You win?")
            afternoonNormal()
        elif choice == '2':
            slow_print("\nYou call emergency services. They patch you up and give your dog a stern talking-to. He is unphased. Life goes on.")
            afternoonNormal()
        elif choice == '3':
            slow_print("\nYou try to press charges. The judge laughs you out of court. Your dog is now a local celebrity.")
            afternoonNormal()
        else:
            slow_print("\nInvalid choice. You collapse from blood loss. The dog, confused, wanders off.")
            slow_print("ENDING 12 - DEATH BY DOG - Time taken: "+str(elapsed))
    elif choice == '3':
        slow_print("\nYou decide to get some more Zzzs, which in all fairness is a sound choice... assuming you didn't have the dog.")
        slow_print("When you wake up again, your house is on fire after your dog accidentally turned on the stove.")
        slow_print("Your dog just looks at you, hungry. What do you do?")
        slow_print("1. Negotiate with him.")
        slow_print("2. Run out of the house.")
        slow_print("3. Try to rebuild the house.")
        choice = input("Enter 1, 2, or 3: ")
        if choice == '1':
            slow_print("\nYou try to negotiate with him, but he's too hungry to care. The fire spreads, and you both have to evacuate. You survive, but your house is gone.")
            afternoonHomeless()
        elif choice == '2':
            slow_print("\nYou run out of the house, leaving him behind. The dogs splits, and you never see him again. You live with the guilt, but at least you're safe.")
            afternoonHomeless()
        elif choice == '3':
            afternoonRebuild()
        else:
            endtime=datetime.datetime.now()
            elapsed=endtime-starttime
            slow_print("\nInvalid choice. You both perish in the fire. The end. Time taken: "+str(elapsed))
            slow_print("Ending 8 - FIRE - Time taken: "+str(elapsed))
    else:
        endtime=datetime.datetime.now()
        elapsed=endtime-starttime
        slow_print("\nInvalid choice. You just lie there. Your dog is hungry, but hasn't commited arson!")
        slow_print("\n ENDING 7 - INACTION - Time taken: "+str(elapsed))
        slow_print("What are you, a speedrunner?")


if __name__ == "__main__":
    main()
    if houseburned and homeless and dogmonopoly:
        slow_print("\nCongratulations! You've reached the secret ending where your dog burned down your house, made you homeless, AND made you his employee. He managed to take everything from you.")
        endtime=datetime.datetime.now()
        elapsed=endtime-starttime
        slow_print("\n SECRET ENDING - DOG MONOPOLY - Time taken: "+str(elapsed))
    
