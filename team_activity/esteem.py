# This program implements the Rosenberg self-esteem scale by
# asking questions a adding point depending on the answer.

# Print the introductory text.

print("\nThis program is an implementation of the Rosenberg\
Self-Esteem Scale. This program will show you ten\
statements that you could possibly apply to yourself.\
\nPlease rate how much you agree with each of the\
statements by responding with one of these four letters:")

print("\nD means you strongly disagree with the statement.\
\nd means you disagree with the statement.\
\na means you agree with the statement.\
\nA means you strongly agree with the statement.")

print()

# Lists for questions and scores.

questions = [
    "1. I feel that I am a person of worth, at least on an equal plane with others.",
    "2. I feel that I have a number of good qualities.",
    "3. All in all, I am inclined to feel that I am a failure.",
    "4. I am able to do things as well as most other people.",
    "5. I feel I do not have much to be proud of.",
    "6. I take a positive attitude toward myself.",
    "7. On the whole, I am satisfied with myself.",
    "8. I wish I could have more respect for myself.",
    "9. I certainly feel useless at times.",
    "10. At times I think I am no good at all."
    ]

scores = []


def main ():
    # Call compute_score function.
    compute_score()
    # Call compute_results function and print the results in the same line of code.
    print(f"\nYour score is {compute_results(scores)}.")
    print("A score below 15 may indicate problematic low self-esteem.")
    print(scores)


def compute_score():
    # Print the questions and get the response from user.
    for i in range(len(questions)):
        print(f"{questions[i]}")
        answer = input("Enter D, d, a, or A: ")
        question_number = i+1

        # Values for positive questions.
        if question_number in (1, 2, 4, 6, 7):
            if answer == "D":
                score = 0
            elif answer == "d":
                score = 1
            elif answer == "a":
                score = 2
            elif answer == "A":
                score = 3
        
        # Values for negative questions.
        if question_number in (3, 5, 8, 9, 10):
            if answer == "D":
                score = 3
            elif answer == "d":
                score = 2
            elif answer == "a":
                score = 1
            elif answer == "A":
                score = 0

        # Add the points of each question to scores list.
        scores.append(score)


# Compute and return the result of adding all the values from the list.
def compute_results(scores):
    final_results = 0

    for i in range(len(scores)):
        score = scores[i]
        final_results += score 
    return final_results
        

# If this file is executed like this:
# > python program.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
