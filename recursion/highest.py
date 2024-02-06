def recursion_highest(highest: int, arr: list[int]): 
    if not arr:
        return -float("inf")
    if len(arr) == 1 and highest > arr[0]:
        return highest
    if len(arr) == 1 and arr[0] > highest:
        return highest
    if arr[0] > highest:
        return recursion_highest(arr[0], arr[1:])
    if arr[0] < highest:
        return recursion_highest(highest, arr[1:])
    return recursion_highest(highest, arr[1:])

def loop_highest(arr: list[int]):
    highest = -float("inf")
    for n in arr:
        if n > highest:
            highest = n
    return highest

list_of_items = [1, 10, 30, 2, 5]

assert recursion_highest(-float("inf"), list_of_items) == 30
assert loop_highest(list_of_items) == 30
