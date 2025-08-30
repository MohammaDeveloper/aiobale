from pydantic import Field, model_serializer, model_validator
from typing import TYPE_CHECKING, Any, Dict

from .base import BaleObject
from .image import Image


class Avatar(BaleObject):
    small_image: Image = Field(..., alias="1")
    large_image: Image = Field(..., alias="2")
    full_image: Image = Field(..., alias="3")
    id: int = Field(..., alias="4")
    date: int = Field(..., alias="5")

    @model_validator(mode="before")
    @classmethod
    def _fix_fields(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        if "4" in data:
            data["4"] = data["4"]["1"]
        if "5" in data:
            data["5"] = data["5"]["1"]

        return data

    @model_serializer(mode="wrap")
    def _ser(self, nxt, info):
        if not info.by_alias:
            return nxt(self)

        out = nxt(self)
        out["4"] = {"1": out["4"]}
        out["5"] = {"1": out["5"]}

        return out
