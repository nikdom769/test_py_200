import numpy as np

class BitSet:
    def __init__(self, value):
        if not isinstance (value, int):
            raise TypeError("Value must be integer")
        self.__value = np.uint64(value)
    
    @staticmethod
    def __to_bit(value: int) -> list:
        val = [int(i) for i in bin(value).split('b')[1]]
        val.reverse()
        #print(val)
        return val
    
    @staticmethod
    def __to_int(value: list) -> int:
        res = 0
        for ind, val in enumerate(value):
            res += int(val * 2 ** ind)
        return res
    
    def __int__(self):
        # Верните число
        return self.__to_int(self.__to_bit(self.__value))
    
    def __iand__(self, other): # &= Удаление бита
        if isinstance(other, int):
            self.__value &= np.uint64(other)
        # Добавьте для объекта BitSet
        if isinstance(other, BitSet):
             self.__value &= np.uint64(int(other))
        return self
        
    def __ior__(self, other): # |= Установка бита
        if isinstance(other, int):
            self.__value |= np.uint64(other)
        if isinstance(other, BitSet):
            self.__value |= np.uint64(int(other))
        return self
        
    def __ixor__(self, other): # ^=
        if isinstance(other, int):
            self.__value ^= np.uint64(other)
        if isinstance(other, BitSet):
            self.__value ^= np.uint64(int(other))
        return self            

    def __invert__(self): # инверсия всех битов (~)
        bit_val = self.__to_bit(self.__value)
        for ind, val in enumerate(bit_val):
            bit_val[ind] = 0 if val == 1 else 1
        self.__value = np.uint64(self.__to_int(bit_val))
        return self
        
    def __str__(self):
        return f"{self.__int__()}"
        
    def __repr__(self):
        return f'BitSet({self.__int__()!r})'
    
    def __getitem__(self, items): # [] - чтение 
        """
        Было
        if isinstance(items, int):
            if items >= 0:
                return 0x1 & (self.__value >> items)
            raise ValueError()
        """
        bit_val = self.__to_bit(self.__value)
        if isinstance(items, int):
            return bit_val[items]
        return list(bit_val[items.start: items.stop])
        
    def __setitem__(self, items, value): # [] - запись 
        bit_val = self.__to_bit(self.__value)
        if not isinstance(items, int):
            raise TypeError("Type items must be integer")
        if  items > len(bit_val):
            raise ValueError(f"Value items must be 0 .. {len(self.__value)-1}")
        if not isinstance(value, int):
            raise TypeError("Type value must be integer")
        if  value not in (1, 0):
            raise ValueError(f"Value items must be 0 or 1")
        
        bit_val[items] = value
        self.__value = np.uint64(self.__to_int(bit_val))
