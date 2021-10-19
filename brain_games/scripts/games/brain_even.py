import random
from .. import NUMBER_COUNT, NUMBER_MIN, NUMBER_MAX, welcome_user, \
    endgame


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(NUMBER_COUNT):
        test_number = random.randint(NUMBER_MIN, NUMBER_MAX)
        correct = 'yes' if not test_number % 2 else 'no'
        if not endgame(test_number, correct, name):
            return False
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
