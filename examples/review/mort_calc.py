# mort_calc.py
# Programmer: Jonah Shortz
# Date: 22 Sep 2022
# Purpose: Claculate monthly mortgage payment, total amount payed

# Functions #

def dispaly_header():
    print('Welcome to Mortgage Calculator!\n')


def get_principle():
    principle = float(input('Enter principle in dollars: '))
    return principle


def get_interest():
    interest_rate = float(input('Enter interest rate: '))
    return interest_rate


def get_years():
    years = int(input('Enter the number of years for loan: '))
    return years


def calc_monthly_mortgage(principle, interest_rate, years):
    n = years * 12
    r = (interest_rate / 100) / 12
    numerator = r * (1 + r) ** n
    denominator = (1 + r) ** n - 1
    monthly = principle * (numerator/denominator)

    return monthly


def calc_total_amount_loan(monthly, years):
    total = years * 12 * monthly

    return total


def display_mortgage_info(monthly, total):
    print(f'\nThe monthly payed amount is ${monthly:.2f}')
    print(f'\nThe total amount payed is ${total:.2f}')


def display_exit():
    print('Exiting...')

# Main #


# Print welcome message
dispaly_header()

do_another = 'y'

# Enable multiple calculations
while do_another == 'y':

    # Get user input
    principle = get_principle()
    interest_rate = get_interest()
    years = get_years()

    # Calculate monthly payment
    monthly = calc_monthly_mortgage(principle, interest_rate, years)

    # Calculate total amount payed
    total = calc_total_amount_loan(monthly, years)

    # Display results
    display_mortgage_info(monthly, total)

    # Add default option of yes
    do_another = input('\nDo another (y/n)? ') or 'y'

# Print exit message
display_exit()
