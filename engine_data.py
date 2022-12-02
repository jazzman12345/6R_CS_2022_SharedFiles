class Engine:
    def __init__(self, name, weight, colour):
        self.name = name
        self.weight = weight
        self.colour = colour

    def display_engine(self):
        print(f"Engine name: {self.name}, weight: {self.weight}, colour: {self.colour}")


engines_list = []
engines_list.append(Engine('Thomas', 600, 'blue'))
engines_list.append(Engine('James', 650, 'red'))
engines_list.append(Engine('Edward', 1000, 'blue'))
engines_list.append(Engine('Gordon', 2500, 'blue'))
engines_list.append(Engine('Henry', 2100, 'green'))

print(engines_list)
for e in engines_list:
    e.display_engine()


