class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        Func: It should be separated into three steps:
        1st : remove the lead and tail space, extra space in the middle
        2st : reverse the whole string
        3ed : reverse each word in the string        
        '''
        def reverseWord(s: list) -> list:
            # reverse a unit
            i = 0
            n = len(s)-1

            while i <= n:
                s[i], s[n] = s[n], s[i]
                i += 1
                n -= 1

            return s

        def removeSpace(s: list) -> list:
            #remove the extra space
            slow = 0
            fast = len(s)-1
            newStr = []

            #remove the head space
            while s[slow] == " ":
                slow += 1
            #remove the tail space
            while s[fast] == " ":
                fast -= 1

            while slow <= fast:
                if s[slow] != " ":
                    newStr.append(s[slow])
                elif s[slow] == " " and s[slow-1] != " ":
                    newStr.append(" ")

                slow = slow + 1

            return newStr

        def reverseEachWord(s: list) -> list:
            # reverse each word in a string
            s_start = 0
            s_end = 0
            while s_end < len(s):
                if (s[s_end] == " ") or (s_end == len(s)-1):
                    if s[s_end] == " ":
                        n = s_end-1
                    if s_end == len(s) -1:
                        n = s_end

                    m = s_start
                    while m <= n:
                        s[m], s[n] = s[n], s[m]
                        m += 1
                        n -= 1

                    s_start = s_end + 1

                s_end += 1

            return "".join(s)

        # 1st :
        s = list(s)
        s = reverseWord(s)

        # 2nd :
        s = removeSpace(s)

        # 3rd : reverse each word
        s = reverseEachWord(s)

        return s