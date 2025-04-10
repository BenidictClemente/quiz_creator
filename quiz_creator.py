def main():
    with open("quiz_data.txt", "a", encoding="utf-8") as file:  # Create or open the file
        while True:
            # User input: question, choices, correct answer
            question = input("Enter your question: ")
            a = input("Choice A: ")
            b = input("Choice B: ")
            c = input("Choice C: ")
            d = input("Choice D: ")
            correct = input("Correct answer (A/B/C/D): ").upper()

            # Write the input to the file
            file.write(f"Question: {question}\n")
            file.write(f"A: {a}\n")
            file.write(f"B: {b}\n")
            file.write(f"C: {c}\n")
            file.write(f"D: {d}\n")
            file.write(f"Correct: {correct}\n")
            file.write("-----\n")  # Separator between questions

            # Ask if user wants to add more questions
            more = input("Do you want to add more questions? (yes/no): ")
            if more.lower() != "yes":
                break

    print("✅ Quiz data has been saved to 'quiz_data.txt'.")

# Call the function to run the program
main()
