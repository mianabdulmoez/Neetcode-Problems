class Solution:
    def hasduplicate(self, num) -> bool:
        self.num = num
        set_num = set(self.num)
        if len(self.num) > len(set_num):
            return False
        else:
            return True
        

# # obj1 = Solution([1,2,3,4,5,6]) --> Without Duplicate
obj1 = Solution([1,2,3,4,5,6,6])# --> With Duplicate
def main():
    nums = [1, 2, 3, 4, 5, 6, 6]
    solution = Solution(nums)  
    print(solution.hasduplicate()) 

if __name__ == "__main__":
    main()


# Method no 2
class Solution:
    def hasDuplicate(self, nums) -> bool:
        nums = list(nums)
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
# obj1 = Solution([1,2,3,4,5,6,6])# --> With Duplicate
# print(obj1.hasduplicate())