import RoomBooker as rb 
import sys

parameters = {
    'date': sys.argv[1],
    'start': sys.argv[2],
    'end': sys.argv[3],
    'room_number': sys.argv[4],
    'partner': 'PartnerUsername'
}

booker = rb.RoomBooker(parameters, 'Username', 'password')
booker.login_and_book()
