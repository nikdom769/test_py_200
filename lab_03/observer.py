from weakref import ref

class Observer:
    # Наблюдатель
    def update(self):
        pass


class Subject:

    """Добавлена слабая ссылка на наблюдателя"""

    def __init__(self):
        self.__o = set()

    def add_observer(self, o: Observer):
        self.__o.add(ref(o))

    def remove_observer(self, o: Observer):
        self.__o.remove(ref(o))

    def notify(self):
        for o in self.__o:
            o().update()

