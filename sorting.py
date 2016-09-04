#Sorting


def bubble_sort(lst):
    """returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap
        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """

    # minus one because we are comparing two numbers. If we reach the end, we don't have a second number to compare --> will lead to error
    for i in range(len(lst) - 1):
        # don't switch out the last numbers we've already sorted to the end.
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list containing all
    integers in the input lists
    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    list3 = []

    while len(list1) > 0 or len(list2) > 0:
        if list1 == []:
            list3.append(list2.pop(0))
        elif list2 == []:
            list3.append(list1.pop(0))
        elif list1[0] < list2[0]:
            list3.append(list1.pop(0))
        else:
            list3.append(list2.pop(0))

    return list3


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.
    Finish the merge sort algorithm by writing another function that
    that takes in a single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all integers from
    thin input list. In other words, the new function should sort a list using merge_lists
    and recursion.
    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """

    if len(lst) < 2:
        return lst

    mid = int(len(lst) / 2)
    list1 = merge_sort(lst[:mid])  # first half of numbers in one list
    list2 = merge_sort(lst[mid:])  # second half of numbers in the other list

    return merge_lists(list1, list2)


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print