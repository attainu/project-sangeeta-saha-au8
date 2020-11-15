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
        print ("Slot No. Registration No Colour") 
        if self.isParkingEmpty:
            print("Parking Lot is vacant. No car details to display")
        else:
             for i in range(len(self.spaces)):
                if self.spaces[i] is not None:
                    print(i+1, self.spaces[i].reg_no, self.spaces[i].colour)

    def leaveCar(self,slot):        
        if slot > len(self.spaces):
            print("Please enter a valid Slot number")
        elif self.spaces[slot - 1] is not None:
            self.spaces[slot - 1] = None
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
                        print(i)
                        return
            print("Not found")
        

class Car:
    def __init__(self, reg_no, colour):
        self.reg_no = reg_no
        self.colour = colour       

def readInputPrompt():
    print("Reading from command prompt")
    print("Start entering inputs")
    PL = None
    while(True):
        ip_command = input()
        if ip_command == "exit":
            break           
        else:           
            arr = ip_command.split()   
            if arr[0] == "create_parking_lot":  
                PL = createParkingLot(arr[1])
                print("Created a parking lot with ", arr[1], "slots")
                              
            elif arr[0] == "park":                
                if PL:
                    colour = arr[2].upper()
                    car = Car(arr[1],colour)  
                    print(car.reg_no,car.colour)                  
                    PL.parkCar(car)
                                        
                else:
                    print("ParkingLot has not yet been created. Cannot issue parking ticket")
            
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



def readInputFile():
    print("Reading from file")
    print("Enter the name of the input file")

def createParkingLot(n):
    ParkingLot1 = ParkingLot(int(n))
    return ParkingLot1



print ("Enter 1 if you want to enter inputs using command prompt")
print ("Enter 2 if you want to enter inputs using a file")
typeOfInput = int(input())
if (typeOfInput) == 1:
    readInputPrompt()
if (typeOfInput) == 2:
    readInputFile()
