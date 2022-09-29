def fib(n):
    """
    The function returns the number in Fibonacci sequence that is at the
    position provided by the argument. If the argument is a negative integer or
    some other type the function returns None.
    Examples:
    0 -> 0
    1 -> 1
    2 -> 1  (0 + 1)
    3 -> 2  (1 + 1)
    4 -> 3  (1 + 2)
    5 -> 5  (2 + 3)
    6 -> 8  (3 + 5)
    https://en.wikipedia.org/wiki/Fibonacci_number
    :param n: integer
    :return: integer
    """
    # Check if the input is less than 0 or not an integer.
    # Return None if any of the above is True.
    if n < 0 or type(n) != int:
        return None
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc = v2*v2
        v1, v2, v3 = v1 * v1 +calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == '1':
            v1, v2, v3 = v1 + v2, v1, v2
    return v2


def is_prime(n):
    """
    The function returns True if the provided argument is an integer that is
    a prime number. It returns False otherwise.
    https://en.wikipedia.org/wiki/Prime_number
    :param n: integer
    :return: boolean
    """
    # If a given integer is greater than 1
    if n > 1 and type(n) == int:
        # Iterate from 2 to n / 2
        for i in range(2, int(n/2) + 1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime.
            if n % i == 0:
                return False
        return True
    return False
    

def merge_sort_in_place(lst):
    """
    The function sorts the list in place using the merge sort algorithm.
    https://en.wikipedia.org/wiki/In-place_algorithm
    https://en.wikipedia.org/wiki/Merge_sort
    :param lst: list
    :return: None
    """
    if len(lst) > 1:
        # Finding the mid of the list
        mid = len(lst) // 2
        # Left half
        left = lst[:mid]
        # Right half
        right = lst[mid:]
        # Recursive call to sort the left half
        merge_sort_in_place(left)
        # Recursive call to sort the right half
        merge_sort_in_place(right)
        # Two iterators for traversing the two halves
        i = 0
        j = 0
        # Iterator for the main list
        k = 0
        # Copy data to temp lists left and right
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                lst[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1
        # Checking if any element was left
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
