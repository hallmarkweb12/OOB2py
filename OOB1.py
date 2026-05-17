class Employee:
    def _init_(self):
        print("Employee Created")
    def _del_(self):
        print("Destructor Called","Employeee deleted")
obj = Employee()
del obj        
obj2  = Employee()