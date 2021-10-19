import random
from .. import NUMBER_COUNT, NUMBER_MIN, NUMBER_MAX, welcome_user, \
    endgame


def calc_exp():
    exp_list = ['*', '-', '+']
    number_one = random.randint(NUMBER_MIN, NUMBER_MAX)
    number_two = random.randint(NUMBER_MIN, NUMBER_MAX)
    oper = random.choice(exp_list)
    if oper == '*':
        rez = number_one * number_two

    if oper == '-':
        rez = number_one - number_two

    if oper == '+':
        rez = number_one + number_two
    return ('{} {} {}'.format(number_one, oper, number_two), str(rez))


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    for i in range(NUMBER_COUNT):
        question, rez = calc_exp()
        if not endgame(question, rez, name):
            return False
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
