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
appointment = {
        'year': vehicle_year,
        'make': vehicle_make,
        'model': vehicle_model,
        'services': service_items
    }
    appointments.append(appointment)
    print(f"Great! New appointment booked for {vehicle_year} {vehicle_make} {vehicle_model} ! The services included are: {', '.join(service_items)}")
