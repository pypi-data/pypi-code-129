import asyncio
import websockets

exg = None
tkn = None
msg = None
ws = None


def get(ws, exchange, token):
    exg = exchange
    tkn = token
    # isi = isShortIdentifier
    asyncio.get_event_loop().run_until_complete(mass_subscribe_n_stream(ws, exg, tkn))
    return


async def mass_subscribe_n_stream(ws, exg, tkn):
    try:
        req_msg = str(
            '{"MessageType":"GetLastQuoteOptionGreeks","Exchange":"' + exg + '","Token":"' + tkn + '"}')
        await ws.send(req_msg)
        print("Request : " + req_msg)
        await get_msg(ws)
    except:
        return msg


async def get_msg(ws):
    while True:
        try:
            message = await ws.recv()
        except websockets.ConnectionClosedOK:
            break
        print(message)
