from LibManagementSystem.Books import Books
from LibManagementSystem.Person import Person

#Class checkOut is adds details of a person and items to cart and displays currentStatus of available books and also total price of items in the cart

#Multiple Inheritance used

class checkOut(Person,Books):#inherits implementation from base classes(parent/ancestor) : Person and Books
    s_cart = [] #data member/ class attribute s_cart is a list used to store items requested by the student
    booksList = None    #class attribute used to store books and their prices from Books Class

    # in-built default constructor __init__ function which creates and initializes data attributes
    def __init__(self, person, bookList, requested_bookname,type):
        self.person = person
        self.cost = 0   #initialize amount due to 0
        if type == "Student":   #if type is student append requested items to cart
            checkOut.s_cart.append(requested_bookname)
            #set person Record with all the detials
        self.personRecord = {'person_name' : person.person_fname + " " + person.person_lname,
                              'person_id' : person.person_id,
                              'person_totalCost': self.cost,
                              'itemscart' : checkOut.s_cart
                              }
        checkOut.booksList = bookList
        self.req_book = requested_bookname

    #below method displays us current available books with number
    def currentStatus(self):
        print("\nDisplay Available Books:")
        for key, value in checkOut.booksList.books.items():
            print(key, value)

    #The method getTotalPrice prints items requested by student in cart along with total amount due
    def getTotalPrice(self):
        print("\nItems in the cart: ",self.personRecord['itemscart'])
        print("\nTotal Amount Due: $",self.personRecord['person_totalCost'])