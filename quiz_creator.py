# Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. Write the collected data to a text file. Ask another question until the user chose to exit.

# Program title
print("\n" + "-" * 50)
print(">>> QUIZ CREATOR <<<".center(50))
print("-" * 50)

# Empty quiz list
quiz = []

# Get the user's questions until he/she chose to exit
while True:
    print("\n=== NEW QUESTION ===")
    
    # Get question or exit
    question = input("Input your question (type 'e' to exit): ")
    if question.lower() == 'e':
        break

# Get the user's choices (a,b,c,d)
    print("Input the four possible answers:")
    choice_a = input("A: ")
    choice_b = input("B: ")
    choice_c = input("C: ")
    choice_d = input("D: ")

# Ask the user what is the correct answer
    correct = ""
    while correct not in ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']:
        correct = input("Which is correct? (A/B/C/D): ")
        if correct not in ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']:
            print("Please enter A, B, C, or D.")

    # Adding questions to the quiz list
    quiz.append({
        'question': question,
        'a': choice_a, 'b': choice_b, 'c': choice_c, 'd': choice_d,
        'correct': correct.lower()
    })

    # Confirmation message
    confirmation = "Done!"
    print(confirmation)

# Save the questions to a text file
if quiz:

    # Get filename
    filename = input("\nName your quiz file (press Enter for 'my_quiz.txt'): ")
    if not filename:
        filename = "my_quiz.txt"
    if not filename.endswith('.txt'):
        filename += '.txt'
        
    with open(filename, 'w') as file:
        
        for i, q in enumerate(quiz, 1):
            file.write(f"Question {i}: {q['question']}\n")
            file.write(f"A. {q['a']}\n")
            file.write(f"B. {q['b']}\n")
            file.write(f"C. {q['c']}\n")
            file.write(f"D. {q['d']}\n")
            file.write(f"Answer: {q['correct'].upper()}\n\n")
    
    print(f"\nYour {len(quiz)} questions saved to '{filename}'")
    print("Your quiz is ready!")

else:
    print("No questions created...")