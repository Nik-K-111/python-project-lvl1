# progression.py for scripts/brain_progression.py

import random

REGULATIONS = 'What number is missing in the progression?'
ROUNDS = 3


def current_game():
    NUMBER_OF_MEMBERS = 10
    MIN_DIFFERENCE, MAX_DIFFERENCE = 3, 9
    MIN_X_TERM, MAX_X_TERM = 1, 10
    LIST_FIRST_TERM = [2, 3, 4, 6, 7, 8, 9, 12, 13, 14, 16, 17, 18, 19]
    progression_string = ''

    [term] = random.sample(LIST_FIRST_TERM, 1)
    difference = random.randint(MIN_DIFFERENCE, MAX_DIFFERENCE)
    num_x_term = random.randint(MIN_X_TERM, MAX_X_TERM)
    j = NUMBER_OF_MEMBERS
    while j > 0:
        if j != num_x_term:
            progression_string = progression_string + str(term) + ' '
        else:
            correct_answer = term
            progression_string = progression_string + '.. '
        term = term + difference
        j -= 1

    question = (f'{progression_string}')

    return question, correct_answer
