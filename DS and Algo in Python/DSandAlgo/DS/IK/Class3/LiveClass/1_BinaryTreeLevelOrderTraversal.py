import collections


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

    def bfs(self, data):
        if data is None:
            return []

        result = []
        q = collections.deque([data])
        while len(q) != 0:
            numnodes = len(q)
            temp = []
            for _ in range(numnodes):
                node = q.popleft()
                temp.append(node.data)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            result.append(temp)

        return result


root = Node(3)
root.insert(9)
root.insert(20)
root.insert(15)
root.insert(7)
print(root.bfs(root))
