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

from asana_asyncio.models.webhook_update_request import WebhookUpdateRequest

class TestWebhookUpdateRequest(unittest.TestCase):
    """WebhookUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebhookUpdateRequest:
        """Test WebhookUpdateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebhookUpdateRequest`
        """
        model = WebhookUpdateRequest()
        if include_optional:
            return WebhookUpdateRequest(
                filters = [
                    null
                    ]
            )
        else:
            return WebhookUpdateRequest(
        )
        """

    def testWebhookUpdateRequest(self):
        """Test WebhookUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
