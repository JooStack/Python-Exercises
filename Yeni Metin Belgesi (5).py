b = 10000  
v = 1  
top = 0 
a = []  
for i in range(b,v-1,-1) :
  top = 0
  for x in range(v,b+1) :
    if i % x == 0 :
      top += x
      
  top -= i
  a.append(top)  

amicable_list = []
t = v-1
liste = list(range(b,v-1,-1))
for p in a : 
  y = 0
  for o in range(b,v-1,-1) :  
    
    if p == o :
      if liste[t] == a[y] and p != liste[t] : 
        
        amicable_list.append(p) 
      
    y += 1     
  t += 1
os = len(amicable_list) - 2
for i in amicable_list[len(amicable_list)-1::-2] :
  print(f"{i} and {amicable_list[os]} are amicable numbers.")
  os -= 2