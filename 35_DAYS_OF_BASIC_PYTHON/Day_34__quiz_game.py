
questions = ("What is Python?: ",
             "When was Python created?: ",
             "Who designed Python?: ",
             "Is the Earth round?: ",
             "Does pineapples belong on pizza?: ")

options = (("A. Coffee ","B. Software","C. Programming language"),
           ("A. 1991","B. 2023","C. 1969"),
           ("A. Bill Gates","B. Guido Van Rossum","C. Elon Musk"),
           ("A. True","B. Sometimes","C. What??"),
           ("A. YES","B. YES","C. All of the above"))

answers = ("C","A","B","A","C")
guesses = []
score = 0
q_num = 0

for question in questions:
    print("-----------------------------------")
    print(question)
    for option in options[q_num]:
        print(option)

    guess = input("Enter (A, B, C): ").upper()
    guesses.append(guess)
    if guess == answers[q_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[q_num]} is the correct answer")
    q_num += 1

print("-----------------------------------")
print("              RESULTS              ")
print("-----------------------------------")

print("Answers: ",end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ",end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")