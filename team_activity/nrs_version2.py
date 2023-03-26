def main():
    print("Introductory text:\
\nThis is an interactive version of the Nature Relatedness Scale(NR-6).")
    print()

    final_score = 0
    final_score += ask_question("1. My ideal vacation spot would be a remote, wilderness area.")
    final_score += ask_question("2. I always think about how my actions affect the environment.")
    final_score += ask_question("3. My connection to nature and the environment is a part of my spirituality.")
    final_score += ask_question("4. I take notice of wildlife wherever I am.")
    final_score += ask_question("5. My relationship to nature is an important part of who I am.")
    final_score += ask_question("6. I feel very connected to all living things and the earth.")

    print(f"Your score is {final_score/6:.2f}.")
    print("Higher scores indicate more nature relatedness.")

def ask_question(statement):
    print(statement)
    response = input("   Enter D, d, N, a, or A: ")
    score = 0
    if response == "D":
        score = 1
    elif response == "d":
        score = 2
    elif response == "N":
        score = 3
    elif response == "a":
        score = 4
    elif response == "A":
        score = 5
    return score

main ()