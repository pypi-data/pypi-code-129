from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse

from dhtc_server.routes.ui import make_response

from dhtc_server.models.Watch import Watch

from dhtc_server.enums.SearchType import SearchType
from dhtc_server.enums.SearchMode import SearchMode

router = APIRouter()


@router.get("/watches", response_class=HTMLResponse)
async def watches(request: Request):
    return make_response(request, {
        "query": "",
        "results": await Watch.find_all().to_list()
    }, "watches.html")


@router.post("/watches", response_class=HTMLResponse)
async def watches(request: Request,
                  type: SearchType = Form(),
                  mode: SearchMode = Form(),
                  text: str = Form()):
    watch = Watch(
        type=type,
        mode=mode,
        text=text
    )

    await watch.save()

    return make_response(request, {
        "query": "",
        "results": await Watch.find_all().to_list()
    }, "watches.html")
