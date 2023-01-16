name=input("Enter a student name")
s1= int(input("Enter subject mark1"))
s2= int(input("Enter subject mark2"))
s3= int(input("Enter subject mark3"))

total= s1+s2+s3

avg= total/3

print("""
Student Name: {}
Subject1  :   {}
Subject2  :   {}
Subject3  :   {}
Total   :     {}
Average  :    {}
""".format(name,s1,s2,s3,total,avg))

