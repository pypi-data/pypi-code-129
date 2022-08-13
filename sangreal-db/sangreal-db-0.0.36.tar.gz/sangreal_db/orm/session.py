from sqlalchemy.orm import Session

from .query import SangrealQuery


class SangrealSession(Session):
    def __init__(self,
                 bind=None,
                 autoflush=True,
                 future=False,
                 expire_on_commit=True,
                 autocommit=False,
                 twophase=False,
                 binds=None,
                 enable_baked_queries=True,
                 info=None,
                 query_cls=SangrealQuery):
        super().__init__(
            bind=bind,
            autoflush=autoflush,
            future=future,
            expire_on_commit=expire_on_commit,
            autocommit=autocommit,
            twophase=twophase,
            binds=binds,
            enable_baked_queries=enable_baked_queries,
            info=info,
            query_cls=query_cls)
