"""
INSTRUCTIONS TO RUN THIS FILE:
Inside the CLI run this command: 
1) To run the pytest framework: pytest task4.py
2) To check the indices lists output: python task4.py
"""

from elasticsearch import Elasticsearch
import unittest
import json


class task4(unittest.TestCase):

    # Initializes the connection
    es = Elasticsearch([{"host": "localhost", "port": 9200}])


    # Creates the index and tests it's existence
    def test_create_index(self):

        # creating the index
        self.es.indices.create(index="process-index", ignore=400)

        # test for index existence
        self.assertTrue(self.es.indices.exists(index="process-index"), "Index does not exists.")


    # List of all the indices and then deleting all indices and then testing the deletion
    def test_list_and_delete_indexes(self):
        # get all the indexes present in elastic
        indices_list = [i for i in self.es.indices.get('*')]
        print(indices_list)

        # deleting all the indices
        self.es.indices.delete(index="*", ignore=[400, 404])

        # test for index deletion
        self.assertFalse(self.es.indices.exists(index="process-index"), "Index still exists.")


    # Recreates the index and adds data from the json file and verification the content
    def test_recreate_and_add_data(self):
        # recreation of the index
        self.es.indices.create(index="process-index", ignore=400)

        # Reading and adding content to the index
        f = open("task3.json", "r")
        current_process_data = json.load(f)
        f.close()
        self.es.index(index="process-index", doc_type='current_process', id=1, body=current_process_data)

        # verifying the content in the index
        index_data = self.es.get(index="process-index", doc_type='current_process', id=1)["_source"]
        self.assertTrue(index_data == current_process_data, "Content in the index does not match.")



if __name__ == '__main__':
    unittest.main()
