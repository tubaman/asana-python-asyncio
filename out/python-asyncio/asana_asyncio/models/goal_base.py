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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GoalBase(BaseModel):
    """
    GoalBase
    """ # noqa: E501
    gid: Optional[StrictStr] = Field(default=None, description="Globally unique identifier of the resource, as a string.")
    resource_type: Optional[StrictStr] = Field(default=None, description="The base type of this resource.")
    name: Optional[StrictStr] = Field(default=None, description="The name of the goal.")
    html_notes: Optional[StrictStr] = Field(default=None, description="The notes of the goal with formatting as HTML.")
    notes: Optional[StrictStr] = Field(default=None, description="Free-form textual information associated with the goal (i.e. its description).")
    due_on: Optional[StrictStr] = Field(default=None, description="The localized day on which this goal is due. This takes a date with format `YYYY-MM-DD`.")
    start_on: Optional[StrictStr] = Field(default=None, description="The day on which work for this goal begins, or null if the goal has no start date. This takes a date with `YYYY-MM-DD` format, and cannot be set unless there is an accompanying due date.")
    is_workspace_level: Optional[StrictBool] = Field(default=None, description="*Conditional*. This property is only present when the `workspace` provided is an organization. Whether the goal belongs to the `workspace` (and is listed as part of the workspace’s goals) or not. If it isn’t a workspace-level goal, it is a team-level goal, and is associated with the goal’s team.")
    liked: Optional[StrictBool] = Field(default=None, description="True if the goal is liked by the authorized user, false if not.")
    __properties: ClassVar[List[str]] = ["gid", "resource_type", "name", "html_notes", "notes", "due_on", "start_on", "is_workspace_level", "liked"]

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
        """Create an instance of GoalBase from a JSON string"""
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
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "gid",
                "resource_type",
            },
            exclude_none=True,
        )
        # set to None if due_on (nullable) is None
        # and model_fields_set contains the field
        if self.due_on is None and "due_on" in self.model_fields_set:
            _dict['due_on'] = None

        # set to None if start_on (nullable) is None
        # and model_fields_set contains the field
        if self.start_on is None and "start_on" in self.model_fields_set:
            _dict['start_on'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GoalBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gid": obj.get("gid"),
            "resource_type": obj.get("resource_type"),
            "name": obj.get("name"),
            "html_notes": obj.get("html_notes"),
            "notes": obj.get("notes"),
            "due_on": obj.get("due_on"),
            "start_on": obj.get("start_on"),
            "is_workspace_level": obj.get("is_workspace_level"),
            "liked": obj.get("liked")
        })
        return _obj


