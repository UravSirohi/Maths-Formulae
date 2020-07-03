import operator


def main():
    print('''Please enter the quadratic by giving these values:
    ax^2+bx+c=y.''')
    a = float(input('Value of a: '))
    b = float(input('Value of b: '))
    c = float(input('Value of c: '))
    if a < 0:
        print('There is no square root of negative numbers')
        raise ZeroDivisionError
    root_of_a = operator.pow(a, 0.5)
    equa_part_1 = operator.mul(b, operator.truediv(1 / 2, root_of_a))
    ans_calc_part_2 = operator.pow(equa_part_1, 2)
    ans_part_1 = ans_calc_part_1(a, root_of_a, ans_calc_part_2)
    new_part_1 = operator.mul(equa_part_1, -1)
    ans_part_2 = operator.add(new_part_1, c)
    if ans_part_2 > 0:
        ans_part_2 = f'+ {ans_part_2}'
    ans = f'''The complete square of that quadratic equation is:
{ans_part_1}^2 {ans_part_2}'''
    print(ans)


def ans_calc_part_1(a, part_1, part_2):
    if a <= 0:
        return 0
    if part_2 >= 0:
        is_negative = f'+ {part_2}'
    elif part_2 < 0:
        is_negative = f'- {part_2}'
    else:
        return 1
    if part_1.is_integer():
        return f'({round(part_1)}x {is_negative})'
    return f'(({part_1})x {is_negative})'


main()
