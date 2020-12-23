def hello():
    print("HELLO WORLD!")

hello()


def hello(name):
    print("HELLO", name )

hello("Andrés Pabón")


def hello(name="person"):
    print("HELLO", name )

hello()


def add(number1, number2):
    return number1 + number2

print(add(10, 20))   


substract = lambda num1, num2: num1 - num2

print(substract(3, 3))