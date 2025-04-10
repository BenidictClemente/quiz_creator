def main():
    with open("quiz_data.txt", "a", encoding="utf-8") as file: #create or open the file
        while True:#create a loop to keep asking the user for questions and answers
            #ask the user for the question and answers
            question = input("Enter the question: ")
            a = input("Enter answer A")
            b = input("Enter answer B")
            c = input("Enter answer C")
            d = input("Enter answer D")
            correct = input("Enter the correct answer (A, B, C, or D").strip().upper()

            #write the user input to the file
            file.write(f"{question}\n")
            file.write(f"A. {a}\n")
            file.write(f"B. {b}\n")
            file.write(f"C. {c}\n")
            file.write(f"D. {d}\n")
            file.write(f"Correct answer: {correct}\n")
            file.write("************\n")# seperator between questions
            

            #ask the user if they want to add another question
            more = input("Do you want to add another question? (yes/no):")
            if more.lower() != "yes":
                break

    print("quiz data has been saved to the file")
main()