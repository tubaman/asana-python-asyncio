# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from asana_asyncio.api.workspaces_api import WorkspacesApi


class TestWorkspacesApi(unittest.TestCase):
    """WorkspacesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = WorkspacesApi()

    def tearDown(self) -> None:
        pass

    def test_add_user_for_workspace(self) -> None:
        """Test case for add_user_for_workspace

        Add a user to a workspace or organization
        """
        pass

    def test_get_workspace(self) -> None:
        """Test case for get_workspace

        Get a workspace
        """
        pass

    def test_get_workspaces(self) -> None:
        """Test case for get_workspaces

        Get multiple workspaces
        """
        pass

    def test_remove_user_for_workspace(self) -> None:
        """Test case for remove_user_for_workspace

        Remove a user from a workspace or organization
        """
        pass

    def test_update_workspace(self) -> None:
        """Test case for update_workspace

        Update a workspace
        """
        pass


if __name__ == '__main__':
    unittest.main()
