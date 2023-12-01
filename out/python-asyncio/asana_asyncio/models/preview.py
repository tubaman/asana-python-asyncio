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
from pydantic import BaseModel, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Preview(BaseModel):
    """
    A collection of rich text that will be displayed as a preview to another app.  This is read-only except for a small group of whitelisted apps.
    """ # noqa: E501
    fallback: Optional[StrictStr] = Field(default=None, description="Some fallback text to display if unable to display the full preview.")
    footer: Optional[StrictStr] = Field(default=None, description="Text to display in the footer.")
    header: Optional[StrictStr] = Field(default=None, description="Text to display in the header.")
    header_link: Optional[StrictStr] = Field(default=None, description="Where the header will link to.")
    html_text: Optional[StrictStr] = Field(default=None, description="HTML formatted text for the body of the preview.")
    text: Optional[StrictStr] = Field(default=None, description="Text for the body of the preview.")
    title: Optional[StrictStr] = Field(default=None, description="Text to display as the title.")
    title_link: Optional[StrictStr] = Field(default=None, description="Where to title will link to.")
    __properties: ClassVar[List[str]] = ["fallback", "footer", "header", "header_link", "html_text", "text", "title", "title_link"]

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
        """Create an instance of Preview from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Preview from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fallback": obj.get("fallback"),
            "footer": obj.get("footer"),
            "header": obj.get("header"),
            "header_link": obj.get("header_link"),
            "html_text": obj.get("html_text"),
            "text": obj.get("text"),
            "title": obj.get("title"),
            "title_link": obj.get("title_link")
        })
        return _obj


