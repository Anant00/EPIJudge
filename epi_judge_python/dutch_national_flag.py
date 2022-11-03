import functools
from operator import eq
from re import S
from turtle import st
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # start = 0
    # end = len(A) - 1
    element = A[pivot_index]
    size = len(A)
    # for i in range(size):
    #     if A[i] < element:
    #         A[i], A[start] = A[start], A[i]
    #         start += 1
    

    # for i in reversed(range(size)):
    #     if A[i] < element:
    #         break
            
    #     if A[i] > element:
    #         A[i], A[end] = A[end], A[i]
    #         end -= 1

    
    equal = 0
    start = 0
    larger = size
    while equal < larger:
        if A[equal] < element:
            A[start], A[equal] = A[equal], A[start]
            start += 1
            equal += 1
        elif A[equal] == element:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]



    return

A = [10, 2, 6, 1, 5, 3, 4, 5, 1, 2, 3, 100, -1]
dutch_flag_partition(7, A)

@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
