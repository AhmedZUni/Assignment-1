from enum import Enum


class Person:
    def __init__(self, first_name, last_name, date_of_birth, gender, emirates_id):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.emirates_id = emirates_id


class Passenger(Person):
    def __init__(self, first_name, last_name, date_of_birth, gender, emirates_id):
        super().__init__(first_name, last_name, date_of_birth, gender, emirates_id)


class Flight:
    def __init__(self, flight_number, airline, departure_airport, arrival_airport, departure_datetime,
                 arrival_datetime):
        self.flight_number = flight_number
        self.airline = airline
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_datetime = departure_datetime
        self.arrival_datetime = arrival_datetime


class BoardingPassGenerationSystem:
    def fetch_passenger_details(self, passenger):
        # Fetch passenger details from the system
        pass

    def fetch_flight_details(self, flight):
        # Fetch flight details from the system
        pass

    def fetch_gate_details(self, flight):
        # Fetch gate details for the flight
        pass

    def allocate_seat_number(self, flight, passenger):
        # Allocate a seat number for the passenger in the specified flight
        pass

    def generate_boarding_pass(self, passenger, flight, gate_details, seat_number):
        # Generate boarding pass for the passenger
        pass


class Seat:
    def __init__(self, seat_number, class_type):
        self.seat_number = seat_number
        self.class_type = class_type


class Employee(Person):
    def __init__(self, first_name, last_name, date_of_birth, gender, emirates_id, empID, empType, empDateOfJoining,
                 empSalary):
        super().__init__(first_name, last_name, date_of_birth, gender, emirates_id)
        self.empID = empID
        self.empType = empType
        self.empDateOfJoining = empDateOfJoining
        self.empSalary = empSalary

    def display_details(self):
        # Display all details of the employee
        pass


# Creating objects and populating data
passenger = Passenger("Ahmed", "Salem", "5/11/2000", "Male", "751884185")
flight = Flight("NA4321", "National Airlines", "Chicago ORD", "New York JFK", "11/2/2010 11:40", "12/6/2020 13:30")
system = BoardingPassGenerationSystem()

# Displaying passenger details
print("Passenger Details:")
print("First Name:", passenger.first_name)
print("Last Name:", passenger.last_name)
print("Date of Birth:", passenger.date_of_birth)
print("Gender:", passenger.gender)
print("Emirates ID:", passenger.emirates_id)

# Fetching and displaying flight details
print("\nFlight Details:")
system.fetch_flight_details(flight)
print("Flight Number:", flight.flight_number)
print("Airline:", flight.airline)
print("Departure Airport:", flight.departure_airport)
print("Arrival Airport:", flight.arrival_airport)
print("Departure Datetime:", flight.departure_datetime)
print("Arrival Datetime:", flight.arrival_datetime)

# Other actions such as fetching gate details, allocating seat number, and generating boarding pass can be similarly implemented and executed.
