# =============  Laboratory Tracker CS5 1st Quarter Project ============= 

# ================= STOCKROOMS =================

# Chemistry Stockroom 
chem_stockroom = [
    "Safety Goggles","Lab Apron","Chemical Resistant Gloves","Beakers",
    "Conical Flasks","Boiling Flasks","Test Tubes","Watch Glass",
    "Crucible/Mortar & Pestle","Funnels","Measuring Cylinders",
    "Volumetric Flasks","Droppers","Pipettes","Burettes",
    "Ring Stands, Rings, and Clamps","Tongs & Forceps",
    "Spatulas & Scopulas","Thermometer","Bunsen Burner",
    "Litmus and Filter Paper"
]
no_chem_stockroom = [10,10,50,20,15,15,30,10,5,10,15,15,10,10,10,10,5,5,10,3,20]

# Biology Stockroom
bio_stockroom = [
    "Microscope","Test tubes and racks","Dissecting tool kit","Hot plate",
    "Electronic balance","Forceps","Beakers","Conical flasks","Evaporating dish",
    "Graduated cylinders","Droppers & pipettes","Dissecting pan",
    "Glass slides & coverslips","Inoculating loops & Petri dishes",
    "Thermometer","Spatulas & Scopulas","Bunsen Burner","Alcohol Burner",
    "Litmus and Filter Paper"
]
no_bio_stockroom = [10,10,5,10,5,5,20,15,20,20,10,5,10,10,20,5,5,5,20]

# Microbiology Stockroom 
microbio_stockroom = [
    "Microscope (high power)","Autoclave","Incubator","Petri dishes",
    "Test tubes","Inoculating loop","Laminar flow hood","Glass slides & coverslips"
]
no_microbio_stockroom = [10, 2, 3, 50, 40, 20, 1, 100]

# Computer Science Stockroom 
cs_stockroom = ["Acer Laptop","PC","Projector 1","Projector 2","Projector 3"]
no_cs_stockroom = [30,30,3,3,3]

# Physics Stockroom 
physics_stockroom = [
    "Multimeter","Power supply","Oscilloscope","Resistors set","Capacitors set",
    "Wires & connectors","Force meter","Pendulum set","Lens & mirrors kit",
    "Projector"
]
no_physics_stockroom = [10, 5, 3, 50, 40, 100, 5, 5, 15, 3]

# ================= MASTER LISTS =================
materials = [
    chem_stockroom,
    bio_stockroom,
    microbio_stockroom,
    cs_stockroom,
    physics_stockroom
]

no_material = [
    no_chem_stockroom,
    no_bio_stockroom,
    no_microbio_stockroom,
    no_cs_stockroom,
    no_physics_stockroom
]

# ================= TRACKING =================
students_reserved = 0
reservations_count = {"Chemistry": 0, "Biology": 0, "Physics": 0, "CS": 0}
borrowed_count = 0
returned_count = 0
reservation_days = {"Chemistry": [], "Biology": [], "Physics": [], "CS": []}  # grouped by lab

# ================= FUNCTIONS =================
def access(index): 
    print("\n============================================")
    print("Id:  Item and availability:")
    for i, item in enumerate(materials[index], start=1):
        print(f"{str(i).zfill(2)}. {item} - {no_material[index][i-1]}")
    print("============================================\n")

def take(no_materials, index, student):
    global borrowed_count
    borrowed_items = []
    while True:
        id=input("Enter the id of the material you want (or 'exit' to stop): ")
        if id.lower()=="exit":
            break
        elif not id.isdigit() or int(id)>len(no_materials) or int(id)<=0:
            print("Id not found.")
        else:
            i=int(id)-1
            print(f"You chose: {materials[index][i]}")
            amt=int(input("Enter how many you want to take: "))
            if amt>no_materials[i]:
                print("Not enough.")
            else:
                no_materials[i]-=amt
                borrowed_count += amt
                borrowed_items.append(f"{materials[index][i]} ({amt})")
                print(f"Reserved successfully. Remaining: {no_materials[i]}")
        more = input("Do you want to borrow another equipment? (y/n): ").lower()
        if more != "y":
            break
    return borrowed_items

def add(avail, index, student): 
    global returned_count
    returned_items = []
    while True:
        id=input("Enter the id of the material you want to return/add (or 'exit' to stop): ")
        if id.lower()=="exit":
            break
        elif not id.isdigit() or int(id)>len(avail) or int(id)<=0:
            print("Id not found.")
        else:
            i=int(id)-1
            print(f"You chose: {materials[index][i]}")
            amt=int(input("Enter how many you want to add: "))
            avail[i]+=amt
            returned_count += amt
            returned_items.append(f"{materials[index][i]} ({amt})")
            print(f"Added successfully. Now available: {avail[i]}")
        more = input("Do you want to return another equipment? (y/n): ").lower()
        if more != "y":
            break
    return returned_items

