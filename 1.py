def rearrange_array(arr):
    n = len(arr)

    if n < 2:
        return arr  # No rearrangement needed for arrays with 0 or 1 element

    # Step 1: Find the Maximum and Minimum Values
    max_val = max(arr)
    min_val = min(arr)

    # Step 2: Create Two Separate Arrays
    largest_values = []
    smallest_values = []

    # Step 3: Distribute Values
    max_index = 0
    min_index = 0
    for i in range(n):
        if i % 2 == 0:
            largest_values.append(arr[max_index])
            max_index += 1
        else:
            smallest_values.append(arr[min_index])
            min_index += 1

    # Step 4: Reconstruct the Original Array
    result = []
    for i in range(n // 2):
        result.append(largest_values[i])
        result.append(smallest_values[i])

    return result

# Example usage:
input_array = [5, 2, 9, 1, 5, 6]
rearranged_array = rearrange_array(input_array)
print(rearranged_array)
