#TASK

#function to create empty dict
def f1():
    d={}
    return d

#function to convert file content to dict
def f2(d):
    fobj=open("D:\\property.txt")
    for var in fobj:
        var.strip() # remove \n
        L=var.split("=")
        k,v= L # multiple  initialization
        d[k]=v # adding data to dict
    return d

# function to display dict
def f3(d):
    for v in d:
        print("{}:{}".format(v,d[v]))
    
#function for dict updation
def f4(d):
    d["interface"]="eth1" # dict modification
    d["bootproto"]="None" #dict modification
    d["onboot"]="yes" # adding new entry to dict
    return d
def f5(d):
    with open("D:\\newproperty.txt","w") as wobj:
        for v in d:
            wobj.write("{}={}\n".format(v,d[v]))
            

d=f1()    # empty dict
d1=f2(d)      # dict append operation
print("Dict details:-")
f3(d1)       # display dic
print("Dict Modification")
newdict=f4(d1)   # dict modification
print("Updated dict details")
f3(newdict)    # display dupdated dict
f5(newdict)    #  write updated dict to newfile