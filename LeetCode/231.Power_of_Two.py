class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n % 2:
            return False
        left = 0
        right = len(str(n)) / 3 * 10 + 10           #Narrow the range of n can save many time
        while right - left  >  1:
            mid = (left + right) / 2
            if 2 ** mid == n:
                return True
            if 2 ** mid > n:
                right = mid
            if 2 ** mid < n:
                left = mid
        return False
