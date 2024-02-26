# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConnectivitySettingEditParams"]


class ConnectivitySettingEditParams(TypedDict, total=False):
    icmp_proxy_enabled: bool
    """A flag to enable the ICMP proxy for the account network."""

    offramp_warp_enabled: bool
    """A flag to enable WARP to WARP traffic."""
