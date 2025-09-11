#Laboratory Tracker CS5 1st Quarter Project


#Initializiation of Variables
chem=["Test Tubes", "Gloves", "Flasks", "Beakers"]
avail=[10,5,5,3]


#Functions
def access(chem,avail):
  i=0
  while i<len(chem):
    print(chem[i]+" - "+str(avail[i]))
    i+=1
def take(avail):
  while True:
    id=input("Enter the id of the material you want: ")
    if id.lower()=="exit":
      break
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
    else:
      id=int(id)
      i=id-1
      amt=int(input("Enter how many you want to add: "))
      avail[i]+=amt
      break
  return avail


#Code
while True:
    command=input("Access/Take/Add: ")
    if command.lower()=="access":
        access(chem,avail)
    elif command.lower()=="take":
        take(avail)
    elif command.lower()=="add":
        add(avail)
    elif command.lower()=="exit":
        break
print("Thank you for checking the logs.")
