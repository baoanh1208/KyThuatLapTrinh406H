class DataConnector:
      def get_all_materials(self):
        jff=JsonFileFactory()
        filename='../dataset/testdoan.json'
        materials=jff.read_data(filename,Material)
        return materials
