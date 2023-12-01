# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from asana_asyncio.api.project_briefs_api import ProjectBriefsApi


class TestProjectBriefsApi(unittest.TestCase):
    """ProjectBriefsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectBriefsApi()

    def tearDown(self) -> None:
        pass

    def test_create_project_brief(self) -> None:
        """Test case for create_project_brief

        Create a project brief
        """
        pass

    def test_delete_project_brief(self) -> None:
        """Test case for delete_project_brief

        Delete a project brief
        """
        pass

    def test_get_project_brief(self) -> None:
        """Test case for get_project_brief

        Get a project brief
        """
        pass

    def test_update_project_brief(self) -> None:
        """Test case for update_project_brief

        Update a project brief
        """
        pass


if __name__ == '__main__':
    unittest.main()
