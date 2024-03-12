# File generated from our OpenAPI spec by Stainless.

from ..._models import BaseModel

__all__ = ["WorkersRoutes"]


class WorkersRoutes(BaseModel):
    id: str
    """Identifier"""

    pattern: str

    script: str
    """Name of the script, used in URLs and route configuration."""