# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .tokens import IamValue
from ..._models import BaseModel

__all__ = ["TokenCreateResponse"]


class TokenCreateResponse(BaseModel):
    value: Optional[IamValue] = None
    """The token value."""
