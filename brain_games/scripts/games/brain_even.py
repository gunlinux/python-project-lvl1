import prompt
import random

NUMBER_COUNT = 3
NUMBER_MIN = 1
NUMBER_MAX = 100


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name


def main():
    name = welcome_user()
    for i in range(NUMBER_COUNT):
        test_number = random.randint(1, 100)
        print('Question: {}'.format(test_number))
        answer = prompt.string('Your answer: ')
        correct = 'yes' if not test_number % 2 else 'no'
        if (answer == correct):
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                answer, correct))
            print("Let's try again, {}!".format(name))
            return False
    print('Congratulations, {}!'.format(name))
    return True


if __name__ == '__main__':
    main()
