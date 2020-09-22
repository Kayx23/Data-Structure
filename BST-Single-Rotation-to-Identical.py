# Program Purpose: Implement an algorithm that transforms any BST, T1, into another BST, T2, via single rotation. 
# The program ask for user input to construct Tree A; it then constructs Tree B using all values in Tree A in shuffled order.
# Single rotation is performed on Tree A nodes when needed to transform Tree A to Tree B. 

# import random.shuffle for shuffling values in Tree A
from random import shuffle 

class Node(): 
    """A Node class for the tree nodes.
    
    The class is called in class BST and is not to be called on its own. 
    """
        
    def __init__(self, val): 
        """Inits an instance of a Node with a node value and two empty pointers to the left and right child. 
        
        Args:
          val:
            The value of the node.    
        """
        self.val = val 
        self.parent = None   # parent node 
        self.left = None     # left child 
        self.right = None    # right child 
    
    def insert(self,val):
        """Inserts a value val to the tree by fixing node pointers, if there isn't a duplicate in the tree. 
        
        This is a recursive method called in the BST class to insert a node; the implementation maintains 
        the BST invariants. 
        
        Args:a
          val:
            The value to be added to the tree. 
        """
        
        # if value already exists in the tree, do not insert
        if self.val == val:  
            return None
        
        # if the node value is greater than inserted value
        elif self.val > val: 
            # if left child node exists
            if self.left:
                # traverse down the left subtree to find an insertion point
                self.left.insert(val) 
            # if left child node does not
            else:
                # add a left child node using val
                self.left = Node(val) 
                # set parent pointer
                self.left.parent = self  
                
        # if the node value is less than inserted value
        else: 
            # if right child node exists
            if self.right:
                # traverse down the right subtree to find an insertion point
                self.right.insert(val) 
            # if right child node does not
            else:
                # add a right child node using val
                self.right = Node(val)
                # set parent pointer
                self.right.parent = self 

    def inorder_to_list(self,lst):  
        """Return a list of all values traversed using inorder traversal."""
        
        # if left child node exists
        if self.left:
            # recersive call down the left subtree
            self.left.inorder_to_list(lst)
        lst.append(self.val)  # append node values to the list
        
        # if right child node exists
        if self.right:
            # recersive call down the right subtree
            self.right.inorder_to_list(lst)
        
        return lst

class BST():
    """A BST class that enables binary search tree construction, insertion, left and right rotation on a tree node.
    
    The class depends on the Node class for tree nodes.
    """
    
    def __init__(self):
        """Inits an empty tree."""
        self.root = None
    
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
    
    def TreeNodes_inorder(self): 
        """Return a list of all values traversed using inorder traversal."""
        
        # if empty tree
        if self.root is None: 
            print("The tree is empty!")
        # if non-empty tree
        else:
            # create an empty list
            tree = []
            # populate the list with node values traversed
            tree = self.root.inorder_to_list(tree)
            return tree
        
    def LeftRotate(self,x): 
        """Left rotates on node x, supposing y is the right child of x."""
        
        print("Left rotating on node",x.val)

        # let y be the right child of x
        y = x.right 
        # record the left child of y for later pointer fixing
        y_left_child = y.left
        # record the parent of x
        topParent = x.parent

        # perform rotation
        y.left = x 
        y.left.parent = y
        y.parent = topParent
        x.right = y_left_child  
        # note that y_left_child could be None in the last step
        # if not none, update x.right parent pointer
        if x.right != None: x.right.parent = x

        # if y is not the root of the tree
        # update the child pointer for the new parent node
        if y.parent != None:  
            if y.parent.left==x:
                y.parent.left=y
            else:
                y.parent.right=y
        # if y is the root of the tree
        else:
            # update tree root node pointer
            self.root=y


    def RightRotate(self,x): 
        """Right rotates on node x, supposing y is the left child of x."""
        
        print("Right rotating on node",x.val)

        # let y be the left child of x
        y = x.left 
        # record the right child of y for later pointer fixing
        y_right_child = y.right 
        # record the parent of x
        topParent = x.parent

        # perform rotation
        y.right = x
        y.right.parent = y
        y.parent = topParent
        x.left = y_right_child 
        # note that y_right_child could be None in the last step
        # if not none, update x.left parent pointer
        if x.left != None: x.left.parent = x

        # if y is not the root of the tree
        # update the child pointer for the new parent node
        if y.parent != None: 
            if y.parent.left==x:
                y.parent.left=y
            else:
                y.parent.right=y
        # if y is the root of the tree
        else:
            # update tree root node pointer
            self.root=y
            
def BSTsearch(root,val):
    """Searches for node of value - val - in the given BST. If found, return the node object. 
    
    This recursive function is used in function rotate_tree() to locate a node."""

    # if empty tree or at the end of the tree
    if root is None:
        # return nothing
        return

    # if root value matches with the value we're looking for
    elif root.val == val: 
        # return the node object
        return root  

    # if root value is less than the value we're looking for
    elif root.val < val: 
        # search left subtree
        return BSTsearch(root.right,val) 

    # if root value is greater than the value we're looking for
    else: 
        # search right subtree
        return BSTsearch(root.left,val) 

