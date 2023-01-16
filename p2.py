p1=input("Enter a partition Name:")
s1= input("Enter {} size: ".format(p1))

p2=input("Enter a partition Name:")
s2= input("Enter {} size: ".format(p2))

total= int(s1)+int(s2)

print("""
Partition : {}\t Size: {} GB
Partition : {}\t Size: {} GB
==============================================
				Total : {} GB
==============================================
""".format(p1,s1,p2,s2,total))
