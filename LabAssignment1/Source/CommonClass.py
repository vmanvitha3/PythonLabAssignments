#Python Program to find the list of students who are attending both the Python and Web Application classes
def commonStudents(pList,waList):   #Common Students function definition
    commonList = []                 # create empty list to store students present in both classes
    uncommonList = []               # create empty list to store students not present in both classes
    for s1 in pList:                #loop for each student in pList(Python Student list text file)
        found = False               #set found t0 False when student is not present in the other class
        for s2 in waList:           #loop for each student in waList(Web Development Student list text file)
            if s1 == s2:
                found = True        #Set found to True if student is in both classes
                commonList.extend([s1])         #add student to commonList if in both classes
        if found == False:                      #if found is False that means students not in both classes
            uncommonList.extend([s1])           #add student to uncommonList if not in both classes
    for s in waList:                #loop for each student in waList(Web Development Student list text file)
        if s not in commonList:     #if student name is not in common list
            uncommonList.extend([s])    #then add to uncommon list
    print("Common Students List: ",commonList)          #print list which contains students in both classes
    print("Uncommon Students List: ",uncommonList)      #print list which doesnot contains students in both classes
#files in which student names are stored
l1 = "PythonList"
l2 = "WebApplicationList"
#Empty lists to store names from files
list1 = []
list2 = []
try:    #if file exists it opens
    f1 = open(l1)   #open file
    for word in f1:     #loop each name present in PythonList
        list1.extend([word.strip()])    #add each name in the file to list1
    print("Python List: ",list1)        #print names stored in list1
except: #if no such file exists it throws an exception and exits
    print ("File cannot be opened",l1)
    exit()
try:    #if file exists it opens
    f2 = open(l2)
    for words in f2:        #loop each name present in WebApplicationList
        list2.extend([words.strip()])       #add each name in the file to list2
    print("Web Application List: ", list2)  #print names stored in list2
except: #if no such file exists it throws an exception and exits
    print ("File cannot be opened",f2)
    exit()
commonStudents(list1,list2) #Call function commonStudents passing both lists as arguments