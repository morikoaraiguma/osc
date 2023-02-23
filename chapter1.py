code = input("hello! please enter your code here. ")
name, object = code.split("#")
choice = 0
choice2 = 0
purseR = 0
print("loading chapter 1...")
print("as you walk to the location inscribed in the letter, you see a mansion in the distance slowly coming into view. as you walk up to it, you can see a red purse standing outside. they notice you as well.")
print('"hello. you must be {}. please come inside, the others are waiting."'.format(name))
while choice2 == 0:
  choice = input("the purse motions for you to follow them.\nfollow? ")
  if choice == "no":
     while choice2 == 0:
      choice2 = input("you stand in place. the purse motions again, a confused look on their face.\nleave or follow? ")
      if choice2 == "leave":
        break
      elif choice2 == "follow":
        break
      else: ("sorry, i didn't understand that.")
  if choice == "no" and yesno2 == "follow" or yesno == "yes" and yesno2 == 0:
    purseR += 1
    print("you walk behind the purse as they slowly open the big wooden doors to the mansion.")
    break
  elif yesno2 == "leave":
    print("you run away. why risk your life in some creepy mansion? the prize isn't worth it, and you don't even know if it's real! the purse is shocked, but doesn't try to stop you.")
    print("THE END.")
    print("thank you for playing!")
    break
  else:
    print("sorry, i didn't understand that.")
print("behind the creaking door is a giant room littered with couches and tables with lots of food. you see various other objects talking and helping themselves to the food. once you walk in, they turn to look at you.")
print('"thank you all for your patience," purse tries to say, but no one hears them. "please give us a few more minutes." they then quickly escape through a small door labelled EMPLOYEES ONLY, leaving you standing at the front of the room.')
print("looking around, there seem to be a few groups of interest.\nto your left are a camera and a die. the camera seems to be boasting and the die is applauding them.\n to your right you see a music sheet stand and an old fashioned telephone. only one of them seems to be talking.\nfinally, by one table with food you can see an unopened chocolate bar and a seed packet. the chocolate bar is talking very loudly, getting a laugh from the seed packet.")
choice = input("you figure it would be a good idea to meet people before this competition. who will you approach?\n1. camera and die\n2. music sheet stand and telephone\n3. chocolate bar and seed packet\n(please answer using 1, 2, and 3!)")
