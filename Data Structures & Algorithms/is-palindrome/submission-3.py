class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        dele = []
        for i in range(len(s)):
            a = ascii(s[i]) 
            print(a)
            if not( (a <= ascii('9') and a >= ascii('0')) or (a <= ascii('z') and a >= ascii('a')) or (a <= ascii('Z') and a >= ascii('A'))):
                dele.append(i)
                
        s = ''.join(c for i,c in enumerate(s) if not i in dele)
        print(s)
                    
        return s == s[::-1]
        