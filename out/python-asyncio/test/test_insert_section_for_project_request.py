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

from asana_asyncio.models.insert_section_for_project_request import InsertSectionForProjectRequest

class TestInsertSectionForProjectRequest(unittest.TestCase):
    """InsertSectionForProjectRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsertSectionForProjectRequest:
        """Test InsertSectionForProjectRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsertSectionForProjectRequest`
        """
        model = InsertSectionForProjectRequest()
        if include_optional:
            return InsertSectionForProjectRequest(
                data = asana_asyncio.models.project_section_insert_request.ProjectSectionInsertRequest(
                    section = '321654', 
                    before_section = '86420', 
                    after_section = '987654', )
            )
        else:
            return InsertSectionForProjectRequest(
        )
        """

    def testInsertSectionForProjectRequest(self):
        """Test InsertSectionForProjectRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()