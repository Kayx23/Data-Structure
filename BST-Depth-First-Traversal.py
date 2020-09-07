# Program Purpose: Implement the following depth first search (DFS) methods for a binary search tree. 
# - preorderNext(x): return the value of the node visited after node x in a preorder traversal.
# - postorderNext(x): return the value of the node visited after node x in a postorder traversal.
# - inorderNext(x): return the value of the node visited after node x in a inorder traversal.

# My notes:
# - Time complexity is O(n) for all three methods (taken into account of the complexities of interacting with the list)
# - The tree traversal is completed before checking if the value x is in the tree or not. A more efficient apporach is to
#   stop the search once the value x is located. In my implementation, I wanted to keep the methods in Node class clean so
#   I can recursively call on them, while writing the post-traversal checks in the BST class. I acknowledge this isn't the
#   most efficient implementation.

# Tutorial Referenced for traversal: 
# Python: Binary Search Tree - BST: https://youtu.be/YlgPi75hIBc


class Node: 
    """A Node class for the tree nodes."""
        
    def __init__(self,val): 
        """Inits an instance of a Node with a node value and two empty pointers to the left and right child. 
        
        Args:
          val:
            The value of the node.    
        """
        self.val = val      # node value
        self.left = None    # left child 
        self.right = None   # right child 
        
    def insert(self,val):
        """Inserts a value val to the tree by fixing node pointers, if there isn't a duplicate in the tree. 
        
        This is a recursive method called in the BST class to insert a node; the implementation maintains 
        the BST invariants. 
        
        Args:
          val:
            The value to be added to the tree. 
        """
           
        # if the current node value is the same as val
        if self.val == val:  
            # do not insert
            return None
        # if the current node value is less than val
        elif self.val > val: 
            # if there is a left child
            if self.left:
                # recursively call to try to insert somewhere in the left sub-tree
                self.left.insert(val)
            # if the left child is empty
            else:
                # create a new node with the value val to be the left child 
                self.left = Node(val)
        # if the current node value is greater than val
        else: 
            # if there is a right child
            if self.right:
                # recursively call to try to insert somewhere in the right sub-tree
                self.right.insert(val)
            # if the right child is empty
            else:
                # create a new node with the value val to be the right child 
                self.right = Node(val) 
    
    
    def inorder(self,lst):  
        """This is a recursive method called in the BST class for inorder traversal.
        
        Args:
          lst:
            A list to where the value traversed would be added to. 
        """
        
        # if there is a left child
        if self.left:
            # recursively call down the left sub-tree
            self.left.inorder(lst)
        # append the node value to a list
        lst.append(self.val)
        # if there is a right child
        if self.right:
            # recursively call down the right sub-tree
            self.right.inorder(lst)
        # return the list of values traversed
        return lst
    
    def preorder(self,lst):
        """This is a recursive method called in the BST class for preorder traversal.
        
        Args:
          lst:
            A list to where the value traversed would be added to. 
        """
        # append the node value to a list
        lst.append(self.val)
        # if there is a left child
        if self.left:
            # recursively call down the left sub-tree
            self.left.preorder(lst)
        # if there is a right child
        if self.right:
            # recursively call down the right sub-tree
            self.right.preorder(lst)
        # return the list of values traversed
        return lst
    
    def postorder(self,lst):
        """This is a recursive method called in the BST class for postorder traversal.
        
        Args:
          lst:
            A list to where the value traversed would be added to. 
        """
        # if there is a left child
        if self.left:
            # recursively call down the left sub-tree
            self.left.postorder(lst)
        # if there is a right child   
        if self.right:
            # recursively call down the right sub-tree
            self.right.postorder(lst)
        # append the node value to a list
        lst.append(self.val)
        # return the list of values traversed
        return lst
    
    
class BST:
    """A BST class to create a binary search tree with no duplicate values. 
    
    The class depends on the Node class for tree nodes.
    """
    
    def __init__(self): 
        """Inits an empty tree."""
        self.root = None   # root node empty
    
    def insert(self,val):
        """Inserts a value val to the tree while maintaining BST invariants. 
        
        Args:
          val:
            The value to be added to the tree. 
        """
        # if the root node is not empty
        if self.root:
            # reversive call on the root node to find the position
            # for insersion to maintain BST invariants
            self.root.insert(val)
        # if the root node is empty
        else:
            # let val be the root node value
            self.root = Node(val)

    def inorderNext(self,x): 
        """Return the node value visited after node x in a inorder traversal of the tree.
        
        Args:
          x:
            The node value after which the method returns of value of. 
        """
        # an empty list used to keep all the node values traversed
        tree = []
        # call inorder method on the tree root node to populate the tree list
        tree = self.root.inorder(tree) 
        # if the value x is not in the tree node values
        if x not in tree:
            print("Error: The node value entered does not exist in the tree!")
        # if the value x is found and it is not the last node visited
        elif tree.index(x)+1 <= len(tree)-1:
            # return the next node value after node x
            return tree[tree.index(x)+1]
        # if the value x is found but it is the last node visited
        else:
            print("No next node: this is already the last node visited!")
    
    def preorderNext(self,x): 
        """Return the node value visited after node x in a preorder traversal of the tree.
        
        Args:
          x:
            The node value after which the method returns of value of. 
        """
        # an empty list used to keep all the node values traversed
        tree = []
        # call preorder method on the tree root node to populate the tree list
        tree = self.root.preorder(tree) 
        # if the value x is not in the tree node values
        if x not in tree:
            print("Error: The node value entered does not exist in the tree!")
        # if the value x is found and it is not the last node visited
        elif tree.index(x)+1 <= len(tree)-1: 
            # return the next node value after node x
            return tree[tree.index(x)+1]
        # if the value x is found but it is the last node visited
        else:
            print("No next node: this is already the last node visited!")

    def postorderNext(self,x): 
        """Return the node value visited after node x in a postorder traversal of the tree.
        
        Args:
          x:
            The node value after which the method returns of value of. 
        """
        # an empty list used to keep all the node values traversed
        tree = []
        # call preorder method on the tree root node to populate the tree list
        tree = self.root.postorder(tree)  
        # if the value x is not in the tree node values
        if x not in tree:
            print("Error: The node value entered does not exist in the tree!")
        # if the value x is found and it is not the last node visited
        elif tree.index(x)+1 <= len(tree)-1:
            # return the next node value after node x
            return tree[tree.index(x)+1]
        # if the value x is found but it is the last node visited
        else:
            print("No next node: this is already the last node visited!")

# -------------------------------------------------------------------------------------------
# UI
print(
'''
Example: 
>>> BST = BST()
>>> for i in [20,18,14,19,27,30,24]:
	BST.insert(i)
>>> BST.inorderNext(14)
18
>>> BST.inorderNext(30)
No next node: this is already the last node visited!
>>> BST.inorderNext(27)
30
>>> BST.inorderNext(133)
Error: The node value entered does not exist in the tree!
>>> BST.preorderNext(27)
24
>>> BST.postorderNext(27)
20
'''
    )
