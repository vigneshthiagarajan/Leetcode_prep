class Node:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.next = nextNode
        
class Bucket:
    def __init__(self):
        self.head = Node(0)
    
    def exists(self, value):
        current = self.head.next
        while(current is not None):
            if current.value == value:
                return True
            current = current.next
        return False
    
    def insert(self, newValue):
        # if not existed, add the new element to the head.
        if not self.exists(newValue):
            newNode = Node(newValue, self.head.next)
            # set the new head.
            self.head.next = newNode
            
    def delete(self, value):
        prev = self.head
        current = self.head.next
        while(current is not None):
            if(current.value == value):
                prev.next = current.next
            prev = current
            current = current.next
        

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_space = 769
        self.hashset = [Bucket() for i in range(self.key_space)]
        
    def _hash(self, key):
        return key % self.key_space

    def add(self, key: int) -> None:
        hash_key = self._hash(key)
        self.hashset[hash_key].insert(key)
        

    def remove(self, key: int) -> None:
        hash_key = self._hash(key)
        self.hashset[hash_key].delete(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hash_key = self._hash(key)
        return self.hashset[hash_key].exists(key)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)