#AlgoExpert: Three Number Sum

def threeNumberSum(array, targetSum):
    array.sort()
    results = []
    for ind in range(len(array)-2):
        result = twoNumberSum(array[ind+1:],array[ind],targetSum)
        for arr in result:
            results.append(arr)
    return results

def twoNumberSum(array, firstInd, targetSum):
    left = 0
    right = len(array)-1
    results = []

    while left < right:
        if array[left] + array[right] + firstInd == targetSum:
            results.append([firstInd,array[left],array[right]])
            
            if array[left]+1 == array[left]:
                left += 1
            else: 
                right -= 1
        elif array[left] + array[right] + firstInd < targetSum:
            left += 1
        elif array[left] + array[right] + firstInd > targetSum:
            right -= 1
    
    return results

""" ^^ Completed successfully in 59:19 ^^ """


# AlgoExpert: BST Construction
# This didn't work.... redo later
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def contains(self, value):
        if self.valueFirstReferenced(value):
            return True
        else:
            return False


    def insert(self, value):
        runner = self
        previous = runner
        while runner is not None:
            if value < runner.value:
                previous = runner
                runner = runner.left
            else:
                previous = runner
                runner = runner.right

        previous.insertValue(value)        
        return self

    def remove(self, value):
        if self.left is None and self.right is None:
            return self

        firstInstance = self.valueFirstReferenced(value)
        
        rightBranch = firstInstance.right.getRightBranch()
        leftBranch = firstInstance.left

        firstInstance = firstInstance.getNewHead()
        firstInstance.left = leftBranch
        firstInstance.right = rightBranch
    
        return self

    
    def valueFirstReferenced(self,value):
        currNode = self
        while currNode is not None:
            if value == currNode.value:
                return currNode
            elif value < currNode.value:
                currNode = currNode.right
            else:
                currNode = currNode.left

        return 

    def insertValue(self,value):
        if value < self.value:
            self.left = BST(value)
        else:
            self.right = BST(value) 
        return self

    def getRightBranch(self):
        runner = self
        previous = runner
        
        while runner.left is not None:
            previous = runner
            runner = runner.left

        previous.left = None
        return self

    def getNewHead(self):
        runner = self
        
        while runner.left is not None:
            runner = runner.left
        
        return runner

"""" ^^ Never got working ^^ """

# AlgoExpert: Task Assignment
def taskAssignment(k, tasks):
    arr = []
    for val in range(len(tasks)):
        arr.append(val)

    for x in range(len(tasks)):
        low = x
        for j in range(x,len(tasks)):
            if tasks[arr[j]] < tasks[arr[low]]:
                low = j

        arr[x], arr[low] = arr[low], arr[x]

    results = []

    for val in range(k):
        results.append([arr[val],arr[-1-val]])

    return results

""" ^^ I completed this successfully in 1hr+ ^^ """

# AlgoExpert: Longest Palindromic Substring
def longestPalindromicSubstring(string):
    longest = string[0]
    for left in range(1,len(string)-1):
        if string[left] == string[left+1]:
            even = longestPalindrome(string,left,left+1)
            if len(even) > len(longest):
                longest = even
        
        odd = longestPalindrome(string,left,right=left)
        if len(odd) > len(longest):
            longest = odd

    return longest


def longestPalindrome(string,left,right):
    while isStringPalindrome(string[left:right+1]) and left >= 0 and right < len(string):
        left-=1
        right +=1
    return string[left+1:right]


def isStringPalindrome(string):
    return string[::] == string[::-1]

"""" ^^ This is completed ater longer than an hour. Also had to review help to get answer ^^ """

# AlgoExpert: Binary Search (easy) (practice)
def binarySearch(array, target):
    left = 0
    right = len(array)-1
    return binarySearchHelper(array,target,left,right)

    
def binarySearchHelper(array, target, left,right):
    while left <= right:
        middle = (left + right)//2
        print(array[middle])
        if array[middle] < target:
            left = middle+1
        elif array[middle] > target:
            right = middle-1
        else:
            return middle

    return -1

""" ^^ Completed in 13:23, could have completed without helper function ^^ """


# AlgoExpert: Kadane's Algorit
def kadanesAlgorithm(array):
    count = 0
    max = -10000000000

    for val in array:
        count += val
        if count > max:
            max = count
        if count < 0:
            count = 0
    
    return max

""" ^^ Completed successfully in less than 15 min ^^ """


# AlgoExpert: Permutations 
def getPermutations(array, results = [], iteration=0):
    thisArray = []
    for ind in range(len(array)):
        thisArray.append(array[ind])

    if thisArray not in results:
        results.append(thisArray)
        newArray = frontToBack(array)
        return getPermutations(newArray,results,iteration = iteration+1)
    elif iteration > 0:
        newArray = swapFront(array)
        return getPermutations(newArray,results,0)
    else:
        return results
    
def frontToBack(array):
    value = array.pop(0)
    array.append(value)
    return array

def swapFront(array):
    array[0], array[1] = array[1], array[0]
    return array

""" ^^ This is not working. It acts differently on office computer vs in algo Expert. Also, it's not getting right answer here either and idk why not ^^ """