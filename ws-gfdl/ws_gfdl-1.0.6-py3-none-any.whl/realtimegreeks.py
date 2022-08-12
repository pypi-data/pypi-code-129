import asyncio
import websockets

url = None
key = None
exg = None
tkn = None
msg = None


def get(ws, exchange, token):
    exg = exchange
    tkn = token
    asyncio.get_event_loop().run_until_complete(mass_subscribe_n_stream(ws, exg, tkn))
    return


def stop(ws, exchange, token):
    exg = exchange
    tkn = token
    asyncio.get_event_loop().run_until_complete(mass_unsubscribe_n_stream(ws, exg, tkn))
    return


async def mass_subscribe_n_stream(ws, exg, tkn):
    req_msg = str('{"MessageType":"SubscribeRealtimeGreeks","Exchange":"' + exg + '","Unsubscribe":"false","Token":"' + tkn + '"}')
    print("Request : " + req_msg)
    await ws.send(req_msg)
    await get_msg(ws)
    return


async def mass_unsubscribe_n_stream(ws, exg, sym):
    req_msg = str('{"MessageType":"SubscribeRealtimeGreeks","Exchange":"' + exg + '","Unsubscribe":"true","Token":"' + tkn + '"}')
    print("Request : " + req_msg)
    await ws.send(req_msg)
    await get_msg(ws)
    return


async def get_msg(ws):
    while True:
        try:
            message = await ws.recv()
        except websockets.ConnectionClosedOK:
            break
        print(message)