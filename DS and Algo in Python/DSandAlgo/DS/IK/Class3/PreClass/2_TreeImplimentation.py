class TreeNode:

    def __init__(self, key):
        self.key = key
        # Value
        self.left = None
        self.right = None

    def __str__(self):
        return f'key: {self.key} leftPointer: {self.left} rightPointer: {self.right}'

    def search(self, root, key):

        curr = root
        while root is not None:
            if key == curr.key:
                return curr
            elif key < curr.key:
                curr = self.left
            else:
                curr = self.right

        return None

    def insert(self, root, key):

        new_node = TreeNode(key)

        if root is None:
            return new_node

        prev = None
        curr = root
        while root is not None:
            if key == curr.key:
                return "Key already exists"
            elif key < curr.key:
                prev = curr
                curr = self.left
            else:
                prev = curr
                curr = self.right

        if prev < key:
            prev.left = new_node
        else:
            prev.right = new_node

        return root

    def find_min(self, root):
        if root is None:
            return None

        curr = root
        while curr.left is not None:
            curr = curr.left

        return curr

    def find_max(self, root):
        if root is None:
            return None

        curr = root
        while curr.right is not None:
            curr = curr.right

        return curr

    def successor(self, root, k):
        if root is None:
            return None
        if k.right is not None:
            curr = k.right
            while curr.left is not None:
                curr = curr.left
            return curr

        ancestor = None
        curr = root
        while curr is not k:
            if k.key == curr.key:
                ancestor = curr
                curr = curr.left
            else:
                curr = curr.right

        return ancestor

# change all lefts to right and vice versa
    def predessor(self, root, k):
        if root is None:
            return None
        if k.right is not None:
            curr = k.right
            while curr.left is not None:
                curr = curr.left
            return curr

        ancestor = None
        curr = root
        while curr is not k:
            if k.key == curr.key:
                ancestor = curr
                curr = curr.left
            else:
                curr = curr.right

        return ancestor


tree1 = TreeNode(10)

print(tree1)

tree1.insert(tree1, 5)
