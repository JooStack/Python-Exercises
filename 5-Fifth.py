users = {"joseph" : "asdqwe", "harvey" : "123qwe" , "serdar" : "123qrqsad", "yusuf" : "qwe123qew"}

user_name = input("isminizi giriniz.. ").lower().strip()


for x in users :
  if x == user_name : 
    print(f"Hello {user_name}. The password is : {users[user_name]} ")

if user_name not in users :
  print(f"Hello {user_name}. See you later")
