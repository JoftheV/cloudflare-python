# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["MembershipDeleteResponse"]


class MembershipDeleteResponse(BaseModel):
    id: Optional[str] = None
    """Membership identifier tag."""
