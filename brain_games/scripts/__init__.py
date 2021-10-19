import prompt


NUMBER_MIN = 1
NUMBER_MAX = 5
NUMBER_COUNT = 3


def welcome_user():
    print('\nWelcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def endgame(question, correct, name):
    print('Question: {}'.format(question))
    answer = prompt.string('Your answer: ')
    if (answer == correct):
        print('Correct!')
        return True
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
            answer, correct))
        print("Let's try again, {}!".format(name))
        return False
