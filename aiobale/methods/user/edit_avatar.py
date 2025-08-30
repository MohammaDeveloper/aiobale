from pydantic import Field
from ...types.responses import DefaultResponse
from ...types import FileInfo
from ...enums import Services
from ..base import BaleMethod


class EditAvatar(BaleMethod):
    __service__ = Services.USER.value
    __method__ = "EditAvatar"

    __returning__ = DefaultResponse

    file: FileInfo = Field(..., alias="1")
