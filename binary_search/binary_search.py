def binary_search(arr: list[int], item: int) -> int | None:
    low = 0  # low and high keep track of which part of the list you'll search in.
    high = len(arr) - 1

    while low <= high:  # While you haven't narrowed it down to one element ...
        half = (low + high) // 2  # ... check the middle element.
        guess = arr[half]
        if guess == item:  # Found the item.
            return half
        if guess > item:  # The guess was too high.
            high = half - 1
        else:  # The guess was too low.
            low = half + 1

    return None  # Item doesn't exist.


"""
# 1.1 Suppose you have a sorted list of 128 names, and you're searching through it using binary search.
What's the maximum number of steps it would take?
log2(128) = x
2^x = 128
x = 7

# 1.2 Suppose you double the size of the list. What's the maximum number of steps now?
log2(256) = x
2^x = 256
x = 8
"""
