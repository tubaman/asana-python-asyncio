# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from asana_asyncio.api.project_templates_api import ProjectTemplatesApi


class TestProjectTemplatesApi(unittest.TestCase):
    """ProjectTemplatesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectTemplatesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_project_template(self) -> None:
        """Test case for delete_project_template

        Delete a project template
        """
        pass

    def test_get_project_template(self) -> None:
        """Test case for get_project_template

        Get a project template
        """
        pass

    def test_get_project_templates(self) -> None:
        """Test case for get_project_templates

        Get multiple project templates
        """
        pass

    def test_get_project_templates_for_team(self) -> None:
        """Test case for get_project_templates_for_team

        Get a team's project templates
        """
        pass

    def test_instantiate_project(self) -> None:
        """Test case for instantiate_project

        Instantiate a project from a project template
        """
        pass


if __name__ == '__main__':
    unittest.main()
