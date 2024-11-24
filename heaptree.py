from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class HeapTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert_recursive(current_node.right, value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current_node, value):
        if current_node is None:
            return current_node

        if value < current_node.value:
            current_node.left = self._delete_recursive(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._delete_recursive(current_node.right, value)
        else:
            # Случай 1: Узел без детей или с одним ребенком
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            # Случай 2: Узел с двумя детьми
            # Найти наименьший элемент в правом поддереве
            temp = self._find_min(current_node.right)
            current_node.value = temp.value
            current_node.right = self._delete_recursive(current_node.right, temp.value)

        return current_node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search_bfs(self, value):
        if self.root is None:
            return False

        queue = deque([self.root])
        while queue:
            current_node = queue.popleft()
            if current_node.value == value:
                return True
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return False

# Пример использования
heap_tree = HeapTree()
heap_tree.insert(5)
heap_tree.insert(3)
heap_tree.insert(7)
heap_tree.insert(2)
heap_tree.insert(4)
heap_tree.insert(6)
heap_tree.insert(8)

print(heap_tree.search_bfs(4))  # True
print(heap_tree.search_bfs(9))  # False

heap_tree.delete(3)
print(heap_tree.search_bfs(3))  # False


