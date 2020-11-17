from time import time


class ParkingLot:
    def __init__(self, n):
        self.spaces = [None] * n
        self.isParkingEmpty = True
        self.isParkingFull = False
        self.rateSlabs = [60, 100, 250, 500]

    def parkCar(self, car):
        # if ParkingLot is full do not check for empty slots
        if self.isParkingFull:
            print("Sorry, Parking lot is full")
        else:
            for i in range(len(self.spaces)):
                if self.spaces[i] is None:
                    self.spaces[i] = car
                    car.set_start_time(time())
                    print('Allocated slot no: ', i + 1)
                    self.isParkingEmpty = False
                    return
            # Setting isParkingFull for the first time.
            self.isParkingFull = True
            print("Sorry, Parking lot is full")

    def printStatus(self):
        h1 = "{0:<10}".format("Slot No.")
        h2 = "{0:<25}".format("Registration No.")
        h3 = "{0:<15}".format("Colour")
        header1 = h1+h2+h3
        print(header1)
        header2 = "-" * 50
        print(header2)
        if self.isParkingEmpty:
            print("Parking Lot is vacant. No car details to display")
        else:
            for i in range(len(self.spaces)):
                if self.spaces[i] is not None:
                    d1 = "{0:<10}".format(i+1)
                    d2 = "{0:<25}".format(self.spaces[i].reg_no)
                    d3 = "{0:<15}".format(self.spaces[i].colour)
                    detail = d1+d2+d3
                    print(detail)

    def leaveCar(self, slot):

        if slot <= 0 or slot > len(self.spaces):
            print("Please enter a valid Slot number")
        elif self.spaces[slot-1] is not None:
            self.spaces[slot-1].set_end_time(time())
            car = self.spaces[slot-1]
            time_elapsed = car .get_end_time()-car.get_start_time()
            hrs = convert(time_elapsed)
            car_reg_no = self.spaces[slot-1].reg_no
            parking = " Parking charges are: ₹"
            if hrs <= 2:
                print(car_reg_no, parking, self.rateSlabs[0])
            elif hrs > 2 and hrs <= 5:
                print(car_reg_no, parking, self.rateSlabs[1])
            elif hrs > 5 and hrs <= 12:
                print(car_reg_no, parking, self.rateSlabs[2])
            elif hrs > 12:
                print(car_reg_no, parking, self.rateSlabs[3])
            self.spaces[slot-1] = None
            print("Slot number ", slot, " is free")
            if self.isParkingFull:
                self.isParkingFull = False
        else:
            print("Slot no. entered is empty")

    def printSlotNumbersForColour(self, colour):
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

    def printRegNumbersForColour(self, colour):
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

    def printSlotNumberForRegNo(self, reg_no):
        if self.isParkingEmpty:
            print("Parking Lot is empty.")
        else:
            for i in range(len(self.spaces)):
                if self.spaces[i] is not None:
                    if self.spaces[i].reg_no == reg_no:
                        print(i + 1)
                        return
            print("Not found")

    def printEmptySlots(self):
        op = ""
        for i in range(len(self.spaces)):
            if self.spaces[i] is None:
                if len(op) == 0:
                    op = op + str(i + 1)
                else:
                    op = op + " ," + str(i + 1)
        if len(op) == 0:
            print("No empty slots")
        else:
            print("Empty slots in the parking lot are ", op)


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    if minutes > 0:
        hour += 1

    return hour
