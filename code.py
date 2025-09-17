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
cs_lab_schedule = []
bio_lab_schedule = []
chem_lab_schedule = []
physics_lab_schedule = []

cs_lab1 = [] 
cs_lab2 = []
cs_lab3 = []

chem1_materials = ["Test Tubes", "Gloves", "Flasks", "Beakers"]
chem2_materials = ["Test Tubes", "Gloves", "Flasks", "Beakers"]
bio_lab1_materials = ["placeholder"]
bio_lab2_materials = ["placeholder"]
bio_lab3_materials = ["placeholder"]
microbio_lab_materials = ["placeholder"]
cs_lab_materials = ["Acer Laptop", "PC"]

materials=[chem1_materials,chem2_materials,bio_lab1_materials,bio_lab2_materials,
           bio_lab3_materials,microbio_lab_materials,cs_lab_materials]

chem_avail1 = [10,5,5,3]
chem_avail2 = [10,5,5,3]
bio_avail = [1]
cs_avail = [10]

avail=[chem_avail1,chem_avail2,bio_avail,cs_avail]


#Functions
def access(materials):
    id=1
    print("Id:  Item and no_materialsability:")
    while id-1<len(materials):
        print(str(id).zfill(2)+".    "+materials[id-1]+" - "+str(materials[1[id-1]]))
        id+=1

def take(no_materials):
    while True:
        id=input("Enter the id of the material you want: ")
        if id.lower()=="exit":
            break
        elif int(id)>len(no_materials) or int(id)<0:
            print("Id not found.")
        else:
            id=int(id)
            i=id-1
            while True:
                amt=int(input("Enter how many you want to take: "))
                if amt>no_materials[i]:
                    print("Not enough.")
                else:
                    no_materials[i]-=amt
                    break
    return no_materials
 
def add(avail):
    while True:
        id=input("Enter the id of the material you want: ")
        if id.lower()=="exit":
            break
        elif int(id)>len(avail) or int(id)<0:
            print("Id not found.")
        else:
            id=int(id)
            i=id-1
            amt=int(input("Enter how many you want to add: "))
            avail[i]+=amt
            break
    return avail
 
 def reservations(index):
    output = ""
    lab_type = ""
    day = input("Day of the week: ")
    time = input("Period/Schedule (ex. 1st Period): ")
    if index == 0:
        lab = "Chem Lab 1"
        lab_type = "Chem Lab"
    elif index == 1:
        lab = "Chem Lab 2"
        lab_type = "Chem Lab"
        
    elif index == 2:
        lab = "Biology Lab 1"
        lab_type = "Bio Lab"
    elif index == 3:
        lab = "Biology Lab 2"
        lab_type = "Bio Lab"
    elif index == 4:
        lab = "Biology Lab 3"
        lab_type = "Bio Lab"
    elif index == 5:
        lab = "Microbio Lab"
        lab_type = "Bio Lab"
        
    elif index == 6:
        lab = "Computer Science Lab 1"
        lab_type = "CS Lab"
    elif index == 7:
        lab = "Computer Science Lab 2"
        lab_type = "CS Lab"
    elif index == 8:
        lab = "Computer Science Lab 3"
        lab_type = "CS Lab"
        
    output = f"{lab} -- {time} on {day}"
    if lab_type == "Chem Lab":
        if output not in chem_lab_schedule:
            chem_lab_schedule.append(output)
        else:
            return ":::::: Error :::::: \n A reservation already exists"
            
    elif lab_type == "Bio Lab":
        if output not in chem_lab_schedule:
            bio_lab_schedule.append(output)
        else:
            return ":::::: Error :::::: \n A reservation already exists"
    elif lab_type == "CS Lab":
        if output not in chem_lab_schedule:
            cs_lab_schedule.append(output)
        else:
            return ":::::: Error :::::: \n A reservation already exists"
    return output


#Code
print("\n\n                   Laboratory Transaction Recorder/Tracker \n")
print("••••••••••• Please input the required specifications for the transaction details •••••••••••")
print("•••••••••••• You may input exit at any stages of the transaction to end early •••••••••••••\n\n\n")
while True:
    print("•Note that the available labs are Bio (1, 2, MicroBio), Chem (1, 2), CS (1,2,3), Physics (1, 2) \n")
    lab=input("Enter the lab you want to check or exit to leave: ").strip().lower()
    if lab=="chem1" or lab=="chemistry1":
        index=0
    elif lab=="chem2" or lab=="chemistry2":
        index=1
    elif lab=="bio1" or lab=="biology1":
        index=2
    elif lab=="bio2" or lab=="biology2":
        index=3
    elif lab=="bio3" or lab=="biology2":
        index=4
    elif lab=="microbio" or lab=="microbioology":
        index=5
    elif lab=="comsci1" or lab=="computerscience1" or lab=="cs1":
        index=6
    elif lab=="comsci2" or lab=="computerscience2" or lab=="cs2":
        index=7
    elif lab=="comsci3" or lab=="computerscience3" or lab=="cs3":
        index=8
    elif lab=="exit":
        break
    else:
        print("Invalid option")
        continue
    while True:
        access(index)
        command=input("Borrowing equipment or Adding/Returning equipment?\n").strip().lower()
        if command=="take":
            take(no_materials[index])
        elif command=="add":
            add(no_materials[index])
        elif command=="exit":
            break
        else:
            print("Invalid option")
    print("Thank you for checking on this lab.")
print("Thank you for checking the logs.")
