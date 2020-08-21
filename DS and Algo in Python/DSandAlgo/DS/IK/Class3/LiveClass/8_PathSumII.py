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

    def dfs(self,root, sum):
        if root is None:
            return []

        self.result = []

        def dfs_helper(node, target, slate):
            # Base case - Leaf Node
            if node.left is None and node.right is None:
                if target == node.val:
                    slate.append(node.val)
                    self.result.append(slate[:])
                    slate.pop()
                return

            # Recursive case - Internal Node
            slate.append(node.val)
            if node.left is not None:
                dfs_helper(node.left, target-node.val, slate)
            if node.right is not None:
                dfs_helper(node.right, target-node.val, slate)
            slate.pop()


        dfs_helper(root, sum, [])
        return self.result


root = Node(3)
root.insert(9)
root.insert(20)
root.insert(15)
root.insert(7)
print(root.dfs(root, 19))