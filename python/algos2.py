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


# AlgoExpert: Two Number Sum
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

# AlgoExpert: Find Closest Value in BST
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

#AlgoExpert: Branch Sums
def branchSums(root):
    left = False
    right = False
    
    if root.left:
        left = branchSums(root.left)
    if root.right:
        right = branchSums(root.right)
    
    results = []

    if left:
        for total in left:
            results.append(total+root.value)
    if right:
        for total in right:
            results.append(total+root.value)
    
    if results:
        return results
    else:
        return [root.value]

""" ^^ Completed successfully in 40:00 ^^ """


# AlgoExpert: Minimum Waiting Time
def minimumWaitingTime(queries):
    queries.sort()
    total = sum(queries)
    results = 0

    for ind in range(len(queries)-1,0,-1):
        total = total-queries[ind]
        results += total
    
    return results

""" ^^ Completed successfully in 13:15 ^^ """

# alternate to above
def minimumWaitingTime(queries):
    total = 0
    queries.sort()
    length = len(queries)

    for ind in range(len(queries)):
        length -= 1
        total += queries[ind]*length
    return total

# AlgoExpert: validate subsequence
def isValidSubsequence(array, sequence):
    arrayInd = 0
    sequenceInd = 0

    while arrayInd < len(array) and sequenceInd < len(sequence):
        if array[arrayInd] == sequence[sequenceInd]:
            sequenceInd += 1
        arrayInd+=1

    if sequenceInd != len(sequence):
        return False
    
    return True

""" ^^ Completed successfully in 20:00 min ^^ """

# AlgoExpert: Bubble Sort
def bubbleSort(array):
    isComplete = False
    while not isComplete:
        isComplete = True
        for ind in range(len(array)-1):
            if array[ind] > array[ind+1]:
                array[ind], array[ind+1] = array[ind+1], array[ind] 
                isComplete = False
    return array

""" ^^ Not timed as it was an algo specifically doing a bubble (new concept to me) ^^ """

# AlgoMaster: Remove Duplicates From Linked List
class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def printList(self):
        if self.next == None:
            print("currVal: ", self.value)
        else:
            print("currVal: ", self.value)
            LinkedList.printList(self.next)

def removeDuplicatesFromLinkedList(linkedList):
    runThroughLinkedList(linkedList)
    return linkedList

def runThroughLinkedList(linkedList):
    print(linkedList.value)
    if not linkedList.next:
        return
    if linkedList.next.value == linkedList.value:
        linkedList.next = linkedList.next.next
        runThroughLinkedList(linkedList)
    return runThroughLinkedList(linkedList.next)

""" ^^ Didn't get right. Worked for me, but not for algo master ^^ """


#AlgoMaster: Binary Search 
def binarySearch(array, target):
    left = 0
    right = len(array)-1

    while left != right:
        middle = (left+right)//2
        print(array[middle])
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle+1
        else:
            right= middle-1

    if array[right] == target:
        return right
    
    return -1

""" ^^ Not timed as it was an algo specifically doing a binary search (new concept to me) ^^ """