def quick_sort(nums, low, high):
    if low < high:        
        nums, p = partition(nums, low, high)
        nums = quick_sort(nums, low, p - 1)
        nums = quick_sort(nums, p + 1, high)
    return nums

def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return nums, i

arr = [0, 1, 5, 6, 1, 2, 0]

print(quick_sort(arr, 0, len(arr)-1))
