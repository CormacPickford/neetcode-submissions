class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        dele = []
        for i in range(len(s)):
            a = ascii(s[i]) 
            
            if not( (a <= ascii('9') and a >= ascii('0')) or (a <= ascii('z') and a >= ascii('a'))):
                dele.append(i)
                
        s = ''.join(c for i,c in enumerate(s) if not i in dele)
        
                    
        return s == s[::-1]
        