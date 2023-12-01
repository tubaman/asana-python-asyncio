# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from asana_asyncio.api.status_updates_api import StatusUpdatesApi


class TestStatusUpdatesApi(unittest.TestCase):
    """StatusUpdatesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StatusUpdatesApi()

    def tearDown(self) -> None:
        pass

    def test_create_status_for_object(self) -> None:
        """Test case for create_status_for_object

        Create a status update
        """
        pass

    def test_delete_status(self) -> None:
        """Test case for delete_status

        Delete a status update
        """
        pass

    def test_get_status(self) -> None:
        """Test case for get_status

        Get a status update
        """
        pass

    def test_get_statuses_for_object(self) -> None:
        """Test case for get_statuses_for_object

        Get status updates from an object
        """
        pass


if __name__ == '__main__':
    unittest.main()