def per_transaction_receipt(name, grade_section, reason, day, time, borrowed, returned): 
    print("\n======= TRANSACTION RECEIPT =======")
    print(f"Name: {name}")
    print(f"Grade and Section: {grade_section}")
    print(f"Reason for using lab: {reason}")
    print(f"Day Reserved: {day}")
    print(f"Time Reserved: {time}")
    print(f"Equipment Borrowed: {borrowed if borrowed else 'n/a'}")
    print(f"Equipment Returned: {returned if returned else 'n/a'}")
    print("===================================\n")

def total_summary(): 
    print("\n======= SUMMARY OF TRANSACTIONS =======")
    print(f"# of students that reserved: {students_reserved}")
    print(f"# of reservations for Biology Labs: {reservations_count['Biology']}")
    print(f"# of reservations for Chemistry Labs: {reservations_count['Chemistry']}")
    print(f"# of reservations for Physics Labs: {reservations_count['Physics']}")
    print(f"# of reservations for CS Labs: {reservations_count['CS']}\n")
    print(f"# of reserved equipment: {borrowed_count}")
    print(f"# of returned equipment: {returned_count}")
    print("\nReservation Days by Lab:")
    for lab, days in reservation_days.items():
        if days:
            print(f"- {lab}:")
            for d in days:
                print(f"   • {d}")
    print("=======================================\n")

# ================= Transaction Main =================
print("\n\n                   Laboratory Transaction Recorder/Tracker \n")
print("••••••••••• Please input the required specifications for the transaction details •••••••••••")
print("•••••••••••• You may input exit at any stages of the transaction to end early •••••••••••••\n\n\n")

while True:
    print("•Note that the available labs are: ")
    print("Chem Labs (1, 2)")
    print("Bio Labs (1, 2, 3, MicroBio)")
    print("CS Labs (1, 2, 3)")
    print("Physics Labs (1, 2, 3)\n")
    
    lab=input("Enter the lab you want to reserve or 'exit' to leave: ").strip().lower()
    
    if lab in ["chem1","chemistry1","chem2","chemistry2"]:
        index=0; labname="Chemistry Lab"; labkey="Chemistry"
    elif lab in ["bio1","biology1","bio2","biology2","bio3","biology3"]:
        index=1; labname="Biology Lab"; labkey="Biology"
    elif lab in ["microbio","microbiology"]:
        index=2; labname="Microbiology Lab"; labkey="Biology"
    elif lab in ["comsci1","computerscience1","cs1","comsci2","computerscience2","cs2",
                 "comsci3","computerscience3","cs3"]:
        index=3; labname="Computer Science Lab"; labkey="CS"
    elif lab in ["physics1","physics2","physics3","physics"]:
        index=4; labname="Physics Lab"; labkey="Physics"
    elif lab=="exit":
        break
    else:
        print("Invalid option\n")
        continue

    # Student info
    print("\n===== Reservation Details =====")
    name = input("Enter your full name (or 'exit' to cancel): ")
    if name.lower() == "exit":
        print("Transaction canceled.\n")
        continue
    grade_section = input("Enter your grade and section (or 'exit' to cancel): ")
    if grade_section.lower() == "exit":
        print("Transaction canceled.\n")
        continue
    reason = input("Enter your purpose for using the lab (or 'exit' to cancel): ")
    if reason.lower() == "exit":
        print("Transaction canceled.\n")
        continue
    day = input("Enter the day of reservation (e.g., Monday, January 1) or 'exit': ")
    if day.lower() == "exit":
        print("Transaction canceled.\n")
        continue
    time = input("Enter the time of reservation (e.g., 10:30 AM or 12 PM) or 'exit': ")
    if time.lower() == "exit":
        print("Transaction canceled.\n")
        continue

    student = (name, grade_section, reason, day, time)
    reservation_days[labkey].append(day)

    # Ask if they want to borrow/return
    print("\n===== Accessing Equipment =====")
    borrowed_items = []
    returned_items = []
    choice = input("Do you want to borrow or return equipment? (yes/no): ").strip().lower()
    if choice == "yes":
        while True:
            access(index)
            command=input("Borrowing equipment (take) or Returning equipment (add)?\n(Type 'exit' to stop): ").strip().lower()
            if command=="take":
                borrowed_items.extend(take(no_material[index], index, student))
            elif command=="add":
                returned_items.extend(add(no_material[index], index, student))
            elif command=="exit":
                break
            else:
                print("Invalid option\n")
    else:
        print("Skipping equipment access...\n")

    students_reserved += 1
    reservations_count[labkey] += 1
    per_transaction_receipt(name, grade_section, reason, day, time,
                            ", ".join(borrowed_items) if borrowed_items else None,
                            ", ".join(returned_items) if returned_items else None)

    print("\nThank you for checking on this lab.\n")

total_summary()
