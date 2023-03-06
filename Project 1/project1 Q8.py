def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError('Cannot divide by zero!')
    return x / y


while True:
    print('Enter operation:')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Quit')

    choice = input('Enter choice (1/2/3/4/5): ')

    if choice == '5':
        break

    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))

    if choice == '1':
        print(num1, '+', num2, '=', add(num1, num2))

    elif choice == '2':
        print(num1, '-', num2, '=', subtract(num1, num2))

    elif choice == '3':
        print(num1, '*', num2, '=', multiply(num1, num2))

    elif choice == '4':
        try:
            print(num1, '/', num2, '=', divide(num1, num2))
        except ValueError as e:
            print(e)