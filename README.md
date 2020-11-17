## PARKING LOT

This application implements an automated ticketing system for a parking lot.
On entering the car registration number and the colour, next free parking slot is allocated.

### Installation

You can download the repo or clone to your local machine

- step 1
  git clone https://github.com/attainu/project-sangeeta-saha-au8.git
- step 2
  cd project-sangeeta-saha-au8
- step 3
  Make sure your machine has python 3.8 installed.
  At the command-prompt > python ParkingLotApp.py

### Execution Modes

There are two modes in which inputs can be given to the application

1.  Type 1 for Interactive mode.
    - Here inputs are given at the command prompt one by one. Type exit to come out.
2.  Type 2 for File mode.

    - Enter all the commands in a file. Enter the filename at the command prompt. Output for all the commands will be given in one shot.

### Input Commands

For both the modes following are a list of valid commands

1. create_parking_lot n
   - This creates a parking lot with n slots
2. park registration_no color
   - This allocates a parking slot to a car with mentioned registration number and color
3. leave slot_no
   - This de-allocates the parking slot.
4. status
   - This prints the Parking Slot number, Registration number and the Car Color for all the parked cars
5. registration_numbers_for_cars_with_colour colour
   - This prints Registration numbers for all the cars with the mentioned color
6. slot_numbers_for_cars_with_colour colour
   - This prints Parking Slot numbers for all the cars with the mentioned color
7. slot_number_for_registration_number registration_no
   - This prints the Parking Slot number for the car with the mentioned Registration number.
8. print_empty_slots
   - This prints all the Parking Slots available at the moment

### Technologies used:

- Python 3.8
- Flake8 for linting

### Additional features:

1. Display empty parking slots
2. Parking charges printed for car at the time of leaving the Parking Lot.

### Future Scope and Extensibility:

1. Many other attributes can be added to the car class, to include the type of car, model etc.
2. More functionalities can be added to the Parking lot class as new methods.
