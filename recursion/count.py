def recursion_count(arr: list[int]):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 1

    return 1 + recursion_count(arr[1:])

def loop_count(arr: list[int]):
    count = 0
    for n in arr:
        count += 1
    return count

list_of_items = [1,2,3,4,5,6]

assert recursion_count(list_of_items) == len(list_of_items)
assert loop_count(list_of_items) == len(list_of_items)
