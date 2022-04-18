age = input("Are you a cigarette addict older than 75 years old?  ").lower().strip()
chronic = input("Do you have a severe chronic disease?  ").lower().strip()
immune = input("Is your immune system too weak?  ").lower().strip()

if age == "yes" and (chronic == "yes" or immune == "yes") :
  print("You are in risky group")
else :
  print("You are not in risky group")