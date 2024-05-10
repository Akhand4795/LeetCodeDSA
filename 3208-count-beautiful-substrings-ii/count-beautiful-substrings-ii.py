vowels = {'a', 'e', 'i', 'o', 'u'}
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        l = [1 if x in vowels else -1 for x in s]
        n = len(l)
        
        lengths_modk = set()
        for i in range(0, k):
            if (i*i)%k == 0:
                lengths_modk.add(i)

        diff_k = {}
        for i in range(k):
            m = set()
            for j in range(k):
                if (i-j)%k in lengths_modk:
                    m.add(j)
            diff_k[i] = m

        x = 0
        count = {0: [(-1, None)]}
        for i, y in enumerate(l):
            x += y
            if x in count:
                prev = count[x]
                length = ((i - prev[-1][0])//2)
                prev.append((i, length))
            else:
                count[x] = [(i, None)]

        total = 0
        for indices in count.values():
            modkd = {i: [] for i in range(k)}
            modkd[0].append(indices[0][0])

            x = 0
            for i, length in indices[1:]:
                x += length
                
                xmk = x%k
                l = diff_k[xmk]
                for j in l:
                    total += len(modkd[j])
                modkd[xmk].append(i)
        
        return total