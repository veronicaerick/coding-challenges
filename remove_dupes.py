def remove_dupes(arr):
    nums = set()
    for num in arr:
        if num in nums:
            continue
        if num not in nums:
            nums.add(num)

    return list(nums)