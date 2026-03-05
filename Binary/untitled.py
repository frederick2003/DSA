def minOperations(self, s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) ==  1:
        return 0
    
    one_first_count = 0
    zero_first_count = 0

    for i in range(len(s)):
        if i%2 == 0:
            if s[i] != "1":
                one_first_count += 1
            if s[i] != "0":
                zero_first_count += 1 
        else:
            if s[i] != "1":
                zero_first_count += 1
            if s[i] != "0":
                one_first_count += 1

    return min(one_first_count, zero_first_count)