import random as rdm

question_Dictionary = {
    "What is the name of the actor of the new spider-man?": [
        'A. Tom Holland', 'B. Andrew Garfield', 'C. Tobey Maguire',
        'D. Miles Morales', 'A'
    ],
    "What is the name of the actor from Shang-Chi?": [
        'A. Willem Dafoe', 'B. Ryan Reynolds', 'C. Simu Liu',
        'D. Neil Patrick Harris', 'C'
    ]
}

questions = [
    "What is the name of the actor of the new spider-man?",
    "What is the name of the actor from Shang-Chi?"
]
answers = ["Tom holland", "Simu Liu"]


def main():
    print('This is a trivia quiz about famous people')
    correct = 0
    incorrect = 0
    while len(question_Dictionary) > 0:
        index = rdm.choice(list(question_Dictionary.keys()))
        answer = input('Q: {}?\n'.format(index) +
                       '\n'.join(question_Dictionary[index][a]
                                 for a in range(4)))

        #print('Q: {}?'.format(questions[index]))
        #answer = input()
        if answer.lower() == question_Dictionary[index][4].lower():
            print('Correct!')
            correct += 1
        else:
            print('Incorrect! The correct answer is {}'.format(
                question_Dictionary[index][4]))
            incorrect += 1
        del question_Dictionary[index]
    print('\nYou got {}% of questions correct.'.format(
        int(correct / (correct + incorrect) * 100)))


main()
