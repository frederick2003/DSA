class Solution(object):

    # Reverses a string
    def reverse(self, x):
        return x[::-1]
    
    # Inverts the bits of a string
    def inverse(self, x):
        inverse_list = []
        for char in x:
            if char == "0":
                inverse_list.append("1")
            else:
                inverse_list.append("0")
        return "".join(inverse_list)

    
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        # Stack or Queue ?

        n1 = "0"

        if n == 1:
            return n1

        # Keep track of the string being built
        s = n1
        
        # Iterate n times 
        for i in range(n - 1):
            s = s + "1" + self.reverse(self.inverse(s))
        
        return s[k-1]