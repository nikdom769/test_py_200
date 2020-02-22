from linked_list import *
from structure_driver import *
from builders import *



l1 = LinkedList()
l1.append("lasy")
l1.append('fily')
l1.append('nik')
#print(l1)

driver_name = input("please enter driver name > ")
builder = SDFabric.get_sd_driver(driver_name)
l1.set_structure_driver(builder.build())
l1.save()

"""
l2 = LinkedList()
l2.set_structure_driver(CSVDriver('test.csv'))
l2.load()
print(l2)
"""
