class Pizza:
    def __init__(self):
        self.__slices = 0
        self.__pizzas = 0
        self.__people = 0
        self.__slices_per_person = 0

    def run(self):
        self.__retrieve_input()
        self.__slices_per_person = self.__calculate_slices_per_person(
            self.people, self.pizzas, self.slices)

        self.__print_response_to_std_out(self.__slices_per_person)

    def __retrieve_input(self):
        print("Welcome to Pizza calculator. Please enter the number of people, amount of pizzas and number of slices per pizza. ")

        self.__people = int(input('How many people are there?'))
        self.__pizzas = int(input('How many pizzas are there?'))
        self.__slices = int(input('How many slices per pizza are there?'))

    def __calculate_slices_per_person(self, people, pizzas, slices):
        return (slices / people) * pizzas

    def __print_response_to_std_out(self, slices_per_person):
        print(
            f"Each person will recieve {slices_per_person} slices of pizza per person.")

    @property
    def slices(self):
        return self.__slices

    @property
    def people(self):
        return self.__people

    @property
    def pizzas(self):
        return self.__pizzas

    @property
    def slices_per_person(self):
        return self.__slices_per_person
