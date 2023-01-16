'''write a python program

read a port number from <STDIN>
test a port number 500-599 '''

port=int(input("Enter a port number"))

if port>=500 and port<600:
    print("Valid port")
else:
    print("Invalid Port")

    
