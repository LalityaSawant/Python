import collections
class Solution:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    # Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Solution(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Solution(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data


    def zigzagLevelOrder(self, root):
        if root is None:
            return []

        result = []
        q = collections.deque([root])
        reverse = False
        while len(q) != 0:
            numnodes = len(q)
            temp = []
            for _ in range(numnodes):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                temp.append(node.data)
            if reverse:
                temp.reverse()
            reverse = not reverse
            result.append(temp)
        return result


root = Solution(3)
root.insert(9)
root.insert(20)
root.insert(15)
root.insert(7)
print(root.zigzagLevelOrder(root))