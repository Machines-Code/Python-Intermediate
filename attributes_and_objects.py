class Employee:
    numberofWorkingHours = 40  # This is known as a Class Attribute


employeeOne = Employee()
employeeTwo = Employee()
print(employeeOne.numberofWorkingHours)

# We have now set something called an Instance Attribute
employeeOne.numberofWorkingHours = 45

# When running a program, Python will first check for an Instance Attribute with a given name, and then a Class Attribute with that given name.
# If neither attribute is found, Python will return an error
# If only one attribute is found, that attribute will be returned
# If both attributes exist, the Instance Attribute will be returned and the Class Attribute ignored. Be mindful of this.


class Worker:
    def workerDetails(self):
        self.name = "Matthew"
        print(f"Name: {self.name}")
        self.age = 30
        print(f"Age: {self.age}")

    def printEmployeeDetails(self):
        print(f"{self.name} is {self.age} years old.")


worker = Worker()
worker.workerDetails()  # Python reads this line as - Worker.workerDetails(worker)
worker.printEmployeeDetails()


# Instance methods

class Employee2:
    def employeeDetails(self):
        self.name = "Ben"

    @staticmethod
    # Without this line, welcomeMessage() will not be expecting a parameter, but will receive one later in the program, which returns an error.
    # The @staticmethod decorator extends the functionality of the function and allows Python to ignore the binding of the object.
    def welcomeMessage():
        print("Welcome to our organisation!")


employee = Employee2()
employee.employeeDetails()
print(employee.name)
employee.welcomeMessage()


# init() method

class Employee3():

    def __init__(self, name):
        self.name = name

    def displayEmployeeDetails(self):
        print(self.name)


employeeOne = Employee3("Mark")
employeeOne.displayEmployeeDetails()
employeeTwo = Employee3("Matthew")
employeeTwo.displayEmployeeDetails()
employeeThree = Employee3("Alice")
employeeThree.displayEmployeeDetails()
