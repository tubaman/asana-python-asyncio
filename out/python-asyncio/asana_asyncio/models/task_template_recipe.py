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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
from asana_asyncio.models.attachment_compact import AttachmentCompact
from asana_asyncio.models.custom_field_compact import CustomFieldCompact
from asana_asyncio.models.project_compact import ProjectCompact
from asana_asyncio.models.task_template_recipe_compact import TaskTemplateRecipeCompact
from asana_asyncio.models.user_compact import UserCompact
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TaskTemplateRecipe(BaseModel):
    """
    TaskTemplateRecipe
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Name of the task that will be created from this template.")
    task_resource_subtype: Optional[StrictStr] = Field(default=None, description="The subtype of the task that will be created from this template.")
    description: Optional[StrictStr] = Field(default=None, description="Description of the task that will be created from this template.")
    html_description: Optional[StrictStr] = Field(default=None, description="HTML description of the task that will be created from this template.")
    memberships: Optional[List[ProjectCompact]] = Field(default=None, description="Array of projects that the task created from this template will be added to")
    relative_start_on: Optional[StrictInt] = Field(default=None, description="The number of days after the task has been instantiated on which that the task will start")
    relative_due_on: Optional[StrictInt] = Field(default=None, description="The number of days after the task has been instantiated on which that the task will be due")
    due_time: Optional[StrictStr] = Field(default=None, description="The time of day that the task will be due")
    dependencies: Optional[List[TaskTemplateRecipeCompact]] = Field(default=None, description="Array of task templates that the task created from this template will depend on")
    dependents: Optional[List[TaskTemplateRecipeCompact]] = Field(default=None, description="Array of task templates that will depend on the task created from this template")
    followers: Optional[List[UserCompact]] = Field(default=None, description="Array of users that will be added as followers to the task created from this template")
    attachments: Optional[List[AttachmentCompact]] = Field(default=None, description="Array of attachments that will be added to the task created from this template")
    subtasks: Optional[List[TaskTemplateRecipeCompact]] = Field(default=None, description="Array of subtasks that will be added to the task created from this template")
    custom_fields: Optional[List[CustomFieldCompact]] = Field(default=None, description="Array of custom fields that will be added to the task created from this template")
    __properties: ClassVar[List[str]] = ["name", "task_resource_subtype", "description", "html_description", "memberships", "relative_start_on", "relative_due_on", "due_time", "dependencies", "dependents", "followers", "attachments", "subtasks", "custom_fields"]

    @field_validator('task_resource_subtype')
    def task_resource_subtype_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('default_task', 'milestone_task', 'approval_task'):
            raise ValueError("must be one of enum values ('default_task', 'milestone_task', 'approval_task')")
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
        """Create an instance of TaskTemplateRecipe from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in memberships (list)
        _items = []
        if self.memberships:
            for _item in self.memberships:
                if _item:
                    _items.append(_item.to_dict())
            _dict['memberships'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in dependencies (list)
        _items = []
        if self.dependencies:
            for _item in self.dependencies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dependencies'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in dependents (list)
        _items = []
        if self.dependents:
            for _item in self.dependents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dependents'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in followers (list)
        _items = []
        if self.followers:
            for _item in self.followers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['followers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item in self.attachments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attachments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in subtasks (list)
        _items = []
        if self.subtasks:
            for _item in self.subtasks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['subtasks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in custom_fields (list)
        _items = []
        if self.custom_fields:
            for _item in self.custom_fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['custom_fields'] = _items
        # set to None if relative_start_on (nullable) is None
        # and model_fields_set contains the field
        if self.relative_start_on is None and "relative_start_on" in self.model_fields_set:
            _dict['relative_start_on'] = None

        # set to None if relative_due_on (nullable) is None
        # and model_fields_set contains the field
        if self.relative_due_on is None and "relative_due_on" in self.model_fields_set:
            _dict['relative_due_on'] = None

        # set to None if due_time (nullable) is None
        # and model_fields_set contains the field
        if self.due_time is None and "due_time" in self.model_fields_set:
            _dict['due_time'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TaskTemplateRecipe from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "task_resource_subtype": obj.get("task_resource_subtype"),
            "description": obj.get("description"),
            "html_description": obj.get("html_description"),
            "memberships": [ProjectCompact.from_dict(_item) for _item in obj.get("memberships")] if obj.get("memberships") is not None else None,
            "relative_start_on": obj.get("relative_start_on"),
            "relative_due_on": obj.get("relative_due_on"),
            "due_time": obj.get("due_time"),
            "dependencies": [TaskTemplateRecipeCompact.from_dict(_item) for _item in obj.get("dependencies")] if obj.get("dependencies") is not None else None,
            "dependents": [TaskTemplateRecipeCompact.from_dict(_item) for _item in obj.get("dependents")] if obj.get("dependents") is not None else None,
            "followers": [UserCompact.from_dict(_item) for _item in obj.get("followers")] if obj.get("followers") is not None else None,
            "attachments": [AttachmentCompact.from_dict(_item) for _item in obj.get("attachments")] if obj.get("attachments") is not None else None,
            "subtasks": [TaskTemplateRecipeCompact.from_dict(_item) for _item in obj.get("subtasks")] if obj.get("subtasks") is not None else None,
            "custom_fields": [CustomFieldCompact.from_dict(_item) for _item in obj.get("custom_fields")] if obj.get("custom_fields") is not None else None
        })
        return _obj


