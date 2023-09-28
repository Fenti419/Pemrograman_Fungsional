class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def evaluate_tree(root):
    if root is None:
        return 0

    if root.value == '+':
        return evaluate_tree(root.left) + evaluate_tree(root.right)
    elif root.value == '-':
        return evaluate_tree(root.left) - evaluate_tree(root.right)
    elif root.value == '*':
        return evaluate_tree(root.left) * evaluate_tree(root.right)
    elif root.value == '/':
        return evaluate_tree(root.left) / evaluate_tree(root.right)
    else:
        return float(root.value)

# Membangun pohon ekspresi aritmatika: (2 + 3) * (5 - 1)
root = TreeNode('*')
root.left = TreeNode('+')
root.right = TreeNode('-')
root.left.left = TreeNode('2')
root.left.right = TreeNode('3')
root.right.left = TreeNode('5')
root.right.right = TreeNode('1')

result = evaluate_tree(root)
print("Hasil evaluasi ekspresi:", result)
