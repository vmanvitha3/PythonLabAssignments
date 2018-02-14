from LibManagementSystem.Books import Books
from LibManagementSystem.Person import Person
from LibManagementSystem.checkOut import checkOut

#Class Library is used to initialize values of person, checkOut and books and also to checkAvailabily of books when a particular book is requested
#Used for student
class Library(checkOut):    #inheritance "checkOut" is passed in class declaration

    bookList = None     #class attribute used to store books and their prices from Books Class

    # in-built default constructor __init__ function which creates and initializes data attributes
    def __init__(self, person_id, person_fname, person_lname, requested_bookname, quantity, username, password,type):
        #person variable is an instance of Person class which initializes values of its class
        person = Person(person_id, person_fname, person_lname, username, password,type)
        # bookList variable is an instance of Books class which initializes values of its class
        Library.bookList = Books(requested_bookname, quantity)
        #call its super/parent class by passing arguments to initialize values
        super(Library, self).__init__(person,Library.bookList,requested_bookname,type)
        self.requestedBook = requested_bookname

    #checkAvailabily method is used to check for availability of requested book by student
    def CheckAvailability(self):
        if  (Library.bookList.books.get(self.requestedBook) > 0):   #checks for availability
            Library.bookList.books[self.requestedBook] -= 1 #if availbale decrements availability by 1
            self.personRecord['person_totalCost']+= Library.bookList.prices[self.requestedBook] #adds cost of book to amount due
            print ("\nRequested Book\n")