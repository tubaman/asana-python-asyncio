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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GoalMetricBase(BaseModel):
    """
    GoalMetricBase
    """ # noqa: E501
    gid: Optional[StrictStr] = Field(default=None, description="Globally unique identifier of the resource, as a string.")
    resource_type: Optional[StrictStr] = Field(default=None, description="The base type of this resource.")
    resource_subtype: Optional[StrictStr] = Field(default=None, description="The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning.")
    precision: Optional[StrictInt] = Field(default=None, description="*Conditional*. Only relevant for goal metrics of type ‘Number’. This field dictates the number of places after the decimal to round to, i.e. 0 is integer values, 1 rounds to the nearest tenth, and so on. Must be between 0 and 6, inclusive. For percentage format, this may be unintuitive, as a value of 0.25 has a precision of 0, while a value of 0.251 has a precision of 1. This is due to 0.25 being displayed as 25%.")
    unit: Optional[StrictStr] = Field(default=None, description="A supported unit of measure for the goal metric, or none.")
    currency_code: Optional[StrictStr] = Field(default=None, description="ISO 4217 currency code to format this custom field. This will be null if the `unit` is not `currency`.")
    initial_number_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="This number is the start value of a goal metric of type number.")
    target_number_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="This number is the end value of a goal metric of type number. This number cannot equal `initial_number_value`.")
    current_number_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="This number is the current value of a goal metric of type number.")
    current_display_value: Optional[StrictStr] = Field(default=None, description="This string is the current value of a goal metric of type string.")
    progress_source: Optional[StrictStr] = Field(default=None, description="This field defines how the progress value of a goal metric is being calculated. A goal's progress can be provided manually by the user, calculated automatically from contributing subgoals, projects, or tasks, or managed by an integration with an external data source, such as Salesforce.")
    __properties: ClassVar[List[str]] = ["gid", "resource_type", "resource_subtype", "precision", "unit", "currency_code", "initial_number_value", "target_number_value", "current_number_value", "current_display_value", "progress_source"]

    @field_validator('resource_subtype')
    def resource_subtype_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('number'):
            raise ValueError("must be one of enum values ('number')")
        return value

    @field_validator('unit')
    def unit_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('none', 'currency', 'percentage'):
            raise ValueError("must be one of enum values ('none', 'currency', 'percentage')")
        return value

    @field_validator('progress_source')
    def progress_source_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('manual', 'subgoal_progress', 'project_task_completion', 'project_milestone_completion', 'task_completion', 'external'):
            raise ValueError("must be one of enum values ('manual', 'subgoal_progress', 'project_task_completion', 'project_milestone_completion', 'task_completion', 'external')")
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
        """Create an instance of GoalMetricBase from a JSON string"""
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
                "resource_subtype",
                "current_display_value",
            },
            exclude_none=True,
        )
        # set to None if currency_code (nullable) is None
        # and model_fields_set contains the field
        if self.currency_code is None and "currency_code" in self.model_fields_set:
            _dict['currency_code'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GoalMetricBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gid": obj.get("gid"),
            "resource_type": obj.get("resource_type"),
            "resource_subtype": obj.get("resource_subtype"),
            "precision": obj.get("precision"),
            "unit": obj.get("unit"),
            "currency_code": obj.get("currency_code"),
            "initial_number_value": obj.get("initial_number_value"),
            "target_number_value": obj.get("target_number_value"),
            "current_number_value": obj.get("current_number_value"),
            "current_display_value": obj.get("current_display_value"),
            "progress_source": obj.get("progress_source")
        })
        return _obj


