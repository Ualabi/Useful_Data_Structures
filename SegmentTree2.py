class SegmentTree:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self._len = int(sqrt(len(nums)))
        self.blocks = []
        for i in range(len(nums)):
            if i % self._len == 0:
                self.blocks.append(nums[i])
            else:
                self.blocks[-1] += nums[i]

    def update(self, i: int, val: int) -> None:
        block_nu = i // self._len
        diff = val - self.nums[i]
        self.blocks[block_nu] += diff
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        start_b, end_b = i // self._len, j // self._len
        _sum = sum(self.blocks[start_b: end_b])
        _sum += sum(self.nums[end_b*self._len: j+1])
        _sum -= sum(self.nums[start_b*self._len: i])
        return _sum

##################################################
# Example code
##################################################

nums = [1, 3, 5]
ST = SegmentTree(nums)
ST.sumRange(0, 2) # 1+3+5 = 9
ST.update(1, 2)
ST.sumRange(0, 2) # 2+3+5 = 8