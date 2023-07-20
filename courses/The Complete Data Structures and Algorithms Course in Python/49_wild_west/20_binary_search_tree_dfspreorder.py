"""Coding Exercise 20: Binary Search Tree - DFSPreOrder"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, curNode):
        if curNode.data > data:
            if curNode.left is None:
                curNode.left = Node(data)

            else:
                self._insert(data, curNode.left)
        else:
            if curNode.right is None:
                curNode.right = Node(data)
            else:
                self._insert(data, curNode.right)

    def depthFirstSearchPreOrder(self, rootNode, data):
        if rootNode is None:
            return data
        # print(rootNode.data)
        data.append(rootNode.data)
        self.depthFirstSearchPreOrder(rootNode.left, data)
        self.depthFirstSearchPreOrder(rootNode.right, data)
        return data
