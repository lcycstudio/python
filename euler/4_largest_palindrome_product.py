"""
Copyright (c) 2022, Lewis Chen
All rights reserved.

This source code is licensed under the MIT-style license found in the
LICENSE file in the root directory of this source tree. 
"""
import time

def is_palindrome(number):
    a = [x for x in str(number)]
    b = int(len(a) / 2)
    c = 0
    for i in range(b):
        if a[i] == a[-i-1]:
            c += 1
    if c == b:
        return True
    return False

def largest_palindrome_product(number):
    """
    A palindromic number reads the same both ways. The largest palindrome 
    made from the product of two 2-digit numbers is 9009 = 91 x 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    smallest = int(number * 0.1)
    largest = 0
    get_i = 0
    get_j = 0
    for i in range(number, smallest, -1):
        found_palindrome = False
        for j in range(i, 99, -1):
            if is_palindrome(i * j):
                found_palindrome = True
                break
        if found_palindrome and len(str(j)) == len(str(number)) and \
            i * j >= largest:
            largest = i * j
            get_i = i
            get_j = j
    print(f'palindrome is {get_i} x {get_j}')
    print(f'product is {largest}')

def quick_sort(arr):

    elements = len(arr)

    # Base case
    if elements < 2:
        return arr
    
    current_index = 0 # Index of the partitioning element

    for i in range(1, elements):
        if arr[i] <= arr[0]:
            current_index += 1
            temp = arr[i]
            arr[i] = arr[current_index]
            arr[current_index] = temp
    
    temp = arr[0]
    arr[0] = arr[current_index] 
    arr[current_index] = temp #Brings pivot to it's appropriate position

    left = quick_sort(arr[0:current_index]) #Sorts the elements to the left of pivot
    right = quick_sort(arr[current_index+1:elements]) #sorts the elements to the right of pivot

    arr = left + [arr[current_index]] + right #Merging everything together
    return arr

largest_palindrome_product(999)
# quick_sort([4,2,7,3])