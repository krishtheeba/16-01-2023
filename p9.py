eno=int(input("Enter the Enquiry number"))

if(eno >= 500  and eno<=600):
    qno=int(input("Enter the quotation number"))
    if (qno>=550 and qno<=650):
        cname=input("Enter customer name")
        if(cname =="IBM" or cname=="ORACLE" or cname=="HP" or cname=="KLABS"):
            po=int(input("Enter the PO Number"))
            if (po<=1000 and po>=500):
                print("Enquiry Number :{}\t Quotation Number :{}".format(eno,qno))
                print("Customer name: {}\t PO number :{}".format(cname,po))
            else:
                print("Invalid PO number")
        else:
            print("Invalid Customer Name")
    else:
        print("Invalid Qno ")

else:
    print("Invalid Enquiry number")
                
