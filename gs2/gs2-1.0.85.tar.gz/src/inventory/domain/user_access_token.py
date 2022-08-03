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
from inventory import Gs2InventoryRestClient, request as request_, result as result_
from inventory.domain.iterator.namespaces import DescribeNamespacesIterator
from inventory.domain.iterator.inventory_model_masters import DescribeInventoryModelMastersIterator
from inventory.domain.iterator.inventory_models import DescribeInventoryModelsIterator
from inventory.domain.iterator.item_model_masters import DescribeItemModelMastersIterator
from inventory.domain.iterator.item_models import DescribeItemModelsIterator
from inventory.domain.iterator.inventories import DescribeInventoriesIterator
from inventory.domain.iterator.inventories_by_user_id import DescribeInventoriesByUserIdIterator
from inventory.domain.iterator.item_sets import DescribeItemSetsIterator
from inventory.domain.iterator.item_sets_by_user_id import DescribeItemSetsByUserIdIterator
from inventory.domain.iterator.reference_of import DescribeReferenceOfIterator
from inventory.domain.iterator.reference_of_by_user_id import DescribeReferenceOfByUserIdIterator
from inventory.domain.cache.namespace import NamespaceDomainCache
from inventory.domain.cache.inventory_model_master import InventoryModelMasterDomainCache
from inventory.domain.cache.inventory_model import InventoryModelDomainCache
from inventory.domain.cache.item_model_master import ItemModelMasterDomainCache
from inventory.domain.cache.item_model import ItemModelDomainCache
from inventory.domain.cache.inventory import InventoryDomainCache
from inventory.domain.cache.item_set import ItemSetDomainCache
from inventory.domain.inventory import InventoryDomain
from inventory.domain.inventory_access_token import InventoryAccessTokenDomain
from inventory.domain.inventory_access_token import InventoryAccessTokenDomain


class UserAccessTokenDomain:
    _session: Gs2RestSession
    _client: Gs2InventoryRestClient
    _namespace_name: str
    _access_token: AccessToken
    _inventory_cache: InventoryDomainCache

    def __init__(
        self,
        session: Gs2RestSession,
        namespace_name: str,
        access_token: AccessToken,
    ):
        self._session = session
        self._client = Gs2InventoryRestClient(
            session,
        )
        self._namespace_name = namespace_name
        self._access_token = access_token
        self._inventory_cache = InventoryDomainCache()

    def inventories(
        self,
    ) -> DescribeInventoriesIterator:
        return DescribeInventoriesIterator(
            self._inventory_cache,
            self._client,
            self._namespace_name,
            self._access_token,
        )

    def inventory(
        self,
        inventory_name: str,
    ) -> InventoryAccessTokenDomain:
        return InventoryAccessTokenDomain(
            self._session,
            self._inventory_cache,
            self._namespace_name,
            self._access_token,
            inventory_name,
        )
