from datetime import datetime

name=input("enter your name:")

list='''
Rice     Rs 20/kg
Sugar    Rs 30/kg
Sampoo   Rs 25/kg
Oil      Rs 80/liter
Salt     Rs 25/kg
Horlicks Rs 150/pks
Boot     Rs 150/pks
Closeup  Rs 25/pks
'''
#Declaration 
Price=0
Pricelist=[]
Totalprice=0
Finalprice=0
Ilist=[]
Qlist=[]
Plist=[]

#Rates for item
Items={"Rice":20,"Sugar":30,"Sampoo":25,"Oil":80,"Salt":25,"Horlicks":150,"Boot":150,"Closeup":25}
option=int(input("for list of item press 1:"))
if option==1:
    print(list)
for i in range(len(Items)):
    inp1=int(input("if u want buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        Item=input("Enter your items:")
        Quantity=int(input("Enter Quantity:"))
        if Item in Items.keys():
            price=Quantity*(Items[Item])
            Pricelist.append((Item,Quantity,Items,Price))
            Totalprice+=price
            Ilist.append(Item)
            Qlist.append(Quantity)
            Plist.append(price)
            GST=(Totalprice*8)/100
            Finalamount=GST+Totalprice
        else:
            print("sorry you enetered item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yess or no:")
    if inp=="yes":
        pass
        if Finalamount!=0:
            print(25*"=","Vasantha Supermarket",25*"=")
            print(28*"=","Gandhi Road",32*"=")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("Sno", 8*" ", "Items",8*" ","Quantity",3*" ","Price")
            for i in range(len(Pricelist)):
                print(i,8*' ',1*' ',Ilist[i],13*' ',Qlist[i],8*" ",Plist[i])
            print(75*"-")
            print(50*" ","Totalamount:","Rs",Totalprice)
            print("GST amount",52*" ","Rs",GST)
            print(75*" -")
            print(50*" ","Finalamount:","Rs",Finalamount)
            print(75*"-")
            print(20*" ","Thanks for visting")
            print(75*"-") 

                
               

           
            





