from pydantic import Field
from typing import TYPE_CHECKING

from .base import BaleObject
from .file_info import FileInfo


class Image(BaleObject):
    file: FileInfo = Field(..., alias="1")
    width: int = Field(..., alias="2")
    height: int = Field(..., alias="3")
    file_size: int = Field(..., alias="4")
