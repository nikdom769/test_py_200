from weakref import ref
       
       
# Перегрузите оператор [] так, чтобы можно было вставлять 
# один LinkedList в другой LinkedList.
# l = LinkedList()
# l1 = LinkedList()
# l1.push_front(7)
# l1.push_front(5)
# l1.push_front(2)
# print(l1) # 2->5->7->

# l2 = LinkedList()
# l2.push_front(6)
# l2.push_front(8)
# print(l2) # 8->6-> (было 6->8-> )

# l1[2] = l2 
# print(l1) # 2->5->8->6->7-> (было 2->5->6->8->7->)
        
class LinkedList:

    class __Node:
        def __init__(self, prev_node=None, next_node=None, data=None):
        
            if prev_node is not None and not isinstance(prev_node, type(self)):
                raise TypeError('prev_node must be Node or None')
        
            if next_node is not None and not isinstance(next_node, type(self)):
                raise TypeError('next_node must be Node or None')
                
            self.prev_node_ = ref(prev_node) if prev_node is not None else None
            self.next_node_ = next_node
            self.data = data
            
        @property
        def prev_node(self):
            return self.prev_node_() if self.prev_node_ is not None else None
            
        @prev_node.setter
        def prev_node(self, value):
            if value is not None and not isinstance(value, type(self)):
                raise TypeError('Value must be Node or None')
            self.prev_node_ = ref(value) if value is not None else None
            
        @property
        def next_node(self):
            return self.next_node_
            
        @next_node.setter
        def next_node(self, value):
            if value is not None and not isinstance(value, type(self)):
                raise TypeError('Value must be Node or None')
            self.next_node_ = value 
        
    
    def __init__(self):
        self.__head = self.__Node()
        self.__tail = self.__Node(self.__head)
        self.__head.next_node = self.__tail
        self.__size = 0
        
    def __iadd__(self, other):
        self.__tail.prev_node.next_node = other.__head.next_node
        other.__head.next_node.prev_node = self.__tail.prev_node
        other.__tail.prev_node.next_node = self.__tail
        self.__tail.prev_node = other.__tail.prev_node
        self.__size += other.__size
        other.clear()
        return self
    
    def __setitem__(self, index, value):
        ind = index - 1
        if not isinstance(index, int):
            raise TypeError('index must be int')
        if not 0 <= ind < self.__size:
            raise ValueError(f'index must be 0 ... {self.__size}')
        if isinstance(value, LinkedList):
            current_node = value.__head.next_node
            for i in range(ind, ind + len(value)):
                self.insert_node(current_node.data, i)
                current_node = current_node.next_node
        elif not isinstance(value, type(iter)):
            self.insert_node(value, ind)

    def clear(self):
        self.__head.next_node = self.__tail
        self.__tail.prev_node = self.__head
        
    def insert_node(self, data, index=0):
        if not isinstance(index, int):
            raise TypeError('index must be int')        
        if index >= 0:    
            if not 0 <= index <= self.__size:
                raise ValueError('Invalid index')
            current_node = self.__head.next_node
            for _ in range(index):
                current_node = current_node.next_node
            self.insert_next_node(current_node, data)
            
    def insert_next_node(self, current_node, data):        
        new_node = self.__Node(current_node, current_node.next_node, data)
        current_node.next_node.prev_node = new_node
        current_node.next_node = new_node
        self.__size += 1
        
    def push_front(self, data):
        current_node = self.__head
        new_node = self.__Node(current_node, current_node.next_node, data)
        current_node.next_node.prev_node = new_node
        current_node.next_node = new_node
        self.__size += 1 # добавил
        
    def __str__(self):
        current_node = self.__head.next_node
        s = ''
        while current_node is not self.__tail:            
            s += f'{current_node.data}->'
            current_node = current_node.next_node            
        return s
    
    def __len__(self):
        return self.__size
