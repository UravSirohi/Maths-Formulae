import operator


def main():
    which_function = input('''Which side's value would you like to work out?
>>>''')
    if which_function == 'a':
        find_value_a()
    elif which_function == 'b':
        find_value_b()
    elif which_function == 'h':
        find_value_c()
    else:
        print('''Input options are either a(adjacent), b(opposite) or h(hypotenuse)''')


def find_value_a():
    h = float(input('Value of h: '))
    b = float(input('Value of b: '))
    h_squared = operator.pow(h, 2)
    b_squared = operator.pow(b, 2)
    a_squared = operator.sub(h_squared, b_squared)
    if a_squared < 0:
        print('There is no square root of negative numbers')
        raise Exception(f'{ZeroDivisionError} there is no square root of negative numbers.')
    a = operator.pow(a_squared, 0.5)
    print(f'Value of a is {a}')
    main()


def find_value_b():
    h = float(input('Value of h: '))
    a = float(input('Value of a: '))
    h_squared = operator.pow(h, 2)
    a_squared = operator.pow(a, 2)
    b_squared = operator.sub(h_squared, a_squared)
    if b_squared < 0:
        print('There is no square root of negative numbers')
        raise Exception(f'{ZeroDivisionError} there is no square root of negative numbers.')
    b = operator.pow(b_squared, 0.5)
    print(f'Value of b is {b}')
    main()


def find_value_c():
    b = float(input('Value of b: '))
    a = float(input('Value of a: '))
    b_squared = operator.pow(b, 2)
    a_squared = operator.pow(a, 2)
    h_squared = operator.add(b_squared, a_squared)
    if h_squared < 0:
        print('There is no square root of negative numbers')
        raise Exception(f'{ZeroDivisionError} there is no square root of negative numbers.')
    h = operator.pow(h_squared, 0.5)
    print(f'Value of h is {h}')
    main()


main()
