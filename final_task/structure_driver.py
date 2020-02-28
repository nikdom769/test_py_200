import json
import csv


class IStructureDriver:
    def read(self):
        pass

    def write(self, d):
        pass


class JSONFileDriver(IStructureDriver):
    def __init__(self, filename):
        self.__filename = f"./db/{filename}"

    def read(self):
        with open(self.__filename, encoding='UTF-8') as f:
            return json.load(f)

    def write(self, d):
        with open(self.__filename, 'w', encoding='UTF-8') as f:
            json.dump(d, f, ensure_ascii=False)


class CSVDriver(IStructureDriver):
    
    def __init__(self, filename):
        self.__filename = f"./db/{filename}"
        self.__fieldnames = ("id",
                             "last_name",
                             "first_name",
                             "title",
                             "series",
                             "volume",
                             "year",
                             "note")
        
    def read(self):
        result = []
        with open(self.__filename, 'r') as f:
            rd = csv.DictReader(f, fieldnames=self.__fieldnames, dialect='unix')
            for row in rd:
                result.append(dict(row))
        return result

    def write(self, list_d):
        """
        param: list_d - список словарей (книг)
        """
        with open(self.__filename, 'w') as f:
            wrt = csv.DictWriter(f, fieldnames=self.__fieldnames, dialect='unix')
            wrt.writeheader()
            for book in list_d:
                wrt.writerow(book)
