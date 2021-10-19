import random
from .. import NUMBER_COUNT, NUMBER_MIN, NUMBER_MAX, welcome_user, \
    endgame


def calc_exp():
    prog_len = random.randint(5, 10)
    hidden_pos = random.randint(2, prog_len - 1)
    base = random.randint(NUMBER_MIN, NUMBER_MAX)
    d = random.randint(1, 10)
    rez = ''
    quest = 0
    for i in range(1, prog_len + 1):
        if i != hidden_pos:
            rez += '{} '.format(base)
        else:
            rez += '.. '
            quest = base
        base += d
    return (rez, str(quest))


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    for i in range(NUMBER_COUNT):
        question, rez = calc_exp()
        if not endgame(question, rez, name):
            return False
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
