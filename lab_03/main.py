from linked_list import *
from structure_driver import *
from builders import *


def main_prog():
    driver_name = input("please enter driver name > ")
    builder = SDFabric.get_sd_driver(driver_name)
    
    l1 = LinkedList()
    l1.set_structure_driver(builder.build())
    l1.append("lasy")
    l1.append('fily')
    print(l1)

    print("Изменим данные с индексом 1 в списке на 'nik'")
    l1.value_set('nik', 1)

    print("Создадим новый LinkedList из файла")
    l2 = LinkedList()
    l2.set_structure_driver(CSVDriver('test.csv'))
    l2.load()
    print(l2)


if __name__ == "__main__":
    main_prog()
