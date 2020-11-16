class ParkingLot:
    def __init__(self, n):
        self.spaces = [None] * n
        self.isParkingEmpty = True
        self.isParkingFull = False
        
 
    def parkCar(self,car):
        # if ParkingLot is already full from previous parkings no need to check for empty slots
        if self.isParkingFull:
             print("Sorry, Parking lot is full")
        else:
            for i in range(len(self.spaces)):
                if self.spaces[i] is None:
                    self.spaces[i] = car
                    print('Allocated slot no: ', i + 1)
                    self.isParkingEmpty = False
                    return
            #Setting isParkingFull for the first time.
            self.isParkingFull = True
            print("Sorry, Parking lot is full")

       
    def printStatus(self): 
        header1 = "{0:<10}".format("Slot No.")  + "{0:<25}".format("Registration No.") + "{0:<15}".format("Colour")
        print (header1) 
        header2 = "-" * 50
        print (header2)
        if self.isParkingEmpty:
            print("Parking Lot is vacant. No car details to display")
        else:
             for i in range(len(self.spaces)):
                if self.spaces[i] is not None:
                    detail =  "{0:<10}".format(i+1)  + "{0:<25}".format( self.spaces[i].reg_no) + "{0:<15}".format(self.spaces[i].colour)                    
                    print(detail)

    def leaveCar(self,slot):
        
        if slot <= 0 or slot > len(self.spaces):
            print("Please enter a valid Slot number")
        elif self.spaces[slot - 1] is not None:
            self.spaces[slot - 1] = None
            print("Slot number ", slot, " is free")
            if self.isParkingFull:
                self.isParkingFull = False
        else:
            print("Slot no. entered is empty")      
        

    def printSlotNumbersForColour(self,colour):
        op = ""
        if self.isParkingEmpty:
            print("Parking Lot is empty.")
        else:
            for i in range(len(self.spaces)):
                if self.spaces[i] is not None:
                    if self.spaces[i].colour == colour:
                        if len(op) == 0:
                            op = op + str(i + 1) 
                        else:
                            op = op + " ," + str(i + 1)  
        if len(op) == 0:
            print("Not found")
        else:
            print(op)

    def printRegNumbersForColour(self,colour):
        op = ""
        if self.isParkingEmpty:
            print("Parking Lot is empty.")
        else:
            for i in range(len(self.spaces)):
                if self.spaces[i] is not None:
                    if self.spaces[i].colour == colour:
                        if len(op) == 0:
                            op = op + self.spaces[i].reg_no 
                        else:
                            op = op + " ," + self.spaces[i].reg_no  
        if len(op) == 0:
            print("Not found")
        else:
            print(op)

    def printSlotNumberForRegNo(self,reg_no):        
        if self.isParkingEmpty:
            print("Parking Lot is empty.")
        else:
            for i in range(len(self.spaces)):
                if self.spaces[i] is not None:
                    if self.spaces[i].reg_no == reg_no:
                        print(i + 1)
                        return
            print("Not found")
        

class Car:
    def __init__(self, reg_no, colour):
        self.reg_no = reg_no
        self.colour = colour

def createParkingLot(n=5):
    ParkingLot1 = ParkingLot(int(n))
    return ParkingLot1

def listValidCommands():
    print("List of valid commands")
    print(" 1> create_parking_lot no" )
    print(" 2> park registration_no color")
    print(" 3> status")
    print(" 4> leave slot_no")
    print(" 5> registration_numbers_for_cars_with_colour colour ")
    print(" 6> slot_numbers_for_cars_with_colour colour ")
    print(" 7> slot_number_for_registration_number registration_no")


def executeCommands(command):
    global PL
    global parkingLotCreated 
    arr = command.split()   
    if arr[0] == "create_parking_lot":        
        if len(arr) < 2:
            if not parkingLotCreated:
                PL = createParkingLot()
                parkingLotCreated = True
                print("As no.of slots was not specified, created a parking lot with default 5 slots ")
            else:
                print("Parking Lot already created")
        else:
            if not parkingLotCreated:
                PL = createParkingLot(arr[1])
                parkingLotCreated = True
                print("Created a parking lot with ", arr[1], "slots")
            else:
                print("Parking Lot already created")        

    elif arr[0] == "park":                       
        if PL:
            if len(arr) == 1:
                print("Enter the command again specifying the car registration number and color")
                return
            elif len(arr) == 2:
                print("Enter the command again specifying the car color")
                return
            elif len(arr) == 3:
                colour = arr[2].upper()
                car = Car(arr[1],colour)  
                PL.parkCar(car)
        else:
            print("Parking Lot has not yet been created. Cannot issue parking ticket")
        
    elif arr[0] == "status": 
        if PL:
            PL.printStatus()
        else:
            print("ParkingLot has not yet been created. Cannot print Status")    
    
    elif arr[0] == "leave": 
        if PL:
            PL.leaveCar(int(arr[1]))            
        else:
            print("ParkingLot has not yet been created.") 
    

    elif arr[0] == "slot_numbers_for_cars_with_colour": 
        if PL:
            PL.printSlotNumbersForColour(arr[1].upper())            
        else:
            print("ParkingLot has not yet been created.")


    elif arr[0] == "registration_numbers_for_cars_with_colour":
        if PL:
            PL.printRegNumbersForColour(arr[1].upper())            
        else:
            print("ParkingLot has not yet been created.")


    elif arr[0] == "slot_number_for_registration_number":
        if PL:
            PL.printSlotNumberForRegNo(arr[1])            
        else:
            print("ParkingLot has not yet been created.")
    else:
        print("Not a valid command") 
       
# For interactive command prompt based shell where commands can be typed in
def readInputPrompt():    
    print("Reading from command prompt")
    listValidCommands()
    print("Start entering inputs")    
    while(True):
        ip_command = input()
        if ip_command == "exit":
            break           
        else:           
            executeCommands (ip_command)  


# For accepting a filename as a parameter at the command prompt and read the commands from that file
def readInputFile():
    
    print("Reading from file")
    print("Enter the name of the input file")
    filename = input()
    file1 = open(filename,"r")    
    for line in file1:
        executeCommands(line)


def main():
    print ("Enter 1 if you want to enter inputs using command prompt")
    print ("Enter 2 if you want to enter inputs using a file")
    #global variable PL to denote ParkingLot object to enusre that all input commands are run for the same  ParkingLot object
    global PL
    PL = None
    #global variable parkingLotCreated to ensure that duplicate ParkingLot objects are not created.
    global parkingLotCreated
    parkingLotCreated = False

    typeOfInput = int(input())
    if (typeOfInput) == 1:
        readInputPrompt()
    if (typeOfInput) == 2:
        readInputFile()


if __name__ == "__main__":
    main()
