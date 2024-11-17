# This file will store and track changes to the code for AutoMate

#AutoMate, a vehicle booking system developed by Michael Cato. Inspiration drawn from cloned code repository. 
print("Welcome to AutoMate! Your car's best booking friend!")
def appointment_booking(appointments):
    print("Booking a new appointment?")
    vehicle_year = input("Enter vehicle year: ")
    vehicle_make = input("Enter vehicle make: ")
    vehicle_model = input("Enter vehicle model: ")
    service = []
while True:
        service_items = input("Please enter requested service, or enter 'done' to complete: ")
        if service_items.lower() == 'done':
            break
        service.append(service_items)
