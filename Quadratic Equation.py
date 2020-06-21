import operator


def main():
    print('''Please enter the quadratic by giving these values:
        ax^2+bx+c=y''')
    a = int(input('Value of a: '))
    b = int(input('Value of b: '))
    c = int(input('Value of c: '))
    in_square_root_value_1 = operator.mul(-4, operator.mul(a, c))
    in_square_root_value = operator.sub(operator.pow(b, 2), in_square_root_value_1)
    square_root_value = operator.pow(in_square_root_value, 0.5)
    ans_1_working_out_1 = operator.sub(operator.mul(b, -1), square_root_value)
    ans_2_working_out_1 = operator.add(operator.mul(b, -1), square_root_value)
    bottom_value = operator.mul(2, a)
    ans_1 = operator.truediv(ans_1_working_out_1, bottom_value)
    ans_2 = operator.truediv(ans_2_working_out_1, bottom_value)
    print(f'''x = {ans_1} or
x = {ans_2}''')


main()
