# Uni Marburg Group Room Booker 📚📚

Stupid simple tool to book group rooms at the university library. Best usage is to create a weekly cronjob to book your favorite room at the same time.

Dependencies:
    - selenium (`pip install selenium`)

## Example Usage as command line tool:
```
import RoomBooker as rb
import sys

parameters = {
    'date': sys.argv[1]
    'start': sys.argv[2]
    'end': sys.argv[3]
    'room_number': sys.argv[4]
    'partner': sys.argv[5]
}

booker = rb.RoomBooker(parameters, 'Username', 'password')
booker.login_and_book()

```

`python3 -W ignore book_room.py 20190928 1150 1450 45 BestFriend`

## Notes:
1. Booking at half past an hour (for example, 1430 instead of 1400) requires you to enter 1450 as a time instead.
2. Creating a booking that is outside of the time limits is possible, but would probably create suspicion around your account.


