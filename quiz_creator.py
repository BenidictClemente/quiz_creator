import random
# input username
name = input("Enter your username: ")


#Questions (question, choices, correct letter)
questions = [
    ("Who is the national hero of the Philippines?", ["A. Aguinaldo", "B. Bonifacio", "C. Rizal", "D. Mabini"], "C"),
    ("When is Philippine Independence Day?", ["A. June 12", "B. July 4", "C. August 30", "D. Sept 21"], "A"),
    ("Who founded the Katipunan?", ["A. Rizal", "B. Bonifacio", "C. Jacinto", "D. Luna"], "B"),
    ("Who declared Martial Law in 1972?", ["A. Aquino", "B. Marcos", "C. Ramos", "D. Roxas"], "B"),
    ("Where did the first revolt against Spain happen?", ["A. Cavite", "B. Bohol", "C. Pampanga", "D. Mactan"], "B")]
random.shuffle(questions) # shuffle the questions
#print quiz in random order
print("Philippine History Quiz")
print("Answer the following questions:")


