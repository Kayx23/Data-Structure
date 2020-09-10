# Program Purpose: Implement a meldable heap with meld and search methods. 

# My notes: 
# - This is my attempt using a binary tree pointer implementation.
# - If there is a space complexity requirement, opt for the array implementation.
# - The heap implemented is a min heap. 
# - heap search method has a time complexity of O(n). 

# Meld Algo (source: en.wikipedia.org/wiki/Randomized_meldable_heap):
# function Meld(Node Q1, Node Q2)
#    if Q1 is nil => return Q2
#    if Q2 is nil => return Q1
#    if Q1 > Q2 => swap Q1 and Q2
#    if coin_toss is 0 => Q1.left = Meld(Q1.left, Q2)
#    else Q1.right = Meld(Q1.right, Q2)
#    return Q1

# ==============================================================================

# for coin toss, random.randint(0,1)
import random

class Node(): 
    """The tree node in the heap."""
    def __init__(self,val): 
        self.val = val 
        self.left = None    # left child 
        self.right = None   # right child

class MeldableHeap():
    """Main structure."""
    
    def __init__(self,root): 
        """Inits a Meldable Heap with a root node."""
        self.root = Node(root)  # root is a numeric value
    
    def __meld_by_node(self,node1,node2):
        """Private recursive method."""
        
        # when one of the tree is empty, return the other one
        if node1 == None:
            return node2
        elif node2 == None:
            return node1

        # swap if the root node of first tree is greater than that of the second tree
        # would be the opposite for a max heap
        if node1.val > node2.val:
            node2, node1 = node1, node2

        # coin toss to decide how to meld
        if random.randint(0,1) == 0 :
            # recusive call down the left subtree
            node1.left = self.__meld_by_node(node1.left,node2)
        else:
            # recusive call down the right subtree
            node1.right = self.__meld_by_node(node1.right,node2)

        return node1
    
    def meld(self,MH2):
        """Returns the root node of the merged Meldable Heap.
        
        MH2 is the second heap. """
        
        node1 = self.root
        node2 = MH2.root
        self.__meld_by_node(node1,node2)
        
        # want self to be the merged tree
        if self.root.val > MH2.root.val:
            self.root=MH2.root
           
    def search(self,node,val):
        """Recursive method to search for a node and return the node.
        
        Nothing would be returned is the node is not found.
        
        Example to search node 3 in a meldable heap called MH:
        >>> search(MH.root,3)
        """

        # if empty node 
        if node == None:
            return

        # if value matched
        if node.val == val:
            return node

        # recursive call down the left subtree to find the node
        sub_node = self.search(node.left,val)
        # if the node is found
        if sub_node:
            return sub_node

        # recursive call down the right subtree to find the node
        sub_node = self.search(node.right,val)
        # if the node is found
        if sub_node:
            return sub_node
        
# ==============================================================================
# UI
print(
'''
Example:
>>> MH1 = MeldableHeap(10)
>>> MH2 = MeldableHeap(6)
>>> MH1.meld(MH2)
>>> # examine structure
>>> MH1.root.val
6
>>> MH1.root.left.val
10
>>> MH1.search(MH1.root,10)
<__main__.Node at 0x7fe2ed10c580>
>>> node_foo = MH1.search(MH1.root,10)
>>> node_foo.val
10
'''
    )
