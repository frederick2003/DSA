def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    closest = float("inf")
    result = 0
    for i in range(n):
        
        l = i + 1
        r = n - 1
        while l < r:
            # Calculate the sum.
            cur_sum = nums[i] + nums[l] + nums[r]

            # If the sum == target return that sum.
            if cur_sum == target:
                return cur_sum
            
            # Calculate the distance between the the cur_sum and the target.
            distance = abs(cur_sum - target)

            # If the current_sum is closer to the target, update the result.
            if distance < closest:
                closest = distance
                result = cur_sum

            # Move the left pointer if the sum is smaller than the target
            if cur_sum < target:
                l += 1
            # Move the right pointer if the sum is greater than the target.
            elif cur_sum > target:
                r -= 1
    return result

print(threeSumClosest([10,20,30,40,50,60,70,80,90], 1))
print(threeSumClosest([-1,2,1,-4], 1))
