import unittest

from flask import json

from swagger_server.models.data_record import DataRecord  # noqa: E501
from swagger_server.models.prediction import Prediction  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_controller_get_predictions(self):
        """Test case for controller_get_predictions

        Dust & temperature predictions
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/Pikha/v1/predictions',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_primary_data(self):
        """Test case for controller_get_primary_data

        All KidBright (primary) readings, with optional filtering & pagination
        """
        query_string = [('place_type', 'place_type_example'),
                        ('start', '2013-10-20T19:20:30+01:00'),
                        ('end', '2013-10-20T19:20:30+01:00'),
                        ('limit', 100),
                        ('offset', 0)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/Pikha/v1/primaryData',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_secondary_data(self):
        """Test case for controller_get_secondary_data

        All TMD (secondary) readings, with optional filtering & pagination
        """
        query_string = [('place_type', 'place_type_example'),
                        ('start', '2013-10-20T19:20:30+01:00'),
                        ('end', '2013-10-20T19:20:30+01:00'),
                        ('limit', 100),
                        ('offset', 0)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/Pikha/v1/secondaryData',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
