var= input("Enter shellname")

if var=="bash":
    fname="/etc/bashrc"
elif var=="ksh":
    fname="/etc/kshrc"
elif var=="csh":
    fname="/etc/cshrc"
else:
    var="/bin/nologin"
    fname="/etc/profile"

print("Shell name :{}\t Profile File :{}".format(var,fname))
