def subset_sum(arr):
    if 0 in arr:
        return [0]

    positive_nums = [num for num in arr if num > 0]
    negative_nums = [num for num in arr if num < 0]
    if not negative_nums:
        return []

    target_sum = -sum(negative_nums)
    subset = []
    current_sum = 0

    for num in positive_nums:
        if current_sum + num <= target_sum:
            current_sum += num
            subset.append(num)

    if sum(subset) == target_sum:
        subset.extend(negative_nums)

    return subset


arr = [-7, -3, -2, 5, 8]
result = subset_sum(arr)
print("Subset with sum 0:", result)