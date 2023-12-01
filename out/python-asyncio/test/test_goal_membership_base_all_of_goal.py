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

from asana_asyncio.models.goal_membership_base_all_of_goal import GoalMembershipBaseAllOfGoal

class TestGoalMembershipBaseAllOfGoal(unittest.TestCase):
    """GoalMembershipBaseAllOfGoal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GoalMembershipBaseAllOfGoal:
        """Test GoalMembershipBaseAllOfGoal
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GoalMembershipBaseAllOfGoal`
        """
        model = GoalMembershipBaseAllOfGoal()
        if include_optional:
            return GoalMembershipBaseAllOfGoal(
                gid = '12345',
                resource_type = 'task',
                name = 'Grow web traffic by 30%',
                owner = None
            )
        else:
            return GoalMembershipBaseAllOfGoal(
        )
        """

    def testGoalMembershipBaseAllOfGoal(self):
        """Test GoalMembershipBaseAllOfGoal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
