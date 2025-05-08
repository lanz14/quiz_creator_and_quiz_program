# Create the Quiz program that read the output file of the Quiz Creator. The user will answer the randomly selected question and check if the answer is correct.

import os
import random
import time

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

        # Extract the choices
        choices = {}
        for number in range(1, 5):
            if number < len(lines):
                parts = lines[number].split(". ", 1)
                if len(parts) == 2:
                    option_letter, option_text = parts[0].lower(), parts[1]
                    choices[option_letter] = option_text

        # Extract the answers
        answer_line = lines[5] if len(lines) > 5 else ""
        if "Answer: " in answer_line:
            correct_answer = answer_line.split("Answer: ")[1].lower()

            # Add question to the list
            questions.append({
                'question': question_text,
                'a': choices.get('a', ''),
                'b': choices.get('b', ''),
                'c': choices.get('c', ''),
                'd': choices.get('d', ''),
                'correct': correct_answer
            })

# Displaying the questions and choices to the user
if not questions:
    print("No questions loaded. Exiting program.")
else:
    print(f"\nLoaded {len(questions)} questions from '{filename}'")

    selected_questions = questions.copy()
    random.shuffle(selected_questions)

    print("\nStarting quiz...")
    time.sleep(1)
    
    score = 0
    question_count = 0
    
    for question in selected_questions:
        question_count += 1
        
        print(f"\nQuestion {question_count}: {question['question']}")
        print(f"A. {question['a']}")
        print(f"B. {question['b']}")
        print(f"C. {question['c']}")
        print(f"D. {question['d']}")

# Get the user's answers
        answer = ""
        while answer not in ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D', 'q', 'Q']:
            answer = input("\nYour answer (A/B/C/D) or 'Q' to quit: ")
            
            if answer.lower() == 'q':
                print("\nQuiz terminated.")
                break
                
            if answer not in ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']:
                print("Please enter A, B, C, D, or Q.")
        
        if answer.lower() == 'q':
            break

# Check if correct
        if answer.lower() == question['correct'].lower():
            print("\n✓ Correct!")
            score += 1
        else:
            print(f"\n✗ Wrong! The correct answer is {question['correct'].upper()}.")
        
        time.sleep(1)

# Display the results of the quiz
    if question_count > 0:
        print("\n" + "-" * 50)
        print(f"Your score: {score}/{question_count}")
        percentage = (score / question_count) * 100
        print(f"Percentage: {percentage:.1f}%")
        
        if percentage >= 90:
            print("Excellent work!")
        elif percentage >= 70:
            print("Good job!")
        elif percentage >= 50:
            print("Not bad, though!")
        else:
            print("You should study, LOL!")
    
    print("-" * 50)