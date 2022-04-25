#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: March 2022
# This is a guess the random number program

import random


def main():
    # This is a random number guesser, with try and catch

    # input
    random_number = random.randint(0, 9)  # a number between 0 and 9
    counter = 0

    # process & output
    while True:
        guess_number_string = input("\nEnter your first guess here (0-9): ")
        try:
            guess_number = int(guess_number_string)
            counter += 1
            if guess_number < 0 or guess_number > 9:
                print("\nInvalid Number!")
            else:
                if guess_number > random_number:
                    print("\nGuess number is too high!")
                elif guess_number < random_number:
                    print("\nGuess number is to low")
                else:
                    print("You guessed correctly!")
                    print("\nThe correct number is {0}.".format(random_number))
                    print("It took you {0} guesses!".format(counter))
                    # how many times through
                    print("\nDone.")
                    break

        except Exception:
            print("\nThat was not an integer")


if __name__ == "__main__":
    main()
