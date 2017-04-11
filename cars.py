
"""| 1 | 2 | 3 | 4 | 5 | 6 |[7]| 8 | 9 |"""
"""|   |   |   |   |   |   |   |   |   |"""
import random
class Vehicle:
    def __init__(self, make, model, year, color):
        self.model = model
        self.make = make
        self.year = year
        self.color = color

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.make,
                                       self.model,
                                       self.year,
                                       self.color)

    def __repr__(self):
        return '{} {}'.format(self.color, self.model)


class ParkingLot:
    def __init__(self, spaces):
        self.spaces = spaces
        self.spaces_left = spaces
        self.parked_vehicles = []

        self.spaces_dic = self.create_space_dic()


        self.string_rep = self.create_string_rep()

    def create_string_rep(self):
        self.string_p = "|"
        for v in range(self.spaces):
            self.string_p += " " + str(v + 1) + " |"
        self.print_lot()
        # print(self.string_p)

    def create_space_dic(self):
        self.space_key = []
        self.spot = {}
        for v in range(self.spaces):
            self.space_key.append( "p" + str(v + 1) )
            self.spot[self.space_key[v]] = None
        return self.spot

    def change_string(self, ins):
        insert = ins-1
        newstring = self.string_p[:insert * 4]
        newstring += '|[{}]'.format(insert+1)
        newstring += self.string_p[4 + insert * 4:]
        self.string_p = newstring
        print(self.string_p)

    def remove_string(self, ins):
        insert = ins-1
        newstring = self.string_p[:insert * 4]
        newstring += '| {} '.format(insert+1)
        newstring += self.string_p[4 + insert * 4:]
        self.string_p = newstring
        print(self.string_p)

    def print_lot(self):
        print(self.string_p, ' #')




            # if 1 is not None:
    #     pass


    def create_vehicle(self):
        # vehicle_make = input('Please enter the make of this vehicle.: ')
        # vehicle_model = input('Please enter the model of this vehicle.: ')
        # vehicle_color = input('Please enter the color of this vehicle.: ')
        # vehicle_year = input('Please enter the year of this vehicle.: ')

        car1 = Vehicle('Dodge', 'Charger', 2017, 'Black')
        car2 = Vehicle('Ford', 'Mustang', 2001, 'Black')
        car3 = Vehicle('BMW', 'm3', 2008, 'Orange')
        car4 = Vehicle('Honda', 'Passport', 1998, 'Black')
        cars = [car1, car2, car3, car4]
        # vehicle = Vehicle(vehicle_make, vehicle_model, vehicle_year, vehicle_color)
        # return vehicle
        return cars[random.randint(1, 9)%4]

    def park(self):
        if self.spaces_left > 0:
            car = self.create_vehicle()
            # self.list_spaces()
            q = input('Which space number would you like to park this {} {} in?: '.format(car.color, car.model))
            # self.parked_vehicles['space_' + q] = car
            # self.spaces_left -= 1

            self.my_park(car, int(q))


            # print('{} {} is parked in {}'.format(car.color, car.model, 'space_' + q.capitalize()))
        else:
            print('There are no spaces left.')


    def my_park(self, obj, to_spot = -1):
        if self.spaces_left > 0:
            self.spaces_left -= 1
            # self.parked_vehicles.append(obj)

            if self.spaces_dic["p" + str(to_spot)] == None:
                self.spaces_dic["p" + str(to_spot)] = obj
            # elif to_spot == 'any':
            else:
                for x, v in self.spaces_dic.items():
                    if v == None:
                        self.spaces_dic[x] = obj
                        self.change_string(x)

            print('There are {} spaces left'.format(self.spaces_left))
            self.change_string(to_spot)
        else:
            print('There are no spaces left.')
            self.change_string(to_spot)
    #
    # def remove(self):
    #     car_list = enumerate(self.parked_vehicles)
    #     for i, v in car_list:
    #         print('{} is in spot {}'.format(v, i))
    #
    #     q = input('Which car would you like to remove or (c)ancel? ')
    #     if q.lower() == 'cancel' or q.lower() == 'c':
    #         quit()
    #     else:
    #         try:
    #
    #             veh = self.parked_vehicles.pop(int(q))
    #             self.spaces_left += 1
    #
    #             print('{} has left the parking lot.'.format(veh.model))
    #             print('There are {} spaces left'.format(self.spaces_left))
    #
    #             print(self.string_p)
    #             removing = False
    #         except ValueError:
    #             print('That is not a valid entry.')
    #         except IndexError:
    #             print('There is no vehicle in that spot.')


    def retrieve(self):
        self.print_lot()
        q = input('Which space number would you like to retrieve?: ')
        if int(q) in range(1, self.spaces + 1) and self.spot[self.space_key[int(q)]] is not None:
            self.spot[self.space_key[int(q)]] = None
            self.remove_string(int(q))
            self.spaces_left += 1
        else:
            print('There is no vehicle in that spot.')

    def main_interface(self):
        while True:
            q = input('Would you like to (P)ark, (R)etrieve, (L)ist Spaces or (Q)uit?: ')
            if q.lower() == 'p':
                self.park()
            elif q.lower() == 'r':
                self.retrieve()
            elif q.lower() == 'l':
                self.print_lot()
            elif q.lower() == 'q':
                print('Goodbye.')
                quit()
            else:
                print('I did not understand that. Please try again.')


plot = ParkingLot(9)

# plot = ParkingLot(5)
plot.main_interface()

car1 = Vehicle('Dodge', 'Charger', 2017, 'Black')
car2 = Vehicle('Ford', 'Mustang', 2001, 'Black')
car3 = Vehicle('BMW', 'm3', 2008, 'Orange')
car4 = Vehicle('Honda', 'Passport', 1998, 'Black')
#
# plot.park(car1, 1)
# plot.park(car2, 2)
# plot.park(car3, 8)
# plot.park(car4, 4)
# print(plot.parked_vehicles)
# plot.remove()



