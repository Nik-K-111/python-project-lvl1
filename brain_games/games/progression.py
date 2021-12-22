# progression.py for scripts/brain_progression.py

import random

DESCRIPTION = 'What number is missing in the progression?'


def a_progression(first_term, num_term, difference):
    progression = [first_term, ]
    for i in range(1, num_term):
        progression.append(first_term + difference * i)
    return progression


def generate_round():
    first_term = random.randint(3, 9)
    num_term = 10
    difference = random.randint(3, 15)
    num_x_term = random.randint(0, num_term - 1)
    progression = a_progression(first_term, num_term, difference)
    correct_answer = progression[num_x_term]

    string_progression = [str(term) for term in progression]
    string_progression[num_x_term] = '..'
    question = ' '.join(string_progression)

    return DESCRIPTION, question, correct_answer
