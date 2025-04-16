questions = (
    "What is the capital of France?",
    "What is the capital of Germany?",
    "What is the capital of Italy?",
    "What is the capital of Spain?",
    "What is the capital of Portugal?",
)
options = (
    ("Paris", "Lyon", "Marseille", "Toulouse"),
    ("Berlin", "Hamburg", "Munich", "Cologne"),
    ("Rome", "Milan", "Naples", "Turin"),
    ("Madrid", "Barcelona", "Valencia", "Seville"),
    ("Lisbon", "Porto", "Vila Nova de Gaia", "Amadora"))
answers = ("PARIS", "BERLIN", "ROME", "MADRID", "LISOBON")
guesses = []
score = 0
question_num = 0

for question in questions:
    print ("------------------------")
    print ("  ", " - ",question, "", "- ")
    for option in options[question_num]:
        print ("    ", " - ",option)
    guess = input("Enter your guess: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("Correct!")
    else:
        print("Incorrect!")
    question_num += 1
print ("------------------------")
print(f"Your score is {score/len(questions)*100:.2f}%")
if score == len(questions):
    print ("Congratulations! You got all the answers right!")
else:
    print ("Better luck next time!")
print ("------------------------")
