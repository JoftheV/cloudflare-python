# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["TopAsesResponse", "Meta", "MetaDateRange", "MetaConfidenceInfo", "MetaConfidenceInfoAnnotation", "Top0"]


class MetaDateRange(BaseModel):
    end_time: datetime = FieldInfo(alias="endTime")
    """Adjusted end of date range."""

    start_time: datetime = FieldInfo(alias="startTime")
    """Adjusted start of date range."""


class MetaConfidenceInfoAnnotation(BaseModel):
    data_source: str = FieldInfo(alias="dataSource")

    description: str

    event_type: str = FieldInfo(alias="eventType")

    is_instantaneous: object = FieldInfo(alias="isInstantaneous")

    end_time: Optional[datetime] = FieldInfo(alias="endTime", default=None)

    linked_url: Optional[str] = FieldInfo(alias="linkedUrl", default=None)

    start_time: Optional[datetime] = FieldInfo(alias="startTime", default=None)


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[MetaConfidenceInfoAnnotation]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[MetaDateRange] = FieldInfo(alias="dateRange")

    last_updated: str = FieldInfo(alias="lastUpdated")

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Top0(BaseModel):
    bandwidth_download: str = FieldInfo(alias="bandwidthDownload")

    bandwidth_upload: str = FieldInfo(alias="bandwidthUpload")

    client_asn: float = FieldInfo(alias="clientASN")

    client_as_name: str = FieldInfo(alias="clientASName")

    jitter_idle: str = FieldInfo(alias="jitterIdle")

    jitter_loaded: str = FieldInfo(alias="jitterLoaded")

    latency_idle: str = FieldInfo(alias="latencyIdle")

    latency_loaded: str = FieldInfo(alias="latencyLoaded")

    num_tests: float = FieldInfo(alias="numTests")

    rank_power: float = FieldInfo(alias="rankPower")


class TopAsesResponse(BaseModel):
    meta: Meta

    top_0: List[Top0]
