class SegmentTree():
    def __init__(self, arr):
        self.N = len(arr)
        deep, lvl = 1, 1
        while lvl < self.N:
            deep += 1
            lvl *= 2
        self.deep = deep
        self.values = [[None]]

        lvl = 2*self.N
        for x in range(self.deep):
            s = []
            sub, index = 1, 0
            lvl = lvl//2+1 if lvl%2 else lvl//2
            for y in range(lvl):
                suma = 0
                if x:
                    while index < len(self.values[x]) and index < 2*sub:
                        suma += self.values[x][index]
                        index += 1
                else:
                    suma += arr[index]
                    index += 1
                s.append(suma)
                sub += 1
            self.values.append(s)
        return None

    def update(self, index, nval):
        pval = self.values[1][index]
        change = nval-pval
        for x in range(self.deep):
            self.values[x+1][index] += change
            index = index//2
        return None

    def sumRange(self, l, r, lvl=None):
        if lvl == None:
            r += 1
            lvl = self.deep
        if l==r or lvl == 0:
            return 0
        a = l//(2**(lvl-1))+1 if l%(2**(lvl-1)) else l//(2**(lvl-1))
        b = r//(2**(lvl-1))  
        if a < b:
            if   a+1 == b:
                suma = self.values[lvl][a]
            elif a+2 == b:
                suma = self.values[lvl][a] + self.values[lvl][a+1] 
            ll = a*(2**(lvl-1))
            rr = b*(2**(lvl-1))
            return self.sumRange(l,ll,lvl-1) + suma + self.sumRange(rr,r,lvl-1)
        else:
            return self.sumRange(l,r,lvl-1)

##################################################
# Example code
##################################################

nums = [1, 3, 5]
ST = SegmentTree(nums)
ST.sumRange(0, 2) # 1+3+5 = 9
ST.update(1, 2)
ST.sumRange(0, 2) # 2+3+5 = 8