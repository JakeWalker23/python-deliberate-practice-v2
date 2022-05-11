class TroubleshootCarIssues:

    def run(self):
        print("Welcome to the car troubleshooting program.")
        print("Please enter y for yes or n for no")

        choice = self.check_car_is_silent_when_turn_key()

        if choice == 'yes':
            return self.__check_if_battery_terminals_corroded()
        elif choice == 'no':
            answer = self.check_if_car_makes_clicking_noise()

            if answer == 'no':
                answer2 = self.check_if_car_cranks_but_fails()

                if answer2 == 'no':
                    answer3 = self.check_if_engine_starts_then_dies()

                    if answer3 == 'y':
                        return self.__check_if_car_has_fuel_injection()
                    else:
                        return False

                else:
                    return answer2

            else:
                return answer
        else:
            return False

    def check_car_is_silent_when_turn_key(self):
        choice = input("Is the car silent when you turn the key?")

        if choice == 'y':
            return 'yes'
        else:
            return 'no'

    def __check_if_battery_terminals_corroded(self):
        choice = input("Are the battery terminals corroded?")

        if choice == 'y':
            print("Clean terminals and try starting again.")

            return "Clean terminals and try starting again."
        elif choice == 'n':
            print("Replace cables and try again.")

            return "Replace cables and try again."

    def check_if_car_makes_clicking_noise(self):
        choice = input("Does the car make a clicking noise?")

        if choice == 'y':
            print("Replace the battery")

            return 'Replace the battery.'
        else:
            return 'no'

    def check_if_car_cranks_but_fails(self):
        choice = input("Does the car crank up but fail?")

        if choice == 'y':
            print("Check spark plug connections")

            return "Check spark plug connections."

        else:
            return 'no'

    def check_if_engine_starts_then_dies(self):
        choice = input("Does the engine start and then die?")

        if choice == 'y':
            return 'yes'
        else:
            return False

    def __check_if_car_has_fuel_injection(self):
        choice = input("Does your car have fuel injection?")

        if choice == 'y':
            return "Get it in for service."
        elif choice == 'n':
            return "Check to ensure the choke is opening and closing."
