# This program implements the Rosenberg self-esteem scale by
# asking questions a adding point depending on the answer.

# Print the introductory text.

print("\nThis is an interactive version of the Nature Relatedness Scale(NR-6).\
The psychological construct of nature relatedness deals with the strength\
of connection to nature that individuals feel. High connection with nature is generally\
considered a good thing in this perspective.\
\nPlease rate how much you agree with each of the\
statements by responding with one of these four letters:")

print("\nD means you strongly disagree with the statement.\
\nd means you disagree with the statement.\
\nN means you are neutral with the statement\
\na means you agree with the statement.\
\nA means you strongly agree with the statement.")

print()

# Lists for questions and scores.

questions = [
    "1. My ideal vacation spot would be a remote, wilderness area.",
    "2. I always think about how my actions affect the environment.",
    "3. My connection to nature and the environment is a part of my spirituality.",
    "4. I take notice of wildlife wherever I am.",
    "5. My relationship to nature is an important part of who I am.",
    "6. I feel very connected to all living things and the earth.",
]

scores = []


def main():
    # Call compute_score function.
    compute_score()
    # Call compute_results function and print the results in the same line of code.
    print(f"\nYour score for nature relatedness was {compute_results(scores):.2f}/5.")
    print("Higher scores indicate more nature relatedness. The average score for \
college students reported by Nisbet & Zelenski (2013) is 3.28")
    print("\nNature relatedness is correlated with psychological wellbeing. \
Increasing nature relatedness can results in \nincreases in positive moods.")


def compute_score():
    # Print the questions and get the response from user.
    for i in range(len(questions)):
        print(f"{questions[i]}")
        answer = input("Enter D, d, N, a, or A: ")


        if answer == "D":
            score = 1
        elif answer == "d":
            score = 2
        elif answer == "N":
            score = 3
        elif answer == "a":
            score = 4
        elif answer == "A":
            score = 5

        # Add the points of each question to scores list.
        scores.append(score)


# Compute and return the result of adding all the values from the list.
def compute_results(scores):
    final_results = 0

    for i in range(len(scores)):
        score = scores[i]
        final_results += score
    
    # Getting the average.
    final_results = final_results / 6
    return final_results


# If this file is executed like this:
# > python program.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
