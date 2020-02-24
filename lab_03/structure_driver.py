import json
import pickle
#import yaml
import csv


class IStructureDriver:
    def read(self):
        pass

    def write(self, d):
        pass


class JSONFileDriver(IStructureDriver):
    def __init__(self, filename):
        self.__filename = filename

    def read(self):
        with open(self.__filename, encoding='UTF-8') as f:
            return json.load(f)

    def write(self, d):
        with open(self.__filename, 'w', encoding='UTF-8') as f:
            json.dump(d, f, ensure_ascii=False)


class JSONStringDriver(IStructureDriver):
    def __init__(self, s='{}'):
        self.__s = s

    def get_string(self):
        return self.__s

    def read(self):
        return json.loads(self.__s)

    def write(self, d):
        self.__s = json.dumps(d, ensure_ascii=False)


class PickleDriver(IStructureDriver):
    def __init__(self, filename):
        self.__filename = filename

    def read(self):
        with open(self.__filename, 'rb') as f:
            return pickle.load(f)

    def write(self, d):
        with open(self.__filename, 'wb') as f:
            pickle.dump(d, f)


class YUMLDriver(IStructureDriver):
    def __init__(self, filename):
        self.__filename = filename

    def read(self):
        with open(self.__filename, 'r') as f:
            return yaml.safe_load(f)

    def write(self, d):
        with open(self.__filename, 'w') as f:
            yaml.dump(d, f)


class CSVDriver(IStructureDriver):
    def __init__(self, filename, fieldnams=['ind', 'value']):
        self.__filename = filename
        self.__fieldnames = fieldnams

    def read(self):
        d = {}
        with open(self.__filename, 'r') as f:
            rd = csv.DictReader(f, dialect='unix')
            for row in rd:
                d[row[self.__fieldnames[0]]] = row[self.__fieldnames[1]]
        return d

    def write(self, d):
        with open(self.__filename, 'w') as f:
            wrt = csv.DictWriter(f, fieldnames=self.__fieldnames, dialect='unix')
            wrt.writeheader()
            for k, v in d.items():
                wrt.writerow({self.__fieldnames[0]: k, self.__fieldnames[1]: v})

"""
# Где применяется этот код
class SDWorker:
    def __init__(self, structure_driver: IStructureDriver):
        self.__structure_driver = structure_driver

    def do_work(self):
        try:
            d = self.__read_from_sd()
        except:
            self.__set_default()
            self.do_work()
            return

        print(f'Before set name: {d}')
        d['name'] = 'Python'
        print(f'After set name: {d}')
        self.__write_to_sd(d)

    def __set_default(self):
        d = {}
        self.__write_to_sd(d)

    def __read_from_sd(self):
        return self.__structure_driver.read()

    def __write_to_sd(self, d):
        self.__structure_driver.write(d)
"""
