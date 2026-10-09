import random

def show_question(question, options):
    print("\n" + question)

    for option in options:
        print (option)


def check_answer(answer, correct_answer):
    return answer == correct_answer

def calculate_score(score, correct):
    if correct:
        return score+1
    return score

def get_result(score,total):
    percentage = (score/total)*100
    if percentage>=90:
        return "Excellent!"
    elif percentage>=70:
        return"Good!"
    else:
        return "Keep practicing"


def main():
    score = 0
    questions=[
    (
        "What does CPU stand for?",
        ["1- Central Processing Unit", "2- Computer Unit", "3- Control Processing Unit"],
        1
    ),
    (
        "Which language are we using?",
        ["1- Java", "2- Python", "3- C++"],
        2
    ),
    (
        "What does RAM stand for?",
        ["1- Random Access Memory", "2- Read Access Memory", "3- Rapid Action Memory"],
        1
    ),
    (
        "What symbol is used for comments in Python?",
        ["1- **", "2- #", "3- //"],
        2
    ),
    (
        "Which keyword is used to define a function in Python?",
        ["1- Function" ,"2-def", "3-print"],
        2
    ),
    (
        "Which symbol is used to assign a data set to a variable?",
        ["1- =","2- ==","3-:"],
         1
    ),
    (
        "Which function is used to dislpay text in Python?",
        ["1- display()","2-print()","3-show()"],
        2
    )
]
    random.shuffle(questions)
    for question, option, correct_answer in questions:
            show_question(question , option)
            while True:
                try:
                    answer= int(input("Your answer: "))
                    if answer not in [1,2,3]:
                        print("Enter a valid number")
                        continue
                    break
                except ValueError:
                    print("Enter a valid number")    

            if check_answer(answer, correct_answer):
                print("Correct!")
                score = calculate_score(score, True)

            else:
                print("Wrong!")

    total=len(questions)
    percentage=(score/total)*100

    print("\nQuiz Finished!")
    print("Your score : ", score,"/",total)
    print("Percentage: ",percentage)
    print(get_result(score,total))



if __name__=="__main__":
    main()