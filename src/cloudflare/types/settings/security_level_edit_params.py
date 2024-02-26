# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SecurityLevelEditParams"]


class SecurityLevelEditParams(TypedDict, total=False):
    value: Required[Literal["off", "essentially_off", "low", "medium", "high", "under_attack"]]
    """Value of the zone setting."""
