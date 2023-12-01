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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from asana_asyncio.models.asana_named_resource import AsanaNamedResource
from asana_asyncio.models.webhook_response_all_of_filters import WebhookResponseAllOfFilters
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WebhookResponse(BaseModel):
    """
    WebhookResponse
    """ # noqa: E501
    gid: Optional[StrictStr] = Field(default=None, description="Globally unique identifier of the resource, as a string.")
    resource_type: Optional[StrictStr] = Field(default=None, description="The base type of this resource.")
    active: Optional[StrictBool] = Field(default=None, description="If true, the webhook will send events - if false it is considered inactive and will not generate events.")
    resource: Optional[AsanaNamedResource] = None
    target: Optional[StrictStr] = Field(default=None, description="The URL to receive the HTTP POST.")
    created_at: Optional[datetime] = Field(default=None, description="The time at which this resource was created.")
    last_failure_at: Optional[datetime] = Field(default=None, description="The timestamp when the webhook last received an error when sending an event to the target.")
    last_failure_content: Optional[StrictStr] = Field(default=None, description="The contents of the last error response sent to the webhook when attempting to deliver events to the target.")
    last_success_at: Optional[datetime] = Field(default=None, description="The timestamp when the webhook last successfully sent an event to the target.")
    filters: Optional[List[WebhookResponseAllOfFilters]] = Field(default=None, description="Whitelist of filters to apply to events from this webhook. If a webhook event passes any of the filters the event will be delivered; otherwise no event will be sent to the receiving server.")
    __properties: ClassVar[List[str]] = ["gid", "resource_type", "active", "resource", "target", "created_at", "last_failure_at", "last_failure_content", "last_success_at", "filters"]

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
        """Create an instance of WebhookResponse from a JSON string"""
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
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "gid",
                "resource_type",
                "active",
                "target",
                "created_at",
                "last_failure_at",
                "last_failure_content",
                "last_success_at",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of resource
        if self.resource:
            _dict['resource'] = self.resource.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in filters (list)
        _items = []
        if self.filters:
            for _item in self.filters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['filters'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WebhookResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gid": obj.get("gid"),
            "resource_type": obj.get("resource_type"),
            "active": obj.get("active"),
            "resource": AsanaNamedResource.from_dict(obj.get("resource")) if obj.get("resource") is not None else None,
            "target": obj.get("target"),
            "created_at": obj.get("created_at"),
            "last_failure_at": obj.get("last_failure_at"),
            "last_failure_content": obj.get("last_failure_content"),
            "last_success_at": obj.get("last_success_at"),
            "filters": [WebhookResponseAllOfFilters.from_dict(_item) for _item in obj.get("filters")] if obj.get("filters") is not None else None
        })
        return _obj


