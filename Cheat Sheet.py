#  MAIN - A summary of Python Code snippets 
    # Object orient programming
        # obj can be var, array etc. objects have properties
        # Function =  Subroutine
        # Class = each file is a class
        # property = 
        # Module = Python .py files that consist of Python code.

def scope():
    # Global vars
    # setters and getters, you this acrross classes which you cant do with global vars.  In fact use s/g to access global vars
    # var a #variable in global scope within entire file
    return()

def install(): #in this example we install boto3 using conda in the currently running Jupyter kernel
    import sys
    !conda install --yes --prefix {sys.prefix} boto3
    
    # PIP install 
    import sys
    !{sys.executable} -m pip install numpy
    return()

def defaultArg( name, msg = "Hello!"):# encode as many parameters as you want
    # var b # local var witin the method (the function here)
    # return()  #only return one thing, but can cirmnavigate with array or dictionary (better?)
    #dictinary is special py array def your own index
    return()

defaultArg ("brad")
    return()

# import # used to call other python scripts

def Pip(): # and Conda both installers for the same Python install
    # PIP= package installer
    # Boto is the AWS SDK that connect jupyter notebook to AWS, 
    # good practice 
    # good practice, rather than 
    return()

# OOP Object orient programming
    # class: Employee a blueprint for an instance, where an individual employee is an INSTANCE of that class
class Employee:
    pass   # if you want to leave empty for time being, no attributes or methods
    emp_1=Employee() #instance variables are unique
    emp_2=Employee()

    emp_1.first = 'Corey'
    emp_1.last = 'Schafer'
    emp_1.email = "Corey.Shfer@comapany.com"
    emp_1.pay=50000

    emp_1.first = 'Test'
    emp_1.last = 'User'
    emp_1.email = "Test.User@comapany.com"
    emp_1.pay=60000

    print(emp_1.email)
    # attributes - data 
    # methods - function associated with a class
    #  
     


