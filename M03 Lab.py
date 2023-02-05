#########################################################
#
# M03 assignment - Lists, Functions, and Classes
#
# Allene Cates
#
# 02/05/2023
#
# This program allows the user to input details about their
# vehicle and the program will print the information entered
#
#########################################################

#Creates a class for automobile
class Automobile:

    def __init__(self, year, make, model, door, roof,):
        self.year = year
        self.make = make
        self.model = model
        self.door = door
        self.roof = roof

# Allows for user input for vehicle details     
    def getYear(self):
        self.year = input('Please enter the vehicle year: ')        

    def getMake(self):
        self.make = input('Please enter the vehicle make: ')        

    def getModel(self):
        self.model = input('Please enter the vehicle model: ')
        
    def getDoor(self):
        self.door = input('Please enter the number of doors. 2 or 4: ')

    def getRoof(self):
        self.roof = input('Please enter the vehicle roof type. Solid or sun: ')

selection = Automobile('n','n','n','n','n')

Automobile.getYear(selection)
Automobile.getMake(selection)
Automobile.getModel(selection)
Automobile.getDoor(selection)
Automobile.getRoof(selection)

#Prints the users vehicle details in a readable format
print(f'Your vehicle is a {selection.year} {selection.make} {selection.model} with {selection.door} doors and a {selection.roof} roof!')