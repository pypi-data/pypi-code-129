from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import List

from dhtc_server.models.Watch import Watch

router = APIRouter()


class AddWatchResponse(BaseModel):
    Id: str


class SearchWatchResponse(BaseModel):
    Watches: List[Watch]


@router.post("/add", response_model=AddWatchResponse)
async def watches_add(watch: Watch = Body(...)):
    return {"Id": (await watch.create()).id}


@router.get("/all", response_model=SearchWatchResponse)
async def watches_all():
    return {"Watches": (await Watch.all().to_list())}
