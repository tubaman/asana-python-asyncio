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

from asana_asyncio.models.goal_update_request import GoalUpdateRequest

class TestGoalUpdateRequest(unittest.TestCase):
    """GoalUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GoalUpdateRequest:
        """Test GoalUpdateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GoalUpdateRequest`
        """
        model = GoalUpdateRequest()
        if include_optional:
            return GoalUpdateRequest(
                gid = '12345',
                resource_type = 'task',
                name = 'Grow web traffic by 30%',
                html_notes = '<body>Start building brand awareness.</body>',
                notes = 'Start building brand awareness.',
                due_on = '2019-09-15',
                start_on = '2019-09-14',
                is_workspace_level = True,
                liked = False,
                team = '12345',
                workspace = '12345',
                time_period = '12345',
                owner = '12345',
                status = 'green'
            )
        else:
            return GoalUpdateRequest(
        )
        """

    def testGoalUpdateRequest(self):
        """Test GoalUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
