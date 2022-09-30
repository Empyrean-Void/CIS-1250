# TODO 1: Define the constants as instructed in the writeup and assign them
#         the correct values.


# TODO 2: Implement the `pop_after_n_years` function.
def pop_after_n_years(init_pop, yearly_growth, years):
    new_population = init_pop * (yearly_growth ** 10)

    return new_population


# TODO 3: Define the 5 `pond_*` variables and assign them the values as
#         instructed in the writeup.
if __name__ == "__main__":
    INIT_POP_POND_1 = 10
    INIT_POP_POND_2 = 25
    INIT_POP_POND_3 = 12
    INIT_POP_POND_4 = 30
    INIT_POP_POND_5 = 4

    YEARLY_GROWTH_POND_1 = 2.0
    YEARLY_GROWTH_POND_2 = 1.5
    YEARLY_GROWTH_POND_3 = 1.8
    YEARLY_GROWTH_POND_4 = 2.2
    YEARLY_GROWTH_POND_5 = 1.5

    YEARS = 3

    pond_1 = pop_after_n_years(INIT_POP_POND_1, YEARLY_GROWTH_POND_1, YEARS)
    pond_2 = pop_after_n_years(INIT_POP_POND_2, YEARLY_GROWTH_POND_2, YEARS)
    pond_3 = pop_after_n_years(INIT_POP_POND_3, YEARLY_GROWTH_POND_3, YEARS)
    pond_4 = pop_after_n_years(INIT_POP_POND_4, YEARLY_GROWTH_POND_4, YEARS)
    pond_5 = pop_after_n_years(INIT_POP_POND_5, YEARLY_GROWTH_POND_5, YEARS)

# TODO 4: Define the `total_population` variable and assign it the sum of
#         the 5 `pond_*` variables defined above.
    total_population = pond_1 + pond_2 + pond_3 + pond_4 + pond_5

    print(total_population)
