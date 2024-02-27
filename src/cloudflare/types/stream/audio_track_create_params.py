# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AudioTrackCreateParams"]


class AudioTrackCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    label: Required[str]
    """
    A string to uniquely identify the track amongst other audio track labels for the
    specified video.
    """

    url: str
    """An audio track URL.

    The server must be publicly routable and support `HTTP HEAD` requests and
    `HTTP GET` range requests. The server should respond to `HTTP HEAD` requests
    with a `content-range` header that includes the size of the file.
    """