"""Using the Python module - Bisect"""


import bisect


an_array = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

"""The bisect_left function finds the index of the target element.
In the event where duplicate entries are satisfying the target element,
the bisect_left function returns the left-most occurrence. The input
parameters to the method are the sorted list and the target element
to be searched"""

# -10 is at index 1
print(bisect.bisect_left(an_array, -10))

# First Occurence of 285 is at index 6
print(bisect.bisect_left(an_array, 285))


"""The bisect_right function returns the insertion point which
comes after, or to the right of, any existing entries of the
target element in the list. It takes in a sorted list as the
first parameter and the target element to be searched as the
second parameter"""

# Index position to right of -10 is 2
print(bisect.bisect_right(an_array, -10))

# Index position after last occurrence of 285 is 9.
print(bisect.bisect_right(an_array, 285))


# Index position to right of -10 is 2. (Same as bisect_right)
print(bisect.bisect(an_array, -10))

# Index position after last occurrence of 285 is 9. (Same as bisect_right).
print(bisect.bisect(an_array, 285))


print(an_array)
bisect.insort_left(an_array, 108)
print(an_array)

bisect.insort_right(an_array, 108)
print(an_array)