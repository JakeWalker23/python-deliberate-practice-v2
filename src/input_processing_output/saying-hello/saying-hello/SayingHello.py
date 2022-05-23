name = ''


def say_hello(name):
    name = input('Please enter your name ')

    if not isinstance(name, str):
        print('Sorry, please enter a string as an input. Try again.')
        return

    return print(f"Hello, {name}, nice to meet you!")


while True:
    say_hello(name)
