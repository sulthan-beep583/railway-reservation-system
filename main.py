 

total_seats = 50
bookings = {}
seat_number = 1


# Function to check available seats
def check_availability():
    available = total_seats - len(bookings)
    print("\nAvailable Seats:", available)


# Function to book a ticket
def book_ticket():
    global seat_number

    if len(bookings) >= total_seats:
        print("\nSorry! No seats available.")
        return

    name = input("Enter Passenger Name: ")
    age = input("Enter Passenger Age: ")

    booking_id = "B" + str(seat_number)

    bookings[booking_id] = {
        "name": name,
        "age": age,
        "seat": seat_number
    }

    print("\nTicket Booked Successfully!")
    print("Booking ID:", booking_id)
    print("Seat Number:", seat_number)

    seat_number += 1


# Function to view reservation details
def view_ticket():
    booking_id = input("\nEnter Booking ID: ")

    if booking_id in bookings:
        print("\n--- Reservation Details ---")
        print("Passenger Name:", bookings[booking_id]["name"])
        print("Passenger Age:", bookings[booking_id]["age"])
        print("Seat Number:", bookings[booking_id]["seat"])
    else:
        print("\nBooking ID not found.")


# Function to cancel ticket
def cancel_ticket():
    booking_id = input("\nEnter Booking ID to Cancel: ")

    if booking_id in bookings:
        del bookings[booking_id]
        print("\nTicket Cancelled Successfully!")
    else:
        print("\nBooking ID not found.")


# Main Menu
while True:

    print("\n===== Railway Reservation System =====")
    print("1. Check Seat Availability")
    print("2. Book Ticket")
    print("3. View Reservation")
    print("4. Cancel Ticket")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        check_availability()

    elif choice == '2':
        book_ticket()

    elif choice == '3':
        view_ticket()

    elif choice == '4':
        cancel_ticket()

    elif choice == '5':
        print("\nThank You for Using Railway Reservation System!")
        break

    else:
        print("\nInvalid Choice! Please try again.")
