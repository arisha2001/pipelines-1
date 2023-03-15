from unittest import mock
from pipelines.tasks import *
import unittest


class UnitTests(unittest.TestCase):
    def test_DataLoader(self):
        query_result = [('1', 'hello', 'http://hello.com/home'),
                        ('2', 'world', 'https://world.org/')]
        with mock.patch('psycopg2.connect') as mock_connect:
            mock_connect.cursor.return_value.fetchall.return_value = query_result
            LoadFile(table='original', input_file='./example_pipeline/original/original.csv').run()

    def test_CTAS(self):
        query_result = [('1', 'hello', 'http://hello.com/home', 'hello.com'),
                        ('2', 'world', 'https://world.org/', 'world.org')]
        with mock.patch('psycopg2.connect') as mock_connect:
            mock_connect.cursor.return_value.fetchall.return_value = query_result
            CTAS(table='norm', sql_query='select *, domain_of_url(url) from original;').run()


if __name__ == '__main__':
    unittest.main()

