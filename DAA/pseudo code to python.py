import math


def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            else:
                return -1
        # Interpolation formula to estimate probe position
        pos = low + ((target - arr[low]) * (high - low)) / (
            arr[high] - arr[low]
        )
        pos = math.floor(pos)
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 70
result = interpolation_search(arr, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")