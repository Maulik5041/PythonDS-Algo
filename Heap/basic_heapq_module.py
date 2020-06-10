"""Implementation of heapq module of python which is the min-heap"""


import heapq as hq
import random as r


list_of_integers = [21, 67, 33, 13, 40, 89, 71, 19]

# Find the two largest values
largest_nums = hq.nlargest(2, list_of_integers)
print(f"The two largest numbers in {list_of_integers} are {largest_nums}")


"""Methods in heapq module"""

# Method 1: heappush()

init_list = list(range(10, 99, 10))
print(f"Step-1: Seed data for the heap: {init_list} \n")

r.shuffle(init_list)
print(f"Step-2: Randomize the seed data: {init_list} \n")

heap = []
print("Step-3: Creating heap...")

# Demonstrating heapq.heappush() function
[hq.heappush(heap, x) for x in init_list]

print(f" a. heap contains: {heap} \n")

print(f"Adding another smaller item to verify the min-heap property: 1 \n")

hq.heappush(heap, 1)

print(f" b. Heap contains: {heap} \n")


# Method 2: heappop()

print(f"Step-4: Removing items from heap...{heap} \n")

out = hq.heappop(heap)
print(f" a. heappop() removed {out} from the above heap and resulting...\n {heap}")

out = hq.heappop(heap)
print(f" b. heappop() removed {out} from the above heap...\n {heap}")

out = hq.heappop(heap)
print(f" c. heappop() removed {out} from the above heap...\n {heap}\n")


# Method 3: heappushpop() pushes a new element and then removes the smallest
# This is a bit faster than the 2 operations combined

print(f"Step-5: Adding and removing items from heap...")
new_item = 99
out = hq.heappushpop(heap, new_item)
print(f" a. heappushpop() added {new_item} and removed {out} from {heap} \n")
new_item = 999
out = hq.heappushpop(heap, new_item)
print(f" a. heappushpop() added {new_item} and removed {out} from {heap} \n")


# Method 4: heapify() converts an arbitrary list into a heap
heap = [78, 34, 78, 11, 45, 13, 99]
print(f"Raw heap: {heap} \n")

hq.heapify(heap)
print(f"heapify(heap): {heap} \n")


# Method 5: heapreplace() is opposite to heappushpop()
heap = [78, 34, 78, 11, 45, 13, 99]
hq.heapify(heap)
print(f"heap: {heap} \n")

hq.heapreplace(heap, 12)
print(f"heapreplace(heap, 12): {heap}")

hq.heapreplace(heap, 100)
print(f"heapreplace(heap, 100): {heap}")
