# Create the Quiz program that read the output file of the Quiz Creator. The user will answer the randomly selected question and check if the answer is correct.

import os

# User's input of the text file name to read the file
filename = input("\nEnter the quiz file name: ")
if not filename.endswith('.txt'):
    filename += '.txt'

# Extracting the contents of the text file
    # Extract the questions
    # Extract the choices
    # Extract the answers
questions = []

if not os.path.exists(filename):
    print(f"Error: File '{filename}' not found.")
else:
    with open(filename, 'r') as file:
        content = file.read().split("\n\n")
        
    for block in content:
        if not block.strip():
            continue
            
        lines = block.strip().split('\n')
        if len(lines) < 6:
            continue
            
        # Extract the question text
        question_text = lines[0].split(": ", 1)[1] if ": " in lines[0] else lines[0]

# Displaying the questions and choices to the user
# Get the user's answers
# Check if correct
# Display the results of the quiz