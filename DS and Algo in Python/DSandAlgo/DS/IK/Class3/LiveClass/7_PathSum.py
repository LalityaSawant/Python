# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.val = data
    # Insert Node
    def insert(self, data):

        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def hasPathSum(self, root, sum):
        if root is None:
            return False

        self.result = [False]

        def dfs(node, target):
            #Base case --> leaf node
            if node.left is None and node.right is None:
                if node.val == target:
                    self.result[0] = True
                return
            #Recursive phase
            if node.left is not None:
                dfs(node.left, target-node.val)
            if node.right is not None:
                dfs(node.right, target-node.val)

        dfs(root, sum)
        return self.result[0]

root = Node(3)
root.insert(9)
root.insert(20)
root.insert(15)
root.insert(7)
print(root.hasPathSum(root, 47))