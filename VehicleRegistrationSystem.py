# Task 1: Vehicle Registration System

# - Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. 
# Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.

# - Code Example: Provide a basic structure for the Vehicle class without methods.

#    class Vehicle:
#        def __init__(self, reg_num, type, owner):
#           self.registration_number = reg_num
#            self.type = type
#           self.owner = owner
# - Expected Outcome: Completion of the Vehicle class with the update_ownermethod and a demonstration 
# script showing the creation of Vehicle objects and updating their owners.


class Vehicle:
    def __init__(self,registration, type, owner):
        self.registrationNumber = registration
        self.type = type
        self.owner = owner

    def printOwner(self):
        print("Current owner is:", self.owner)

    def updateOwner(self, newOwner):
        print("New owner is:", newOwner)

vehicle1 = Vehicle(8675309, "Tesla", "Jon")
vehicle1.printOwner()

vehicle1.updateOwner("Katie")


        