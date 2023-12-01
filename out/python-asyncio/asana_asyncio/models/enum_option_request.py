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

class EnumOptionRequest(BaseModel):
    """
    EnumOptionRequest
    """ # noqa: E501
    gid: Optional[StrictStr] = Field(default=None, description="Globally unique identifier of the resource, as a string.")
    resource_type: Optional[StrictStr] = Field(default=None, description="The base type of this resource.")
    name: Optional[StrictStr] = Field(default=None, description="The name of the enum option.")
    enabled: Optional[StrictBool] = Field(default=None, description="Whether or not the enum option is a selectable value for the custom field.")
    color: Optional[StrictStr] = Field(default=None, description="The color of the enum option. Defaults to ‘none’.")
    insert_before: Optional[StrictStr] = Field(default=None, description="An existing enum option within this custom field before which the new enum option should be inserted. Cannot be provided together with after_enum_option.")
    insert_after: Optional[StrictStr] = Field(default=None, description="An existing enum option within this custom field after which the new enum option should be inserted. Cannot be provided together with before_enum_option.")
    __properties: ClassVar[List[str]] = ["gid", "resource_type", "name", "enabled", "color", "insert_before", "insert_after"]

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
        """Create an instance of EnumOptionRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EnumOptionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gid": obj.get("gid"),
            "resource_type": obj.get("resource_type"),
            "name": obj.get("name"),
            "enabled": obj.get("enabled"),
            "color": obj.get("color"),
            "insert_before": obj.get("insert_before"),
            "insert_after": obj.get("insert_after")
        })
        return _obj


