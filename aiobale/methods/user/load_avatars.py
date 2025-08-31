from pydantic import Field

from ...types.responses import LoadAvatarsResponse
from ...types import InfoPeer
from ...enums import Services
from ..base import BaleMethod


class LoadAvatars(BaleMethod):
    __service__ = Services.USER.value
    __method__ = "LoadAvatars"

    __returning__ = LoadAvatarsResponse

    peer: InfoPeer = Field(..., alias="1")
