class Observer:
    # Наблюдатель
    def update(self):
        pass


class Subject:

    def __init__(self):
        self.__o = set()

    def add_observer(self, o: Observer):
        self.__o.add(o)

    def remove_observer(self, o: Observer):
        self.__o[o].remove(o)

    def notify(self):
        for o in self.__o:
            o.update(self)


"""
class PrintView(Observer):
    def update(self, subject):
        print(f'Value changed: {hex(id(subject))}')


class SimpleView(Observer):
    def update(self, subject):
        print(f'SimpleView: {hex(id(subject))}')



class InputSubject(Subject):

    def __init__(self):
        super().__init__()
        self.__value = 0

    def enter_value(self):
        value = input("Enter new value >")
        if value != self.__value:
            self.__value = value
            self.notify()
"""