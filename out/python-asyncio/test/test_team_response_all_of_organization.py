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

from asana_asyncio.models.team_response_all_of_organization import TeamResponseAllOfOrganization

class TestTeamResponseAllOfOrganization(unittest.TestCase):
    """TeamResponseAllOfOrganization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamResponseAllOfOrganization:
        """Test TeamResponseAllOfOrganization
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamResponseAllOfOrganization`
        """
        model = TeamResponseAllOfOrganization()
        if include_optional:
            return TeamResponseAllOfOrganization(
                gid = '12345',
                resource_type = 'task',
                name = 'My Company Workspace'
            )
        else:
            return TeamResponseAllOfOrganization(
        )
        """

    def testTeamResponseAllOfOrganization(self):
        """Test TeamResponseAllOfOrganization"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()