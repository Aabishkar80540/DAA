def interpolation_search(arr, target):
    if not arr:
        return -1

    low, high = 0, len(arr) - 1

    if target < arr[low] or target > arr[high]:
        return -1

    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            return low if arr[low] == target else -1

        if arr[high] == arr[low]:
            return low if arr[low] == target else -1

        pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))

        if pos < low or pos > high:
            pos = (low + high) // 2

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