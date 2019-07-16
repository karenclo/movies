import unittest
from unittest.mock import patch
from movies import solution


class TestSolution(unittest.TestCase):

    @patch('requests.get')
    def test_get_titles_bad_response(self, requests_mock):
        requests_mock.status_code.return_value = 400

        with self.assertRaises(AssertionError):
            solution.get_titles('http://url')

    def test_get_actors_unsupported_type(self):
        with self.assertRaises(TypeError):
            solution.get_actors([1234], 'youtube')

    @patch('requests.get')
    def test_get_actors_bad_response(self, requests_mock):
        requests_mock.status_code.return_value = 404

        with self.assertRaises(AssertionError):
            solution.get_actors([1234], 'movie')




