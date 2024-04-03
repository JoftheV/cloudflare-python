# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["HostnameAssociationUpdateResponse"]


class HostnameAssociationUpdateResponse(BaseModel):
    hostnames: Optional[List[str]] = None
