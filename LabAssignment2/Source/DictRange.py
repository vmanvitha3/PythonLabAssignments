#Write a program to find the books from the dictionary in the range given by user.

#Dictionary with book title as key and range as value
bookDict = {"python":50,"web":30,"c":20,"java":40}

list=[] #Empty List

#for each key, value pair in dictionary
for key, value in bookDict.items():
    if value>=30 and value<=40: #if value is in range 30 and 40 inclusive
        list.append(key)        #then append book name that is title of book to the list

#print list of books with in the given range in the form of tuple
print("You can purchase books in range(30-40) inclusive of values: \n",tuple(list))