from ParkingLot import ParkingLot


class Car:
    def __init__(self, reg_no, colour):
        self.reg_no = reg_no
        self.colour = colour
        self.__start_time = 0
        self.__end_time = 0

    def get_start_time(self):
        return self.__start_time

    def set_start_time(self, a):
        self.__start_time = a

    def get_end_time(self):
        return self.__start_time

    def set_end_time(self, a):
        self.__start_time = a


def createParkingLot(n=5):
    ParkingLot1 = ParkingLot(int(n))
    return ParkingLot1


def listValidCommands():
    print("List of valid commands")
    print(" 1> create_parking_lot no")
    print(" 2> park registration_no color ")
    print(" 3> status")
    print(" 4> leave slot_no")
    print(" 5> registration_numbers_for_cars_with_colour colour")
    print(" 6> slot_numbers_for_cars_with_colour colour")
    print(" 7> slot_number_for_registration_number registration_no")
    print(" 8> print_empty_slots")


def executeCommands(command):
    global PL
    global parkingLotCreated
    if len(command) == 0:
        print("Please enter a valid command")
    else:
        arr = command.split()
        if arr[0] == "create_parking_lot":
            if len(arr) < 2:
                if not parkingLotCreated:
                    PL = createParkingLot()
                    parkingLotCreated = True
                    print("Creating parking lot with default 5 slots ")
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
                if len(arr) <= 2:
                    print("One or more arguments missing.")
                    return
                elif len(arr) == 3:
                    colour = arr[2].upper()
                    car = Car(arr[1], colour)

                    PL.parkCar(car)
            else:
                print("Parking Lot has not yet been created.")

        elif arr[0] == "status":
            if PL:
                PL.printStatus()
            else:
                print("ParkingLot not yet created. Cannot print Status")

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
        elif arr[0] == "print_empty_slots":
            if PL:
                PL.printEmptySlots()
            else:
                print("ParkingLot has not yet been created.")

        else:
            print("Not a valid command")


# For interactive command prompt based inputs
def readInputPrompt():
    print("Reading from command prompt")
    listValidCommands()
    print("Start entering inputs")
    while(True):
        ip_command = input()
        if ip_command == "exit":
            break
        else:
            executeCommands(ip_command)


# For accepting a filename  parameter at the command prompt
def readInputFile():

    print("Reading from file")
    print("Enter the name of the input file")
    filename = input()
    try:
        file1 = open(filename, "r")
    except IOError:
        print("Cannot find File name entered")
        return
    if file1:
        for line in file1:
            lineToSend = line.rstrip()
            executeCommands(lineToSend)
    else:
        print("Please enter a valid file")


def main():
    print("Enter 1 if you want to enter inputs using command prompt")
    print("Enter 2 if you want to enter inputs using a file")
    # The ParkingLot object
    global PL
    PL = None
    # To ensure no duplicate ParkingLot objects
    global parkingLotCreated
    parkingLotCreated = False
    typeOfInput = 0

    try:
        typeOfInput = int(input())
    except ValueError:
        print("Input is not a number")
        return
    if typeOfInput == 1 or typeOfInput == 2:
        if (typeOfInput) == 1:
            readInputPrompt()
        if (typeOfInput) == 2:
            readInputFile()
    else:
        print("Input must be 1 or 2 only")


if __name__ == "__main__":
    main()
