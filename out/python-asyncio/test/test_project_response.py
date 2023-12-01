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

from asana_asyncio.models.project_response import ProjectResponse

class TestProjectResponse(unittest.TestCase):
    """ProjectResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectResponse:
        """Test ProjectResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectResponse`
        """
        model = ProjectResponse()
        if include_optional:
            return ProjectResponse(
                gid = '12345',
                resource_type = 'task',
                name = 'Stuff to buy',
                archived = False,
                color = 'light-green',
                created_at = '2012-02-22T02:06:58.147Z',
                current_status = None,
                current_status_update = None,
                custom_field_settings = [
                    null
                    ],
                default_view = 'calendar',
                due_date = 'Sun Sep 15 00:00:00 UTC 2019',
                due_on = 'Sun Sep 15 00:00:00 UTC 2019',
                html_notes = '<body>These are things we need to purchase.</body>',
                members = [
                    null
                    ],
                modified_at = '2012-02-22T02:06:58.147Z',
                notes = 'These are things we need to purchase.',
                public = False,
                start_on = 'Sat Sep 14 00:00:00 UTC 2019',
                default_access_level = 'admin',
                minimum_access_level_for_customization = 'admin',
                minimum_access_level_for_sharing = 'admin',
                custom_fields = [
                    null
                    ],
                completed = False,
                completed_at = '2012-02-22T02:06:58.147Z',
                completed_by = None,
                followers = [
                    null
                    ],
                owner = None,
                team = None,
                icon = 'chat_bubbles',
                permalink_url = 'https://app.asana.com/0/resource/123456789/list',
                project_brief = None,
                created_from_template = None,
                workspace = None
            )
        else:
            return ProjectResponse(
        )
        """

    def testProjectResponse(self):
        """Test ProjectResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()