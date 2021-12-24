# Leetcode 155:
from python.test_2 import tournamentWinner


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
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
    current = linkedList
    while current is not None:
        nextNode = current.next
        while current.value == nextNode.value: 
            nextNode = nextNode.next

        current.next = nextNode
        current = nextNode

    return linkedList


""" ^^ Did not time, I failed originally^^ """


#AlgoMaster: Binary Search 
def binarySearch(array, target):
    left = 0 
    right = len(array)-1

    while left <= right:
        mid = (left+right) //2 
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid+1
        else:
            right = mid-1
    
    return -1

""" ^^ Not timed as it was an algo specifically doing a binary search (new concept to me) ^^ """


#AlgoExpert: Palindrome Check
def isPalindrome(string):
    palindrome = True
    count = 0
    
    while palindrome and count < len(string):
        if string[count] != string[-1*(count+1)]:
            palindrome = False

        count+=1

    return palindrome

""" ^^ Completed successfully in 10:42 min ^^ """


#AlgoExpert: Nth Fibonacci
#Pure recursive
def getNthFib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    return getNthFib(n-1)+getNthFib(n-2)

#Memory, no recursive
def getNthFib(n):
    data = {
        1:0,
        2:1
    }
    for val in range(3,n+1):
        data[val] = data[val-1] + data[val-2]
    
    return data[n]

#Hybrid with help from algoexpert prof
def getNthFib(n,data = {1:0,2:1}):
    if n not in data:
        data[n] = getNthFib(n-1,data)+getNthFib(n-2,data)
    return data[n]

""" ^^ Completed successfully in under 25 (forgot to start timer) ^^ """

