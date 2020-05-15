"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


from collections import deque
# from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # pass
        node = BSTNode(value)
        if value < self.value:
            if not self.left:
                self.left = node
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = node
            else:
                self.right.insert(value)     

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self
        #
        # Criteria for returning False: we know we need to go in one direction
        # but there's nothing in the left or right direction
        if target == self.value:
            return True
        if target < self.value:
            # go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # go right if right is a BSTNode
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        max_value = self.value
        if self.right:
            max_value = self.right.get_max()
        return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        # self.for_each(fn)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if not self.left and not self.right:
            print(self.value)
            return
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = deque()
        # add the root node
        queue.append(self)
        # loop so long as the stack still has elements 
        while len(queue) > 0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            print(current.value)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack() 
        # add the root node
        s.push(node)
        # loop so long as the stack still has elements 
        while s.len() > 0:
            current = s.pop()
            print(current.value)
            if current.left:
                s.push(current.left)
            if current.right:
                s.push(current.right)
            # print(current.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
