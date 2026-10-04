import requests
import unittest
from unittest.mock import patch, Mock

from python_repos import get_api_response

class GetApiTestCase(unittest.TestCase):
    """Test case to test api response function from Python Repos File"""

    @patch('python_repos.requests.get')
    def test_get_api_response_success(self, mock_get):
        """Test that the function returns a response object when the API call is successful."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'total_count': 100, 'items': []}
        mock_get.return_value = mock_response

        response = get_api_response()
        mock_get.assert_called_once()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'total_count': 100, 'items': []})

    @patch('python_repos.requests.get')
    def test_get_api_response_failure(self, mock_get):
        """Test that the function raises a SystemExit when the API call fails."""
        mock_get.side_effect = requests.exceptions.RequestException("API call failed")

        with self.assertRaises(SystemExit):
            get_api_response()

    @patch('python_repos.requests.get')
    def test_get_api_response_timeout(self, mock_get):
        """Test that the function raises a SystemExit when the API call times out."""
        mock_get.side_effect = requests.exceptions.Timeout("API call timed out")

        with self.assertRaises(SystemExit):
            get_api_response()

    @patch('python_repos.requests.get')
    def test_get_api_response_connection_error(self, mock_get):
        """Test that the function raises a SystemExit when there is a connection error."""
        mock_get.side_effect = requests.exceptions.ConnectionError("Connection error")

        with self.assertRaises(SystemExit):
            get_api_response()

    @patch('python_repos.requests.get')
    def test_get_api_response_http_error(self, mock_get):
        """Test that the function raises a SystemExit when the API call returns an HTTP error."""
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("HTTP error")
        mock_get.return_value = mock_response

        with self.assertRaises(SystemExit):
            get_api_response()

    @patch('python_repos.requests.get')
    def test_get_api_response_invalid_url(self, mock_get):
        """Test that the function raises a SystemExit when the API call is made to an invalid URL."""
        mock_get.side_effect = requests.exceptions.InvalidURL("Invalid URL")

        with self.assertRaises(SystemExit):
            get_api_response()

if __name__ == '__main__':
    unittest.main()