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
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from asana_asyncio.models.user_compact import UserCompact
from asana_asyncio.models.workspace_compact import WorkspaceCompact
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TagResponse(BaseModel):
    """
    TagResponse
    """ # noqa: E501
    gid: Optional[StrictStr] = Field(default=None, description="Globally unique identifier of the resource, as a string.")
    resource_type: Optional[StrictStr] = Field(default=None, description="The base type of this resource.")
    name: Optional[StrictStr] = Field(default=None, description="Name of the tag. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer.")
    color: Optional[StrictStr] = Field(default=None, description="Color of the tag.")
    notes: Optional[StrictStr] = Field(default=None, description="Free-form textual information associated with the tag (i.e. its description).")
    created_at: Optional[datetime] = Field(default=None, description="The time at which this resource was created.")
    followers: Optional[List[UserCompact]] = Field(default=None, description="Array of users following this tag.")
    workspace: Optional[WorkspaceCompact] = None
    permalink_url: Optional[StrictStr] = Field(default=None, description="A url that points directly to the object within Asana.")
    __properties: ClassVar[List[str]] = ["gid", "resource_type", "name", "color", "notes", "created_at", "followers", "workspace", "permalink_url"]

    @field_validator('color')
    def color_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('dark-pink', 'dark-green', 'dark-blue', 'dark-red', 'dark-teal', 'dark-brown', 'dark-orange', 'dark-purple', 'dark-warm-gray', 'light-pink', 'light-green', 'light-blue', 'light-red', 'light-teal', 'light-brown', 'light-orange', 'light-purple', 'light-warm-gray', 'null'):
            raise ValueError("must be one of enum values ('dark-pink', 'dark-green', 'dark-blue', 'dark-red', 'dark-teal', 'dark-brown', 'dark-orange', 'dark-purple', 'dark-warm-gray', 'light-pink', 'light-green', 'light-blue', 'light-red', 'light-teal', 'light-brown', 'light-orange', 'light-purple', 'light-warm-gray', 'null')")
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
        """Create an instance of TagResponse from a JSON string"""
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
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "gid",
                "resource_type",
                "created_at",
                "followers",
                "permalink_url",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in followers (list)
        _items = []
        if self.followers:
            for _item in self.followers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['followers'] = _items
        # override the default output from pydantic by calling `to_dict()` of workspace
        if self.workspace:
            _dict['workspace'] = self.workspace.to_dict()
        # set to None if color (nullable) is None
        # and model_fields_set contains the field
        if self.color is None and "color" in self.model_fields_set:
            _dict['color'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TagResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gid": obj.get("gid"),
            "resource_type": obj.get("resource_type"),
            "name": obj.get("name"),
            "color": obj.get("color"),
            "notes": obj.get("notes"),
            "created_at": obj.get("created_at"),
            "followers": [UserCompact.from_dict(_item) for _item in obj.get("followers")] if obj.get("followers") is not None else None,
            "workspace": WorkspaceCompact.from_dict(obj.get("workspace")) if obj.get("workspace") is not None else None,
            "permalink_url": obj.get("permalink_url")
        })
        return _obj

