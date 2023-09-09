class Node:
    def __init__(self, node):
        self.value = node
        self.right = None
        self.left = None

    def add_node(self, node):
        if self.value is None:
            self.value = node
        else:
            if node < self.value:
                if self.left is None:
                    self.left = Node(node)
                else:
                    self.left.add_node(node)
            else:
                if self.right is None:
                    self.right = Node(node)
                else:
                    self.right.add_node(node)

                     

if __name__=='__main__':
    print('welcome to the tree')
    root = Node(4)
    root.add_node(3)
    print(root.value)
    print(root.left)
