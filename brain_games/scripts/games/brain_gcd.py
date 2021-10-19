import random
from .. import NUMBER_COUNT, NUMBER_MIN, NUMBER_MAX, welcome_user, \
    endgame


def gcd(x, y):
    if (y == 0):
        return x
    return gcd(y, x % y)


def calc_exp():
    x = random.randint(NUMBER_MIN, NUMBER_MAX)
    y = random.randint(NUMBER_MIN, NUMBER_MAX)
    return ('{} {}'.format(x, y), str(gcd(x, y)))


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    for i in range(NUMBER_COUNT):
        question, rez = calc_exp()
        if not endgame(question, rez, name):
            return False
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
