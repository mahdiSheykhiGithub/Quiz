import random

mathOperators = ['+', '-', '*']


# FUNCTIONS
def create_questions():
    phrase = ''
    for i in range(4):
        phrase += str(random.randint(0, 9))
        if len(phrase) <= 5:
            phrase += random.choice(mathOperators)
        elif len(phrase) == 7:
            return phrase


def get_answer(phrase):
    while True:
        user_answer = input(f'\n\t{phrase} = ')
        try:
            if str(abs(int(user_answer))).isnumeric():
                answer = user_answer
                return answer
        except ValueError:
            print("\n\tPlease insert a number")
            continue


def check_answers(user_answer, phrase):
    global grade
    correct_answer = eval(phrase)
    if correct_answer == int(user_answer):
        print('\n\tcorrect')
        print('\n\t*************************************')
    else:
        grade -= 1
        print(f'\n\tWrong ... The correct answer is {correct_answer}')
        print('\n\t*************************************')
    return grade


# BODY
print('\n\t********** WELCOME TO MATH QUIZ PLEASE ANSWER THE QUESTIONS CAREFULLY **********')
while True:
    number = input('\n\tHow many questions do you want to answer? ')
    if not number.isnumeric():
        print('\n\tPlease enter a POSITIVE INTEGER number ')
        continue
    elif int(number) <= 0 or int(number) // 1 != int(number):
        print('\n\tPlease enter a POSITIVE INTEGER number ')
        continue
    else:
        break

grade = number

print(f'\n\tYou should answer to {number} question')
for t in range(10):
    math_phrase = create_questions()
    confirmed_answer = get_answer(math_phrase)
    grade = check_answers(confirmed_answer, math_phrase)

if grade >= 8:
    print(f'\n\tPerfect\nyour grade: {grade}/{number} ')
elif grade >= 6:
    print(f'Not bad\nyour grade: {grade}/{number} ')
else:
    print(f'You have to try harder\nyour grade: {grade}/{number} ')
input()
