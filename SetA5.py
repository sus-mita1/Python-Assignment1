a = 1
b = 1
next_term = a+b
print(f"The numbers of series are :" )    
for i in range(0,10):
    print(a,",",end ="")
    a = b
    b = next_term
    next_term = a+b
   
#The numbers of series are :
#1 ,1 ,2 ,3 ,5 ,8 ,13 ,21 ,34 ,55 ,