def lengthOfLongestSubstring(s):

    n = len(s)
    if n == 0:
        return 0
    if n == 1:
        return 1
    char_set = set()
    count = 1
    longest = 0
    l = 0
    r = 1
    char_set.add(s[l])
    while r <= n - 1:
        left = s[l]
        right = s[r]
        if right not in char_set:
            char_set.add(right)
            r += 1
            count += 1
            longest = max(longest, count)
        else:
            while s[r] in char_set and l < r:
                char_set.remove(s[l])
                l += 1
                count -= 1
    return longest




def lengthOfLongestSubstringSecond(s):
    if len(s) == 0:
        return 0
    
    ss_element_set = set()
    l = 0
    ss_element_set.add(s[l])
    max_ss_length = 1

    for r in range(1, len(s)):
        
        while s[r] in ss_element_set and l < r:
            ss_element_set.remove(s[l])
            l += 1
        
        ss_element_set.add(s[r])
        if len(ss_element_set) > max_ss_length:
            max_ss_length = len(ss_element_set)
        
    return max_ss_length

print(lengthOfLongestSubstringSecond("abcabcbb"))
print(lengthOfLongestSubstringSecond(""))
print(lengthOfLongestSubstringSecond("    "))
print(lengthOfLongestSubstringSecond("bbbbb"))
print(lengthOfLongestSubstringSecond("pwwkew"))