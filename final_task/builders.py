from structure_driver import CSVDriver, JSONFileDriver


class SDBuilder:

    def build(self):
        return None


class JSONFileBuilder(SDBuilder):

    def build(self, filename=None):
        if not filename:
            filename = input('Enter filename (.json)>')
        return JSONFileDriver(filename)


class CSVBuilder(SDBuilder):

    def build(self, filename=None):
        if not filename:
            filename = input('Enter filename (.csv)>')
        return CSVDriver(filename)


class SDFabric:

    @staticmethod
    def get_sd_driver(driver_name):
        builders = {'json': JSONFileBuilder,
                    'csv': CSVBuilder,
                    }
        try:
            return builders[driver_name]()
        except:
            raise ValueError("Wrong driver name")
            #return SDBuilder()
