class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        '''
        Func: reverse String
        '''
        i = 0
        s = list(s)
        n = len(s)

        while True:
            j = i + 2 * k
            h = i
            
            #Normal condition
            if i + k < n:
                m = i + k - 1
            #Boudary condition
            elif i >= n - 1- k and i <= n + k -1:
                m = n - 1

            while (h <= m):
                s[h], s[m] = s[m], s[h]
                h = h + 1
                m = m - 1

            i = j
            if i > n:
                return ''.join(s)
            