"""LinkedList"""

from weakref import ref
from structure_driver import IStructureDriver
from observer import Subject, Observer


class Data(Subject):

    # обертка  для простых данных
    def __init__(self, value):
        super().__init__()
        # если убрать ошибка AttributeError: 'Node' object
        # has no attribute '_Subject__o'
        self.__value = value

    def read_val(self):
        return self.__value

    def write_val(self, value):
        if value != self.__value:
            self.__value = value
            self.notify()


class LinkedList(IStructureDriver, Observer):

    class Node(Data):

        def __init__(self, data, nxt=None, prev=None):
            super().__init__(data)
            # исли пользователь введет для ссылок, что то не то установиться None
            self.__next = nxt if isinstance(nxt, (type(self))) else None
            self.__prev = ref(prev) if isinstance(prev, (type(self))) else None

        @property
        def prev(self):
            return self.__prev()

        @property
        def next_(self):
            return self.__next

        @property
        def data(self):
            return self.read_val()

        @prev.setter
        def prev(self, prev):
            if isinstance(prev, type(self)):
                self.__prev = ref(prev)
            else:
                raise TypeError("Prev must be None or Node")

        @next_.setter
        def next_(self, nxt):
            if isinstance(nxt, type(self)):
                self.__next = nxt
            else:
                raise TypeError("Next must be None or Node")

        def __repr__(self):
            return f"Node({self.data}, {self.__prev}, {self.__next})"

        def __str__(self):
            return f"{self.data}"

    def __init__(self, structure_driver=None):
        self.__head = self.Node('head')
        self.__tail = self.Node('tail', prev=self.__head)
        self.__head.next_ = self.__tail
        self.len = 0
        self.__structure_driver = structure_driver

    # Служебные методы
    def _insert_node(self, current, data):
        """
        Insert data after current:Node
        """
        new_node = self.Node(data, nxt=current.next_, prev=current)
        current.next_.prev = new_node
        current.next_ = new_node
        new_node.add_observer(self)  # добавление в качестве слушателя
        # self.update()  # обновление данных при вставке новой Node
        self.len += 1
    
    def _find_ind(self, ind=0):
        """
        Find "Node" for index
        Return "Node"
        """
        if 0 <= ind < self.len:
            f_node = self.__head
            for i in range(self.len):
                if i == ind:
                    return f_node
                else:
                    f_node = f_node.next_
        elif -self.len < ind <= -1:
            f_node = self.__tail.prev
            for i in range(1, self.len):
                if i == abs(ind):
                    return f_node
                else:
                    f_node = f_node.prev
        else:
            raise ValueError("Index error")

    def _del_node(self, current):
        """
        Delete Node(current)
        """
        current.prev.next_ = current.next_
        current.next_.prev = current.prev  # если строки поменять местами работать не будет
        current.remove_observer(self)  # удаление данных из наблюдателя
        # self.update()  # обновление данных при удалении Node
        self.len -= 1
        
    # Пользовательские методы
    def append(self, data):
        """
        Insert Node in Tail List
        """
        self._insert_node(self.__tail.prev, data)
        return self

    def insert(self, data, ind=0):
        """
        Insert Node for index
        index: 0 ... lenght or -lenght ... -1
        """
        f_node = self._find_ind(ind)
        self._insert_node(f_node, data)
        return self

    def find(self, value):
        """
        Find index Node(data)
        Return: int (Index)
        """
        f_node = self.__head.next_
        for i in range(self.len):
            if f_node.data == value:
                return i
            else:
                f_node = f_node.next_
        else:
            raise ValueError("Value not found")

    def delete(self, ind=0):
        """
        Delete Node for index
        Return: value 
        """
        f_node = self._find_ind(ind)
        # проверка правильности индекса вынесена в методе _find_ind
        if ind >= 0:
            self._del_node(f_node.next_)
            return f"{f_node.next_.data}"
        else:
            self._del_node(f_node)
            return f"{f_node.data}"
        
    def remove(self, data):
        """
        Delete Node for value
        Return (index, value)
        """
        ind = self.find(data)
        self.delete(ind)
        return ind, data

    def clear(self):
        """
        Clear Linked list
        """
        self.__init__()

    def value(self, ind=0):
        """
        Return value Node for index 
        """
        node = self._find_ind(ind)
        return node.next_.data
    
    def value_set(self, data, ind=0):
        """
        Rewriter value Node for index
        """
        node = self._find_ind(ind)
        node.next_.write_val(data)

    def __str__(self):
        if self.len:
            nxt_node = self.__head.next_
            out = "["
            for i in range(self.len):
                out += f"{nxt_node.data}, "
                nxt_node = nxt_node.next_
            return out + "]"
        return "[]"

    def set_structure_driver(self, structure_driver):
        self.__structure_driver = structure_driver  # для добавления интерфейса чтения записи

    def __to_dict(self):
        """
        from LinkedList to dict
        """
        res = {}
        node = self.__head.next_
        for i in range(self.len):
            res[i] = node.data
            node = node.next_
        return res

    def __from_dict(self, dict_):
        """
        from dict to LinkedList
        """
        for ind, value in dict_.items():
            self.append(value)
        return self

    def save(self):
        self.__structure_driver.write(self.__to_dict())

    def load(self):
        self.__from_dict(self.__structure_driver.read())

    def update(self):
        print('Linked list update')
        self.save()
