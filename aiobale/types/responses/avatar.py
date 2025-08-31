from typing import Optional, TYPE_CHECKING
from pydantic import Field

from ..base import BaleObject
from ..avatar import Avatar


class AvatarResponse(BaleObject):
    avatar: Optional[Avatar] = Field(None, alias="1")

    if TYPE_CHECKING:
        # This init is only used for type checking and IDE autocomplete.
        # It will not be included in runtime behavior.
        def __init__(
            __pydantic__self__, *, avatar: Optional[Avatar] = None, **__pydantic_kwargs
        ) -> None:
            super().__init__(avatar=avatar, **__pydantic_kwargs)
