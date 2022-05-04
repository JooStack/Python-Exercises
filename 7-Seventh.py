import random

rand = random.randint(1,51)

print("Game of guessing number..")
print("You have 5 chances..")

x = 8

while x > 0 :
  guess = int(input("enter a number.."))
  x -= 1
  if guess > rand :
    print("Less..")
    
  elif guess < rand :
    print("More..")
    
  else :
    print("congratulations")
    break
  
  print(f"you have {x} chances ")
  