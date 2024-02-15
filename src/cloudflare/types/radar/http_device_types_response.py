# File generated from our OpenAPI spec by Stainless.

from typing import List

from ..._models import BaseModel

__all__ = ["HTTPDeviceTypesResponse", "Serie0"]


class Serie0(BaseModel):
    desktop: List[str]

    mobile: List[str]

    other: List[str]

    timestamps: List[str]


class HTTPDeviceTypesResponse(BaseModel):
    meta: object

    serie_0: Serie0
