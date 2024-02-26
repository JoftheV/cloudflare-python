# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import (
    ClientCertificateGetResponse,
    ClientCertificateEditResponse,
    ClientCertificateListResponse,
    ClientCertificateCreateResponse,
    ClientCertificateDeleteResponse,
)
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClientCertificates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        client_certificate = client.client_certificates.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICY....\n-----END CERTIFICATE REQUEST-----\n",
            validity_days=3650,
        )
        assert_matches_type(ClientCertificateCreateResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.client_certificates.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICY....\n-----END CERTIFICATE REQUEST-----\n",
            validity_days=3650,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_certificate = response.parse()
        assert_matches_type(ClientCertificateCreateResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.client_certificates.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICY....\n-----END CERTIFICATE REQUEST-----\n",
            validity_days=3650,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_certificate = response.parse()
            assert_matches_type(ClientCertificateCreateResponse, client_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.client_certificates.with_raw_response.create(
                "",
                csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICY....\n-----END CERTIFICATE REQUEST-----\n",
                validity_days=3650,
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        client_certificate = client.client_certificates.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            SyncV4PagePaginationArray[ClientCertificateListResponse], client_certificate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        client_certificate = client.client_certificates.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            limit=10,
            offset=10,
            page=1,
            per_page=5,
            status="all",
        )
        assert_matches_type(
            SyncV4PagePaginationArray[ClientCertificateListResponse], client_certificate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.client_certificates.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_certificate = response.parse()
        assert_matches_type(
            SyncV4PagePaginationArray[ClientCertificateListResponse], client_certificate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.client_certificates.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_certificate = response.parse()
            assert_matches_type(
                SyncV4PagePaginationArray[ClientCertificateListResponse], client_certificate, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.client_certificates.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        client_certificate = client.client_certificates.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ClientCertificateDeleteResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.client_certificates.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_certificate = response.parse()
        assert_matches_type(ClientCertificateDeleteResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.client_certificates.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_certificate = response.parse()
            assert_matches_type(ClientCertificateDeleteResponse, client_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.client_certificates.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `client_certificate_id` but received ''"):
            client.client_certificates.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        client_certificate = client.client_certificates.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ClientCertificateEditResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.client_certificates.with_raw_response.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_certificate = response.parse()
        assert_matches_type(ClientCertificateEditResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.client_certificates.with_streaming_response.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_certificate = response.parse()
            assert_matches_type(ClientCertificateEditResponse, client_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.client_certificates.with_raw_response.edit(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `client_certificate_id` but received ''"):
            client.client_certificates.with_raw_response.edit(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        client_certificate = client.client_certificates.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ClientCertificateGetResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.client_certificates.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_certificate = response.parse()
        assert_matches_type(ClientCertificateGetResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.client_certificates.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_certificate = response.parse()
            assert_matches_type(ClientCertificateGetResponse, client_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.client_certificates.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `client_certificate_id` but received ''"):
            client.client_certificates.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncClientCertificates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        client_certificate = await async_client.client_certificates.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICY....\n-----END CERTIFICATE REQUEST-----\n",
            validity_days=3650,
        )
        assert_matches_type(ClientCertificateCreateResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.client_certificates.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICY....\n-----END CERTIFICATE REQUEST-----\n",
            validity_days=3650,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_certificate = await response.parse()
        assert_matches_type(ClientCertificateCreateResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.client_certificates.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICY....\n-----END CERTIFICATE REQUEST-----\n",
            validity_days=3650,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_certificate = await response.parse()
            assert_matches_type(ClientCertificateCreateResponse, client_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.client_certificates.with_raw_response.create(
                "",
                csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICY....\n-----END CERTIFICATE REQUEST-----\n",
                validity_days=3650,
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        client_certificate = await async_client.client_certificates.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            AsyncV4PagePaginationArray[ClientCertificateListResponse], client_certificate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        client_certificate = await async_client.client_certificates.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            limit=10,
            offset=10,
            page=1,
            per_page=5,
            status="all",
        )
        assert_matches_type(
            AsyncV4PagePaginationArray[ClientCertificateListResponse], client_certificate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.client_certificates.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_certificate = await response.parse()
        assert_matches_type(
            AsyncV4PagePaginationArray[ClientCertificateListResponse], client_certificate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.client_certificates.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_certificate = await response.parse()
            assert_matches_type(
                AsyncV4PagePaginationArray[ClientCertificateListResponse], client_certificate, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.client_certificates.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        client_certificate = await async_client.client_certificates.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ClientCertificateDeleteResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.client_certificates.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_certificate = await response.parse()
        assert_matches_type(ClientCertificateDeleteResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.client_certificates.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_certificate = await response.parse()
            assert_matches_type(ClientCertificateDeleteResponse, client_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.client_certificates.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `client_certificate_id` but received ''"):
            await async_client.client_certificates.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        client_certificate = await async_client.client_certificates.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ClientCertificateEditResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.client_certificates.with_raw_response.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_certificate = await response.parse()
        assert_matches_type(ClientCertificateEditResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.client_certificates.with_streaming_response.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_certificate = await response.parse()
            assert_matches_type(ClientCertificateEditResponse, client_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.client_certificates.with_raw_response.edit(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `client_certificate_id` but received ''"):
            await async_client.client_certificates.with_raw_response.edit(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        client_certificate = await async_client.client_certificates.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ClientCertificateGetResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.client_certificates.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_certificate = await response.parse()
        assert_matches_type(ClientCertificateGetResponse, client_certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.client_certificates.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_certificate = await response.parse()
            assert_matches_type(ClientCertificateGetResponse, client_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.client_certificates.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `client_certificate_id` but received ''"):
            await async_client.client_certificates.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
