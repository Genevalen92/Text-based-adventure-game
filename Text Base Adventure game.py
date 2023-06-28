import time
import random 

def test():
  print("Welcome To AI")
  time.sleep(3)
  print("where you choose your own path")
  time.sleep(3)


  choice_1 = input("You wake up and notice that you are in a forest and thirsty. you see two paths going [left] or [right] which one do you choose? \n")
  if choice_1 == "left":
    left()
  elif choice_1 == "right":
    right()

def left():
  print("You took the left path.")
  time.sleep(3)
  print("As you contiued down this path you you begin to grow delirious.")
  time.sleep(3)
  print("You start to think if the sounds you are hearing is the thirst or legit.")
  left_choice_1 = input("Do you [investigate] the sound or [continue] walking?\n")
  if left_choice_1 == "investigate":
    investigate()
  elif left_choice_1 == "continue":
    progress()

  
def right():
  print("you went right")
  time.sleep(3)
  print("You see a sign that says random trail")
  trail_opt = ['L', 'R', 'S']
  trail_choice = random.choice(trail_opt)

  if trail_choice == "L":
    left_trail()
  elif trail_choice == "R":
    right_trail()  
  else:
    special_trail()


def right_trail():
  print("You took the right trail")
  time.sleep(1)
  print("...")
  time.sleep(1)
  print("...")
  

















def left_trail():
  time.sleep(4)
  print("You suddenly find yourself in a frozen tundra")
  time.sleep(3)
  print("You are the wind whips through the air \n making you extremely cold.")
  time.sleep(3)
  print("You are clearly undressed")
  winter_map = input("what will you do: look for [heat], look for [food]").lower()

  if winter_map == "heat":
    heat()
  elif winter_map == "food":
    food()
  else:
    retry()
    








def investigate():
  print("You went to check to see where the noise was coming from.")
  time.sleep(3)
  print("However, you discover that there were no sounds and pass out from exhaustion .")
  time.sleep(3)
  print("Game over!")
  restart = input("Would you like to try again? \n")
  if restart != "yes":
    print("Thanks for playing!")
  else:
    test()


def progress():
  print("You disregarded the sounds and continued onward!")
  time.sleep(2)
  print("As you advance through the dense forest you begin to feel very weak from thirst.")
  time.sleep(2)
  print("You decide to sit for a second and rest..........")
  time.sleep(2)
  print("..........")
  time.sleep(2)
  print("................")
  left_choice_2 = input("You suddenly wake up \n and its dark should you continue \n [rest] or [look] for something to drink?" ).lower()

  if left_choice_2 == "rest":
    rest()
  elif left_choice_2 == "look":
    look()
  
  








def rest():
  print("You decided to continue sleeping")
  time.sleep(3)
  print("You wake up feeling worse than yesterday.")
  time.sleep(2)
  print("........")
  time.sleep(2)
  print("........")
  time.sleep(2)
  print("Game Over!")
  
  retry()
  
  
  







def look():
  print("You give one push and you began to hear the rush of water.")
  time.sleep(2)
  print("You head towards the sound and find a river.")
  time.sleep(2)
  print("You have finally found some water!!")
  time.sleep(2)
  print("")









def retry():
  restart = input("Would you like to try again? \n")
  if restart != "yes":
    print("Thanks for playing!")
  else:
    test()



test()  
