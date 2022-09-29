from task4 import fib, is_prime, merge_sort_in_place


def test_fib():
    """
    This is a suite of tests for the fib function.
    :return:
    """
    assert fib(1) == 1
    # TODO 1: PLACE YOUR CODE HERE



def test_is_prime():
    """
    This is a suite of tests for the is_prime function.
    :return:
    """
    assert is_prime(3) == True
    # TODO 2: PLACE YOUR CODE HERE


# Lists to use for binarySearch() and mergeSort() tests
lst1 = [1, 5, 2, 6, 2]
lst2 = [9, 8, 7, 6.5]
lst3 = [5, -3, 7, -3]
lst4 = [1]
lst5 = []
lst6 = ['hello', 'a', 'the']

def test_merge_sort_in_place():
    """
    This is a suite of tests for the merge_sort_in_place function.
    :return:
    """
    # The below lines apply the `merge_sort_in_place` function to the `lst_*`
    # lists. After the application the lists should be sorted.
    merge_sort_in_place(lst1)
    merge_sort_in_place(lst2)
    merge_sort_in_place(lst3)
    merge_sort_in_place(lst4)
    merge_sort_in_place(lst5)
    merge_sort_in_place(lst6)
    
    assert lst1 == [1, 2, 2, 5, 6]
    # Below, please, write tests based on `lst2` - `lst6`. A sample test for
    # `lst1 is provided above.`
    # TODO 3: PLACE YOUR CODE HERE


if __name__ == '__main__':
    test_fib()
    print('-' * 5)
    test_is_prime()
    print('-' * 5)
    test_merge_sort_in_place()
