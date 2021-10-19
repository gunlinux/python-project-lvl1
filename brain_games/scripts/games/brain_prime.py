import random
from .. import NUMBER_COUNT, NUMBER_MIN, NUMBER_MAX, welcome_user, \
    endgame


def calc_exp():
    x = random.randint(NUMBER_MIN, NUMBER_MAX)
    if x == 1:
        return ('1', 'yes')
    for i in range(2, x - 1):
        if not x % i:
            return ('{}'.format(x), 'no')
    return ('{}'.format(x), 'yes')


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(NUMBER_COUNT):
        question, rez = calc_exp()
        if not endgame(question, rez, name):
            return False
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
