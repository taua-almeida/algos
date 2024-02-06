def recursive_binary_search(arr: list[int], item: int, low: int, high: int) -> int | None:
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == item:
            return item

        elif arr[mid] > item:
            recursive_binary_search(arr, item, low, mid - 1)

        else:
            return recursive_binary_search(arr, item, mid + 1, high)
    else:
        return None

arr = [2, 3, 4, 10, 10]
x = 10

assert recursive_binary_search(arr, x, 0, len(arr) - 1) == x
