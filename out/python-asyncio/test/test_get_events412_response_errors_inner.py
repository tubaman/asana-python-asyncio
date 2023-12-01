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

from asana_asyncio.models.get_events412_response_errors_inner import GetEvents412ResponseErrorsInner

class TestGetEvents412ResponseErrorsInner(unittest.TestCase):
    """GetEvents412ResponseErrorsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetEvents412ResponseErrorsInner:
        """Test GetEvents412ResponseErrorsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetEvents412ResponseErrorsInner`
        """
        model = GetEvents412ResponseErrorsInner()
        if include_optional:
            return GetEvents412ResponseErrorsInner(
                message = 'Sync token invalid or too old. If you are attempting to keep resources in sync, you must fetch the full dataset for this query now and use the new sync token for the next sync.'
            )
        else:
            return GetEvents412ResponseErrorsInner(
        )
        """

    def testGetEvents412ResponseErrorsInner(self):
        """Test GetEvents412ResponseErrorsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
