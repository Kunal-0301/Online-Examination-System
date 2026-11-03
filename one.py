# PS No. 68 
#Project Title: Online Examination System
#Stdent Name: Kunal Das
#Email: kunal.das1@rungta.org
#Section: B.Tech 1st Sem A2
#------------------------------------------------------------------------------------------------------------------------------

def get_questions():
    """
    Creates and returns a list of 5 multiple-choice questions (MCQs).
    Each question is stored as a dictionary containing:
      - 'question': The question text (string)
      - 'options' : A list of 4 option strings (a to d)
      - 'answer'  : The correct option letter (string)
    Answer Key as per problem statement: Q1-b, Q2-c, Q3-b, Q4-b, Q5-b
    """
    questions_list = [
        {
            # Question 1 (Correct Answer: b)
            "question": "Q1. Which data type in Python is mutable?",
            "options": ["a) Tuple", "b) List", "c) String", "d) Integer"],
            "answer": "b"
        },
        {
            # Question 2 (Correct Answer: c)
            "question": "Q2. Which keyword is used to define a function in Python?",
            "options": ["a) func", "b) define", "c) def", "d) function"],
            "answer": "c"
        },
        {
            # Question 3 (Correct Answer: b)
            "question": "Q3. How are key-value pairs stored in Python?",
            "options": ["a) List", "b) Dictionary", "c) Set", "d) Tuple"],
            "answer": "b"
        },
        {
            # Question 4 (Correct Answer: b)
            "question": "Q4. What is the output of 2 ** 3 in Python?",
            "options": ["a) 6", "b) 8", "c) 9", "d) 5"],
            "answer": "b"
        },
        {
            # Question 5 (Correct Answer: b)
            "question": "Q5. Which function is used to accept input from the console in Python 3?",
            "options": ["a) get()", "b) input()", "c) scanf()", "d) read()"],
            "answer": "b"
        }
    ]
    return questions_list


def validate_input(q_num):
    """
    Prompts the student to enter an answer for a specific question number (q_num).
    Continuously loops until the student enters a valid choice ('a', 'b', 'c', 'd', or 's').
    Returns the validated choice.
    """
    # List of allowed inputs ('a'-'d' for options, 's' to skip the question)
    valid_choices = ['a', 'b', 'c', 'd', 's']

    # Infinite loop that only breaks when a valid input is provided
    while True:
        # Read user input, remove leading/trailing spaces, and convert to lowercase
        choice = input(f"Enter your answer for Q{q_num} (a/b/c/d or 's' to skip): ").strip().lower()

        # Check if the entered option is valid
        if choice in valid_choices:
            if choice == 's':
                # Inform the student that the question was skipped
                print(f"Q{q_num} skipped.\n")
            else:
                # Confirm the recorded answer (matches Test Case 3 output format)
                print(f"Answer recorded for Q{q_num}: {choice}\n")
            return choice  # Return the valid choice and exit the function
        else:
            # Display error message for invalid inputs (matches Test Case 3 output format)
            print("Invalid option. Enter a, b, c, d or s to skip.")


def conduct_exam(questions):
    """
    Displays the exam instructions, iterates through each question one by one,
    collects the validated response from the student, and returns the list of responses.
    """
    # Display exam header and instructions
    print("=" * 55)
    print("           ONLINE EXAMINATION SYSTEM")
    print("=" * 55)
    print("Instructions:")
    print("- Total Questions: 5 MCQs (2 marks each, Total = 10 marks)")
    print("- Enter 'a', 'b', 'c', or 'd' to answer.")
    print("- Enter 's' to skip a question (0 marks for skipped/wrong).")
    print("- Minimum Passing Percentage: 40.00%\n")

    # List to store the student's answers for all questions
    user_answers = []

    # Loop through each question dictionary using enumerate (starting question number at 1)
    for index, q in enumerate(questions, start=1):
        # Print the question text
        print(q["question"])

        # Print all 4 options (a, b, c, d) for the current question
        for opt in q["options"]:
            print(f"  {opt}")

        # Get validated input from the student for the current question
        ans = validate_input(index)

        # Append the student's response to the user_answers list
        user_answers.append(ans)

    return user_answers


def calculate_results(questions, user_answers):
    """
    Compares the student's answers against the official answer key.
    Calculates:
      - Number of correct, wrong, and skipped questions
      - Total score (2 marks per correct answer, 0 for wrong or skipped)
      - Percentage score
      - Final Result ('Pass' if percentage >= 40%, otherwise 'Fail')
    """
    # Initialize counters for question statuses
    correct = 0
    wrong = 0
    skipped = 0

    # Define marking scheme constants
    marks_per_question = 2
    total_marks = len(questions) * marks_per_question  # 5 questions * 2 marks = 10 marks

    # Pair each question dictionary with the student's corresponding answer
    for q, user_ans in zip(questions, user_answers):
        if user_ans == 's':
            # Student chose to skip the question (0 marks)
            skipped += 1
        elif user_ans == q["answer"]:
            # Student's answer matches the correct answer key (+2 marks)
            correct += 1
        else:
            # Student's answer is incorrect (0 marks)
            wrong += 1

    # Calculate total marks scored and overall percentage
    score = correct * marks_per_question
    percentage = (score / total_marks) * 100

    # Determine Pass/Fail status (Pass requires at least 40%)
    if percentage >= 40.0:
        result = "Pass"
    else:
        result = "Fail"

    # Return all computed metrics as a tuple
    return correct, wrong, skipped, score, total_marks, percentage, result


def display_summary(correct, wrong, skipped, score, total_marks, percentage, result):
    """
    Prints the final exam result summary formatted according to the test cases.
    """
    print("=" * 55)
    print("                 EXAM RESULT SUMMARY")
    print("=" * 55)

    # Display counts of Correct, Wrong, and Skipped answers
    print(f"Correct: {correct} | Wrong: {wrong} | Skipped: {skipped}")

    # Display Score, Percentage (formatted to 2 decimal places), and Pass/Fail Result
    # Special check for exactly 40.00% to include '(minimum pass marks)' as per Test Case 2
    if percentage == 40.0 and result == "Pass":
        print(f"Score: {score}/{total_marks} | Percentage: {percentage:.2f}% | Result: {result} (minimum pass marks)")
    else:
        print(f"Score: {score}/{total_marks} | Percentage: {percentage:.2f}% | Result: {result}")

    print("=" * 55)


def main():
    """
    Main driver function to execute the Online Examination System workflow.
    """
    # Step 1: Load the list of MCQ dictionaries
    questions = get_questions()

    # Step 2: Conduct the exam and collect student responses
    user_answers = conduct_exam(questions)

    # Step 3: Evaluate responses and calculate score, percentage, and result
    correct, wrong, skipped, score, total_marks, percentage, result = calculate_results(questions, user_answers)

    # Step 4: Display the final result summary on the console
    display_summary(correct, wrong, skipped, score, total_marks, percentage, result)


# Entry point of the Python script
if __name__ == "__main__":
    main()