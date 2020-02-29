# Перегрузите операторы:
# 1.	Битовое «И» (c1 & c2):	             __and__(self, other);
# 2.	Битовое «ИЛИ» (c1 | c2):	         __or__(self, other);
# 3.	Битовое «ИСКЛЮЧАЮЩЕЕ ИЛИ» (c1 ^ c2): __xor__(self, other);



class Color:
    def __init__(self, *args):
        
        if len(args) > 3:
            raise TypeError()
        
        if len(args) == 0:
            r = 0
            g = 0
            b = 0
            
        if len(args) == 1 and isinstance(args[0], str):
            value = args[0].split('x')[1]
            r = int(value[0:2], 16)
            g = int(value[2:4], 16)
            b = int(value[4:6], 16)
            
        if len(args) == 3:
            for i in args:
                if not isinstance(i, int):
                    raise TypeValue()
                if not 0 <= i < 256:
                    raise ValueError()
            r, g, b = args
            
        self.__r = r
        self.__g = g
        self.__b = b
        
        
    def __and__(self, other): # c1 & c2
        r = self.__r & other.__r 
        g = self.__g & other.__g
        b = self.__b & other.__b
        return Color(r, g, b)
        
    def __or__(self, other):  # c1 | c2
        r = self.__r | other.__r 
        g = self.__g | other.__g
        b = self.__b | other.__b
        return Color(r, g, b)
        
    def __xor__(self, other): # c1 ^ c2
        r = self.__r ^ other.__r 
        g = self.__g ^ other.__g
        b = self.__b ^ other.__b
        return Color(r, g, b)
        
    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        r = min(((self.__r + other.__r), 255))
        g = min(((self.__g + other.__g), 255))
        b = min(((self.__b + other.__b), 255))
        
        return Color(r, g, b)
    
    def __sub__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        r = max(((self.__r - other.__r), 0))
        g = max(((self.__g - other.__g), 0))
        b = max(((self.__b - other.__b), 0))
        
        return Color(r, g, b)
    
    def __repr__(self):
        return f'Color({self.__r!r}, {self.__g!r}, {self.__b!r})'
