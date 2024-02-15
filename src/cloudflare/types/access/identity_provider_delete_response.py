# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["IdentityProviderDeleteResponse"]


class IdentityProviderDeleteResponse(BaseModel):
    id: Optional[str] = None
    """UUID"""
