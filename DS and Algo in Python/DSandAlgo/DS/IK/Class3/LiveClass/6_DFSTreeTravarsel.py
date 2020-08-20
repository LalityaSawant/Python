class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    # Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def dfs(self, root):
        if root is None:
            return

        def helper(node):
            #base case
            if node.left is None and node.right is None:
                pass
                # print(node.data) # to print intermediate leaf nodes

            #recurssive code here
            if node.left is not None:
                helper(node.left)
            print(node.data)
            if node.right is not None:
                helper(node.right)

        helper(root)


root = Node(3)
root.insert(9)
root.insert(20)
root.insert(15)
root.insert(7)
root.dfs(root)
