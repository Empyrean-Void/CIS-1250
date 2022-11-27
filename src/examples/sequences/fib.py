# Functions #
def fib_add():
    fib = [0, 1]
    print(fib)

    num = int(input('How many numbers: '))

    for i in range(num - 2):
        new_num = fib[-1] + fib[-2]
        fib.append(new_num)

        print(fib)


# Main #
if __name__ == "__main__":
    fib_add()
