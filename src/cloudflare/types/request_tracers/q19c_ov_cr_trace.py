# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional

from ..._compat import PYDANTIC_V2
from ..._models import BaseModel

__all__ = ["Q19cOvCrTrace", "Q19cOvCrTraceItem"]


class Q19cOvCrTraceItem(BaseModel):
    action: Optional[str] = None
    """If step type is rule, then action performed by this rule"""

    action_parameters: Optional[object] = None
    """If step type is rule, then action parameters of this rule as JSON"""

    description: Optional[str] = None
    """If step type is rule or ruleset, the description of this entity"""

    expression: Optional[str] = None
    """If step type is rule, then expression used to match for this rule"""

    kind: Optional[str] = None
    """If step type is ruleset, then kind of this ruleset"""

    matched: Optional[bool] = None
    """Whether tracing step affected tracing request/response"""

    name: Optional[str] = None
    """If step type is ruleset, then name of this ruleset"""

    step_name: Optional[str] = None
    """Tracing step identifying name"""

    trace: Optional[Q19cOvCrTrace] = None

    type: Optional[str] = None
    """Tracing step type"""


Q19cOvCrTrace = List[Q19cOvCrTraceItem]

if PYDANTIC_V2:
    Q19cOvCrTraceItem.model_rebuild()
else:
    Q19cOvCrTraceItem.update_forward_refs()  # type: ignore
