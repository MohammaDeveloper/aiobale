from typing import TYPE_CHECKING
from pydantic import Field

from ..enums import GivingType
from .base import BaleObject


class GoldGiftPacket(BaleObject):
    """
    Represents a packet of gold gifts that can be distributed among users.

    Used in scenarios like sending monetary gold gifts in a group or channel.  
    Includes information such as total amount, number of recipients, message, and distribution type.
    """

    id: int = Field(0, alias="1")
    """Unique identifier for the gold gift packet."""

    total_amount: int = Field(0, alias="2")
    """Total amount of the gold gift to be distributed."""

    count: int = Field(0, alias="3")
    """Number of recipients who can claim the gold gift."""

    message: str = Field(..., alias="4")
    """Custom message that accompanies the gold gift packet."""

    giving_type: GivingType = Field(GivingType.SAME, alias="5")
    """Defines how the gold gift is distributed (e.g., equally or randomly)."""

    if TYPE_CHECKING:
        def __init__(
            __pydantic__self__,
            *,
            id: int,
            total_amount: int,
            count: int,
            message: str,
            giving_type: GivingType = GivingType.SAME,
            **__pydantic_kwargs
        ) -> None:
            super().__init__(
                id=id,
                total_amount=total_amount,
                count=count,
                message=message,
                giving_type=giving_type,
                **__pydantic_kwargs
            )
