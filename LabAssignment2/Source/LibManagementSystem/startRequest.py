from LibManagementSystem.Library import Library
from LibManagementSystem.AdminHandler import AdminHandler

#Main program-Program starts here

print("***************************")
print("Login as Administrator")
#instance of AdminHandler
A1 = AdminHandler("3","Admin","User","sql","1","admin","admin1234","Admin")
A1.currentStatus()  #calling method currentStatus to display available items on shelf
A1.addItemToShelf() #calling method addItemToShelf to add item
A1.currentStatus()  #calling method currentStatus to display available items on shelf

print("\n")
print("***************************")


print("Login as Student")
s1 = Library("3","xyz","abc","Python","1","root","1234","Student")  #instance of Library
s1.CheckAvailability()  #calling method CheckAvailability to display available and to deduct if available
s1.currentStatus()      #calling method currentStatus to display available items on shelf
s1.getTotalPrice()      #calling method getTotalPrice to display amount due for the items in cart
print("***************************")