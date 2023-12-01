# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, field_validator
from pydantic import Field
from asana_asyncio.models.custom_field_compact import CustomFieldCompact
from asana_asyncio.models.enum_option import EnumOption
from asana_asyncio.models.like import Like
from asana_asyncio.models.preview import Preview
from asana_asyncio.models.project_compact import ProjectCompact
from asana_asyncio.models.section_compact import SectionCompact
from asana_asyncio.models.story_compact import StoryCompact
from asana_asyncio.models.story_response_all_of_new_date_value import StoryResponseAllOfNewDateValue
from asana_asyncio.models.story_response_all_of_old_date_value import StoryResponseAllOfOldDateValue
from asana_asyncio.models.story_response_all_of_target import StoryResponseAllOfTarget
from asana_asyncio.models.story_response_dates import StoryResponseDates
from asana_asyncio.models.tag_compact import TagCompact
from asana_asyncio.models.task_compact import TaskCompact
from asana_asyncio.models.user_compact import UserCompact
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class StoryResponse(BaseModel):
    """
    StoryResponse
    """ # noqa: E501
    gid: Optional[StrictStr] = Field(default=None, description="Globally unique identifier of the resource, as a string.")
    resource_type: Optional[StrictStr] = Field(default=None, description="The base type of this resource.")
    created_at: Optional[datetime] = Field(default=None, description="The time at which this resource was created.")
    resource_subtype: Optional[StrictStr] = Field(default=None, description="The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning.")
    text: Optional[StrictStr] = Field(default=None, description="The plain text of the comment to add. Cannot be used with html_text.")
    html_text: Optional[StrictStr] = Field(default=None, description="[Opt In](/docs/inputoutput-options). HTML formatted text for a comment. This will not include the name of the creator.")
    is_pinned: Optional[StrictBool] = Field(default=None, description="*Conditional*. Whether the story should be pinned on the resource.")
    sticker_name: Optional[StrictStr] = Field(default=None, description="The name of the sticker in this story. `null` if there is no sticker.")
    created_by: Optional[UserCompact] = None
    type: Optional[StrictStr] = None
    is_editable: Optional[StrictBool] = Field(default=None, description="*Conditional*. Whether the text of the story can be edited after creation.")
    is_edited: Optional[StrictBool] = Field(default=None, description="*Conditional*. Whether the text of the story has been edited after creation.")
    hearted: Optional[StrictBool] = Field(default=None, description="*Deprecated - please use likes instead* *Conditional*. True if the story is hearted by the authorized user, false if not.")
    hearts: Optional[List[Like]] = Field(default=None, description="*Deprecated - please use likes instead*  *Conditional*. Array of likes for users who have hearted this story.")
    num_hearts: Optional[StrictInt] = Field(default=None, description="*Deprecated - please use likes instead*  *Conditional*. The number of users who have hearted this story.")
    liked: Optional[StrictBool] = Field(default=None, description="*Conditional*. True if the story is liked by the authorized user, false if not.")
    likes: Optional[List[Like]] = Field(default=None, description="*Conditional*. Array of likes for users who have liked this story.")
    num_likes: Optional[StrictInt] = Field(default=None, description="*Conditional*. The number of users who have liked this story.")
    previews: Optional[List[Preview]] = Field(default=None, description="*Conditional*. A collection of previews to be displayed in the story.  *Note: This property only exists for comment stories.*")
    old_name: Optional[StrictStr] = Field(default=None, description="*Conditional*'")
    new_name: Optional[StrictStr] = Field(default=None, description="*Conditional*")
    old_dates: Optional[StoryResponseDates] = None
    new_dates: Optional[StoryResponseDates] = None
    old_resource_subtype: Optional[StrictStr] = Field(default=None, description="*Conditional*")
    new_resource_subtype: Optional[StrictStr] = Field(default=None, description="*Conditional*")
    story: Optional[StoryCompact] = None
    assignee: Optional[UserCompact] = None
    follower: Optional[UserCompact] = None
    old_section: Optional[SectionCompact] = None
    new_section: Optional[SectionCompact] = None
    task: Optional[TaskCompact] = None
    project: Optional[ProjectCompact] = None
    tag: Optional[TagCompact] = None
    custom_field: Optional[CustomFieldCompact] = None
    old_text_value: Optional[StrictStr] = Field(default=None, description="*Conditional*")
    new_text_value: Optional[StrictStr] = Field(default=None, description="*Conditional*")
    old_number_value: Optional[StrictInt] = Field(default=None, description="*Conditional*")
    new_number_value: Optional[StrictInt] = Field(default=None, description="*Conditional*")
    old_enum_value: Optional[EnumOption] = None
    new_enum_value: Optional[EnumOption] = None
    old_date_value: Optional[StoryResponseAllOfOldDateValue] = None
    new_date_value: Optional[StoryResponseAllOfNewDateValue] = None
    old_people_value: Optional[List[UserCompact]] = Field(default=None, description="*Conditional*. The old value of a people custom field story.")
    new_people_value: Optional[List[UserCompact]] = Field(default=None, description="*Conditional*. The new value of a people custom field story.")
    old_multi_enum_values: Optional[List[EnumOption]] = Field(default=None, description="*Conditional*. The old value of a multi-enum custom field story.")
    new_multi_enum_values: Optional[List[EnumOption]] = Field(default=None, description="*Conditional*. The new value of a multi-enum custom field story.")
    new_approval_status: Optional[StrictStr] = Field(default=None, description="*Conditional*. The new value of approval status.")
    old_approval_status: Optional[StrictStr] = Field(default=None, description="*Conditional*. The old value of approval status.")
    duplicate_of: Optional[TaskCompact] = None
    duplicated_from: Optional[TaskCompact] = None
    dependency: Optional[TaskCompact] = None
    source: Optional[StrictStr] = Field(default=None, description="The component of the Asana product the user used to trigger the story.")
    target: Optional[StoryResponseAllOfTarget] = None
    __properties: ClassVar[List[str]] = ["gid", "resource_type", "created_at", "resource_subtype", "text", "html_text", "is_pinned", "sticker_name", "created_by", "type", "is_editable", "is_edited", "hearted", "hearts", "num_hearts", "liked", "likes", "num_likes", "previews", "old_name", "new_name", "old_dates", "new_dates", "old_resource_subtype", "new_resource_subtype", "story", "assignee", "follower", "old_section", "new_section", "task", "project", "tag", "custom_field", "old_text_value", "new_text_value", "old_number_value", "new_number_value", "old_enum_value", "new_enum_value", "old_date_value", "new_date_value", "old_people_value", "new_people_value", "old_multi_enum_values", "new_multi_enum_values", "new_approval_status", "old_approval_status", "duplicate_of", "duplicated_from", "dependency", "source", "target"]

    @field_validator('sticker_name')
    def sticker_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('green_checkmark', 'people_dancing', 'dancing_unicorn', 'heart', 'party_popper', 'people_waving_flags', 'splashing_narwhal', 'trophy', 'yeti_riding_unicorn', 'celebrating_people', 'determined_climbers', 'phoenix_spreading_love'):
            raise ValueError("must be one of enum values ('green_checkmark', 'people_dancing', 'dancing_unicorn', 'heart', 'party_popper', 'people_waving_flags', 'splashing_narwhal', 'trophy', 'yeti_riding_unicorn', 'celebrating_people', 'determined_climbers', 'phoenix_spreading_love')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('comment', 'system'):
            raise ValueError("must be one of enum values ('comment', 'system')")
        return value

    @field_validator('source')
    def source_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('web', 'email', 'mobile', 'api', 'unknown'):
            raise ValueError("must be one of enum values ('web', 'email', 'mobile', 'api', 'unknown')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StoryResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "gid",
                "resource_type",
                "created_at",
                "resource_subtype",
                "type",
                "is_editable",
                "is_edited",
                "hearted",
                "hearts",
                "num_hearts",
                "liked",
                "likes",
                "num_likes",
                "previews",
                "new_name",
                "old_resource_subtype",
                "new_resource_subtype",
                "old_text_value",
                "new_text_value",
                "old_number_value",
                "new_number_value",
                "old_people_value",
                "new_people_value",
                "old_multi_enum_values",
                "new_multi_enum_values",
                "new_approval_status",
                "old_approval_status",
                "source",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in hearts (list)
        _items = []
        if self.hearts:
            for _item in self.hearts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['hearts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in likes (list)
        _items = []
        if self.likes:
            for _item in self.likes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['likes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in previews (list)
        _items = []
        if self.previews:
            for _item in self.previews:
                if _item:
                    _items.append(_item.to_dict())
            _dict['previews'] = _items
        # override the default output from pydantic by calling `to_dict()` of old_dates
        if self.old_dates:
            _dict['old_dates'] = self.old_dates.to_dict()
        # override the default output from pydantic by calling `to_dict()` of new_dates
        if self.new_dates:
            _dict['new_dates'] = self.new_dates.to_dict()
        # override the default output from pydantic by calling `to_dict()` of story
        if self.story:
            _dict['story'] = self.story.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assignee
        if self.assignee:
            _dict['assignee'] = self.assignee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of follower
        if self.follower:
            _dict['follower'] = self.follower.to_dict()
        # override the default output from pydantic by calling `to_dict()` of old_section
        if self.old_section:
            _dict['old_section'] = self.old_section.to_dict()
        # override the default output from pydantic by calling `to_dict()` of new_section
        if self.new_section:
            _dict['new_section'] = self.new_section.to_dict()
        # override the default output from pydantic by calling `to_dict()` of task
        if self.task:
            _dict['task'] = self.task.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tag
        if self.tag:
            _dict['tag'] = self.tag.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_field
        if self.custom_field:
            _dict['custom_field'] = self.custom_field.to_dict()
        # override the default output from pydantic by calling `to_dict()` of old_enum_value
        if self.old_enum_value:
            _dict['old_enum_value'] = self.old_enum_value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of new_enum_value
        if self.new_enum_value:
            _dict['new_enum_value'] = self.new_enum_value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of old_date_value
        if self.old_date_value:
            _dict['old_date_value'] = self.old_date_value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of new_date_value
        if self.new_date_value:
            _dict['new_date_value'] = self.new_date_value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in old_people_value (list)
        _items = []
        if self.old_people_value:
            for _item in self.old_people_value:
                if _item:
                    _items.append(_item.to_dict())
            _dict['old_people_value'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in new_people_value (list)
        _items = []
        if self.new_people_value:
            for _item in self.new_people_value:
                if _item:
                    _items.append(_item.to_dict())
            _dict['new_people_value'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in old_multi_enum_values (list)
        _items = []
        if self.old_multi_enum_values:
            for _item in self.old_multi_enum_values:
                if _item:
                    _items.append(_item.to_dict())
            _dict['old_multi_enum_values'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in new_multi_enum_values (list)
        _items = []
        if self.new_multi_enum_values:
            for _item in self.new_multi_enum_values:
                if _item:
                    _items.append(_item.to_dict())
            _dict['new_multi_enum_values'] = _items
        # override the default output from pydantic by calling `to_dict()` of duplicate_of
        if self.duplicate_of:
            _dict['duplicate_of'] = self.duplicate_of.to_dict()
        # override the default output from pydantic by calling `to_dict()` of duplicated_from
        if self.duplicated_from:
            _dict['duplicated_from'] = self.duplicated_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dependency
        if self.dependency:
            _dict['dependency'] = self.dependency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target
        if self.target:
            _dict['target'] = self.target.to_dict()
        # set to None if new_name (nullable) is None
        # and model_fields_set contains the field
        if self.new_name is None and "new_name" in self.model_fields_set:
            _dict['new_name'] = None

        # set to None if old_number_value (nullable) is None
        # and model_fields_set contains the field
        if self.old_number_value is None and "old_number_value" in self.model_fields_set:
            _dict['old_number_value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of StoryResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gid": obj.get("gid"),
            "resource_type": obj.get("resource_type"),
            "created_at": obj.get("created_at"),
            "resource_subtype": obj.get("resource_subtype"),
            "text": obj.get("text"),
            "html_text": obj.get("html_text"),
            "is_pinned": obj.get("is_pinned"),
            "sticker_name": obj.get("sticker_name"),
            "created_by": UserCompact.from_dict(obj.get("created_by")) if obj.get("created_by") is not None else None,
            "type": obj.get("type"),
            "is_editable": obj.get("is_editable"),
            "is_edited": obj.get("is_edited"),
            "hearted": obj.get("hearted"),
            "hearts": [Like.from_dict(_item) for _item in obj.get("hearts")] if obj.get("hearts") is not None else None,
            "num_hearts": obj.get("num_hearts"),
            "liked": obj.get("liked"),
            "likes": [Like.from_dict(_item) for _item in obj.get("likes")] if obj.get("likes") is not None else None,
            "num_likes": obj.get("num_likes"),
            "previews": [Preview.from_dict(_item) for _item in obj.get("previews")] if obj.get("previews") is not None else None,
            "old_name": obj.get("old_name"),
            "new_name": obj.get("new_name"),
            "old_dates": StoryResponseDates.from_dict(obj.get("old_dates")) if obj.get("old_dates") is not None else None,
            "new_dates": StoryResponseDates.from_dict(obj.get("new_dates")) if obj.get("new_dates") is not None else None,
            "old_resource_subtype": obj.get("old_resource_subtype"),
            "new_resource_subtype": obj.get("new_resource_subtype"),
            "story": StoryCompact.from_dict(obj.get("story")) if obj.get("story") is not None else None,
            "assignee": UserCompact.from_dict(obj.get("assignee")) if obj.get("assignee") is not None else None,
            "follower": UserCompact.from_dict(obj.get("follower")) if obj.get("follower") is not None else None,
            "old_section": SectionCompact.from_dict(obj.get("old_section")) if obj.get("old_section") is not None else None,
            "new_section": SectionCompact.from_dict(obj.get("new_section")) if obj.get("new_section") is not None else None,
            "task": TaskCompact.from_dict(obj.get("task")) if obj.get("task") is not None else None,
            "project": ProjectCompact.from_dict(obj.get("project")) if obj.get("project") is not None else None,
            "tag": TagCompact.from_dict(obj.get("tag")) if obj.get("tag") is not None else None,
            "custom_field": CustomFieldCompact.from_dict(obj.get("custom_field")) if obj.get("custom_field") is not None else None,
            "old_text_value": obj.get("old_text_value"),
            "new_text_value": obj.get("new_text_value"),
            "old_number_value": obj.get("old_number_value"),
            "new_number_value": obj.get("new_number_value"),
            "old_enum_value": EnumOption.from_dict(obj.get("old_enum_value")) if obj.get("old_enum_value") is not None else None,
            "new_enum_value": EnumOption.from_dict(obj.get("new_enum_value")) if obj.get("new_enum_value") is not None else None,
            "old_date_value": StoryResponseAllOfOldDateValue.from_dict(obj.get("old_date_value")) if obj.get("old_date_value") is not None else None,
            "new_date_value": StoryResponseAllOfNewDateValue.from_dict(obj.get("new_date_value")) if obj.get("new_date_value") is not None else None,
            "old_people_value": [UserCompact.from_dict(_item) for _item in obj.get("old_people_value")] if obj.get("old_people_value") is not None else None,
            "new_people_value": [UserCompact.from_dict(_item) for _item in obj.get("new_people_value")] if obj.get("new_people_value") is not None else None,
            "old_multi_enum_values": [EnumOption.from_dict(_item) for _item in obj.get("old_multi_enum_values")] if obj.get("old_multi_enum_values") is not None else None,
            "new_multi_enum_values": [EnumOption.from_dict(_item) for _item in obj.get("new_multi_enum_values")] if obj.get("new_multi_enum_values") is not None else None,
            "new_approval_status": obj.get("new_approval_status"),
            "old_approval_status": obj.get("old_approval_status"),
            "duplicate_of": TaskCompact.from_dict(obj.get("duplicate_of")) if obj.get("duplicate_of") is not None else None,
            "duplicated_from": TaskCompact.from_dict(obj.get("duplicated_from")) if obj.get("duplicated_from") is not None else None,
            "dependency": TaskCompact.from_dict(obj.get("dependency")) if obj.get("dependency") is not None else None,
            "source": obj.get("source"),
            "target": StoryResponseAllOfTarget.from_dict(obj.get("target")) if obj.get("target") is not None else None
        })
        return _obj

