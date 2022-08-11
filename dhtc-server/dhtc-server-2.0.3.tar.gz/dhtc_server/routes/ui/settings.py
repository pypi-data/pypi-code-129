from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from dhtc_server.models.Torrent import Torrent, TorrentFile
from dhtc_server.routes.ui import make_response

router = APIRouter()


@router.get("/settings", response_class=HTMLResponse)
async def settings(request: Request):
    return make_response(request, {}, "settings.html")


@router.post("/settings", response_class=HTMLResponse)
async def settings(request: Request):
    await Torrent.delete_all()  # TODO
    await TorrentFile.delete_all()  # TODO
    return make_response(request, {}, "settings.html")
