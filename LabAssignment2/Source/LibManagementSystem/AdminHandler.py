from LibManagementSystem.Books import Books
from LibManagementSystem.Person import Person
from LibManagementSystem.checkOut import checkOut

#Class AdminHandler is used to initialize values of person, checkOut and books and also to checkAvailabily of books when a particular book is requested
#Used for administrator
class AdminHandler(checkOut):#inheritance "checkOut" is passed in class declaration
    # class attribute used to store books and their prices from Books Class
    bookList = None

    # in-built default constructor __init__ function which creates and initializes data attributes
    def __init__(self, student_id, student_fname, student_lname, requested_bookname, quantity, username, password,type):
        # person variable is an instance of Person class which initializes values of its class
        person = Person(student_id, student_fname, student_lname, username, password,type)
        # bookList variable is an instance of Books class which initializes values of its class
        AdminHandler.bookList = Books(requested_bookname, quantity)
        # call its super/parent class by passing arguments to initialize values
        super(AdminHandler, self).__init__(person, AdminHandler.bookList,requested_bookname,type)
        self.requestedBook = requested_bookname

    # checkAvailabily method is used to check for availability of requested book by Administrator
    def addItemToShelf(self):
        if  (AdminHandler.bookList.books.get(self.requestedBook)):  #checks for availability
            AdminHandler.bookList.books[self.requestedBook] += 1    #if availbale increments availability by 1
            print ("\n*********Added Book To Shelf*********\n")
        else:   #adds book to booklist for the firsttime
            AdminHandler.bookList.books[self.requestedBook] = 1     #Make availability to 1
            AdminHandler.booksList.prices[self.requestedBook] = 30  #sets price of book
            print("\n*********Added New Book To Shelf*********\n")