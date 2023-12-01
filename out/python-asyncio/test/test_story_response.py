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

from asana_asyncio.models.story_response import StoryResponse

class TestStoryResponse(unittest.TestCase):
    """StoryResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StoryResponse:
        """Test StoryResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StoryResponse`
        """
        model = StoryResponse()
        if include_optional:
            return StoryResponse(
                gid = '12345',
                resource_type = 'task',
                created_at = '2012-02-22T02:06:58.147Z',
                resource_subtype = 'comment_added',
                text = 'This is a comment.',
                html_text = '<body>This is a comment.</body>',
                is_pinned = False,
                sticker_name = 'dancing_unicorn',
                created_by = None,
                type = 'comment',
                is_editable = False,
                is_edited = False,
                hearted = False,
                hearts = [
                    asana_asyncio.models.like.Like(
                        gid = '12345', 
                        user = null, )
                    ],
                num_hearts = 5,
                liked = False,
                likes = [
                    asana_asyncio.models.like.Like(
                        gid = '12345', 
                        user = null, )
                    ],
                num_likes = 5,
                previews = [
                    asana_asyncio.models.preview.Preview(
                        fallback = 'Greg: Great! I like this idea.\n\nhttps//a_company.slack.com/archives/ABCDEFG/12345678', 
                        footer = 'Mar 17, 2019 1:25 PM', 
                        header = 'Asana for Slack', 
                        header_link = 'https://asana.comn/apps/slack', 
                        html_text = '<body>Great! I like this idea.</body>', 
                        text = 'Great! I like this idea.', 
                        title = 'Greg', 
                        title_link = 'https://asana.slack.com/archives/ABCDEFG/12345678', )
                    ],
                old_name = 'This was the Old Name',
                new_name = 'This is the New Name',
                old_dates = asana_asyncio.models.story_response_dates.StoryResponseDates(
                    start_on = 'Sat Sep 14 00:00:00 UTC 2019', 
                    due_at = '2019-09-15T02:06:58.158Z', 
                    due_on = 'Sun Sep 15 00:00:00 UTC 2019', ),
                new_dates = asana_asyncio.models.story_response_dates.StoryResponseDates(
                    start_on = 'Sat Sep 14 00:00:00 UTC 2019', 
                    due_at = '2019-09-15T02:06:58.158Z', 
                    due_on = 'Sun Sep 15 00:00:00 UTC 2019', ),
                old_resource_subtype = 'default_task',
                new_resource_subtype = 'milestone',
                story = None,
                assignee = None,
                follower = None,
                old_section = None,
                new_section = None,
                task = None,
                project = None,
                tag = None,
                custom_field = None,
                old_text_value = 'This was the Old Text',
                new_text_value = 'This is the New Text',
                old_number_value = 1,
                new_number_value = 2,
                old_enum_value = None,
                new_enum_value = None,
                old_date_value = None,
                new_date_value = None,
                old_people_value = [
                    null
                    ],
                new_people_value = [
                    null
                    ],
                old_multi_enum_values = [
                    null
                    ],
                new_multi_enum_values = [
                    null
                    ],
                new_approval_status = 'approved',
                old_approval_status = 'pending',
                duplicate_of = None,
                duplicated_from = None,
                dependency = None,
                source = 'web',
                target = None
            )
        else:
            return StoryResponse(
        )
        """

    def testStoryResponse(self):
        """Test StoryResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()