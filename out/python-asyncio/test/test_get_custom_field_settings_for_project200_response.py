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

from asana_asyncio.models.get_custom_field_settings_for_project200_response import GetCustomFieldSettingsForProject200Response

class TestGetCustomFieldSettingsForProject200Response(unittest.TestCase):
    """GetCustomFieldSettingsForProject200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCustomFieldSettingsForProject200Response:
        """Test GetCustomFieldSettingsForProject200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCustomFieldSettingsForProject200Response`
        """
        model = GetCustomFieldSettingsForProject200Response()
        if include_optional:
            return GetCustomFieldSettingsForProject200Response(
                data = [
                    null
                    ],
                next_page = asana_asyncio.models.next_page.NextPage(
                    offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9', 
                    path = '/tasks/12345/attachments?limit=2&offset=eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9', 
                    uri = 'https://app.asana.com/api/1.0/tasks/12345/attachments?limit=2&offset=eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9', )
            )
        else:
            return GetCustomFieldSettingsForProject200Response(
        )
        """

    def testGetCustomFieldSettingsForProject200Response(self):
        """Test GetCustomFieldSettingsForProject200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
