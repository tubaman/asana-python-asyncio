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

from asana_asyncio.models.time_period_base_all_of_parent import TimePeriodBaseAllOfParent

class TestTimePeriodBaseAllOfParent(unittest.TestCase):
    """TimePeriodBaseAllOfParent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimePeriodBaseAllOfParent:
        """Test TimePeriodBaseAllOfParent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimePeriodBaseAllOfParent`
        """
        model = TimePeriodBaseAllOfParent()
        if include_optional:
            return TimePeriodBaseAllOfParent(
                gid = '12345',
                resource_type = 'task',
                end_on = '2019-09-14',
                start_on = '2019-09-13',
                period = 'Q1',
                display_name = 'Q1 FY22'
            )
        else:
            return TimePeriodBaseAllOfParent(
        )
        """

    def testTimePeriodBaseAllOfParent(self):
        """Test TimePeriodBaseAllOfParent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
