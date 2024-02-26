# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SubmitCreateParams"]


class SubmitCreateParams(TypedDict, total=False):
    url: str
    """URL(s) to filter submissions results by"""
