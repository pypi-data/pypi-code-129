"""
Type annotations for personalize-runtime service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/type_defs/)

Usage::

    ```python
    from mypy_boto3_personalize_runtime.type_defs import GetPersonalizedRankingRequestRequestTypeDef

    data: GetPersonalizedRankingRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "GetPersonalizedRankingRequestRequestTypeDef",
    "PredictedItemTypeDef",
    "ResponseMetadataTypeDef",
    "PromotionTypeDef",
    "GetPersonalizedRankingResponseTypeDef",
    "GetRecommendationsResponseTypeDef",
    "GetRecommendationsRequestRequestTypeDef",
)

_RequiredGetPersonalizedRankingRequestRequestTypeDef = TypedDict(
    "_RequiredGetPersonalizedRankingRequestRequestTypeDef",
    {
        "campaignArn": str,
        "inputList": Sequence[str],
        "userId": str,
    },
)
_OptionalGetPersonalizedRankingRequestRequestTypeDef = TypedDict(
    "_OptionalGetPersonalizedRankingRequestRequestTypeDef",
    {
        "context": Mapping[str, str],
        "filterArn": str,
        "filterValues": Mapping[str, str],
    },
    total=False,
)


class GetPersonalizedRankingRequestRequestTypeDef(
    _RequiredGetPersonalizedRankingRequestRequestTypeDef,
    _OptionalGetPersonalizedRankingRequestRequestTypeDef,
):
    pass


PredictedItemTypeDef = TypedDict(
    "PredictedItemTypeDef",
    {
        "itemId": str,
        "score": float,
        "promotionName": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)

PromotionTypeDef = TypedDict(
    "PromotionTypeDef",
    {
        "name": str,
        "percentPromotedItems": int,
        "filterArn": str,
        "filterValues": Mapping[str, str],
    },
    total=False,
)

GetPersonalizedRankingResponseTypeDef = TypedDict(
    "GetPersonalizedRankingResponseTypeDef",
    {
        "personalizedRanking": List[PredictedItemTypeDef],
        "recommendationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetRecommendationsResponseTypeDef = TypedDict(
    "GetRecommendationsResponseTypeDef",
    {
        "itemList": List[PredictedItemTypeDef],
        "recommendationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetRecommendationsRequestRequestTypeDef = TypedDict(
    "GetRecommendationsRequestRequestTypeDef",
    {
        "campaignArn": str,
        "itemId": str,
        "userId": str,
        "numResults": int,
        "context": Mapping[str, str],
        "filterArn": str,
        "filterValues": Mapping[str, str],
        "recommenderArn": str,
        "promotions": Sequence[PromotionTypeDef],
    },
    total=False,
)
