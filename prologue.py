##
#prologue to my little object show sim
#2/15/23 - 2/22/23
name = input("hello! whta is your name? ")
object = input("and whta is your object? ")
code = 0
print("loading prologue...")
print("you are chilling by yourself when out of nowhere,\na small red envelope falls from the sky\n and lands right in front of you.")
while True:
    choice = input("open it? ")
    if choice == "yes":
        print('"Dear {},\nyou have been chosen for a very special competition!\nFind me at xxx to play. Theres a big sum of money at stake.\nSee you there!\n- Your host"\n'.format(name))
        print("excited for a chance at lots of money, you head off\nto this location with the envelope in hand.")
        print("as you walk down the street, you unknowingly step on\na faded missing poster featuring a padlock and a scarf.\n")
        break
    elif choice == "no":
        print("no reason to do that, anyway.")
        print("THE END.")
        print("thank you for playing!")
        break
    else:
        print("sorry, i didn't understand that.")
code = name+"#"+object
print("here is your chapter code. please keep it saved for the next chapter.")
print(code)
print("end of prologue. thank you for playing!")