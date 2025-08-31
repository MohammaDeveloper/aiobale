from pydantic import Field

from ...types.responses import AvatarResponse
from ...types import Peer
from ...enums import Services
from ..base import BaleMethod


class LoadAvatars(BaleMethod):
    __service__ = Services.USER.value
    __method__ = "LoadAvatars"

    __returning__ = AvatarResponse

    peer: Peer = Field(..., alias="1")
