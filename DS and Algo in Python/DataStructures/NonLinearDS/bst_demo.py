class Node:
    def __init__(self,key):
        self.data = key
        self.left_child = None
        self.right_child = None

class BSTDemo:
    def __init__(self):
        self.root = None

    def insert(self,key):
        if not isinstance(key,Node):
            key = Node(key)

        if self.root == None:
            self.root = key
        else:
            self._insert(self.root,key)

#methods starting with _ are private methods as per python practices
# and should not be used outside the class
    def _insert(self,curr,key):
        if key.data > curr.data:
            if curr.right_child == None:
                curr.right_child = key
            else:
                self._insert(curr.right_child,key)
        elif key.data < curr.data:
            if curr.left_child == None:
                curr.left_child = key
            else:
                self._insert(curr.left_child,key)

    def in_order(self):
        #left, root, right
        self._in_order(self.root)
        print("") #IGNORE: just to handle printing after the promt

    def _in_order(self,curr):
        if curr:
            self._in_order(curr.left_child)
            print(curr.data , end=" ")  # IGNORE end: just for printing in straight line
            self._in_order(curr.right_child)

    def pre_order(self):
        #root, left, right
        self._pre_order(self.root)
        print("") #IGNORE: just to handle printing after the promt

    def _pre_order(self,curr):
        if curr:
            print(curr.data, end=" ")
            self._pre_order(curr.left_child)
            self._pre_order(curr.right_child)

    def post_order(self):
        self._post_order(self.root)
        print("") #IGNORE: just to handle printing after the promt

    def _post_order(self,curr):
        if curr:
            self._post_order(curr.left_child)
            self._post_order(curr.right_child)
            print(curr.data, end=" ")

    def find_val(self,key):
        return self._find_val(self.root,key)

    def _find_val(self,curr,key):
        if curr:
            if key == curr.data:
                return "Value found in tree"
            elif key < curr.data:
                return self._find_val(curr.left_child,key)
            else:
                return self._find_val(curr.right_child,key)

        return "Value not found in tree" # return for no value found as well as curr is None

    def min_right_subtree(self,curr):
        if curr.left_child == None:
            return curr
        else:
            return self.min_right_subtree(curr.left_child)

    def delete_val(self,key):
        self._delete_val(self.root,None, None, key)

    def _delete_val(self,curr,prev, is_left, key):
        if curr:
            if key == curr.data:
                if curr.left_child and curr.right_child:
                    min_child = self.min_right_subtree(curr.right_child)
                    curr.data = min_child.data
                    self._delete_val(curr.right_child,curr,False,min_child.data)

                elif curr.left_child == None and curr.right_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = None
                        else:
                            prev.right_child = None
                    else:
                        self.root = None
                elif curr.left_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = curr.right_child
                        else:
                            prev.right_child = curr.right_child
                    else:
                        self.root = curr.right_child
                #elif curr.right_child == None:
                else:
                    if prev:
                        if is_left:
                            prev.left_child = curr.left_child
                        else:
                            prev.right_child = curr.left_child
                    else:
                        self.root = curr.left_child
            elif key < curr.data:
                self._delete_val(curr.left_child,curr,True,key)
            elif key > curr.data:
                self._delete_val(curr.right_child,curr,False,key)
        else:
            print(f'{key} not found in Tree')

#tree = BSTDemo()
# tree.insert('F')
# #print(tree.root.data)
# tree.insert('C')
# #print(tree.root.left_child.data)
# tree.insert('G')
# #print(tree.root.right_child.data)
# tree.insert('A')
# #print(tree.root.left_child.left_child.data)
# tree.insert('B')
# #print(tree.root.left_child.left_child.right_child.data)
# tree.insert('K')
# #print(tree.root.right_child.right_child.data)
# tree.insert('H')
# #print(tree.root.right_child.right_child.left_child.data)
# tree.insert('E')
# tree.insert('D')
# tree.insert('I')
# tree.insert('M')
# tree.insert('J')
# tree.insert('L')
#tree.in_order()
# tree.pre_order()
# tree.post_order()

# treequiz = BSTDemo()
# treequiz.insert('H')
# treequiz.insert('D')
# treequiz.insert('I')
# treequiz.insert('M')
# treequiz.insert('J')
# treequiz.insert('L')
# treequiz.insert('F')
# treequiz.insert('C')
# treequiz.insert('G')
# treequiz.insert('A')
# treequiz.insert('B')
# treequiz.insert('K')
# treequiz.insert('E')
#
# treequiz.in_order()
# treequiz.pre_order()
# treequiz.post_order()

#find value
# print(tree.find_val('E'))
# print(tree.find_val('J'))
# print(tree.find_val('Z'))

#delet Value
#tree.delete_val('Z')
tree = BSTDemo()
tree.insert("F")
tree.insert("C")
print("Test deleting leaf node which is left child of parent")
tree.in_order()
tree.delete_val("C")
tree.in_order()
tree.insert("G")
print("Test deleting leaf node which is right child of parent")
tree.in_order()
tree.delete_val("G")
tree.in_order()
tree.insert("A")
print("Test deleting parent/root node which has one child")
tree.in_order()
tree.delete_val("F")
tree.in_order()
print("Test deleting root node which has no children")
tree.in_order()
tree.delete_val("A")
tree.in_order()
tree.insert("F")
tree.insert("C")
tree.insert("G")
tree.insert("A")
tree.insert("B")
tree.insert("K")
tree.insert("E")
tree.insert("H")
tree.insert("D")
tree.insert("I")
tree.insert("M")
tree.insert("J")
tree.insert("L")
tree.in_order()
tree.delete_val("F")
tree.in_order()
tree.in_order()
tree.delete_val("K")
tree.in_order()
tree.in_order()
tree.delete_val("C")
tree.in_order()
tree.delete_val("Z")
tree.in_order()
