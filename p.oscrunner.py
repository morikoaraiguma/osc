##
#p.oscrunner
#little fun thing personal project little goofy thing!
#2/15/22 - 2/17/22
lazy = 0
name = input("hello! whta is your name? ")
object = input("and whta is your object? ")
print("loading prologue...")
print("you are chilling by yourself when out of nowhere,\na small red envelope",
      "falls from the sky and lands right in front of you.")
while True:
    yesno = input("open it? ")
    if yesno == "yes":
        print('"Dear {},\nyou have been chosen for a very special competition!\nFind me at xxx to play. Theres a big sum of money at stake.\nSee you there!\n- Your host"'.format(name))
        print("excited for a chance at lots of money, you head off\nto this location with the envelope in hand.")
        print("as you walk down the street, you unknowingly step on\na faded missing poster picturing a padlock and a scarf.")
        break
    elif yesno == "no":
        print("no reason to do that, anyway.")
        print("THE END.")
        print("(somewhere in the distance, a trophy appears on a shelf.)")
        lazy = 1
        break
    else:
        print("sorry, i didn't understand that.")
print("end of prologue. thank you for playing!")
