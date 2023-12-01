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

from asana_asyncio.models.task_compact import TaskCompact

class TestTaskCompact(unittest.TestCase):
    """TaskCompact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TaskCompact:
        """Test TaskCompact
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaskCompact`
        """
        model = TaskCompact()
        if include_optional:
            return TaskCompact(
                gid = '12345',
                resource_type = 'task',
                name = 'Bug Task',
                resource_subtype = 'default_task',
                created_by = asana_asyncio.models.task_compact_all_of_created_by.TaskCompact_allOf_created_by(
                    gid = '1111', 
                    resource_type = 'user', )
            )
        else:
            return TaskCompact(
        )
        """

    def testTaskCompact(self):
        """Test TaskCompact"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()