x = 1
while x <= 10 :
  if x % 2 == 0 :
    if x % 3 == 0 :
      print(f" {x} is divisible by 2 and 3")
    else :
      print(f" {x} number is only divisible by 2")
  elif x % 3 == 0 :
    print(f"{x} number is only divisible by 3")
  else :
    print(f"{x} the number is not divisible by 2 or 3")

  x += 1
