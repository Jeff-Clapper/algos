# Leetcode 155:
class MinStack:
    def __init__(self):
        self.array = [] 

    def push1(self, val: int) -> None:
        self.array.insert(len(self.array),val)
        return self

    def pop1(self) -> None:
        del self.array[-1]
        return self.array

    def top1(self) -> int:
        return self.array[-1]

    def getMin1(self) -> int:
        min = self.array[0]
        for val in self.array:
            if val < min:
                min = val
        return min


# Leetcode 307
class NumArray:

    def __init__(self, nums):
        self.array = nums

    def update(self, index: int, val: int) -> None:
        self.array[index] = val
        return self

    def sumRange(self, left: int, right: int) -> int:
        total = 0
        for val in self.array[left:right+1]:
            total += val
        return total

""" ^^ TIMES OUT WITH HIGH VOLUME OF CALLS ^^ """

# 29. Divide Two Integers
def divide(dividend, divisor):
    if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
        isNeg = False
    else:
        isNeg = True

    count = 0
    if dividend < 0:
        dividend = str(dividend)
        dividend = dividend[1:]
        dividend = int(dividend)
        
    if divisor < 0:
        divisor = str(divisor)
        divisor = divisor[1:]
        divisor = int(divisor)

    for ind in range(divisor,dividend,divisor):
        count+=1

    if isNeg == True:
        count = str(count)
        count = "-"+count
        count = int(count)

    return count

#Time to finish: 30 minutes
""" ^^ TIMES OUT WITH HIGH VOLUME OF CALLS ^^ """


# AlgoMaster: Two Number Sum
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array)-1
    answer = []

    while left <= right:
        if array[left]+array[right] == targetSum:
            answer.append([array[left],array[right]])
            left +=1 
        elif array[left]+array[right] > targetSum:
            right -= 1
        else:
            left += 1
    return answer

""" ^^ Completed successfully in 24:50 ^^ """

# AlgoMaster: Find Closest Value in BST
def findClosestValueInBst(tree, target):
    if tree.value == target:
        return tree.value
    
    if tree.value > target:
        if tree.left:
            closest = findClosestValueInBst(tree.left,target)
        else: closest = 10000000000
    elif tree.value < target:
        if tree.right:
            closest = findClosestValueInBst(tree.right, target)
        else: closest = 10000000000

    if abs(tree.value-target) < abs(closest - target):
        return tree.value
    else:
        return closest

""" ^^ Completed successfully in 38:50 ^^ """