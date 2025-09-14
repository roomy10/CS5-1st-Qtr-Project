#Laboratory Tracker CS5 1st Quarter Project

'''
Flow

-- User can end or backtrack transaction at any point (need function)
-- Record transactions that happened in the day ie. current session. 
-- User can input "standing" to check current standing of all transactions
-- End with a receipt showing which lab and equipment are reserved (ex. cs_lab1 -- 1st period, previous quanitity >> current quantity)

Command (Which lab for transaction) --> if

--> cs lab --> lab transaction (Reservation) --> 
cs_lab_reservations list (in periods, 10 periods total, excluding wellness and break period) --> 
who's reserving, which lab, period, and the reason for use --> prompt to record another transaction (loop back)


--> bio lab --> Reservation (in periods, 10 periods total, excluding wellness and break period) 
--> lab transaction (Access available equipment/Borrowing equipment from the stockroom/Add or Returning of borrowed equipment/NA)
--> who's reserving, which lab, period, and the reason for use --> prompt to record another transaction (loop back)


--> chem lab--> Reservation (in periods, 10 periods total, excluding wellness and break period) 
--> lab transaction (Access available equipment/Borrowing equipment from the stockroom/Add or Returning of borrowed equipment/NA)
--> who's reserving, which lab, period, and the reason for use --> prompt to record another transaction (loop back)

 
'''

#Initializiation of Variables
materials=[["Test Tubes", "Gloves", "Flasks", "Beakers"],["Bio stuff"]]
avail=[[10,5,5,3],[1]]


#Functions
def access(materials,avail):
    id=1
    print("Id:  Item and availability:")
    while id-1<len(materials):
        print(str(id)+".    "+materials[id-1]+" - "+str(avail[id-1]))
        id+=1

def take(avail):
    while True:
        id=input("Enter the id of the material you want: ")
        if id.lower()=="exit":
            break
        elif int(id)>=len(avail) or int(id)<0:
            print("Id not found.")
            continue
        else:
            id=int(id)
            i=id-1
            while True:
                amt=int(input("Enter how many you want to take: "))
                if amt>avail[i]:
                    print("Not enough.")
                else:
                    avail[i]-=amt
                    break
    return avail
 
def add(avail):
    while True:
        id=input("Enter the id of the material you want: ")
        if id.lower()=="exit":
            break
        elif int(id)>=len(avail) or int(id)<0:
            print("Id not found.")
            continue
        else:
            id=int(id)
            i=id-1
            amt=int(input("Enter how many you want to add: "))
            avail[i]+=amt
            break
    return avail


#Code
while True:
    lab=input("Enter the lab you want to check or exit to leave: ")
    if lab.lower()=="chem" or lab.lower()=="chemistry":
        a=0
    elif lab.lower()=="bio" or lab.lower()=="biology":
        a=1
    elif lab.lower()=="exit":
        break
    else:
        print("Invalid option")
        continue
    while True:
        command=input("Access/Take/Add: ")
        if command.lower()=="access":
            access(materials[a],avail[a])
        elif command.lower()=="take":
            take(avail[a])
        elif command.lower()=="add":
            add(avail[a])
        elif command.lower()=="exit":
            break
        else:
            print("Invalid option")
            continue
    print("Thank you for checking on this lab.")
print("Thank you for checking the logs.")
