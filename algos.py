#Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
def longestCommonPrefix(input): 
    if (type(input) != list):
        return ""
    if (len(input) < 2):
        return input[0]
    for ind in range(0,len(input)):
        if len(input[ind]) == 0:
            return ""
        input[ind] = str(input[ind])
    output = input[0][0]
    answer = ""
    while len(answer) < len(input[0]):
        for index in range(0,len(input)):
            if (input[index][0] != output[0]):
                return answer
            elif input[index][0:len(output)] != output:
                return answer
        answer = output
        output = input[0][0:len(output)+1]
    return answer

# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string. You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
def addStrings(num1, num2):
    compare = ['0','1','2','3','4','5','6','7','8','9']
    contrast =[0,1,2,3,4,5,6,7,8,9]
    final = []

    while len(num1) != len(num2):
        if len(num1) < len(num2):
            num1 = '0'+num1
        else:
            num2 = '0'+num2
    
    char = ''
    for index in range(len(num1)-1,-1,-1):
        char = char + num1[index]
    num1 = char
    char = ''

    for a in range(len(num1)):
        for i in range(len(compare)):
            if num1[a] == compare[i]:
                final.append(contrast[i]*(10**a))

    for index in range(len(num2)-1,-1,-1):
        char = char + num2[index]
    num2 = char
    char = ''

    for a in range(len(num2)):
        for i in range(len(compare)):
            if num2[a] == compare[i]:
                final.append(contrast[i]*(10**a))
    
    return str(sum(final))

#Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer. The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit. You may assume the integer does not contain any leading zero, except the number 0 itself.
def plusOne(digits):
    holder = ""
    output = []
    for digit in digits:
        holder = holder + str(digit)
    holder = str(int(holder)+1)
    for value in holder:
        output.append(int(value))
    return output

#Given a string s, find the length of the longest substring without repeating characters.
#This doesn't work yet
def lengthOfLongestSubstring(string):
    if string == "":
        return 0
    num_of_letters = 0
    word = ""
    for ind in range(0,len(string)):
        if string[ind] not in word:
            word = word+string[ind]
            if num_of_letters < len(word):
                num_of_letters = len(word)
        else:
            if num_of_letters < len(word):
                num_of_letters = len(word)
                word = string[ind]
            else: 
                word = string[ind]

    return num_of_letters
    # test = lengthOfLongestSubstring('abcabcbb')
    # print(test)
    # test = lengthOfLongestSubstring('!!ab!!cab!!c.bb')
    # print(test)
    # test = lengthOfLongestSubstring('au')
    # print(test)
    # test = lengthOfLongestSubstring(' what up butter cup ')
    # print(test)
    # test = lengthOfLongestSubstring('....')
    # print(test)
    # test = lengthOfLongestSubstring('')
    # print(test)


#Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result. It should remove all values from list a, which are present in list b keeping their order.
def array_diff(a, b):
    output = []
    for ind in range(len(a)):
        if a[ind] not in b:
            output.append(a[ind])
    return output

    #had an idea for a different method. I like this because it doesn't create another variable to take up memory and it is one less line of code
    def array_diff(a, b):
        for ind in range(len(a)-1,-1,-1):
            if a[ind] in b:
                del a[ind]
        return a

#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.
#ex: Input: nums = [-1,0,1,2,-1,-4], Output: [[-1,-1,2],[-1,0,1]]
#ex: Input: nums = [0], Output: []
#SPECIAL Note: This breaks with a ton of values
def threeSum(nums):
    output = []

    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                if (nums[i]+nums[j]+nums[k] == 0) and (sorted([nums[i],nums[j],nums[k]]) not in output):
                    output.append(sorted([nums[i],nums[j],nums[k]]))
    return output

#Given an integer numRows, return the first numRows of Pascal's triangle.
def generate(row):
    triangle = []
    for num in range(0, row):
        triangle.append(num)

    for level in triangle:
        value = [1]
        for ind in range(level):
            if len(value) < 2:
                value.append(1)
            else:
                for item in range(len(value)-1,0,-1):
                    value[item] += value[item-1]
                value.append(1)
        triangle[level] = value
    return triangle


#Given an integer array nums, handle multiple queries of the following type: Calculate the sum of the elements of nums between indices left and right inclusive where left <= right. Implement the NumArray class:
    #NumArray(int[] nums) Initializes the object with the integer array nums. int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
    #EX: ["NumArray", "sumRange", "sumRange", "sumRange"]:::::: [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]] ::::::: Output:  [null, 1, -1, -3]
class NumArray(object):

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        self.left = left
        self.right = right
        self.output = 0
        for ind in range(left,right+1):
            self.output = self.output + self.nums[ind]
        return self.output

#Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
#Notice that you may not slant the container.
#EX: input: [1,8,6,2,5,4,8,3,7], accepts 8 and 7 for an output of 49
#ex: Input: height = [4,3,2,1,4], accepts 4 and 4 for an output of 16
#ex: input: gheight = [1,2,1], accepts just 2, for an output of 2
#ex: input: height = [1,1], accepts 1 and 1, for an output of 1

#I didn't solve the right problem
def maxArea(height):
    ai = 0
    bi = len(height)-1
    comp = (ai,bi,0)
    
    while ai <= bi:
        sum = 0
        for ind in range(ai,bi+1):
            if (height[ind] <= height[ai]) and (height[ind] <= height[bi]): 
                sum += height[ind]
        if sum >= comp[2]:
            comp = (ai,bi,sum)
        if height[comp[0]] < height[bi]:
            ai += 1
            while (height[ai] < height[comp[0]]) and (ai <= bi): 
                ai += 1
        else:
            bi -=1
            while (height[bi] <= height[comp[1]]) and (ai <= bi): 
                bi -= 1

    if comp[0] == comp[1]:
        print(comp)
        return height[comp[0]]
    else:
        print(comp)
        return height[min(height[comp[0]],height[comp[1]])]**2

#Lets try this again: The question is saying that it wants the max volume of possible using the smaller of the two indexes multiplied by the amount of points between them
#SO: example one is correct becasue 8 and 7 are 7 paces away, so 7 x 7 is 49. you cant use 8 because 8 and 8 are only 5 paces away and 8*5 is only 40
#Ex: The last example 1,2,1 is two because the length between 1 and 1 is 2, so 2x1=2
def maxArea(height):
    a = 0
    b = len(height)-1
    output = (0,0,0)

    while a <= b:
        x = b - a
        y = min(height[a],height[b])
        if output[0] < x*y:
            output = (x*y,x,y)
        while (y >= min(height[a],height[b])) and (a <= b):
            if height[b] <= height[a]:
                b -=1
            else:
                a += 1
    return output[0]

#Given an integer, convert it to a roman numeral.
def intToRoman(num):
    romans = {1:'I',4:'IV', 5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
    keys = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman_number = ''

    index = len(keys)-1
    while num > 0:
        if num < keys[index]:
            index -= 1
        else:
            roman_number += romans[keys[index]]
            num -= keys[index]

    return roman_number

#You are given two non0empty linked lists representing two non-neg ints. The digits are stored in reverse order, and each of their nodes contains a singledigit. Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zeros, except 0 itself.
# EX:2-4-6,5-6-4 --> 7-0-8: ie: 246+564=708
class ListNode(object): 
    def __init__(self, val=0,next=None):
        self.val=val
        self.next=next

class SLL(object):
    def __init__(self, head=None):
        self.head = head
        self.runner = None

def addTwoNumbers(l1, l2):
    sll_1 = SLL(l1)
    sll_2 = SLL(l2)
    sll_1.runner = sll_1.head
    sll_2.runner = sll_2.head

    new_val = add_nodes(sll_1.head.val, sll_2.head.val)
    sll_3 = SLL(ListNode(new_val[0]))
    sll_3.runner = sll_3.head
    
    while (sll_1.runner.next != None) and (sll_2.runner.next != None):
        sll_1.runner = sll_1.runner.next
        sll_2.runner = sll_2.runner.next
        new_val = add_nodes(sll_1.runner.val, sll_2.runner.val, new_val[1])
        sll_3.runner.next = (ListNode(new_val[0]))
        sll_3.runner = sll_3.runner.next
    
    if sll_1.runner.next != None:
        new_val = add_rest(sll_1,sll_3,new_val[1])
        sll_3 = new_val[0]
    
    elif sll_2.runner.next != None:
        new_val = add_rest(sll_2,sll_3,new_val[1])
        sll_3 = new_val[0]
    
    if new_val[1] == 1:
        sll_3.runner.next = ListNode(1)
    return sll_3.head

def add_nodes(val1,val2, carrier=0):
    new_val = val1 + val2 + carrier
    carrier = 0
    if new_val > 9:
        carrier = 1
        new_val -= 10
    return [new_val,carrier]

def add_rest(sll,sll_3,carrier):
    while sll.runner.next != None:
        sll.runner = sll.runner.next
        results = add_nodes(0, sll.runner.val, carrier)
        sll_3.runner.next = (ListNode(results[0]))
        sll_3.runner = sll_3.runner.next
        carrier = results[1]
    return [sll_3,carrier]

def get_nodes(sll):
    nodes = []
    runner = sll.head
    nodes.append(runner.val)
    while runner.next != None:
        runner = runner.next
        nodes.append(runner.val)
    return nodes

def print_nodes(sll):
    runner = sll.head
    print(runner.val)
    while runner.next != None:
        runner = runner.next
        print(runner.val)

#more efficient result here


#next one here