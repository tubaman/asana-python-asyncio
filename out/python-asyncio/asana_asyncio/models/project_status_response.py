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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ProjectStatusResponse(BaseModel):
    """
    ProjectStatusResponse
    """ # noqa: E501
    gid: Optional[StrictStr] = Field(default=None, description="Globally unique identifier of the resource, as a string.")
    resource_type: Optional[StrictStr] = Field(default=None, description="The base type of this resource.")
    title: Optional[StrictStr] = Field(default=None, description="The title of the project status update.")
    text: Optional[StrictStr] = Field(default=None, description="The text content of the status update.")
    html_text: Optional[StrictStr] = Field(default=None, description="[Opt In](/docs/inputoutput-options). The text content of the status update with formatting as HTML.")
    color: Optional[StrictStr] = Field(default=None, description="The color associated with the status update.")
    author: Optional[UserCompact] = None
    created_at: Optional[datetime] = Field(default=None, description="The time at which this resource was created.")
    created_by: Optional[UserCompact] = None
    modified_at: Optional[datetime] = Field(default=None, description="The time at which this project status was last modified. *Note: This does not currently reflect any changes in associations such as comments that may have been added or removed from the project status.*")
    __properties: ClassVar[List[str]] = ["gid", "resource_type", "title", "text", "html_text", "color", "author", "created_at", "created_by", "modified_at"]

    @field_validator('color')
    def color_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('green', 'yellow', 'red', 'blue', 'complete'):
            raise ValueError("must be one of enum values ('green', 'yellow', 'red', 'blue', 'complete')")
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
        """Create an instance of ProjectStatusResponse from a JSON string"""
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
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "gid",
                "resource_type",
                "created_at",
                "modified_at",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProjectStatusResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gid": obj.get("gid"),
            "resource_type": obj.get("resource_type"),
            "title": obj.get("title"),
            "text": obj.get("text"),
            "html_text": obj.get("html_text"),
            "color": obj.get("color"),
            "author": UserCompact.from_dict(obj.get("author")) if obj.get("author") is not None else None,
            "created_at": obj.get("created_at"),
            "created_by": UserCompact.from_dict(obj.get("created_by")) if obj.get("created_by") is not None else None,
            "modified_at": obj.get("modified_at")
        })
        return _obj


