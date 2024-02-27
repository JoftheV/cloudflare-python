# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.zones.settings import (
    PrefetchPreloadGetResponse,
    PrefetchPreloadEditResponse,
    prefetch_preload_edit_params,
)

__all__ = ["PrefetchPreload", "AsyncPrefetchPreload"]


class PrefetchPreload(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrefetchPreloadWithRawResponse:
        return PrefetchPreloadWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrefetchPreloadWithStreamingResponse:
        return PrefetchPreloadWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PrefetchPreloadEditResponse]:
        """
        Cloudflare will prefetch any URLs that are included in the response headers.
        This is limited to Enterprise Zones.

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/prefetch_preload",
            body=maybe_transform({"value": value}, prefetch_preload_edit_params.PrefetchPreloadEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PrefetchPreloadEditResponse]], ResultWrapper[PrefetchPreloadEditResponse]),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PrefetchPreloadGetResponse]:
        """
        Cloudflare will prefetch any URLs that are included in the response headers.
        This is limited to Enterprise Zones.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/settings/prefetch_preload",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PrefetchPreloadGetResponse]], ResultWrapper[PrefetchPreloadGetResponse]),
        )


class AsyncPrefetchPreload(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrefetchPreloadWithRawResponse:
        return AsyncPrefetchPreloadWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrefetchPreloadWithStreamingResponse:
        return AsyncPrefetchPreloadWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PrefetchPreloadEditResponse]:
        """
        Cloudflare will prefetch any URLs that are included in the response headers.
        This is limited to Enterprise Zones.

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/prefetch_preload",
            body=maybe_transform({"value": value}, prefetch_preload_edit_params.PrefetchPreloadEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PrefetchPreloadEditResponse]], ResultWrapper[PrefetchPreloadEditResponse]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PrefetchPreloadGetResponse]:
        """
        Cloudflare will prefetch any URLs that are included in the response headers.
        This is limited to Enterprise Zones.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/settings/prefetch_preload",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[PrefetchPreloadGetResponse]], ResultWrapper[PrefetchPreloadGetResponse]),
        )


class PrefetchPreloadWithRawResponse:
    def __init__(self, prefetch_preload: PrefetchPreload) -> None:
        self._prefetch_preload = prefetch_preload

        self.edit = to_raw_response_wrapper(
            prefetch_preload.edit,
        )
        self.get = to_raw_response_wrapper(
            prefetch_preload.get,
        )


class AsyncPrefetchPreloadWithRawResponse:
    def __init__(self, prefetch_preload: AsyncPrefetchPreload) -> None:
        self._prefetch_preload = prefetch_preload

        self.edit = async_to_raw_response_wrapper(
            prefetch_preload.edit,
        )
        self.get = async_to_raw_response_wrapper(
            prefetch_preload.get,
        )


class PrefetchPreloadWithStreamingResponse:
    def __init__(self, prefetch_preload: PrefetchPreload) -> None:
        self._prefetch_preload = prefetch_preload

        self.edit = to_streamed_response_wrapper(
            prefetch_preload.edit,
        )
        self.get = to_streamed_response_wrapper(
            prefetch_preload.get,
        )


class AsyncPrefetchPreloadWithStreamingResponse:
    def __init__(self, prefetch_preload: AsyncPrefetchPreload) -> None:
        self._prefetch_preload = prefetch_preload

        self.edit = async_to_streamed_response_wrapper(
            prefetch_preload.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            prefetch_preload.get,
        )