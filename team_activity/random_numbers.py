# Import random module to use random.uniform and 
# random.choice later in the program.
import random

def main():
    # Creates a list of numbers and print the list.
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers {numbers}")
    # Call append_random_numbers() to select and
    # add an N quantity of numbers onto the list.
    append_random_numbers(numbers)
    print(f"numbers {numbers}")
    append_random_numbers(numbers, 3)
    print(f"numbers {numbers}")

    # Creates an empty list of words.
    words = []
    # Call append_random_words() to select and 
    # add an N quantity of words onto the list.
    append_random_words(words, 9)
    print(f"words {words}")

def append_random_numbers(numbers_list,quantity=1):
    """
    Use random.uniform to get a number between
    the range and added it onto the list.
    Parameters:
       numbers_list: A list of numbers.
       quantity: Number of items that will be choosen and added.
    Return: Nothing because it pass numbers = numbers_list.
    """

    for _ in range(quantity):
        # will select N random numbers 
        # based on the values of quantity.
        random_number = random.uniform(0,100)
        numbers_list.append(round(random_number,1))


def append_random_words(words_list,quantity=1):
    """
    Creates a list of possible words to choose.
    Use random.choice to get a word from the list
    and add it onto the list.
    Parameters:
       words_list: A list of words.
       quantity: Number of items that will be choosen and added.
    Return: Nothing because it pass words = words_list.
    """
    
    possible_words = ["arm", "car", "cloud", "head", "heal", "hydrogen", "jog",
                      "join", "laugh", "love", "sleep", "smile", "speak",
                      "sunshine", "toothbrush", "tree", "truth", "walk", "water"]

    for _ in range(quantity):
        # Will choose N random words from the list.
        random_word = random.choice(possible_words)
        words_list.append(random_word)



if __name__ == "__main__":
    main()
