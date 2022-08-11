from typing import Any, Dict, List, Optional, Text, Tuple, Union

import numpy as np
from pydantic import BaseModel
from vector_search_api.config import settings
from vector_search_api.helper.utils import batch_chunks
from vector_search_api.helper.vector import distance_to_similarity
from vector_search_api.searcher.base_vector_search import BaseVectorSearch

logger = settings.logger

try:
    import faiss
except ImportError:
    logger.warning('Trying import faiss but uninstalled.')


class FaissVectorSearch(BaseVectorSearch):

    def __init__(
        self,
        project_name: Text,
        dims: Union[Tuple, int],
        search_field: Text = 'text',
        metadata_field: Text = 'metadata',
        vector_field: Text = 'vector',
        similarity_field: Text = 'similarity',
        **kwargs
    ):
        super(FaissVectorSearch, self).__init__(
            dims=dims,
            search_field=search_field,
            metadata_field=metadata_field,
            vector_field=vector_field,
            similarity_field=similarity_field,
            **kwargs
        )
        self.project_name = project_name
        self._project = {'project_name': self.project_name}

        self._data: Dict[Text, List[Any]] = {
            self.search_field: [],
            self.metadata_field: [],
            self.vector_field: [],
        }

        self._index = faiss.IndexFlatL2(dims)

    def create_project_if_not_exists(
        self, *args, **kwargs
    ) -> Union[BaseModel, Dict[Text, Any]]:
        """Create project."""

        if self._project is None:
            self._project = {'name': self.project_name}
        return self._project

    def get_project_or_none(
        self, *args, **kwargs
    ) -> Optional[Union[BaseModel, Dict[Text, Any]]]:
        """Get project information, return None if not exists.."""

        return self._project

    def insert_documents(
        self, documents: List[Dict], batch_size: int = 200, **kwargs
    ) -> int:
        """Insert documents"""

        for batch_docs in batch_chunks(documents, batch_size=batch_size):

            batch_vectors = []
            batch_search_items = []
            brach_metadata_items = []

            for doc in batch_docs:
                batch_vectors += [doc[self.vector_field]]
                batch_search_items += [doc[self.search_field]]
                brach_metadata_items += [doc.get(self.metadata_field, {})]

            self._index.add(np.array(batch_vectors).astype('float32'))

            self._data[self.vector_field].extend(batch_vectors)
            self._data[self.search_field].extend(batch_search_items)
            self._data[self.metadata_field].extend(brach_metadata_items)

        return self.count_documents()

    def search_documents(
        self, query: List[float], size: int = 20, *args, **kwargs
    ) -> List[Dict]:
        """search documents"""

        query_np = np.array([query]).astype('float32')
        size = self._index.ntotal if size >= self._index.ntotal else size

        distances, doc_indexes = self._index.search(query_np, size)

        result: List[Dict] = [
            {
                self.search_field: self._data[self.search_field][idx],
                self.metadata_field: self._data[self.metadata_field][idx],
                self.vector_field: self._data[self.vector_field][idx],
                self.similarity_field: distance_to_similarity(distance),
            } for distance, idx in zip(distances[0], doc_indexes[0])
        ]
        return result

    def refresh_documents(
        self,
        documents: List[Dict],
        batch_size: int = 200
    ) -> List:
        """Refresh vectors."""

        self._data: Dict[Text, List[Any]] = {
            self.search_field: [],
            self.metadata_field: [],
            self.vector_field: [],
        }
        self.insert_documents(
            documents=documents,
            batch_size=batch_size
        )
        return self.count_documents()

    def count_documents(self) -> int:
        """Count documents."""

        return len(self._data.get(self.vector_field, []))
