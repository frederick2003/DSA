def twoSum(self, numbers, target):
    if len(numbers) == 2:
        return [1,2]
        
    n = len(numbers) 
    left = 0
    right = n - 1

    while left < right:
        if numbers[left] + numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
           [left + 1, right + 1]
            
    return [left + 1, right + 1]