class Solution:

    def encode(self, strs: List[str]) -> str:
        key = ''
        for i in range(len(strs)):
            cand = strs[i]
            clen = len(cand)
            seq = str(clen)
            while len(seq) < 3:
                seq = '0' + seq
            key = key + seq
        key = key + '<' * (300-len(key))
        print(len(key))
        compact = ''
        for i in strs:
            compact = compact + i
        return key + compact

    def decode(self, s: str) -> List[str]:
        key = s[:300]
        compact = s[300:]
        arr = []
        p = 0
        for i in range(0,300,3):
            if key[i] == '<':
                return arr
            clen = int(key[i:i+3])
            if clen == 0:
                element = ""
            else:
                element = compact[p:p+clen]
                p+=clen
            arr.append(element)
        return arr
            
            




