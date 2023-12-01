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

from asana_asyncio.models.get_memberships200_response import GetMemberships200Response

class TestGetMemberships200Response(unittest.TestCase):
    """GetMemberships200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetMemberships200Response:
        """Test GetMemberships200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetMemberships200Response`
        """
        model = GetMemberships200Response()
        if include_optional:
            return GetMemberships200Response(
                data = [
                    null
                    ],
                next_page = asana_asyncio.models.next_page.NextPage(
                    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9', 
                    path = '/tasks/12345/attachments?limit=2&offset=eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9', 
                    uri = 'https://app.asana.com/api/1.0/tasks/12345/attachments?limit=2&offset=eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9', )
            )
        else:
            return GetMemberships200Response(
        )
        """

    def testGetMemberships200Response(self):
        """Test GetMemberships200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
