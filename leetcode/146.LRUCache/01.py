class DoubleNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.head = DoubleNode()
        self.tail = DoubleNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p

    def _add_to_head(self, node):
        after_head = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = after_head
        after_head.prev = node

    def get(self, key: int) -> int:
        if key in self.data:
            node = self.data[key]
            self._remove(node)
            self._add_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            node = self.data[key]
            self._remove(node)
            node.val = value
            self._add_to_head(node)
        else:
            if len(self.data) >= self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.data[lru_node.key]

            new_node = DoubleNode(key, value)
            self.data[key] = new_node
            self._add_to_head(new_node)
