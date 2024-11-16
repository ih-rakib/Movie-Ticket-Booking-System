# 🎬 Movie Ticket Booking System
<sub><b>Author: Ikramul Hasan Rakib</b></sub>

A simple Python-based Cinema Ticket Booking System that allows users to view shows, check available seats, and book tickets. It also allows movie show entries and management of seat availability in multiple halls.

---

## Features

### 🛠️ Show Management
- Manage multiple halls with different rows and columns for seats.
- Add new movie shows with show ID, movie name, and show time.
  
### 📅 View Shows
- View all the movie shows for the day with their show ID, movie name, and show time.

### 🎟️ Book Tickets
- Users can book tickets for available seats.
- Prevents double booking for the same seat.
- Displays the ticket details like name, phone number, movie name, time, and booked seats.

### 🪑 View Available Seats
- Displays the seating chart for a movie show with booked and available seats.

---

## How It Works

1. **Create Movie Shows**: Create new movie shows with a unique ID, movie name, and show time for a particular hall.
2. **View Available Shows**: Users can view all the available shows for the day.
3. **Seat Booking**: Users can book seats by providing the seat number, and the system will prevent double booking.
4. **View Available Seats**: The seating chart displays which seats are available and which are booked for each show.
5. **Dynamic Show and Seat Management**: The system allows users to manage different halls, rows, columns, and available seats dynamically.

---

## Code Structure

### Classes

- **Star_Cinema**: Manages the overall cinema system and halls.
- **Hall**: Manages movie shows and seat bookings for a particular hall.

---

## Example

```python
# Create an instance of Hall and add shows
shows = Hall()
shows.entry_show('ae123', 'Black Adam', 'Oct 26 2022 10:00 PM')
shows.entry_show('ae50', 'Superman', 'Oct 26 2022 8:00 PM')

# Interact with the system (view shows, book tickets, view available seats)
while(True):
    print('1. VIEW ALL SHOWS TODAY')
    print('2. VIEW AVAILABLE SEATS')
    print('3. BOOK TICKET')
    option = int(input('ENTER OPTION: '))
    if(option == 1):
        shows.view_show_list(shows._show_list)
    elif(option == 2):
        show_id = input('ENTER SHOW ID: ')
        shows.view_available_seats(show_id)
    elif(option == 3):
        name = input('ENTER CUSTOMER NAME: ')
        number = input('ENTER CUSTOMER PHONE NUMBER: ')
        show_id = input('ENTER SHOW ID: ')
        shows.book_seats(name, number, show_id)
