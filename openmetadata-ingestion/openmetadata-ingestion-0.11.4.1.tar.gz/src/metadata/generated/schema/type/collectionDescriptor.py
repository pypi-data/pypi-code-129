# generated by datamodel-codegen:
#   filename:  schema/type/collectionDescriptor.json
#   timestamp: 2022-08-03T16:24:31+00:00

from __future__ import annotations

from typing import Optional

from pydantic import AnyUrl, BaseModel, Extra, Field

from . import profile


class CollectionInfo(BaseModel):
    class Config:
        extra = Extra.forbid

    name: Optional[str] = Field(
        None, description='Unique name that identifies a collection.'
    )
    documentation: Optional[str] = Field(None, description='Description of collection.')
    href: Optional[AnyUrl] = Field(
        None,
        description='URL of the API endpoint where given collections are available.',
    )
    images: Optional[profile.ImageList] = None


class CollectionDescriptor(BaseModel):
    class Config:
        extra = Extra.forbid

    collection: Optional[CollectionInfo] = None