def rotate_tree(Tree1_root,Tree2_root):
    """Transforms binary search tree, Tree 1 into Tree 2, by performing single rotation. """
    
    # exit function if the current root node in Tree B is at NIL node
    if Tree2_root is None:
        return
    
    # if the root nodes don't match
    if (Tree1_root is None or Tree1_root.val != Tree2_root.val): 
        
        # find the node in Tree 1 that has the current root value of Tree 2 
        Tree1_node = BSTsearch(root=TreeA.root,val=Tree2_root.val)

        # To rotate this node to the root of Tree 1 (in other words, 
        #    same position as in Tree 2):
        # -  First, figure out if this node is a left or right child node
        # -  if it's a left child node, then call right rotation on the parent node
        # -  if it's a right child node, then call left rotation on the parent node
        # until the node is a root node
        
        # while the Tree1_node is not in the same position as node of the same 
        # value in Tree 2, continue to perform rotation
        
        # a node is in the right position if the value of which matches up with the value of the same node in the other tree
        # so while the parent node values do not match up for the same node in two tree
        while Tree1_node.parent != Tree2_root.parent:
            # if both parent nodes are not None
            if  Tree1_node.parent != None and Tree2_root.parent!=None:
                # if parent node values match, exit while loop
                if (Tree1_node.parent.val == Tree2_root.parent.val) and \
                (Tree1_node.val == Tree2_root.val):
                    Tree1_root = Tree1_node
                    break

            # if one of the parent nodes is None
            # if the parent's left child is not empty, and right child is empty
            if Tree1_node.parent.left != None: 
                # check if the node is the left child node by comparing value
                if Tree1_node.parent.left.val == Tree1_node.val:
                    # call right rotation on the parent node
                    TreeA.RightRotate(Tree1_node.parent)
                else: 
                    # call left rotation on the parent node
                    TreeA.LeftRotate(Tree1_node.parent)
            # if the parent's right child is not empty, and left child is empty
            else: 
                # call left rotation on the parent node
                TreeA.LeftRotate(Tree1_node.parent)
    
    # recursivelly call itself for the left and right subtrees of the current node
    rotate_tree(Tree1_root.left,Tree2_root.left)
    rotate_tree(Tree1_root.right,Tree2_root.right)
    
def isIdentical(x, y):
    """Returns a Boolean value indicating whether the two BST trees are identical.
    
    x and y should be the root node of the tree.
    
    Example: 
    >>> isIdentical(TreeA.root,TreeB.root)
    True
    
    Algorithm referenced:
    https://www.techiedelight.com/check-if-two-binary-trees-are-identical-not-iterative-recursive/
    """
    
    # if both tree are empty 
    if x is None and y is None:
        return True
    # if both trees are non-empty
    else: 
        # compares the value of x and y, as well as the child nodes through recursive calls
        return (x and y) and (x.val == y.val) and \
        isIdentical(x.left, y.left) and isIdentical(x.right, y.right)

def main():
    """drive code"""
    
    # initiate an empty tree, Tree A
    global TreeA 
    TreeA = BST()

    # ask for user input for tree node values
    userInput = None

    # while the user does not finish inputing values
    while userInput != "q": 
        # show message on the console to ask for user input
        userInput = input("Enter a numeric value to be added to the Binary Search Tree A (enter \"q\" to quit): ") 
        # If "q" is entered, exit the program
        if userInput == "q":
            break
        # If "q" is not entered
        else:
            # make sure user input is a numeric value; if not, try again
            try:
                userInput = int(userInput)
            except ValueError:
                print("Value entered is not an integer. Please try again.\n")
                continue
            # if userInput is numeric, add a node to Tree A, unless the value is already in the tree
            TreeA.insert(userInput)
            print(userInput," is added to Tree A (if not already exists in the tree).\n")

    # Now the user has hit "q" to finish adding nodes to Tree A
    # Inorder traverse Tree A, save all nodes to a list, shuffle the list, and construct a Tree B using the list
    # This is to make sure both trees have the same values but of different shape

    # inorder traverse Tree A and return all values in a list
    TreeNodes = TreeA.TreeNodes_inorder()

    # if the tree is non-empty
    if TreeNodes is not None:
        # let user know what nodes are available to be added to Tree B
        print("Tree A has nodes: ",TreeNodes,"based on an inorder tree traversal")
    # if the tree is non-empty
    else:
        # break out of the program
        raise Exception("Tree A needs to have at least one node to proceed!")

    # initiate an empty tree, Tree B
    global TreeB 
    TreeB = BST()

    # shuffle tree node value order from Tree A
    shuffle(TreeNodes)

    # add the values to Tree B in the shuffled order
    for i in range(len(TreeNodes)): 
        TreeB.insert(TreeNodes[i])

    # let user know the shuffled list order that was used to constrcut Tree B
    print("A Binary Search Tree B is created with the same values from tree A, but with a shuffled order of inputs: ",
          TreeNodes, ", resulting in a binary search tree of different shape than Tree A.")
    
    # let the user know how to rotate and check if tree are identical
    print(
    '''

    Now, you have TreeA and TreeB in the global environment. 
    
    To rotate TreeA to TreeB, you can run:
    >>> rotate_tree(TreeA.root,TreeB.root)

    To check if the two tree are identical, you can run:
    >>> isIdentical(TreeA.root,TreeB.root)
    True
    
    If you wish to manually check node values, you can run: 
    >>> TreeA.root.val
    >>> TreeA.root.right.val
    >>> TreeA.root.left.val
    >>> TreeB.root.val
    etc. as long as the root is not NIL. 
    
    However, if the node is a NIL node, you will see an error like the following:
        Traceback (most recent call last):
        File "<pyshell#17>", line 1, in <module>
        TreeA.root.right.right.val
        AttributeError: 'NoneType' object has no attribute 'val'
    '''
    )
    
# ========= UI ===========

print(
'''
To initiate the program, run: 
>>> main()
''')
