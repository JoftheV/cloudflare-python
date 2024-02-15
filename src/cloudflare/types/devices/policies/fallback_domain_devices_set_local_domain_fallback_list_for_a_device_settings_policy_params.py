# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyParams", "Body"]


class FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyParams(TypedDict, total=False):
    identifier: Required[object]

    body: Required[Iterable[Body]]


class Body(TypedDict, total=False):
    suffix: Required[str]
    """The domain suffix to match when resolving locally."""

    description: str
    """A description of the fallback domain, displayed in the client UI."""

    dns_server: Iterable[object]
    """A list of IP addresses to handle domain resolution."""
