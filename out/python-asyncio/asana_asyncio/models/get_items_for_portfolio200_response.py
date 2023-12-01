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
from pydantic import BaseModel
from asana_asyncio.models.next_page import NextPage
from asana_asyncio.models.project_compact import ProjectCompact
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetItemsForPortfolio200Response(BaseModel):
    """
    GetItemsForPortfolio200Response
    """ # noqa: E501
    data: Optional[List[ProjectCompact]] = None
    next_page: Optional[NextPage] = None
    __properties: ClassVar[List[str]] = ["data", "next_page"]

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
        """Create an instance of GetItemsForPortfolio200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
        # override the default output from pydantic by calling `to_dict()` of next_page
        if self.next_page:
            _dict['next_page'] = self.next_page.to_dict()
        # set to None if next_page (nullable) is None
        # and model_fields_set contains the field
        if self.next_page is None and "next_page" in self.model_fields_set:
            _dict['next_page'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetItemsForPortfolio200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data": [ProjectCompact.from_dict(_item) for _item in obj.get("data")] if obj.get("data") is not None else None,
            "next_page": NextPage.from_dict(obj.get("next_page")) if obj.get("next_page") is not None else None
        })
        return _obj

