# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["TraceCreateResponse"]


class TraceCreateResponse(BaseModel):
    status_code: Optional[int] = None
    """HTTP Status code of zone response"""

    trace: Optional["Q19cOvCrTrace"] = None


from .q19c_ov_cr_trace import Q19cOvCrTrace

if PYDANTIC_V2:
    TraceCreateResponse.model_rebuild()
else:
    TraceCreateResponse.update_forward_refs()  # type: ignore
