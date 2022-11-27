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

        round_winner = 'tie'

    elif user_choice == 'rock':
        if computer_choice == 'paper':
            print(f'\nComputer picked {computer_choice}... You Lose!')

            round_winner = 'computer'
        else:
            print(f'\nComputer picked {computer_choice}... You Win!')

            round_winner = 'user'

    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            print(f'\nComputer picked {computer_choice}... You Lose!')

            round_winner = 'computer'
        else:
            print(f'\nComputer picked {computer_choice}... You Win!')

            round_winner = 'user'

    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            print(f'\nComputer picked {computer_choice}... You Lose!')

            round_winner = 'computer'

        else:
            print(f'\nComputer picked {computer_choice}... You Win!')

            round_winner = 'user'

    return round_winner


def get_computer_score():
    computer_score = 0

    return computer_score


def get_user_score():
    user_score = 0

    return user_score


def display_score(computer_score, user_score):
    print(f'\nComputer score: {computer_score} | User score: {user_score}')


def display_exit():
    print('\nThank you for playing Rock Paper Scissors Ultimate!')


# Main #
if __name__ == "__main__":

    # Print welcome message
    display_header()

    # Allow multiple rounds
    do_another = 'y'

    computer_score = get_computer_score()

    user_score = get_user_score()

    while True:
        # Get move from user
        user_choice = get_user_choice()

        # Get move from computer
        computer_choice = get_computer_choice()

        # Display moves
        display_choices(user_choice, computer_choice)

        # Determine round winner
        round_winner = determine_winner(user_choice, computer_choice)

        # Keep score
        if round_winner == 'computer':
            computer_score += 1

        elif round_winner == 'user':
            user_score += 1

        else:
            print('\nRound was a tie, score unchanged.')

        display_score(computer_score, user_score)

        if user_score == 3:
            print('\nYou win!')

            break

        if computer_score == 3:
            print('\nGame over! Better luck next time...')

            break

    # Print exit message
    display_exit()
