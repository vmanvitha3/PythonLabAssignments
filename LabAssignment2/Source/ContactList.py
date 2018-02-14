#In any mobile , there is contact list. Create a list of contacts and then prompt the user to do the following:
#a) Display contact by name b) Display contact by number c) Edit contact by name d) Exit

def displayByName(Name):    #method to display contact by name
    list = []           #create empty list
    flag = False        #create boolean variable found initialize it to false
    print("Contact details of",Name,":\n")
    for i in ContactList:   #loop through each contact
        for k, v in i.items():  #for each contact's key value pair
            if v.lower() == Name.lower():   #if contact name matches with the user input contact name
                list.append(i)              #append requested contact details to list
                flag = True                 #change found to true
    if flag:                                # if contact found
        for j in list:
            for k,v in j.items():
                print(k," : ",v)            #print details of contact
        print("\n")
    else:                                   # if contact not found
        print("No contact found with the name ",Name)   #print not found

def displayByNumber(Number):    #method to display contact by number
    list = []                   #create empty list
    flag = False                #create boolean variable found initialize it to false
    print("Contact details of", Number, ":")
    for i in ContactList:               #loop through each contact
        for k, v in i.items():          #for each contact's key value pair
            if v == Number:             #if contact number matches with the user input contact number
                list.append(i)          #append requested contact details to list
                flag = True             #change found to true
    if flag:                            # if contact found
        for j in list:
            for k,v in j.items():
                print(k," : ",v)        #print details of contact
        print("\n")
    else:                               # if contact not found
        print("No contact found with the number ",Number)   #print not found

def editByName(Name,newName):       #method to edit contact name
    for x in ContactList:           #loop through each contact from contactList
        if x["name"].lower() == Name.lower():   #if requested contact name is found
            x["name"] = newName      #Change their name to new name entered by user
    print("\nAfter Editing Name:\n",ContactList)  #print new contact list after editing

def editByNumber(Name,newNumber):   #method to edit number
    for x in ContactList:           #loop through each contact from contactList
        if x["name"].lower() == Name.lower():   #if requested contact name is found
            x["number"] = newNumber             #Change their number to new number entered by user
    print("\nAfter Editing Number:\n",ContactList)    #print new contact list after editing


def editByEmail(Name,newEmail): #method to edit contact email
    for x in ContactList:           #loop through each contact from contactList
        if x["name"].lower() == Name.lower():   #if requested contact name is found
            x["email"] = newEmail               #Change their email to new email entered by user
    print("\nAfter Editing Email:\n",ContactList) #print new contact list after editing


def editContact(Name):  #method to edit contact
    list = []           #create empty list
    flag = False        #create boolean variable found initialize it to false
    print("Edit Contact By \n'1' : Name  \n'2' : Number  \n'3' : Email  \n")    #Select how to edit contact
    choice = input("Enter choice\n")    #Enter choice to edit contact
    if choice == '1':
        newName = input("Enter Name to edit\n")
        editByName(Name,newName)    #call method to edit contact by name
    elif choice == '2':
        newNumber = input("Enter Number to edit\n")
        editByNumber(Name,newNumber)    #call method to edit contact by number
    elif choice == '3':
        newEmail = input("Enter Email to edit\n")
        editByEmail(Name,newEmail)      #call method to edit contact by email
    else:                               #if chosen wrong choice
        print("Invalid choice to edit contact")

#Contact details list
ContactList = [{'name':'Rashmi','number':'8797989821','email':'rr@gmail.com'},{'name':'Saria','number':'9897989822','email':'ss@gmail.com'}]
#Choose What to do with contact display or edit
print("ENTER \n'a' : Display contact by name  \n'b' : Display contact by number  \n'c' : Edit contact by name  \n'd' : Exit ")

while True: #keep asking till user exits
    print("Contact List: ", ContactList)
    choice = input("\nEnter your choice: \n") #Enter choice
    if choice.lower() == 'a':   #if diplay by name
        Name = input("Enter Name to display contact")
        displayByName(Name)     #call method to display by name
    elif choice.lower() == 'b': #if diplay by number
        Number = input("Enter Number to display contact")
        displayByNumber(Number) #call method to by number
    elif choice.lower() == 'c': #if edit by name
        edit = input("Enter Name to edit contact")
        editContact(edit)       #call method to edit by name
    elif choice.lower() == 'd': #if choosen exit
        print("Contact List: ", ContactList)
        print("Exiting...!!!")
        break
    else:   #if nothing is chosen break program to exit
        print("Invalid Choice")
        print("Exiting...!!!")
        break