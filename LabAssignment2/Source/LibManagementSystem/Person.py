class Person():
    def __init__(self,id,fname,lname,username,password,type):#in-built default constructor __init__ function which creates and initializes data attributes
        #Stores values in variables
        self.person_id = id
        self.person_fname = fname
        self.person_lname = lname
        self.s_userName = "root"
        self.s_passwd = "1234"
        self.a_userName = "admin"
        self.a_passwd = "admin1234"
        self.validateUser = username
        self.validatePassword = password
        print("welcome To Library Management System")
        #Validates UserName and Password for student type
        if (self.s_userName == self.validateUser) and (self.s_passwd == self.validatePassword) and type=="Student":
            print("Student Login Successful")   #prints successful login message
            print("***************************")
        # Validates UserName and Password for Admin type
        elif (self.a_userName == self.validateUser) and (self.a_passwd == self.validatePassword) and type=="Admin":
            print("Admin Login Successful")     #prints successful login message
            print("***************************")
        else:#Exits program if wrong credentials are entered
            print("Wrong Credentials")          #print unsuccessful login message
            print("*********Exiting!!!*********")
            exit(0)