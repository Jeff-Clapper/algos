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

#Remove this node creator for a significant jump in faster than percentage (already in their program, I must define it to work in mine)
#better speed same mem usage
class ListNode(object): 
    def __init__(self, val=0,next=None):
        self.val=val
        self.next=next

def addTwoNumbers(l1, l2):
    l1_results = read_node(l1)
    l1_number = convert_list(l1_results)
    l2_results = read_node(l2)
    l2_number = convert_list(l2_results)
    l3 = l1_number + l2_number
    return convert_number_to_node(str(l3))

def read_node(node):
    results = []
    results.append(node.val)
    while node.next != None:
        node = node.next
        results.append(node.val)
    return results

def convert_list(array):
    x = len(array)-1
    number = ""
    while x >= 0:
        number += str(array[x])
        x -=1
    return int(number)

def convert_number_to_node(number):
    for x in range(0,len(number)):
        if x == 0:
            node = ListNode(number[x])
        else:
            node = ListNode(number[x],node)
    return node

#better mem, worse speed than prev but fater than original
def addTwoNumbers(l1, l2):
    results = []
    results.append(l1.val)
    while l1.next != None:
        l1 = l1.next
        results.append(l1.val)
    
    x = len(results)-1
    number1 = ""
    while x >= 0:
        number1 += str(results[x])
        x -=1

    results = []
    results.append(l2.val)
    while l2.next != None:
        l2 = l2.next
        results.append(l2.val)

    x = len(results)-1
    number2 = ""
    while x >= 0:
        number2 += str(results[x])
        x -=1
    
    l3 = int(number1) + int(number2)
    l3 = str(l3)
    for x in range(0,len(l3),1):
        if x == 0:
            node = ListNode(l3[x])
        else:
            node = ListNode(l3[x],node)
    return node

# Given a string s, find the length of the longest substring without repeating characters
def lengthOfLongestSubstring(inp: str) -> int:
    longestLength = 0
    if len(inp) < 1:
        return longestLength
    for index in range(len(inp)):
        if len(range(index,len(inp))) < longestLength:
            break
        longestLengthFromPoint = assessString(inp,index)
        if longestLengthFromPoint > longestLength:
            longestLength = longestLengthFromPoint
    return longestLength
        

def assessString(inp,index):
    run = ""
    val = inp[index]
    
    while val not in run:
        run += inp[index]
        index+=1
        if index == len(inp):
            break
        
        val = inp[index]
    return len(run)

#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n))
def findMedianSortedArrays(nums1, nums2) -> float:
    #Gets the Index of the median value
    median_index = (len(nums1)+len(nums2)-1)/2
    if median_index%1 == 0:
        results = get_median(nums1,nums2,int(median_index)) 
        return float(results[-1])
    else:
        median_index += .5 
        results = get_median(nums1,nums2,int(median_index)) 
        result = (results[-1]+results[-2])/2
        return float(result)

    
def get_median(nums1, nums2, index):
    #creates an array from beginning to 
    values = []
    count1 = 0
    count2 = 0
    for ind in range(index+1):
        if count1 == len(nums1):
            values.append(nums2[count2])
            count2 += 1
        elif count2 == len(nums2):
            values.append(nums1[count1])
            count1 += 1
        elif nums1[count1] <= nums2[count2]:
            values.append(nums1[count1])
            count1 +=1
        else:
            values.append(nums2[count2])
            count2 += 1
    print(values)
    return values


# Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap. Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".
#LEETCODE num-1044
# Too Slow
def longestDupSubstring(s):
    combinations = []
    longest_dup = ""

    for ind in range(len(s)):
        test = ""
        for combos in range(ind,len(s)):
            test = test + (s[combos])
            if test in combinations:
                if len(test) > len(longest_dup):
                    longest_dup = test
            else:
                combinations.append(test)
    return longest_dup


# also too slow
def longestDupSubstring(s):
    longest = ""
    for ind in range(len(s)):
        results = isInString(s,ind,ind+1)
        if len(results) > len(longest):
            longest = results
    return longest


def isInString(s,index,index_range,char=""):
    char = char
    while index_range <= len(s):
        if (s[index:index_range] in s[index+1:len(s)]):
            char = isInString(s,index,index_range+1,s[index:index_range])
        return char

#Someone elses answer:
#Very similar to mine, except uses while instead of recursion and very vew variables/functions
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        ans = ''
        j   = 1
        for i in range(len(s)):
            longest = s[i:i+j]
            temp    = s[i+1:]
            while longest in temp:
                ans = longest
                j += 1
                longest = s[i:i+j]
        return ans

# 404. Sum of Left Leaves: Given the root of a binary tree, return the sum of all left leaves.
    #Faster than 98.39%, memory usage less than 48.54%
def sumOfLeftLeaves(root):
    total = 0
    if root.left:
        total += go_left(root.left)
    if root.right:
        total += go_right(root.right)
    return total

def go_left(node,total=0):
    if not node.left and not node.right:
        total += node.val
    if node.left:
        total += go_left(node.left)
    if node.right:
        total += go_right(node.right)
    return total

def go_right(node,total=0):
    if node.left:
        total += go_left(node.left)
    if node.right:
        total += go_right(node.right)
    return total

# 260. Single Number III: Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order. You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
def singleNumber(arr):
    results = []
    while len(results) < 2:
        val = arr.pop(0)
        if val in arr:
            arr.append(val)
        else:
            results.append(val)
    return results

#43. Multiply Strings: Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string. Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
def multiply(num1: str, num2: str) -> str:
    num1 = convert_string(num1)*convert_string(num2)
    return f'{num1}'

def convert_string(num: str) -> int:
    nums = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
    count, val = len(num)-1, 0
    
    for digit in num:
        val += nums[digit] * (10**count)
        count -= 1
    
    return val

#AFTER READING DISCUSSIONS FOR 43, I am have misunderstood what "directly convert string" meant, so here is a second go at it (less fast but better memory usage)
def multiply(num1: str, num2: str) -> str:
    val = 0
    count2 = len(num2)-1
    for digit in num2:
        count1 = len(num1)-1
        digit = int(digit)*(10**count2)
        for number in num1:
            val += (int(number)*(10**count1))*digit
            count1 -= 1
        count2-=1
    return f'{val}'

"""122. Best Time to Buy and Sell Stock II: You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve."""
def maxProfit(arr):
    total = 0
    for ind in range(len(arr)-1):
        if arr[ind] < arr[ind+1]:
            total += arr[ind+1]-arr[ind]
    return total
