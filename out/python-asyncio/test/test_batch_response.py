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

from asana_asyncio.models.batch_response import BatchResponse

class TestBatchResponse(unittest.TestCase):
    """BatchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BatchResponse:
        """Test BatchResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BatchResponse`
        """
        model = BatchResponse()
        if include_optional:
            return BatchResponse(
                status_code = 200,
                headers = {"location":"/tasks/1234"},
                body = {"data":{"gid":"1967","completed":false,"name":"Hello, world!","notes":"How are you today?"}}
            )
        else:
            return BatchResponse(
        )
        """

    def testBatchResponse(self):
        """Test BatchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()