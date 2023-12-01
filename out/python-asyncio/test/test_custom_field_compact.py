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

from asana_asyncio.models.custom_field_compact import CustomFieldCompact

class TestCustomFieldCompact(unittest.TestCase):
    """CustomFieldCompact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomFieldCompact:
        """Test CustomFieldCompact
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomFieldCompact`
        """
        model = CustomFieldCompact()
        if include_optional:
            return CustomFieldCompact(
                gid = '12345',
                resource_type = 'task',
                name = 'Status',
                resource_subtype = 'text',
                type = 'text',
                enum_options = [
                    null
                    ],
                enabled = True,
                is_formula_field = False,
                date_value = asana_asyncio.models.custom_field_compact_all_of_date_value.CustomFieldCompact_allOf_date_value(
                    date = '2024-08-23', 
                    date_time = '2024-08-23T22:00:00.000Z', ),
                enum_value = None,
                multi_enum_values = [
                    null
                    ],
                number_value = 5.2,
                text_value = 'Some Value',
                display_value = 'blue'
            )
        else:
            return CustomFieldCompact(
        )
        """

    def testCustomFieldCompact(self):
        """Test CustomFieldCompact"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
