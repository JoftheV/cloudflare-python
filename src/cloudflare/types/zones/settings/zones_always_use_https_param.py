# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ZonesAlwaysUseHTTPSParam"]


class ZonesAlwaysUseHTTPSParam(TypedDict, total=False):
    id: Required[Literal["always_use_https"]]
    """ID of the zone setting."""

    value: Required[Literal["on", "off"]]
    """Current value of the zone setting."""