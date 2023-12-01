# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from asana_asyncio.api.user_task_lists_api import UserTaskListsApi


class TestUserTaskListsApi(unittest.TestCase):
    """UserTaskListsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserTaskListsApi()

    def tearDown(self) -> None:
        pass

    def test_get_user_task_list(self) -> None:
        """Test case for get_user_task_list

        Get a user task list
        """
        pass

    def test_get_user_task_list_for_user(self) -> None:
        """Test case for get_user_task_list_for_user

        Get a user's task list
        """
        pass


if __name__ == '__main__':
    unittest.main()