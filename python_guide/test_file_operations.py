import unittest
import os


class FileOperationsTest(unittest.TestCase):

    _filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'kafka-python.txt')

    def test_read(self):
        with open(self._filepath, 'r') as f:

            self.assertEqual(f.read(7), 'Python ')  # if no param, it returns all data of the file, if reaches the end, it returns ''

            self.assertEqual(f.readline(7), 'client ')  # if pass param to readline(), it works same as read()
            self.assertEqual(f.readline(), 'for the Apache Kafka distributed stream processing system.\n')

            # f.close() is not needed, it will be closed automatically


if __name__ == '__main__':
    unittest.main()
