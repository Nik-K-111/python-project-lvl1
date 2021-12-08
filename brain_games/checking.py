# games/*.py < checking.py


def checking(i, user_answer, correct_answer, name):
    if str(user_answer) == str(correct_answer):
        print('Correct!')
        final = (f"Congratulations, {name}!")
    else:
        i = 0
        final = (
            f"'{user_answer}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'.\n"
            f"Let's try again, {name}!"
        )
    return final, i
