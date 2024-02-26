# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PayloadLogUpdateParams"]


class PayloadLogUpdateParams(TypedDict, total=False):
    public_key: Required[Optional[str]]
    """The public key to use when encrypting extracted payloads, as a base64 string"""
