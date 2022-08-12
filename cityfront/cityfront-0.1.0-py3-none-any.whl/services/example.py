# pylint: disable=too-few-public-methods
import debugpy
import devtools as dtv
import vcr
from anyio import run
from loguru import logger as log
from pydantic import BaseModel

from cityfront.client import BaseService, ClientBase


class CreateExample(BaseModel):
    """This is an example model for the CreateExample service."""

    name: str
    description: str


class Example(BaseService):
    def __init__(self, client: "ClientBase"):
        super().__init__(client, "/example")

    async def create_example(self, data: CreateExample) -> dict:
        headers = {}

        return await self.client.post(self.svc_path("/"), data=data, headers=headers)


async def main():

    BASE_URL = "https://appwrite.autoworkz.org/v1"
    with vcr.use_cassette(
        "synopsis.yaml", allow_playback_repeats=False, record_mode="all"
    ) as cass:
        client = ClientBase(base_url=BASE_URL)
        client.project = "62ea325a84fe91d4179d"
        client.set_self_signed()
        example_svc = Example(client)

        exp_path = example_svc.client.create_path(example_svc.svc_path("/"))
        log.info(exp_path)
        await example_svc.create_example(
            CreateExample(name="tests", description="test")
        )
        dtv.debug(cass.requests[-1].headers)
        dtv.debug(cass.requests[-1].headers)


if __name__ == "__main__":
    run(main)
