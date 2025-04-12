# Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d) and the correct answer. Write the collected data to a text file. Ask another question until the user chose to exit.

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
# Save the questions to a text file