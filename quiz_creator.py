import random

# Input username
name = input("Enter your username: ")

# Questions (question, choices, correct letter)
questions = [
    ("Who is the national hero of the Philippines?", ["A. Aguinaldo", "B. Bonifacio", "C. Rizal", "D. Mabini"], "C"),
    ("When is Philippine Independence Day?", ["A. June 12", "B. July 4", "C. August 30", "D. Sept 21"], "A"),
    ("Who founded the Katipunan?", ["A. Rizal", "B. Bonifacio", "C. Jacinto", "D. Luna"], "B"),
    ("Who declared Martial Law in 1972?", ["A. Aquino", "B. Marcos", "C. Ramos", "D. Roxas"], "B"),
    ("Where did the first revolt against Spain happen?", ["A. Cavite", "B. Bohol", "C. Pampanga", "D. Mactan"], "B")
]

random.shuffle(questions)  # Shuffle the questions

# Print quiz intro
print("\nPhilippine History Quiz")
print("Answer the following questions:\n")

score = 0

# Loop through each question
for index, (question, choices, correct) in enumerate(questions, start=1):
    print(f"Q{index}: {question}")
    for choice in choices:
        print(choice)
    answer = input("Your answer: ").strip().upper()

    if answer == correct:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect! The correct answer is {correct}.\n")

# Final score
print(f"{name}, your final score is {score}/{len(questions)}.")




