class Wagon:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'<Wagon: {self.name}>'

class OpenWagon(Wagon):
    def __init__(self, name):
        super().__init__(name)

class ClosedWagon(Wagon):
    def __init__(self, name):
        super().__init__(name)

class Siding:
    def __init__(self):
        self._top_of_stack = -1
        self._wagon_array = [None] * 30

    def push_wagon(self, wagon):
        self._top_of_stack += 1
        self._wagon_array[self._top_of_stack] = wagon

    def pop_wagon(self):
        if self._top_of_stack > -1:
            return_wagon = self._wagon_array[self._top_of_stack]
            self._top_of_stack -= 1
            return return_wagon
        else:
            raise Exception("No wagon found in siding")

    def get_siding_details(self):
        display_str = ''
        for i in range(self._top_of_stack, -1, -1):
            display_str += self._wagon_array[i].name + ' '
        display_str += '::'
        return display_str


class Yard:
    def __init__(self, number_of_sidings):
        self.sidings = []
        for _ in range(number_of_sidings):
            self.sidings.append(Siding())

    def add_wagon_to_siding(self, wagon, siding_index):
        print(f'Adding {wagon} to siding number {siding_index}')
        self.sidings[siding_index].push_wagon(wagon)

    def get_wagon_from_siding(self, siding_index):
        return_wagon = self.sidings[siding_index].pop_wagon()
        print(f'Removing wagon from siding number {siding_index}. It was {return_wagon}')
        return return_wagon

    def display_yard(self):
        for i, siding in enumerate(self.sidings):
            print(f'siding {i}: ', end='')
            print(siding.get_siding_details())

def testing():
    # Create a yard with 5 sidings
    yard = Yard(5)

    wagon1 = OpenWagon('Bob')
    wagon2 = ClosedWagon('Fred')
    wagon3 = Wagon('Thomas')

    yard.add_wagon_to_siding(wagon1, 3)
    yard.add_wagon_to_siding(wagon2, 3)
    yard.add_wagon_to_siding(wagon3, 2)

    yard.display_yard()

    yard.add_wagon_to_siding(yard.get_wagon_from_siding(3), 4)
    yard.add_wagon_to_siding(yard.get_wagon_from_siding(3), 4)

    yard.display_yard()

    yard.get_wagon_from_siding(3)



testing()


