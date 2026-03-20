from collections import defaultdict
def maximumSubarraySum(nums, k):
    # the max_count to return
    max_count = float("-inf")
    # A set to keep track of elements in the substring
    num_count = defaultdict(int)
    # A current count of the substring sum 
    subarray_count = 0
    # A left pointer, which points to the beginning of the subarray
    l = 0
    for r in range(len(nums)):
        subarray_count += nums[r]
        num_count[nums[r]] += 1
        if r - l + 1 == k:
            if len(num_count) == k:
                max_count = max(subarray_count, max_count)
                subarray_count -= nums[l]
                del num_count[nums[l]]
                l += 1
            else:
                num_count[nums[l]] -= 1
                subarray_count -= nums[l]
                if num_count[nums[l]] == 0:
                    del num_count[nums[l]]
                l += 1

    return max(0, max_count)


def maximumSubarraySumFred(nums, k):
    cur_sum = 0
    max_sum = float("-inf")
    num_count = defaultdict(int)
    left = 0
    for right in range(len(nums)):
        cur_sum += nums[right]
        num_count[nums[right]] += 1
        
        if right - left + 1 == k:
            # If the subarray is of size k we have two possibilities
            # 1. The subarray is valid e.g all elements are distinct len(num_count) == k
            if len(num_count) == k:
                # Calculate the max_sum
                max_sum = max(max_sum, cur_sum)
                cur_sum -= nums[left]
                del num_count[nums[left]]
            #2. The subarray is invalid, len(num_count) != k 
            else:
                # Subtract the value at the left pointer
                cur_sum -= nums[left]
                # If the number count at the left pointer == 1, remove it from the number count
                # mapping
                if num_count[nums[left]] == 1:
                    del num_count[nums[left]]
                # Otherwise there is still more than one occurance of the element at the left
                # index, so subtract the number count by 1
                else:
                    num_count[nums[left]] -= 1
                # Push the left pointer onto the next window.
            left += 1	
    return max(0, max_sum)	


maximumSubarraySumFred([1,5,4,2,9,9,9], 3)