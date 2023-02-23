code = input("hello! please enter your code here. ")
name, object = code.split("#")
yesno = 0
yesno2 = 0
print("loading chapter 1...")
print("as you walk to the location inscribed in the letter, you see a mansion in the distance slowly coming into view. as you walk up to it, you can see a red purse standing outside. they notice you as well.")
print('"hello. you must be {}. please come inside, the others are waiting."'.format(name))
while True:
  yesno = input("the purse motions for you to follow them.\nfollow? ")
  if yesno == "no":
     while True:
      yesno2 = input("you stand in place. the purse motions again, a confused look on their face.\nleave or follow? ")
      if yesno2 == "leave":
        break
      elif yesno2 == "follow":
        break
      else: ("sorry, i didn't understand that.")
  elif yesno == "yes" and yesno2 == "follow" or "0":
    print("you walk behind the purse as they open the big wooden doors to the mansion.")
    break
  elif yesno2 == "leave":
    print("you run away. why risk your life in some creepy mansion? the prize isn't worth it, and you don't even know if it's real! the purse is shocked, but doesn't try to stop you.")
    print("THE END.")
    print("thank you for playing!")
    break
  else:
    print("sorry, i didn't understand that.")
