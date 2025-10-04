Light="green"

if(Light=="red"):
    print("stop")
elif(Light=="green"):
    print("go")
elif(Light=="yellow"):
    print("look")
    
else:
    print("ligh is broken")
    

Marks=int (input("Enter Student Marks :"))

if(Marks>=90):
    Grade="A"
    
elif(Marks>=80 and Marks<90):
    Grade ="B"
    
elif(Marks>=70 and Marks< 80):
    Grade="C"
    print(Grade)
else:
    print("fail")
    
    
#nesting
Age=45
if(Age>=18):
    if(Age>=80):
        print("cannot drive")
    else:
        print("Can Drive")

else:
    print("Cannot Drive")
        
