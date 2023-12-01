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

from asana_asyncio.models.task_base_all_of_completed_by import TaskBaseAllOfCompletedBy

class TestTaskBaseAllOfCompletedBy(unittest.TestCase):
    """TaskBaseAllOfCompletedBy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TaskBaseAllOfCompletedBy:
        """Test TaskBaseAllOfCompletedBy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaskBaseAllOfCompletedBy`
        """
        model = TaskBaseAllOfCompletedBy()
        if include_optional:
            return TaskBaseAllOfCompletedBy(
                gid = '12345',
                resource_type = 'task',
                name = 'Greg Sanchez'
            )
        else:
            return TaskBaseAllOfCompletedBy(
        )
        """

    def testTaskBaseAllOfCompletedBy(self):
        """Test TaskBaseAllOfCompletedBy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()