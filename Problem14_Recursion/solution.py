class Solution:

    def subset(self, in_nums: List[int], out_nums: List[int]):
        if len(in_nums) == 0:
            self.my_solution.append(out_nums)
            return

        new_ip = in_nums[1:] if len(in_nums) > 1 else []
        self.subset(new_ip, out_nums + [in_nums[0]])
        self.subset(new_ip, out_nums)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.my_solution = []
        self.subset(nums, [])
        return self.my_solution
