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
from dictionary import Gs2DictionaryRestClient, request as request_, result as result_
from dictionary.domain.iterator.namespaces import DescribeNamespacesIterator
from dictionary.domain.iterator.entry_models import DescribeEntryModelsIterator
from dictionary.domain.iterator.entry_model_masters import DescribeEntryModelMastersIterator
from dictionary.domain.iterator.entries import DescribeEntriesIterator
from dictionary.domain.iterator.entries_by_user_id import DescribeEntriesByUserIdIterator
from dictionary.domain.cache.namespace import NamespaceDomainCache
from dictionary.domain.cache.entry_model import EntryModelDomainCache
from dictionary.domain.cache.entry_model_master import EntryModelMasterDomainCache
from dictionary.domain.cache.entry import EntryDomainCache
from dictionary.domain.entry import EntryDomain
from dictionary.domain.entry_access_token import EntryAccessTokenDomain
from dictionary.domain.entry_access_token import EntryAccessTokenDomain


class UserDomain:
    _session: Gs2RestSession
    _client: Gs2DictionaryRestClient
    _namespace_name: str
    _user_id: str
    _entry_cache: EntryDomainCache

    def __init__(
        self,
        session: Gs2RestSession,
        namespace_name: str,
        user_id: str,
    ):
        self._session = session
        self._client = Gs2DictionaryRestClient(
            session,
        )
        self._namespace_name = namespace_name
        self._user_id = user_id
        self._entry_cache = EntryDomainCache()

    def add_entries(
        self,
        request: request_.AddEntriesByUserIdRequest,
    ) -> result_.AddEntriesByUserIdResult:
        request.with_namespace_name(self._namespace_name)
        request.with_user_id(self._user_id)
        r = self._client.add_entries_by_user_id(
            request,
        )
        return r

    def reset(
        self,
        request: request_.ResetByUserIdRequest,
    ) -> result_.ResetByUserIdResult:
        request.with_namespace_name(self._namespace_name)
        request.with_user_id(self._user_id)
        r = self._client.reset_by_user_id(
            request,
        )
        return r

    def entries(
        self,
    ) -> DescribeEntriesByUserIdIterator:
        return DescribeEntriesByUserIdIterator(
            self._entry_cache,
            self._client,
            self._namespace_name,
            self._user_id,
        )

    def entry(
        self,
        entry_model_name: str,
    ) -> EntryDomain:
        return EntryDomain(
            self._session,
            self._entry_cache,
            self._namespace_name,
            self._user_id,
            entry_model_name,
        )
