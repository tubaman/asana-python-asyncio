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
from asana_asyncio.models.custom_field_setting_response_all_of_custom_field import CustomFieldSettingResponseAllOfCustomField
from asana_asyncio.models.custom_field_setting_response_all_of_parent import CustomFieldSettingResponseAllOfParent
from asana_asyncio.models.custom_field_setting_response_all_of_project import CustomFieldSettingResponseAllOfProject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CustomFieldSettingResponse(BaseModel):
    """
    CustomFieldSettingResponse
    """ # noqa: E501
    gid: Optional[StrictStr] = Field(default=None, description="Globally unique identifier of the resource, as a string.")
    resource_type: Optional[StrictStr] = Field(default=None, description="The base type of this resource.")
    project: Optional[CustomFieldSettingResponseAllOfProject] = None
    is_important: Optional[StrictBool] = Field(default=None, description="`is_important` is used in the Asana web application to determine if this custom field is displayed in the list/grid view of a project or portfolio.")
    parent: Optional[CustomFieldSettingResponseAllOfParent] = None
    custom_field: Optional[CustomFieldSettingResponseAllOfCustomField] = None
    __properties: ClassVar[List[str]] = ["gid", "resource_type", "project", "is_important", "parent", "custom_field"]

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
        """Create an instance of CustomFieldSettingResponse from a JSON string"""
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
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "gid",
                "resource_type",
                "is_important",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parent
        if self.parent:
            _dict['parent'] = self.parent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_field
        if self.custom_field:
            _dict['custom_field'] = self.custom_field.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CustomFieldSettingResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gid": obj.get("gid"),
            "resource_type": obj.get("resource_type"),
            "project": CustomFieldSettingResponseAllOfProject.from_dict(obj.get("project")) if obj.get("project") is not None else None,
            "is_important": obj.get("is_important"),
            "parent": CustomFieldSettingResponseAllOfParent.from_dict(obj.get("parent")) if obj.get("parent") is not None else None,
            "custom_field": CustomFieldSettingResponseAllOfCustomField.from_dict(obj.get("custom_field")) if obj.get("custom_field") is not None else None
        })
        return _obj


