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

from asana_asyncio.models.project_membership_compact_response import ProjectMembershipCompactResponse

class TestProjectMembershipCompactResponse(unittest.TestCase):
    """ProjectMembershipCompactResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectMembershipCompactResponse:
        """Test ProjectMembershipCompactResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectMembershipCompactResponse`
        """
        model = ProjectMembershipCompactResponse()
        if include_optional:
            return ProjectMembershipCompactResponse(
                gid = '12345',
                resource_type = 'membership',
                parent = None,
                member = None,
                access_level = 'admin',
                resource_subtype = 'project_membership'
            )
        else:
            return ProjectMembershipCompactResponse(
        )
        """

    def testProjectMembershipCompactResponse(self):
        """Test ProjectMembershipCompactResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
