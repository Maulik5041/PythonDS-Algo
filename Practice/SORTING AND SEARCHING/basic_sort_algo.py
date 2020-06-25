"""Basic algorithms for sorting"""


# Sorting 1: Selection Sort --> Finding the min element and placing it at index 0
def selection_sort(lst):

    for idx, val in enumerate(lst):
        min_index = idx

        for j in range(idx+1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j

        lst[idx], lst[min_index] = lst[min_index], lst[idx]


if __name__ == '__main__':
    unsorted_lst = [3, 2, 1, 5, 4]
    selection_sort(unsorted_lst)
    print(f"Sorted array by selection sort: {unsorted_lst} \n\n")


# Sorting 2: Bubble Sort --> Swapping adjacent till sorted
def bubble_sort(lst2):
    for i in range(len(lst2)):
        for j in range(0, len(lst2) - i - 1):
            if lst2[j] > lst2[j + 1]:
                lst2[j], lst2[j + 1] = lst2[j + 1], lst2[j]


if __name__ == '__main__':
    unsorted_lst_2 = [3, 2, 1, 5, 4]
    bubble_sort(unsorted_lst_2)
    print(f"Sorted array by bubble sort: {unsorted_lst_2} \n\n")


# Sorting 3: Insertion Sort --> Inserting correct element in its place
def insertion_sort(lst3):
    for i in range(1, len(lst3)):
        key = lst3[i]
        j = i - 1

        while j >= 0 and key < lst3[j]:
            lst3[j + 1] = lst3[j]
            j -= 1
        lst3[j + 1] = key


if __name__ == '__main__':
    unsorted_lst_3 = [3, 2, 4, 1, 5]
    insertion_sort(unsorted_lst_3)
    print(f"Sorted array by insertion sort: {unsorted_lst_3}")
