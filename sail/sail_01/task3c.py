# TODO 1: Define the constants as instructed in the writeup and assign them
#         the correct values.


# TODO 2: Implement the `amount_after_n_years` function.


# TODO 3: Define the 3 `amount_*` variables and assign them the values as
#         instructed in the writeup.

c1 = 10000 * (1 + 0.027) ** 5
c2 = 10000 * (1 + 0.0268 / 12) ** (5 * 12)
c3 = 10000 * (1 + 0.0266 / 365) ** (5 * 365)

if __name__ == "__main__":
    # TODO 4: Follow the instructions in the writeup to comment out the two
    #         print statements and uncomment the remaining lines of the code
    #         block.
    print(c1, c2, c3)
    print(max(c1, c2, c3))
    # print(f"Account option 1 will hold ${amount_1:,.2f}.")
    # print(f"Account option 2 will hold ${amount_2:,.2f}.")
    # print(f"Account option 3 will hold ${amount_3:,.2f}.")
    # print(f"The maximum amount that can be reached is "
    #       f"${max(amount_1, amount_2, amount_3):,.2f}.")
