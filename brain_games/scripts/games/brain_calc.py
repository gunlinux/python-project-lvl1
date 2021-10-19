import prompt
import random

NUMBER_COUNT = 3
NUMBER_MIN = 1
NUMBER_MAX = 5


def welcome_user():
    print('\nWelcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name

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
        # refactor
        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')

        correct = rez == answer
        # refactor
        if (answer == rez):
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, rez))
            print("Let's try again, {}!".format(name))
            return False
    print('Congratulations, {}!'.format(name))
    return True


if __name__ == '__main__':
    main()
