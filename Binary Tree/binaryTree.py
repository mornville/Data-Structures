class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_traversal(tree.root, "")
        elif traversal_type =="inorder":
            return self.inorder_traversal(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_traversal(tree.root, "")
        else:
            return None

    ## Preorder - Root Left Right
    def preorder_traversal(self, start, traversal):
        if start:
            traversal+= (str(start.value) + '-')
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    ## Inorder - Left Root Right
    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal+= (str(start.value) + '-')
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    ## PostOrder - Left Right Root
    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal+= (str(start.value) + '-')
        return traversal

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)



     

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))