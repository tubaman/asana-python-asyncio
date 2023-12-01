# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from asana_asyncio.models.project_brief_compact import ProjectBriefCompact

class TestProjectBriefCompact(unittest.TestCase):
    """ProjectBriefCompact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectBriefCompact:
        """Test ProjectBriefCompact
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectBriefCompact`
        """
        model = ProjectBriefCompact()
        if include_optional:
            return ProjectBriefCompact(
                gid = '12345',
                resource_type = 'task'
            )
        else:
            return ProjectBriefCompact(
        )
        """

    def testProjectBriefCompact(self):
        """Test ProjectBriefCompact"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()