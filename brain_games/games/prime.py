# scripts/brain_prime.py > prime.py


import prompt
import random
from brain_games.offer import acquaintance
from brain_games.checking import checking


def define_prime():
    regulations = (
        'Answer "yes" if given number is prime. Otherwise answer "no".'
        )
    name = acquaintance(regulations)
    final = ''
    
    def is_prime(a):
        if a & 1 == 0:
            return False
        d = 3
        while d ** 2 <= a and a % d != 0:
            d += 2
        return d ** 2 > a
    i = 3
    while i > 0:
        i -= 1
        a = random.randint(17, 99)
        if is_prime(a) == True:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        
        print(f'Question: {a}')
        user_answer = prompt.string('Your answer: ')
        final, i = checking(i, user_answer, correct_answer, name)

    print(final)
