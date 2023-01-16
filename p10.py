'''read login name
test login name is root (or) admin---> matched'''


i=0
while i<3: #while(i<3):
    v= input("Enter login name")
    if v=="root" or v=="admin":
       print("Success")
       break
    else:
        print("Try-Again")
    i=i+1


    
