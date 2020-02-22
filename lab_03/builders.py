from structure_driver import *


class SDBuilder:

    def build(self):
        return None


class JSONFileBuilder(SDBuilder):

    def build(self):
        filename = input('Enter filename (.json)>')
        return JSONFileDriver(filename)


class JSONStrBuilder(SDBuilder):

    def build(self):
        return JSONStringDriver()


class PickleBuilder(SDBuilder):

    def build(self):
        filename = input('Enter filename (.bin)>')
        return PickleDriver(filename)


class CSVBuilder(SDBuilder):

    def build(self):
        filename = input('Enter filename (.csv)>')
        return CSVDriver(filename)




class SDFabric:

    @staticmethod
    def get_sd_driver(driver_name):
        builders = {'json': JSONFileBuilder,
                    'json_str': JSONStrBuilder,
                    'pickle': PickleBuilder,
                    'csv': CSVBuilder,
                    }
        try:
            return builders[driver_name]()
        except:
            raise ValueError("Wrong driver name")
            #return SDBuilder()
