# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.
from __future__ import annotations

from core import Gs2RestSession
from core.domain.access_token import AccessToken
from ranking import Gs2RankingRestClient, request as request_, result as result_
from ranking.domain.iterator.namespaces import DescribeNamespacesIterator
from ranking.domain.iterator.category_models import DescribeCategoryModelsIterator
from ranking.domain.iterator.category_model_masters import DescribeCategoryModelMastersIterator
from ranking.domain.iterator.subscribes_by_category_name import DescribeSubscribesByCategoryNameIterator
from ranking.domain.iterator.subscribes_by_category_name_and_user_id import DescribeSubscribesByCategoryNameAndUserIdIterator
from ranking.domain.iterator.scores import DescribeScoresIterator
from ranking.domain.iterator.scores_by_user_id import DescribeScoresByUserIdIterator
from ranking.domain.iterator.rankings import DescribeRankingsIterator
from ranking.domain.iterator.rankings_by_user_id import DescribeRankingsByUserIdIterator
from ranking.domain.iterator.near_rankings import DescribeNearRankingsIterator
from ranking.domain.cache.namespace import NamespaceDomainCache
from ranking.domain.cache.category_model import CategoryModelDomainCache
from ranking.domain.cache.category_model_master import CategoryModelMasterDomainCache
from ranking.domain.cache.subscribe_user import SubscribeUserDomainCache
from ranking.domain.cache.score import ScoreDomainCache
from ranking.domain.cache.ranking import RankingDomainCache


class CategoryModelMasterDomain:
    _session: Gs2RestSession
    _client: Gs2RankingRestClient
    _category_model_master_cache: CategoryModelMasterDomainCache
    _namespace_name: str
    _category_name: str

    def __init__(
        self,
        session: Gs2RestSession,
        category_model_master_cache: CategoryModelMasterDomainCache,
        namespace_name: str,
        category_name: str,
    ):
        self._session = session
        self._client = Gs2RankingRestClient(
            session,
        )
        self._category_model_master_cache = category_model_master_cache
        self._namespace_name = namespace_name
        self._category_name = category_name

    def load(
        self,
        request: request_.GetCategoryModelMasterRequest,
    ) -> result_.GetCategoryModelMasterResult:
        request.with_namespace_name(self._namespace_name)
        request.with_category_name(self._category_name)
        r = self._client.get_category_model_master(
            request,
        )
        self._category_model_master_cache.update(r.item)
        return r

    def update(
        self,
        request: request_.UpdateCategoryModelMasterRequest,
    ) -> result_.UpdateCategoryModelMasterResult:
        request.with_namespace_name(self._namespace_name)
        request.with_category_name(self._category_name)
        r = self._client.update_category_model_master(
            request,
        )
        self._category_model_master_cache.update(r.item)
        return r

    def delete(
        self,
        request: request_.DeleteCategoryModelMasterRequest,
    ) -> result_.DeleteCategoryModelMasterResult:
        request.with_namespace_name(self._namespace_name)
        request.with_category_name(self._category_name)
        r = self._client.delete_category_model_master(
            request,
        )
        self._category_model_master_cache.delete(r.item)
        return r
