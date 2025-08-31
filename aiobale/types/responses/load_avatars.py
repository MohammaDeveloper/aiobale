from typing import Any, Dict, List, Optional, TYPE_CHECKING
from pydantic import Field, model_validator

from ..base import BaleObject
from ..avatar import Avatar


class LoadAvatarsResponse(BaleObject):
    avatars: List[Avatar] = Field(default_factory=list, alias="1")

    if TYPE_CHECKING:
        # This init is only used for type checking and IDE autocomplete.
        # It will not be included in runtime behavior.
        def __init__(
            __pydantic__self__, *, avatars: List[Avatar] = None, **__pydantic_kwargs
        ) -> None:
            super().__init__(avatars=avatars, **__pydantic_kwargs)

    @model_validator(mode="before")
    @classmethod
    def _normalize_lists(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        if "1" in data and not isinstance(data["1"], list):
            data["1"] = [data["1"]]
        return data