# AlgoExpert: Ceasar Cipher
def caesarCipherEncryptor(string, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    results = ""

    dictionary = {}
    reverseDictionary = {}
    for ind in range(len(alphabet)):
        dictionary[ind] = alphabet[ind]
        reverseDictionary[alphabet[ind]] = ind
    
    for ind in range(len(string)):
        currentLet = string[ind]
        currentLetVal = reverseDictionary[currentLet]
        convertedVal = currentLetVal + key
        
        while convertedVal > 25:
            convertedVal -=26

        convertedLetter = dictionary[convertedVal]
        results += convertedLetter

    return results

# gross
""" ^^ Completed successfully in 23:30 min ^^ """


# AlgoExpert: Sorted Squared Array : This is O(nlogn) time due to sort()
def sortedSquaredArray(array):
    newArray = []

    for val in array:
        newArray.append(val*val)
    
    newArray = sorted(newArray)
    return newArray

""" ^^ Completed successfully in 8:00 min ^^ """

# AlgoExpert: Sorted Squared Array O(n) solution
def sortedSquaredArray(array):
    newArr = ["a" for val in range(len(array))]
    left = 0
    right = len(array) - 1

    for ind in range(len(array)-1,-1,-1):
        if abs(array[left]) < abs(array[right]):
            newArr[ind] = array[right] * array[right]
            right -= 1
        else:
            newArr[ind] = array[left] * array[left]
            left += 1

    return newArr

""" ^^ Did not time, it was post test ^^ """


# AlgoExpert: Insert Sort
def insertionSort(array):
    for ind in range(1,len(array)):
        val = ind
        while val >= 1 and array[val] < array[val-1]:
            array[val], array[val-1] = array[val-1], array[val]
            val -=1

    return array

""" ^^ Not timed as it was an algo specifically doing a insertion Sort (new concept to me) ^^ """


#AlgoExpert: Run-Length Encoding
def runLengthEncoding(string):
    char_count = 1
    character = string[0]
    results = ""

    for ind in range(1,len(string)):
        if string[ind] != character:
            results += f'{char_count}{character}'
            char_count = 1
            character = string[ind]
        else:
            char_count +=1

        if char_count == 10:
            results += f'9{character}'
            char_count = 1

    results += f'{char_count}{character}'
    return results

""" ^^ Completed successfully in 20:20 min ^^ """


#AlgoMaster: Class Photos
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    if redShirtHeights[0] > blueShirtHeights[0]:
        br = redShirtHeights
        fr = blueShirtHeights
    else:
        br = blueShirtHeights
        fr = redShirtHeights

    for ind in range(len(redShirtHeights)):
        if fr[ind] >= br[ind]:
            return False
        
    return True

""" ^^ Completed successfully in 24:12 min ^^ """
""" Special Note: Failed to clarify all the boundries and assumed I could not move everyone. This cost me time"""


# AlgoExpert: Tournament Winner O(2n) solution
def tournamentWinner(competitions, results):
    teams = {}
    highest = ["none",-1]        

    for ind in range(len(competitions)):
        if results[ind] == 0:
            results[ind] = 1
        else:
            results[ind] = 0

        if competitions[ind][results[ind]] not in teams:
            teams[competitions[ind][results[ind]]] = 3
        else:
            teams[competitions[ind][results[ind]]] += 3

    for key,value in teams.items():
        if value > highest[1]:
            highest = [key,value]
    
    return highest[0]


""" ^^ Completed successfully in 24:12 min ^^ """
""" I put this at time O(2n)""" 

# AlgoExpert: Tournament Winner O(n) solution
def tournamentWinner(competitions, results):
    teams = {}
    highest = ["none",-1]        

    for ind in range(len(competitions)):
        if results[ind] == 0:
            results[ind] = 1
        else:
            results[ind] = 0

        team = competitions[ind][results[ind]]
        
        if team not in teams:
            teams[team] = 3
        else:
            teams[team] += 3

        if teams[team] > highest[1]:
            highest = [team,teams[team]]
    
    return highest[0]

""" ^^ Completed successfully in 24:12 min ^^ """
""" I put this at time O(n)""" 


# AlgoMaster: Generate Document
def generateDocument(characters, document):
    char = {}

    for val in characters:
        if val not in char:
            char[val] = 1 
        else:
            char[val] += 1

    for val in document:
        if val not in char:
            return False
        else:
            char[val] -= 1
        if char[val] < 0:
            return False

    return True
    
""" ^^ Completed successfully in 14:33 min ^^ """


# AlgoMaster: Node Depths
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def nodeDepths(root, depth=0):
    depth = depth+1
    total_depth = 0

    if root.left is not None:
        total_depth += depth
        total_depth += nodeDepths(root.left,depth)
    if root.right is not None:
        total_depth += depth
        total_depth += nodeDepths(root.right, depth)
    return total_depth

""" ^^ Completed successfully in 24:00 min ^^ """


# AlgoMaster: Find Three Largest Numbers
def findThreeLargestNumbers(array):
    first = -1000000
    second = -1000000
    third = -1000000

    for val in array:
        if val > first:
            third = second
            second = first
            first = val
        elif val > second:
            third = second
            second = val
        elif val > third:
            third = val

    return [third,second,first]

""" ^^ Completed successfully in 10:30 min ^^ """


# AlgoMaster: First Non-Repeating Character
# This is more efficient to the improvement if the string is longer with less unique characters
def firstNonRepeatingCharacter(string):
    values = {}

    for ind in range(len(string)):
        if string[ind] not in values:
            values[string[ind]] = [1,ind]
        else:
            values[string[ind]] = [values[string[ind]][0]+1,values[string[ind]][1]]

    firstInd = 10000000000
    for key in values.keys():
        if values[key][0] == 1 and values[key][1] < firstInd:
            firstInd = values[key][1]

    if firstInd == 10000000000:
        return -1
    
    return firstInd

""" ^^ Completed successfully in 14:05 min ^^ """

# AlgoMaster: First Non-Repeating Character IMPROVEMENT ON MY ANSWER
# This is an improvement if the string is shorter with more unique characters
def firstNonRepeatingCharacter(string):
    values = {}

    for ind in range(len(string)):
        if string[ind] not in values:
            values[string[ind]] = [1,ind]
        else:
            values[string[ind]] = [values[string[ind]][0]+1,values[string[ind]][1]]

    for ind in range(len(string)):
        if values[string[ind]][0] == 1:
            return values[string[ind]][1]
    return -1

""" ^^ Not timed as it was a change to original to make it somewhat more efficient in some cases^^ """


# Algo Master: Depth First Search
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        
        for child in self.children:
            array = child.depthFirstSearch(array)

        return array

""" ^^ Completed successfully in 12:22 min ^^ """

# AlgoExpert: Product Sum
def productSum(array,depth=1):
    total = sum(convertArray(array,depth))*depth
    return total


def convertArray(array,depth):
    for ind in range(len(array)):
        if type(array[ind]) == int:
            continue
        else:
            array[ind] = productSum(array[ind],depth = depth+1)
    return array

""" ^^ Completed successfully in 45:50 min ^^ """


#AlgoExpert: Tandem Bicycle
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    print(redShirtSpeeds)
    print(blueShirtSpeeds)
    
    if fastest:
        return tandemBicycleMax(redShirtSpeeds,blueShirtSpeeds)
    else:
        return tandemBicycleMin(redShirtSpeeds, blueShirtSpeeds)

def tandemBicycleMax(redShirtSpeeds, blueShirtSpeeds):
    rInd = len(redShirtSpeeds)-1
    bInd = len(blueShirtSpeeds)-1
    total = 0

    while rInd+bInd >= len(redShirtSpeeds)-1:
        if redShirtSpeeds[rInd] > blueShirtSpeeds[bInd]:
            total += redShirtSpeeds[rInd]
            rInd -=1
        else:
            total += blueShirtSpeeds[bInd]
            bInd -= 1

    return total

def tandemBicycleMin(redShirtSpeeds, blueShirtSpeeds):
    total = 0
    for ind in range(len(redShirtSpeeds)-1,-1,-1):
        if redShirtSpeeds[ind] > blueShirtSpeeds[ind]:
            total += redShirtSpeeds[ind]
        else:
            total += blueShirtSpeeds[ind]
    return total

""" ^^ Completed successfully in 51:50 min ^^ """
""" My initial attempt to come up with the answer resulted in going in the wrong direction. Could have been managed by coming up with more examples and running my solution through """


