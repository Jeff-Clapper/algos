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


# AlgoExpert: Three Number Sum (Practice re run)
def threeNumberSum(array, targetSum):
    array.sort()
    results = []

    for ind in range(len(array)-2):
        left = ind+1
        right = len(array)-1
        
        while left < right:
            if array[ind] + array[left] + array[right] == targetSum:
                results.append([array[ind],array[left],array[right]])
                if array[left+1] == left:
                    left += 1
                else:
                    right -= 1
            elif array[ind] + array[left] + array[right] < targetSum:
                left += 1
            else:
                right -= 1

    return results

""" ^^ Completed successfully in 13:00 minutes ^^ """

# AlgoExpert: BST Construction 
#Insertion and contains is working
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        runner = self
        while True:
            if value >= runner.value:
                if runner.right is not None:
                    runner = runner.right
                else:
                    runner.right = BST(value)
                    break
            else:
                if runner.left is not None:
                    runner = runner.left
                else:
                    runner.left = BST(value)
                    break
        return self

    def contains(self, value):
        runner = self
        while runner is not None:
            if value > runner.value:
                runner = runner.right
            elif value < runner.value:
                runner = runner.left
            else:
                return True
        return False

    def remove(self, value):
        toBeTrimmed = self
        previous = toBeTrimmed
        
        while toBeTrimmed is not None and toBeTrimmed.value != value:
            if value > toBeTrimmed.value:
                previous = toBeTrimmed
                toBeTrimmed = toBeTrimmed.right
            elif value < toBeTrimmed.value:
                previous = toBeTrimmed
                toBeTrimmed = toBeTrimmed.left
        
        if toBeTrimmed is None:
            return self
        
        newHead = toBeTrimmed
        while newHead.left is not None:
            newHead = newHead.left

        toBeTrimmed = toBeTrimmed.removeLowestHigh()
        newHead.left = toBeTrimmed.left
        newHead.right = toBeTrimmed.right

        if previous != toBeTrimmed:
            if value < previous.value:
                previous.left = None
            else:
                previous.right = None
        else:
            self = None

        self.insert(newHead.value)
        return self

    def removeLowestHigh(self):
        runner = self
        previous = runner
        while runner.left is not None:
            previous = runner
            runner = runner.left
        
        previous.left = None
        return self

""" ^^ Insert and Contains working, not remove ^^ """

# AlgoExpert: Linked List Construction
# This is an input class. Do not edit.
class Node:
    def __init__(self, value, prev=None):
        self.value = value
        self.prev = prev
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node,removing=False):
        if removing == True and node.prev == self.head:
            node.prev.next = None
        elif self.head and self.containsNode(node):
            if node.next:
                node.next.prev = node.prev
            if node.prev:
                node.prev.next = node.next
        
        node.prev = None
        if self.head and not removing:
            node.next = self.head
            self.head.prev = node
        self.head = node

        if not self.tail:
            runner =self.head
            while runner.next is not None:
                runner = runner.next
            self.setTail(runner)

    def setTail(self, node, removing=False):
        if removing == True and node.next == self.tail:
            node.next.prev = None
        elif self.tail and self.containsNode(node):
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
        node.next = None
        if self.tail and not removing:
            node.prev = self.tail
            self.tail.next = node
        self.tail = node
        
        if not self.head: 
            runner = self.tail
            while runner.prev is not None:
                runner = runner.prev
            self.setHead(runner)

    def insertBefore(self, node, nodeToInsert):
        if self.containsNode(nodeToInsert):
            if self.head == nodeToInsert:
                self.setHead(nodeToInsert.next)
            elif self.tail == nodeToInsert:
                self.setTail(nodeToInsert.prev)
            else:
                self.remove(nodeToInsert)

        if self.head == node:
            self.setHead(nodeToInsert)
        else:
            nodeToInsert.prev = node.prev
            nodeToInsert.prev.next = nodeToInsert
            nodeToInsert.next = node
            node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if self.containsNode(nodeToInsert):
            if self.head == nodeToInsert:
                self.setHead(nodeToInsert.next)
            elif self.tail == nodeToInsert:
                self.setTail(nodeToInsert.prev)
            else:
                self.remove(nodeToInsert)

        if node == self.tail:
            self.setTail(nodeToInsert)
        else:
            self.insertBefore(node.next)

    def insertAtPosition(self, position, nodeToInsert):
        runner = self.head
        count = 1
        while count != position and runner is not None:
            runner = self.next
            count+=1

        self.insertBefore(runner,nodeToInsert)

    def removeNodesWithValue(self, value):
        runner = self.head
        while runner is not None:
            if runner.value == value:
                if self.head == runner:
                    self.setHead(runner.next,True)
                elif self.tail == runner:
                    self.setTail(runner.prev, True)
                else: 
                    runner.prev.next = runner.next
                    runner.next.prev = runner.prev

            runner = runner.next

    def remove(self, node):
        if self.head == node:
            self.setHead(node.next, True)
        elif self.tail == node:
            self.setTail(node.prev, True)
        else: 
            node.prev.next = node.next
            node.next.prev = node.prev
        node.next =  None
        node.prev = None


    def containsNodeWithValue(self, value):
        runner = self.head
        while runner is not None:
            if runner.value == value:
                return True
            runner = runner.next
        return False

    def containsNode(self, node):
        runner = self.head
        while runner is not None:
            if runner == node:
                return True
            runner = runner.next
        return False

""" ^^ Everything is working except remove items with value ^^ """
""" ^^ This may stem from the add to head and add to tail not working. Reassessing Later ^^ """