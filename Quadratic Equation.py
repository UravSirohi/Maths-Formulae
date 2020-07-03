import operator


def main():
    while True:
        print('''Please enter the quadratic by giving these values:
            ax^2+bx+c=0''')
        a = float(input('Value of a: '))
        b = float(input('Value of b: '))
        c = float(input('Value of c: '))
        in_square_root_value_1 = operator.mul(-4, operator.mul(a, c))
        in_square_root_value = operator.add(operator.pow(b, 2), in_square_root_value_1)
        if in_square_root_value < 0:
            print('There is no square root of negative numbers')
            raise Exception(f'{ZeroDivisionError} There is no square root of negative numbers.')
        else:
            square_root_value = operator.pow(in_square_root_value, 0.5)
            ans_1_working_out_1 = operator.sub(operator.mul(b, -1), square_root_value)
            ans_2_working_out_1 = operator.add(operator.mul(b, -1), square_root_value)
            bottom_value = operator.mul(2, a)
            ans_1 = operator.truediv(ans_1_working_out_1, bottom_value)
            ans_2 = operator.truediv(ans_2_working_out_1, bottom_value)
            if ans_2.is_integer():
                ans_2 = int(ans_2)
            if ans_1.is_integer():
                ans_1 = int(ans_1)
            print(f'''x = {ans_1} or
x = {ans_2}''')


main()
