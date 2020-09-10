# Program Purpose: Implement a meldable heap with meld and remove(x) methods. 

# My notes: 
# - a binary tree pointer implementation of the min heap
# - unable to use array implementation due to the nature of the meldable heap
# - remove(x) method has a time complexity is O(n) due to the research down the tree

# Algorithm: 

# function Meld(Node Q1, Node Q2)
#    if Q1 is nil => return Q2
#    if Q2 is nil => return Q1
#    if Q1 > Q2 => swap Q1 and Q2
#    if coin_toss is 0 => Q1.left = Meld(Q1.left, Q2)
#    else Q1.right = Meld(Q1.right, Q2)
#    return Q1
# 
# source: en.wikipedia.org/wiki/Randomized_meldable_heap

# function Remove()
#    fix parent pointers
#    root = Meld(root.left, root.right)

# ==============================================================================

# for coin toss, random.randint(0,1)
import random

class Node(): 
    def __init__(self,val=None): 
        self.val = val 
        self.parent = None
        self.left = None
        self.right = None

class MeldableHeap():
    
    def __init__(self,root): 
        """Inits a Meldable Heap with a root node."""
        self.root = Node(root)  # root is a numeric value
    
    def __meld_by_node(self,node1,node2):
        """private method"""
        if node1 == None:
            return node2
        elif node2 == None:
            return node1

        # swap
        if node1.val > node2.val:
            node2, node1 = node1, node2

        # coin toss
        if random.randint(0,1) == 0 :
            node1.left = self.__meld_by_node(node1.left,node2)
            node1.left.parent = node1
        else:
            node1.right = self.__meld_by_node(node1.right,node2)
            node1.right.parent = node1

        return node1
    
    def meld(self,MH2):
        """Returns the root node of the merged Meldable Heap."""
        
        node1 = self.root
        node2 = MH2.root
        self.__meld_by_node(node1,node2)
        
        # we want self to be the merged tree
        if self.root.val > MH2.root.val:
            self.root=MH2.root
        
    def __search(self,node,val):

        # if empty node 
        if node == None:
            return

        # if value matched
        if node.val == val:
            return node

        # recursive call down the left subtree to find the node
        sub_node = self.__search(node.left,val)
        # if the node is found
        if sub_node:
            return sub_node

        # recursive call down the right subtree to find the node
        sub_node = self.__search(node.right,val)
        # if the node is found
        if sub_node:
            return sub_node
        
    def __update_ptr_child_parent(self,node_remove,meld_root):
        """update child node pointer to the parent during removal.
        
        meld_root is replacing node_remove.
        """
        # fix child pointer to the parent 
        meld_root.parent = node_remove.parent
        
        if node_remove.parent is None:   
            # if node_remove is the tree root, reset tree root node
            self.root = meld_root
        else:
            # fix parent pointer
            if node_remove.parent.left:
                if node_remove.parent.left.val == node_remove.val:
                    node_remove.parent.left = meld_root
            else:
                node_remove.parent.right = meld_root
        
    def remove(self,val):
        
        # find the node we want to remove
        node_remove = self.__search(self.root,val)
        
        # if the node is found
        if node_remove:
            # meld the left and right subtrees
            node1 = node_remove.left
            node2 = node_remove.right
            
            # if at least one of the subtrees is non-empty
            if node1 or node2:
                self.__meld_by_node(node1,node2)

                # set node_remove
                # case 1 - if both subtrees are not empty
                if node1 and node2:
                    if node1.val < node2.val:
                        # update pointer 
                        self.__update_ptr_child_parent(node_remove,node1)
                    
                    # > or ==
                    else:
                        self.__update_ptr_child_parent(node_remove,node2)
                        
                # case 2 - one of the subtrees empty
                elif node1 or node2:
                    if node1:
                        # update pointer 
                        self.__update_ptr_child_parent(node_remove,node1)
                    else:
                        # update pointer 
                        self.__update_ptr_child_parent(node_remove,node2) 
            
            # both subtrees are empty      
            else:
                # remove by fixing parent pointer
                if node_remove.parent.left:
                    if node_remove.parent.left.val == node_remove.val:
                        node_remove.parent.left = None
                else:
                    node_remove.parent.right = None

        # if the node is not found
        else:
            print(val,"is not in the heap!")
            
# ==============================================================================
# to visulize the tree (for debug purpose)
# use the code from https://www.geeksforgeeks.org/print-binary-tree-2-dimensions/

def print2DUtil(root, space) : 
  
    # Base case  
    if (root == None) : 
        return
  
    # Increase distance between levels  
    space += COUNT[0] 
  
    # Process right child first  
    print2DUtil(root.right, space)  
  
    # Print current node after space  
    # count  
    print()  
    for i in range(COUNT[0], space): 
        print(end = " ")  
    print(root.val)  
  
    # Process left child  
    print2DUtil(root.left, space) 
    
# Wrapper over print2DUtil()  
def print2D(root) : 
      
    # space=[0] 
    # Pass initial space count as 0  
    print2DUtil(root, 0)
# ==============================================================================
# driver 
print(
'''
Example:
>>> MH1 = MeldableHeap(10)
>>> for i in [6,30,50,2,3,5,4]:
        MH1.meld(MeldableHeap(i))

>>> # see the tree
>>> COUNT = [10]  # parameter for spacing between each tree levels
>>> print2D(MH1.root) 

>>> MH1.remove(6)
>>> print2D(MH1.root) 
    
'''
    )




