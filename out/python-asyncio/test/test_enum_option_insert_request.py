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

from asana_asyncio.models.enum_option_insert_request import EnumOptionInsertRequest

class TestEnumOptionInsertRequest(unittest.TestCase):
    """EnumOptionInsertRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnumOptionInsertRequest:
        """Test EnumOptionInsertRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnumOptionInsertRequest`
        """
        model = EnumOptionInsertRequest()
        if include_optional:
            return EnumOptionInsertRequest(
                enum_option = '97285',
                before_enum_option = '12345',
                after_enum_option = '12345'
            )
        else:
            return EnumOptionInsertRequest(
                enum_option = '97285',
        )
        """

    def testEnumOptionInsertRequest(self):
        """Test EnumOptionInsertRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()