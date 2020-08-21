'''
    For your reference:

    class TreeNode:
    def __init__(self, node_value):
        self.val = node_value
        self.left_ptr = None
        self.right_ptr = None
'''
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

    def kth_smallest_element(root, k):
        if root is None:
            return root

        result = []

        def helper(node, k):
            if node.left is None and node.right is None:
                pass

            if node.left is not None:
                helper(node.left,k)
            result.append(node.val)
            if node.right is not None:
                helper(node.right,k)

        helper(root, k)
        return result[k-1]

root = Node(3)
root.insert(9)
root.insert(20)
root.insert(15)
root.insert(7)
print(root.helper(root, 2))