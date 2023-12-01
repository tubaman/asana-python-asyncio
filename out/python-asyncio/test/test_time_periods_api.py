# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from asana_asyncio.api.time_periods_api import TimePeriodsApi


class TestTimePeriodsApi(unittest.TestCase):
    """TimePeriodsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TimePeriodsApi()

    def tearDown(self) -> None:
        pass

    def test_get_time_period(self) -> None:
        """Test case for get_time_period

        Get a time period
        """
        pass

    def test_get_time_periods(self) -> None:
        """Test case for get_time_periods

        Get time periods
        """
        pass


if __name__ == '__main__':
    unittest.main()