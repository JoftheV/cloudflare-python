# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.gateways import LoggingGetResponse, LoggingUpdateResponse, logging_update_params

__all__ = ["Loggings", "AsyncLoggings"]


class Loggings(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LoggingsWithRawResponse:
        return LoggingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoggingsWithStreamingResponse:
        return LoggingsWithStreamingResponse(self)

    def update(
        self,
        account_id: object,
        *,
        redact_pii: bool | NotGiven = NOT_GIVEN,
        settings_by_rule_type: logging_update_params.SettingsByRuleType | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoggingUpdateResponse:
        """
        Updates logging settings for the current Zero Trust account.

        Args:
          redact_pii: Redact personally identifiable information from activity logging (PII fields
              are: source IP, user email, user ID, device ID, URL, referrer, user agent).

          settings_by_rule_type: Logging settings by rule type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/accounts/{account_id}/gateway/logging",
            body=maybe_transform(
                {
                    "redact_pii": redact_pii,
                    "settings_by_rule_type": settings_by_rule_type,
                },
                logging_update_params.LoggingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LoggingUpdateResponse], ResultWrapper[LoggingUpdateResponse]),
        )

    def get(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoggingGetResponse:
        """
        Fetches the current logging settings for Zero Trust account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/gateway/logging",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LoggingGetResponse], ResultWrapper[LoggingGetResponse]),
        )


class AsyncLoggings(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLoggingsWithRawResponse:
        return AsyncLoggingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoggingsWithStreamingResponse:
        return AsyncLoggingsWithStreamingResponse(self)

    async def update(
        self,
        account_id: object,
        *,
        redact_pii: bool | NotGiven = NOT_GIVEN,
        settings_by_rule_type: logging_update_params.SettingsByRuleType | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoggingUpdateResponse:
        """
        Updates logging settings for the current Zero Trust account.

        Args:
          redact_pii: Redact personally identifiable information from activity logging (PII fields
              are: source IP, user email, user ID, device ID, URL, referrer, user agent).

          settings_by_rule_type: Logging settings by rule type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/accounts/{account_id}/gateway/logging",
            body=maybe_transform(
                {
                    "redact_pii": redact_pii,
                    "settings_by_rule_type": settings_by_rule_type,
                },
                logging_update_params.LoggingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LoggingUpdateResponse], ResultWrapper[LoggingUpdateResponse]),
        )

    async def get(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoggingGetResponse:
        """
        Fetches the current logging settings for Zero Trust account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/gateway/logging",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LoggingGetResponse], ResultWrapper[LoggingGetResponse]),
        )


class LoggingsWithRawResponse:
    def __init__(self, loggings: Loggings) -> None:
        self._loggings = loggings

        self.update = to_raw_response_wrapper(
            loggings.update,
        )
        self.get = to_raw_response_wrapper(
            loggings.get,
        )


class AsyncLoggingsWithRawResponse:
    def __init__(self, loggings: AsyncLoggings) -> None:
        self._loggings = loggings

        self.update = async_to_raw_response_wrapper(
            loggings.update,
        )
        self.get = async_to_raw_response_wrapper(
            loggings.get,
        )


class LoggingsWithStreamingResponse:
    def __init__(self, loggings: Loggings) -> None:
        self._loggings = loggings

        self.update = to_streamed_response_wrapper(
            loggings.update,
        )
        self.get = to_streamed_response_wrapper(
            loggings.get,
        )


class AsyncLoggingsWithStreamingResponse:
    def __init__(self, loggings: AsyncLoggings) -> None:
        self._loggings = loggings

        self.update = async_to_streamed_response_wrapper(
            loggings.update,
        )
        self.get = async_to_streamed_response_wrapper(
            loggings.get,
        )
