from pydantic import Field

from ...types.responses import DefaultResponse
from ...types import IntValue
from ...enums import Services
from ..base import BaleMethod


class RemoveAvatar(BaleMethod):
    __service__ = Services.USER.value
    __method__ = "RemoveAvatar"

    __returning__ = DefaultResponse

    avatar_id: IntValue = Field(..., alias="1")
