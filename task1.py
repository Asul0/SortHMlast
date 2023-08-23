class RedBlackNode:
    def __init__(self, key, color, parent=None, left=None, right=None):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right


class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = RedBlackNode(None, color="black")
        self.root = self.NIL_LEAF

def left_rotate(self, node):
    right_child = node.right
    node.right = right_child.left
    if right_child.left != self.NIL_LEAF:
        right_child.left.parent = node
        right_child.parent = node.parent
    if node.parent is None:
        self.root = right_child
    elif node == node.parent.left:
        node.parent.left = right_child
    else:
        node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

def right_rotate(self, node):
    left_child = node.left
    node.left = left_child.right
    if left_child.right != self.NIL_LEAF:
        left_child.right.parent = node
        left_child.parent = node.parent
    if node.parent is None:
        self.root = left_child
    elif node == node.parent.right:
        node.parent.right = left_child
    else:
        node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

def insert(self, key):
    new_node = RedBlackNode(key, color="red")
    parent = None
    current = self.root

    while current != self.NIL_LEAF:
        parent = current
    if new_node.key < current.key:
        current = current.left
    else:
        current = current.right

    new_node.parent = parent
    if parent is None:
        self.root = new_node
    elif new_node.key < parent.key:
        parent.left = new_node
    else:
        parent.right = new_node

    self._balance_insert(new_node)

def _balance_insert(self, node):
    while node.parent.color == "red":
        if node.parent == node.parent.parent.left:
            uncle = node.parent.parent.right
    if uncle.color == "red":
        node.parent.color = "black"
        uncle.color = "black"
        node.parent.parent.color = "red"
        node = node.parent.parent
    else:
        if node == node.parent.right:
            node = node.parent
            self.left_rotate(node)
            node.parent.color = "black"
            node.parent.parent.color = "red"
            self.right_rotate(node.parent.parent)
        else:
            uncle = node.parent.parent.left
        if uncle.color == "red":
            node.parent.color = "black"
            uncle.color = "black"
            node.parent.parent.color = "red"
            node = node.parent.parent
        else:
            if node == node.parent.left:
                node = node.parent
                self.right_rotate(node)
                node.parent.color = "black"
                node.parent.parent.color = "red"
                self.left_rotate(node.parent.parent)
                self.root.color = "black"

def inorder_traversal(self, node):
    if node != self.NIL_LEAF:
        self.inorder_traversal(node.left)
        print(node.key, node.color)
        self.inorder_traversal(node.right)

# Пример использования
rb_tree = RedBlackTree()
keys = [55, 40, 65, 60, 75, 57, 44, 62, 48]
for key in keys:
    rb_tree.insert(key)

print("Inorder Traversal:")
rb_tree.inorder_traversal(rb_tree.root)