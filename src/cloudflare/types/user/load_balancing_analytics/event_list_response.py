# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["EventListResponse", "EventListResponseItem"]


class EventListResponseItem(BaseModel):
    id: Optional[int] = None

    origins: Optional[List[object]] = None

    pool: Optional[object] = None

    timestamp: Optional[datetime] = None


EventListResponse = List[EventListResponseItem]