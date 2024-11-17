# This file will store and track changes to the code for AutoMate

#AutoMate, a vehicle booking system developed by Michael Cato. Inspiration drawn from cloned code repository. 
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
        service_items = input("Please enter requested service, or enter 'done' to complete: ")
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
    print(f"Great! New appointment booked for {vehicle_year} {vehicle_make} {vehicle_model} ! The services included are: {', '.join(service_items)}")
#Commit 4 below
def add_new(appointments):
    vehicle_year = input("Enter the car's year: ")
    vehicle_make = input("Enter the car's make: ")
    vehicle_model = input("Enter the car's model: ")
# Commit 5 below 
    for appointment in appointments:
        if (appointment['year'] == car_year and
            appointment['make'] == car_make and
            appointment['model'] == car_model):
            service = input("Enter the service to add: ")
            if service not in appointment['services']:
                appointment['services'].append(service)
                print(f"Service '{service}' added to appointment for {car_year} {car_make} {car_model}")
            else:
                print(f"Service '{service}' already exists for this appointment.")
            return
    
    print("Appointment not found!")
    
