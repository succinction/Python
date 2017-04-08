"| 1 | 2 | 3 | 4 | 5 | 6 |[7]| 8 | 9 |"


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
        self.string_rep = create_string_rep()

    def create_string_rep(self):
        self.string_p = "|"
        for v in range(len(self.spaces)):
            self.string_p += " " + (v + 1) + " |"

    def create_space_dic(self):
        self.space_key = []
        self.spot = {}
        for v in range(len(self.spaces)):
            self.space_key[v] = "p" + (v + 1)
            self.spot[space_key[v]] = None
        return self.spot

    def park(self, obj, to_spot='any'):
        if self.spaces_left > 0:
            self.spaces_left -= 1
            # self.parked_vehicles.append(obj)
            if to_spot == 'any':
                for x, v in self.spaces_dic.items():
                    if v == None:
                        self.spaces_dic[x] = obj

                elif self.spaces_dic["p" + to_spot] == None:
                self.spaces_dic["p" + to_spot] = obj
            else:

        print('There are {} spaces left'.format(self.spaces_left))

    else:
    print('There are no spaces left.')


def remove(self):
    car_list = enumerate(self.parked_vehicles)
    for i, v in car_list:
        print('{} is in spot {}'.format(v, i))
    removing = True
    while removing:
        q = input('Which car would you like to remove or (c)ancel? ')
        if q.lower() == 'cancel' or q.lower() == 'c':
            break
        else:
            try:
                veh = self.parked_vehicles.pop(int(q))
                self.spaces_left += 1
                print('{} has left the parking lot.'.format(veh.model))
                print('There are {} spaces left'.format(self.spaces_left))
                removing = False
            except ValueError:
                print('That is not a valid entry.')
            except IndexError:
                print('There is no vehicle in that spot.')


plot = ParkingLot(5)

car1 = Vehicle('Dodge', 'Charger', 2017, 'Black')
car2 = Vehicle('Ford', 'Mustang', 2001, 'Black')
car3 = Vehicle('BMW', 'm3', 2008, 'Orange')
plot.park(car1)
plot.park(car2)
plot.park(car3)
# print(plot.parked_vehicles)
plot.remove()
