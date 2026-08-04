# Group Coding Challenge
# Create a function called boarding_pass() tha takes in: 
# passenger name
# airline 
# flight number
# seat number
# carry-on bag?
# return the boarding pass
# Challenge: Add another function that allows a traveler to calculate their layover time at the airport between connecting flights

def boarding_pass(passenger_name, airline, flight_number, seat_number, carry_on):
    boarding_pass_text = f"""
    ----BOARDING PASS----
    Passenger: {passenger_name}
    Airline: {airline}
    Flight: {flight_number}
    Seat: {seat_number}
    carry-on bag: {carry_on}
    -----------------------------
    """
    
    return boarding_pass_text

my_pass = boarding_pass(
    "Joey C",
    "Delta",
    "DL205",
    "14A", 
    "Yes",
)

print(my_pass)


# Another way to do it with user input would be this way

def boarding_pass(passenger_name, airline, flight_number, seat_number, carry_on):
    boarding_pass_text = f"""
----- BOARDING PASS -----
Passenger: {passenger_name}
Airline: {airline}
Flight: {flight_number}
Seat: {seat_number}
Carry-on bag: {carry_on}
-------------------------
"""

    return boarding_pass_text


passenger_name = input("What is the passenger's name? ")
airline = input("What is the airline? ")
flight_number = input("What is the flight number? ")
seat_number = input("What is the seat number? ")
carry_on = input("Does the passenger have a carry-on bag? Yes or no: ")

my_pass = boarding_pass(
    passenger_name,
    airline,
    flight_number,
    seat_number,
    carry_on
)

print(my_pass)
