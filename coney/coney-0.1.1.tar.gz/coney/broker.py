from enum import Enum
from typing import Any, Callable, Optional, overload

import aio_pika
from aio_pika.abc import (
    AbstractChannel,
    AbstractConnection,
    AbstractExchange,
    AbstractIncomingMessage,
    AbstractMessage,
    AbstractQueue,
    ConsumerTag,
)
from aiormq.abc import ConfirmationFrameType


class BindingType(str, Enum):
    queue = "queue"
    exchange = "exchange"


class Binding:
    source: str
    destination: str
    type: BindingType
    keys: list[str]
    args: dict[str, Any]

    def __init__(
        self, s: str, d: str, t: BindingType = BindingType.queue, *k: str, **args: Any
    ):
        self.source = s
        self.destination = d
        self.type = t
        self.keys = list(k)
        self.args = args


class Broker:
    connection: AbstractConnection
    channel: AbstractChannel
    exchanges: dict[str, AbstractExchange]
    queues: dict[str, AbstractQueue]
    _args: tuple[Any]
    _kwargs: dict[str, Any]

    @overload
    def __init__(self, *args: Any, **kwargs: Any):
        ...

    @overload
    def __init__(
        self,
        *args: Any,
        exchanges: dict[str, dict[str, Any]] = {},
        queues: dict[str, dict[str, Any]] = {},
        bindings: list[Binding] = [],
        **kwargs: Any,
    ):
        ...

    def __init__(
        self,
        *args: Any,
        **kwargs: Any,
    ):
        self._args = args
        self._kwargs = kwargs

    async def publish(
        self, ex: str, msg: AbstractMessage, key: str
    ) -> Optional[ConfirmationFrameType]:
        exchange = self.exchanges.get(ex)

        if not exchange:
            return None

        return await exchange.publish(msg, key)

    async def subscribe(
        self,
        q: str,
        cb: Callable[[AbstractIncomingMessage], Any],
        no_ack: bool = False,
    ) -> Optional[ConsumerTag]:
        queue = self.queues.get(q)

        if not queue:
            return None

        return await queue.consume(cb, no_ack)

    async def bind(
        self,
        src: str,
        dst: str,
        keys: list[str],
        type: Optional[BindingType] = BindingType.queue,
        **kwargs: Any,
    ):
        source = self.exchanges.get(src)
        destination = (
            self.queues.get(dst)
            if type == BindingType.queue
            else self.exchanges.get(dst)
        )

        if not destination or not source:
            raise KeyError()

        if len(keys):
            for k in keys:
                await destination.bind(source, k, **kwargs)
        else:
            await destination.bind(source, **kwargs)
        await destination.bind(source)

    async def close(self):
        await self.connection.close()

    async def connect(self) -> "Broker":
        if self.connection and not self.connection.is_closed:
            return self

        args = self._args
        kwargs = self._kwargs

        exchanges: dict[str, dict[str, Any]] = kwargs.pop("exchanges", {})
        queues: dict[str, dict[str, Any]] = kwargs.pop("queues", {})
        bindings: list[Binding] = kwargs.pop("bindings", [])

        self.connection = await aio_pika.connect_robust(*args, **kwargs)

        self.channel = await self.connection.channel()

        e = dict(
            [
                (k, await self.channel.declare_exchange(**v))
                for k, v in exchanges.items()
            ]
        )

        self.exchanges = e

        q = dict(
            [(k, await self.channel.declare_queue(**v)) for k, v in queues.items()]
        )

        self.queues = q

        for b in bindings:
            await self.bind(b.source, b.destination, b.keys, b.type, **b.args)

        return self

    async def __aenter__(self):
        return await self.connect()

    async def __aexit__(self):
        return await self.connection.close()
