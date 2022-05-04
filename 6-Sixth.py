print("Welcome to the player registration program...")
x = 1
informations = {}
for n in range(1,3):
  informations[int(input("No.."))] = {
      "Name" : input("Name..").capitalize(),
      "Age" : input("Age.."),
      "Team" : input("Team..").capitalize(),
      "Position" : input("Position..").capitalize()
  }

print("Informations are recording..")
for n in informations :
  spc = informations[x]["Name"]
  
  print("No:", x, "---", "Name :", spc)
  x += 1
request = int(input("please enter the the No.."))
print(informations[request])