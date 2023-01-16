''' read shellname and test whether it matches with ksh or bash. -Valid/Invalid'''

var= input("Enter shellname")

if var== "bash" or var == "ksh":
    print("Valid shell")
else:
    print("Invalid Shell")
    
