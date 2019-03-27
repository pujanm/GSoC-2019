"""
INSTRUCTIONS TO RUN THIS FILE:
Inside the CLI run this command: pytest task1.py
"""

import os
import unittest


class task1(unittest.TestCase):

    # Basic initialization
    filename = "task1.txt"


    # Create the file and tests whether it was created
    def test_create_file(self):
    
        # Creates the file
        f = open(self.filename, "w+")

        # Tests the file creation
        self.assertTrue(os.path.isfile(self.filename), "File was not created.")


    # Deletes the file and tests whether it was deleted
    def test_delete_file(self):

        # Deletes the file
        os.remove(self.filename)

        # Tests the file deletion
        self.assertFalse(os.path.isfile(self.filename), "File was not deleted.")


if __name__ == '__main__':
    unittest.main()