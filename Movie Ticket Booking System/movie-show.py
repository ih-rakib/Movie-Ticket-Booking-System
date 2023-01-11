class Star_Cinema:
    _hall_list = []

    def entry_hall(self,hall) :
        self._hall_list.append(hall)

class Hall(Star_Cinema) :
    _seats = {}
    _show_list = []

    _rows = 3
    _cols = 5
    _hall_no = 1
    _twoD = []

    for row in range(_rows) :
        for col in range(_cols) :
            _twoD.append((f'{chr(row+65)}{col}',False))

    def __init__(self):
        self._rows = Hall._rows
        self._cols = Hall._cols
        self._hall_no = Hall._hall_no
        super().entry_hall(f'Rows: {self._rows}, Cols: {self._cols}, Hall No: {self._hall_no}')
        Hall._hall_no += 1

    def entry_show(self, id, movie_name, time):
        self._id = id
        self._movie_name = movie_name
        self._time = time
        self._show_list.append((self._id,self._movie_name,self._time))
        self._seat=([[f"empty" for i in range(self._cols)] for j in range(self._rows)])
        self._seats[id]=self._seat

    def book_seats(self,name, phone_number,id):
        _booked_seatList = []
        _ticket_quantity=int(input("ENTER THE NUMBER OF TICKETS: "))
        for i in range(_ticket_quantity):
            seat = input('ENTER THE SEAT NO : ')
            _row = seat[0]
            _col = int(seat[1::]) 
            # print(f'seat row : {_row} col : {_col}')
            if ((ord(_row) < ord('A') or ord(_row) > ord('D')) or (_col < 0 or _col > 4)) : 
                print(f"\n{100 * '_'} \n")
                print('\n   INVALID SEAT NUMBER! PLEASE TRY AGAIN\n')
                print(f"\n{100 * '_'} \n")
                return

            for keys, value in self._seats.items() :
                if (keys==id):
                    if (self._seats[keys][ord(_row)-65][_col])=="empty" :
                        self._seats[keys][ord(_row)-65][_col]="BOOKED"
                        _booked_seatList.append(f'{_row}{_col}')
                    else:
                        print(f"\n{100 * '_'} \n")
                        print(f'    SEATS ALREADY BOOKED : {_row}{_col}, ')
                        print(f"\n{100 * '_'} \n")
                        return
                    
        print('\n''####### TICKET BOOKED SUCCESSFULLY!! #######')
        print(f"\n{100 * '_'}\n")
        print(f'NAME: {name}')
        print(f'PHONE NUMBER: {phone_number}\n')
        for show in self._show_list:
            if(show[0]==id):
                print(f'MOVIE NAME: {show[1]}\t MOVIE TIME: {show[2]}')
        print(f'TICKETS: ',*_booked_seatList)
        print(f'HALL: {self._hall_no}')
        print(f"\n{100 * '_'}\n")

    def view_show_list(self,_show_list):
        for show in _show_list:    
            print(f' MOVIE NAME: {show[1]}\t\t SHOW ID: {show[0]}\t\t TIME: {show[2]}\t\t')

    def view_available_seats(self,id):
        i = 0
        flag = 0
        for show in self._show_list:
            if(id==show[0]):
                flag += 1
                print('\n')
                print(f'MOVIE NAME: {show[1]}\t\t TIME : {show[2]}')
                print('BOOKED FOR ALREADY BOOKED SEATS')
                print(f"\n{100 * '_'} \n")
                for keys in self._seats.keys():
                    if(keys==id):
                        for j in range(self._rows):
                            for k in range(self._cols):
                                if(i==self._cols):
                                    i=0
                                    print('\n')
                                print(f' {chr(j+65)}{k}: {self._seats[keys][j][k]}',end='\t')
                                i += 1
                print(f"\n{100 * '_'} \n")
        if(flag == 0):
                print(f"\n{100 * '_'} \n")
                print(f" INVALID SHOW ID! PLEASE TRY AGAIN")
                print(f"\n{100 * '_'} \n")
                return
        
            
if __name__ == '__main__':
    shows = Hall()
    shows.entry_show('ae123','Black Adam','Oct 26 2022 10:00 PM')
    shows.entry_show('ae50','Superman','Oct 26 2022 8:00 PM')
    # print(Hall.seats)
    while(True):
        print('1. VIEW ALL SHOWS TODAY')
        print('2. VIEW AVAILABLE SEATS')
        print('3. BOOK TICKET')
        option = int(input('ENTER OPTION: '))
        if(option == 1):
            print(f"\n{100 * '_'} \n")
            shows.view_show_list(shows._show_list)
            print(f"\n{100 * '_'} \n")
        elif(option == 2):
            show_id=input('ENTER SHOW ID: ') 
            shows.view_available_seats(show_id)
        elif(option == 3):
            name=input('ENTER CUSTOMER NAME: ')
            number=input('ENTER CUSTOMER PHONE NUMBER: ')
            show_id=input('ENTER SHOW ID: ')

            i = 0
            flag = 0
            for i in range(2) : 
                # print(shows._show_list[i][0])
                if show_id == shows._show_list[i][0] : 
                    flag = 1
                else :
                    i += 1
            if flag : 
                shows.book_seats(name,number,show_id)
            else : 
                print(f"\n{100 * '_'} \n")
                print(f" INVALID SHOW ID! PLEASE TRY AGAIN")
                print(f"\n{100 * '_'} \n")