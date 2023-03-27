"""
Delete a node from a Binary Tree using Python List

Binary Tree
                Drinks
               /    \  
             /        \  
           /            \  
         Hot            Cold
        /  \            /  \ 
      /      \        /      \ 
    Tea     Coffee   N6       N7



0   1   2   3   4   5   6   7   8   9   10    11
x   N1  N2  N3  N4  N5  N6  N7  N8  N9  new

Left child = cell[2x]       ---->     x = 3, cell[2x3 = 6]
Right child = cell[2x+1]    ---->     x = 3, cell[2x3+1=7]

Time complexity:  O(1)
Space complexity: O(n)
"""


class BinaryTree:
  def __init__(self, size):
    self.customList = size * [None]
    self.lastUsedIndex = 0
    self.maxSize = size

  def insertNode(self, value):
    if self.lastUsedIndex + 1 == self.maxSize:
      return 'The Binary Tree is full.'
    self.customList[self.lastUsedIndex + 1] = value
    self.lastUsedIndex += 1
    return 'The value has been successfully inserted'

  def searchNode(self, nodeValue):
    for i in range(len(self.customList)):
      if self.customList[i] == nodeValue:
        return 'Success'
    return 'Not found'
  
  def preOrderTraversal(self, index, arr):
    if index > self.lastUsedIndex:
      return
    print(self.customList[index])
    arr.append(self.customList[index])
    self.preOrderTraversal(index*2, arr)
    self.preOrderTraversal(index*2 + 1, arr)

  def inOrderTraversal(self, index, arr):
    if index > self.lastUsedIndex:
      return
    self.inOrderTraversal(index*2, arr)
    print(self.customList[index])
    arr.append(self.customList[index])
    self.inOrderTraversal(index*2 + 1, arr)

  def postOrderTraversal(self, index, arr):
    if index > self.lastUsedIndex:
      return
    self.postOrderTraversal(index*2, arr)
    self.postOrderTraversal(index*2 + 1, arr)
    print(self.customList[index])
    arr.append(self.customList[index])

  def levelOrderTraversal(self, index, arr):
    if index > self.lastUsedIndex:
      return
    for i in range(index, self.lastUsedIndex + 1):
      print(self.customList[i])
      arr.append(self.customList[i])

  def deleteNode(self, value):
    if self.lastUsedIndex == 0:
      return 'There is not any node to delete'
    for i in range(1, self.lastUsedIndex + 1):
      if self.customList[i] == value:
        self.customList[i] = self.customList[self.lastUsedIndex]
        self.customList[self.lastUsedIndex] = None
        self.lastUsedIndex -= 1
        return 'The node has been successfully deleted'

  def entire(self):
    self.customList = None
    self.lastUsedIndex = 0
    return 'The BT has been successfully deleted.'


newBT = BinaryTree(8)
print(newBT.insertNode('Drinks'))
print(newBT.insertNode('Hot'))
print(newBT.insertNode('Cold'))
print(newBT.insertNode('Tea'))
print(newBT.insertNode('Coffee'))
print(newBT.insertNode('Cola'))
print(newBT.insertNode('Sprite'))


arr = []
newBT.deleteNode('Tea')
newBT.levelOrderTraversal(1, arr)
print('arr: ', arr)
print('\n')

arr = []
newBT.deleteNode('Hot')
newBT.levelOrderTraversal(1, arr)
print('arr: ', arr)
print('\n')

newBT.entire()
newBT.levelOrderTraversal(1, arr)