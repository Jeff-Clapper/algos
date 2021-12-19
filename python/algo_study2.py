# Leetcode 307: A study of Tree Nodes
class Node(object):
    def __init__(self,start,end,total,left=None,right=None):
        self.start = start
        self.end = end
        self.total = total
        self.left = left
        self.right = right

class NumArray(object):
    def __init__(self, nums):
        def create_tree(left,right, nums):
            if left == right:
                return Node(left,right,nums[left])
            start = left
            end = right
            mid = left + (right-left)//2
            left = create_tree(left,mid,nums[left:mid+1])
            right = create_tree(mid+1,right,nums[mid:right+1])

            root = Node(start,end,left.total+right.total,left,right)
            return root
        self.root = create_tree(0,len(nums)-1,nums)

    
    def update(self, index: int, val: int) -> None:
        def update_tree_node(index,val,root):
            if root.start == root.end == index:
                root.total = val
                return
            mid = root.left + (root.right - root.left)//2
            if index <= mid:
                update_tree_node(index,val,root.left)
            else:
                update_tree_node(index,val,root.right)
            root.total = root.right.total + root.left.total

        update_tree_node(index,val,self.root)

    def sumRange(self, left: int, right: int) -> int:
        def sum_tree_range(left,right,root):
            if left == root.start and right == root.end:
                return root.total
            mid = root.left + (root.right-root.left)//2

            if right <= mid:
                return sum_tree_range(left,right,root.left)
            elif left > mid:
                return sum_tree_range(left,right,root.right)
            else:
                return sum_tree_range(left,mid,root.left) + sum_tree_range(mid+1,right,root.right)

        return sum_tree_range(left,right,self.root)


