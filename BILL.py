import time
item={
          1001:"Milk",
          1002:"Juice",
          1003:"Chocla.",
          1004:"Biscute",
          1005:"Soap",
          1006:"Toothp.",
          1007:"Spice",
          1008:"Salt",
          1009:"Tomato",
          1010:"Chilli"
          }

price={
          1001:56,
          1002:35,
          1003:10,
          1004:20,
          1005:25,
          1006:33,
          1007:25,
          1008:10,
          1009:58,
          1010:76
          }


#printing bill

def bill():
    time_=time.asctime()
    total=0
    print("\t==================================\n\n\t\tJAY'S GLOCERY SHOP\n\n\t==================================\n")
    print("\nNAME : {}\nTIME : {}".format(name,time_[11:19]))
    print("S.NO\tITEM\t\tRATE\tQUANTITY\tTOTAL\n=======================================================================")
    for i in range(len(tray)):
        
        print("{}\t{}\t\t{}\t{}\t\t{}\n".format(i+1,item[tray[i][0]],price[tray[i][0]],tray[i][1],int(price[tray[i][0]])*int(tray[i][1])))
        total+=int(price[tray[i][0]])*int(tray[i][1])

    print("=======================================================================")
    print("\n\n\nTOTAL = ",total)

    moneyGot=int(input("\nAmount Bought : "))
    
    while moneyGot<total:
        print("\nINSUFICIENT MONEY PLEASE GET MORE\n")
        moneyGot=int(input("Amount Bought : "))
        
    if moneyGot!=total:
        print("\nGIVE BACK {}".format(moneyGot-total))
        time.sleep(2)
    print("\n\n***THANK YOU VISIT AGAIN***")
    
    


    
def add(id_):

    print("\nITS SEEMS LIKE THE ITEM NOT IN THE LIST, PLEASE ADD IT TO THE LIST\n")
    
    item[id_]=input("ENTER THE NAME OF ITEM WITH ID {} : ".format(id_))
    price[id_]=input("ENTER THE RATE OF THE ITEM : ")
    
    print("\tITEM ADDED SUCCESFULLY\n")






#main function








idx =0

tray=[]
while True:
    
    print("\t===================================\n\n\t\tJAY'S GLOCERY SHOP\n\n\t===================================")
    print("\nWELCOME BACK!\n\nUSE '0' TO PRINT THE BILL\nENTER 'close' TO CLOSE THE PROGRAM")
    
    name=input("\nCUSTOMER NAME : ")
    if name=="close":
            break
    
    while True:
            
        temp1=int(input("\n-->Item ID: "))        
        if temp1==0:                   # for exiting loop
            bill()
            break

        if temp1 not in item:           #adding item if not in the list
            id_=int(temp1)
            add(id_)
            
        tray.append([temp1])   
        temp2=int(input("   Item Count: "))
        tray[idx].append(temp2)
        idx+=1




        
    
    
            
    
