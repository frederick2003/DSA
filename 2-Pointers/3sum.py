def threeSum(nums):
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    triplets = []
    for i in range(n):
        if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
            continue
        l = i + 1
        r = n - 1
        while l < r:
            if sorted_nums[i]  + sorted_nums[l] + sorted_nums[r] == 0:
                triplets.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                l += 1
                while sorted_nums[l] == sorted_nums[l-1] and l < r:
                    l += 1
            elif sorted_nums[i]  + sorted_nums[l] + sorted_nums[r] < 0:
                l += 1
            else:
                r -= 1
    return triplets