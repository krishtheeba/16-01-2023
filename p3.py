var=input("Enter shellname")
if(var == "bash"):
    fname= "bashrc"
else:
    fname= "/etc/profile"

print("Shell name is :{} Profile file name :{}".format(var,fname))

