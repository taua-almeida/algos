def recursion_sum(arr: list[int]):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    return arr[0] + recursion_sum(arr[1:])

def normal_sum(arr: list[int]):
    total = 0
    for num in arr:
        total += num
    return total

list_of_nums = [2, 4, 6]

assert recursion_sum(list_of_nums) == 12
assert normal_sum(list_of_nums) == 12
