# This file will store and track changes to the code for AutoMate
#AutoMate, a vehicle booking system developed by Michael Cato. Inspiration for idea drawn from cloned code repository. 

# Commit 10 below

def automate_logo():
    logo = """ 
    XXXXX  X   X  XXXXX  XXXXX  X   X XXXXX XXXXX XXXXX 
    X   X  X   X    X    X   X  XXxXX X   X   X   XX
    XXXXX  X   X    X    X   X  XX XX XXXXX   X   XXXXX
    X   X  X   X    X    X   X  X   X X   X   X   XX
    X   X  XXXXX    X    XXXXX  X   X X   X   X   XXXXX
    """
    print(logo)
if __name__ == "__main__":
    automate_logo()
#Commit 1 below
print("Welcome to AutoMate! Your car's best booking friend!")
def appointment_booking(appointments):
    print("Booking a new appointment?")
    vehicle_year = input("Enter vehicle year: ")
    vehicle_make = input("Enter vehicle make: ")
    vehicle_model = input("Enter vehicle model: ")
    service = []
#Commit 2 below
    while True:
        service_items = input("Please enter requested service: ")
        if service_items.lower() == 'done':
            break
        service.append(service_items)
#Commit 3 below
    appointment = {
        'year': vehicle_year,
        'make': vehicle_make,
        'model': vehicle_model,
        'services': service_items
        }
    appointments.append(appointment)
    print(f"Great! New appointment booked for {vehicle_year} {vehicle_make} {vehicle_model} ! The services have been added!/n")
#Commit 4 below
def add_new(appointments):
    vehicle_year = input("Vehicle year?")
    vehicle_make = input("Vehicle make?")
    vehicle_model = input("Vehicle model?")
# Commit 5 below 
    for appointment in appointments:
        if (appointment['year'] == vehicle_year and
            appointment['make'] == vehicle_make and
            appointment['model'] == vehicle_model):
            service = input("Enter the service to add: ")
            if service not in appointment['service']:
                appointment['services'].append(service)
                print(f"{service} applied!")
            else:
                print(f"{service} has already been added!")
            return
    
    print("No appointment to show!")
# Commit 6 below    
def deleted_appointment(appointments):
    vehicle_year = input("Vehicle year?")
    vehicle_make = input("Vehicle make?")
    vehicle_model = input("Vehicle model?")
# Commit 7 below    
    for appointment in appointments:
        if (appointment['year'] == vehicle_year and
            appointment['make'] == vehicle_make and
            appoitnment['model'] == vehicle_model):
            appointments.remove(appointment)
            print("Appointment deleted!")
            return

    print("No appointment to show!")
# Commit 8 below
def main():
    appointments = []
    while True: 
        print("Please see menu options below:")
        print(" -Type 1 to book a new appointment.")
        print(" -Type 2 to add a service to an existing appointment.")
        print(" -Type 3 to delete an existing appointment.")
        print(" -Type 4 to exit")

        option = input("Enter input here:")
# Commit 9
        if option == '1': 
            appointment_booking(appointments)
        elif option == '2':
            service_items(appointments)
        elif option == '3':
            deleted_appointment(appointments)
        elif option == '4':
            print("Speed along! We'll see you next time!")
            break
if __name__ == "__main__":
    main()


    
