# Лабораторная работа № 2
# Слушатель (ФИО): Домичев Н.Н.


class Figure:

    def __init__(self, x=0, y=0, height=0, width=0):
        # координаты верхнего правого угла
        self.__x = x
        self.__y = y
        # высота и ширина фигуры
        self.__height = height
        self.__width = width

    def area(self):
        ...

    def perimeter(self):
        ...

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def width(self):
        return self.__width

    def height(self):
        return self.__height


class Rectangle(Figure):

    def __init__(self, x=0, y=0, height=0, width=0):
        super().__init__(x, y, height, width)
    
    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return 2 * (self.__height + self.__width)


class Ellipse(Figure):
    
    def __init__(self, x=0, y=0, a=0, b=0):
        super().__init__(x, y)
        self.__a = a # длина большой полуоси
        self.__b = b # длина малой полуоси
    
    def width(self):
        return 2 * self.__a

    def height(self):
        return 2 * self.__b
    
    def area(self):
        return 3.14 * self.__a * self.__b 

    def perimeter(self):
        return 4 * ((self.aria() + (self.__a - self.__b)) / (self.__a + self.__b))


class CloseFigure(Figure):

    def __init__(self, x: list, y: list):
        super().__init__()
        if not isinstance(x, list):
            raise TypeError("Coordinate 'X' must be list")
        if not isinstance(y, list):
            raise TypeError("Coordinate 'Y' must be list")
        if len(x) != len(y):
            raise ValueError("Legnth list x & y must be equvalent")
        self.__x = x
        self.__y = y
        self.__points = [{'x': x, 'y': y} for x, y in zip(self.__x, self.__y)]
        self.__ind = len(self.__points)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__ind == 0:
            raise StopIteration
        self.__ind = self.__ind - 1
        return self.__points[self.__ind] 

