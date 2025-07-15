import pickle


class TreeNode:

    def __init__ (self, value):
        self.left = None
        self.right = None
        self.value = value


    def insert(self, key):

        if key<self.value:

            if self.left is None:
                self.left=TreeNode(key)

            else:
                self.left.insert(key)

        elif key>self.value:

            if self.right is None:
                self.right=TreeNode(key)

            else:
                self.right.insert(key)


    def find(self, key):

        if key<self.value:

            if self.left is None:
                return False
            else:
                return self.left.find(key)
        elif key>self.value:

            if self.right is None:
                return False
            else:
                return self.right.find(key)
        else:
            return True

    def preorder_traversal(self):

        print(self.value)

        if self.left:
            self.left.preorder_traversal()

        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):

        if self.left:
            self.left.postorder_traversal()

        if self.right:
            self.right.postorder_traversal()

        print(self.value)

    def inorder_traversal(self):

        if self.left:
            self.left.inorder_traversal()

        print (self.value)

        if self.right:
            self.right.inorder_traversal()


if __name__=='__main__':

    Tree = TreeNode(10)

    Tree.insert(5)
    Tree.insert(3)
    Tree.insert(4)
    # Tree.insert("14")
    # Tree.insert("15")
    # Tree.insert("17")
    # Tree.insert("18")
    # Tree.insert("20")
    # Tree.insert("25")
    Tree.insert(11)
    Tree.insert(12)
    Tree.insert(13)

    print("\npre order_traversal : ")
    Tree.preorder_traversal()
    print("\nin order_traversal : ")
    Tree.inorder_traversal()
    print("\npost order_traversal : ")
    Tree.postorder_traversal()




