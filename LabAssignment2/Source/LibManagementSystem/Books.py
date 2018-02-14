#This class stores details of books along with their quantities and prices
class Books():
    def __init__(self,book,price):#in-built __init__ function which creates and initializes data attributes
        #variable "books" store books along with their availability count in the form of dictionary(key - value pairs)
        self.books = {'Python': 10,
                      'DataScience': 5,
                      'DBMS': 3,
                      'WebDevelopment': 10}
        # variable "prices" store books along with their prices in the form of dictionary(key - value pairs)
        self.prices = {'Python': 10,
                       'DataScience': 20,
                       'DBMS': 15,
                       'WebDevelopment': 25}