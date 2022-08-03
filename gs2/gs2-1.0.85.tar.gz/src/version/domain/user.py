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
from version import Gs2VersionRestClient, request as request_, result as result_
from version.domain.iterator.namespaces import DescribeNamespacesIterator
from version.domain.iterator.version_model_masters import DescribeVersionModelMastersIterator
from version.domain.iterator.version_models import DescribeVersionModelsIterator
from version.domain.iterator.accept_versions import DescribeAcceptVersionsIterator
from version.domain.iterator.accept_versions_by_user_id import DescribeAcceptVersionsByUserIdIterator
from version.domain.cache.namespace import NamespaceDomainCache
from version.domain.cache.version_model_master import VersionModelMasterDomainCache
from version.domain.cache.version_model import VersionModelDomainCache
from version.domain.cache.accept_version import AcceptVersionDomainCache
from version.domain.accept_version import AcceptVersionDomain
from version.domain.accept_version_access_token import AcceptVersionAccessTokenDomain
from version.domain.accept_version_access_token import AcceptVersionAccessTokenDomain


class UserDomain:
    _session: Gs2RestSession
    _client: Gs2VersionRestClient
    _namespace_name: str
    _user_id: str
    _accept_version_cache: AcceptVersionDomainCache

    def __init__(
        self,
        session: Gs2RestSession,
        namespace_name: str,
        user_id: str,
    ):
        self._session = session
        self._client = Gs2VersionRestClient(
            session,
        )
        self._namespace_name = namespace_name
        self._user_id = user_id
        self._accept_version_cache = AcceptVersionDomainCache()

    def check_version(
        self,
        request: request_.CheckVersionByUserIdRequest,
    ) -> result_.CheckVersionByUserIdResult:
        request.with_namespace_name(self._namespace_name)
        request.with_user_id(self._user_id)
        r = self._client.check_version_by_user_id(
            request,
        )
        return r

    def accept_versions(
        self,
    ) -> DescribeAcceptVersionsByUserIdIterator:
        return DescribeAcceptVersionsByUserIdIterator(
            self._accept_version_cache,
            self._client,
            self._namespace_name,
            self._user_id,
        )

    def accept_version(
        self,
        version_name: str,
    ) -> AcceptVersionDomain:
        return AcceptVersionDomain(
            self._session,
            self._accept_version_cache,
            self._namespace_name,
            self._user_id,
            version_name,
        )
