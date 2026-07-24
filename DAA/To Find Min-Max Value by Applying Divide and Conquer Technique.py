def min_max_dc(arr, low, high):
    """
    Finds the minimum and maximum elements in arr[low...high] using Divide and Conquer.
    Returns a tuple: (min_value, max_value)
    """
    # Base Case 1: Single element
    if low == high:
        return (arr[low], arr[low])

    # Base Case 2: Two elements (1 comparison)
    if high == low + 1:
        if arr[low] < arr[high]:
            return (arr[low], arr[high])
        else:
            return (arr[high], arr[low])

    # Recursive divide
    mid = (low + high) // 2
    lmin, lmax = min_max_dc(arr, low, mid)
    rmin, rmax = min_max_dc(arr, mid + 1, high)

    # Combine: 2 comparisons
    overall_min = min(lmin, rmin)  # 1 comparison
    overall_max = max(lmax, rmax)  # 1 comparison

    return (overall_min, overall_max)


# Wrapper function for convenient usage
def find_min_max(arr):
    if not arr:
        raise ValueError("Array must not be empty.")
    return min_max_dc(arr, 0, len(arr) - 1)


# ==========================================
# EXAMPLE USAGE
# ==========================================
if __name__ == "__main__":
    numbers = [3, 8, 1, 9, 4, 12, -2, 7, 0, 15]

    min_val, max_val = find_min_max(numbers)

    print(f"Input Array: {numbers}")
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")