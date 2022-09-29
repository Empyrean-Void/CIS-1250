# Project 2
# Programmer: Jonah Shortz
# Email: jshortz@cnm.edu
# Purpose: Play Rock Paper Scissors

# Imports #

from random import randint  # Generate random number for computer choice

# Functions #


def display_header():
    print('Welcome to Rock Paper Scissors Ultimate')


def get_user_choice():
    # Make sure input is lower case
    user_choice = input('\nSelect a move (rock, paper, scissors): ').lower()

    return user_choice


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']

    computer_choice = choices[randint(0, 2)]

    return computer_choice


def validate_user_choice(user_choice):
    pass


def display_choices(user_choice, computer_choice):
    print(f'\nYou picked {user_choice}. Computer picked {computer_choice}.')


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('\nTie!')

    elif user_choice == 'rock':
        if computer_choice == 'paper':
            print(f'\nComputer picked {computer_choice}... You Lose!')
        else:
            print(f'\nComputer picked {computer_choice}... You Win!')

    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            print(f'\nComputer picked {computer_choice}... You Lose!')
        else:
            print(f'\nComputer picked {computer_choice}... You Win!')

    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            print(f'\nComputer picked {computer_choice}... You Lose!')
        else:
            print(f'\nComputer picked {computer_choice}... You Win!')


def display_score():
    pass


def display_exit():
    print('\nThank you for playing Rock Paper Scissors Ultimate!')

# Main #


# Print welcome message
display_header()

# TODO: Setup score tracking
user_wins = 0
computer_wins = 0

# while user_wins or computer_wins < 3:

# Allow multiple rounds
do_another = 'y'

while do_another == 'y':
    # Get move from user
    user_choice = get_user_choice()

    # Get move from computer
    computer_choice = get_computer_choice()

    # Display moves
    display_choices(user_choice, computer_choice)

    # Determine round winner
    determine_winner(user_choice, computer_choice)

    # Increment user score if user wins else increment computer score
    # user_wins += 1
    # computer_wins += 1

    # Set default option to yes
    do_another = input('\nPlay again (y/n)? ').lower() or 'y'

# Print exit message
display_exit()
