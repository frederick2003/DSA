from collections import defaultdict
def characterReplacement(s, k):
    if len(s) == 1:
        return 1
    
    result = 0
    l = 0
    mapping = defaultdict(int)
    for r in range(len(s)):
        # Add the right char to the map
        mapping[s[r]] += 1
        max_char = max(mapping.values())
        cur_length = r - l + 1
        if cur_length - max_char > k:
            mapping[s[l]] -= 1
            l+=1 
        result = max(result, r - l + 1)
    return result
print(characterReplacement("AABABBA", 1))