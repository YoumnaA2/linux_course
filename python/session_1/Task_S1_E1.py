list=[1,4,6,7,4]
counter=0
#1 st methd
for x in list:  
    if(x==4):
        counter+=1
print(counter)    
#using built in function 
print(list.count(4))