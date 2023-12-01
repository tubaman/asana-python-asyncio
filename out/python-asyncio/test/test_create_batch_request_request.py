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

from asana_asyncio.models.create_batch_request_request import CreateBatchRequestRequest

class TestCreateBatchRequestRequest(unittest.TestCase):
    """CreateBatchRequestRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateBatchRequestRequest:
        """Test CreateBatchRequestRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateBatchRequestRequest`
        """
        model = CreateBatchRequestRequest()
        if include_optional:
            return CreateBatchRequestRequest(
                data = asana_asyncio.models.batch_request.BatchRequest(
                    actions = [
                        asana_asyncio.models.batch_request_action.BatchRequestAction(
                            relative_path = '/tasks/123', 
                            method = 'get', 
                            data = {"assignee":"me","workspace":"1337"}, 
                            options = {"limit":3,"fields":["name","notes","completed"]}, )
                        ], )
            )
        else:
            return CreateBatchRequestRequest(
        )
        """

    def testCreateBatchRequestRequest(self):
        """Test CreateBatchRequestRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
