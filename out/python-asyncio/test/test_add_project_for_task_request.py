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

from asana_asyncio.models.add_project_for_task_request import AddProjectForTaskRequest

class TestAddProjectForTaskRequest(unittest.TestCase):
    """AddProjectForTaskRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddProjectForTaskRequest:
        """Test AddProjectForTaskRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddProjectForTaskRequest`
        """
        model = AddProjectForTaskRequest()
        if include_optional:
            return AddProjectForTaskRequest(
                data = asana_asyncio.models.task_add_project_request.TaskAddProjectRequest(
                    project = '13579', 
                    insert_after = '124816', 
                    insert_before = '432134', 
                    section = '987654', )
            )
        else:
            return AddProjectForTaskRequest(
        )
        """

    def testAddProjectForTaskRequest(self):
        """Test AddProjectForTaskRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
