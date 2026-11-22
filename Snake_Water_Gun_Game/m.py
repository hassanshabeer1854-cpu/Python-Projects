import random
def menu():
 print("\t Welcome to snake water gun game")
 print("1.snake")
 print("2.water")
 print("3.gun")

def game():
 while True:
  computer=random.randint(1,3)
  try:
   user=int(input("enter your choice or  0 to stop:"))
  except ValueError:
   print("Invalid input")
   continue
  if user==0:
   print("thnk you for plying")
   break
  if computer==1:
   print('computr: 1.snake')
  elif computer==2:
   print("computr: 2.water")
  else:
   print("computr: 3.gun")
  if user<1 or user>3:
   print("Invalid choice, enter a valid number")
   continue
  else:
   if computer==user:
    print("draw match")
   elif computer==1 and user==2:
    print("you lose")
   elif computer==2 and user==1:
    print("you win")
   elif computer==1 and user==3:
    print("you win")
   elif computer==3 and user==1:
    print("you lose")
   elif computer==2 and user==3:
    print("you lose")
   elif computer==3 and user==2:
    print("you win")


menu()
game()