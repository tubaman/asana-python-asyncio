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

from asana_asyncio.models.time_tracking_entry_compact import TimeTrackingEntryCompact

class TestTimeTrackingEntryCompact(unittest.TestCase):
    """TimeTrackingEntryCompact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeTrackingEntryCompact:
        """Test TimeTrackingEntryCompact
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeTrackingEntryCompact`
        """
        model = TimeTrackingEntryCompact()
        if include_optional:
            return TimeTrackingEntryCompact(
                gid = '12345',
                resource_type = 'task',
                duration_minutes = 12,
                entered_on = 'Sat Mar 14 00:00:00 UTC 2015',
                created_by = None
            )
        else:
            return TimeTrackingEntryCompact(
        )
        """

    def testTimeTrackingEntryCompact(self):
        """Test TimeTrackingEntryCompact"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
