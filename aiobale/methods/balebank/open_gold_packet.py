from pydantic import Field
from typing import TYPE_CHECKING

from ...types.responses import PacketResponse
from ...enums import Services
from ..base import BaleMethod


class OpenGoldGiftPacket(BaleMethod):
    """
    Opens a gold gift packet by its unique ID.

    This method is used to open and claim the contents of a gold gift packet.
    returns the result of the opening, and may include pagination and sorting options.

    Returns a `PacketResponse` containing detailed info about the gold gift opening.
    """

    __service__ = Services.GOLD_GIFT_PACKET.value
    __method__ = "OpenGoldGiftPacket"
    
    __returning__ = PacketResponse

    id: int = Field(0, alias="1")
    """Unique identifier of the gold gift packet to be opened."""

    if TYPE_CHECKING:
        # This init is only used for type checking and IDE autocomplete.
        # It will not be included in runtime behavior.
        def __init__(
            __pydantic__self__,
            *,
            id: int,
            **__pydantic_kwargs,
        ) -> None:
            super().__init__(
                id=id,
                **__pydantic_kwargs,
            )
