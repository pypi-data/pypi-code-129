#   Copyright 2020-2022 Exactpro (Exactpro Systems Limited)
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from typing import Iterator, List, Optional, Union

from th2_grpc_common.common_pb2 import Checkpoint, Message, RequestStatus


class ActResponse:
    """ActResponse may be returned to act implementation by Act. The class instance can contain message, status and
    checkpoint fields, which can be used when creating custom response objects.
    """

    __slots__ = ('message', 'status', 'checkpoint')

    def __init__(self,
                 message: Optional[Message] = None,
                 status: Union[str, int] = RequestStatus.SUCCESS,
                 checkpoint: Optional[Checkpoint] = None) -> None:
        self.message = message
        self.status = RequestStatus(status=status)  # type: ignore
        self.checkpoint = checkpoint


class ActMultiResponse:
    """ActMultiResponse may be returned to act implementation by Act. The class instance can contain list of messages,
    status and checkpoint fields, which can be used when creating custom response objects.
    """

    __slots__ = ('messages', 'status', 'checkpoint')

    def __init__(self,
                 messages: Optional[List[Message]] = None,
                 status: Union[str, int] = RequestStatus.SUCCESS,
                 checkpoint: Optional[Checkpoint] = None) -> None:
        if messages is None:
            self.messages = []
        else:
            self.messages = messages
        self.status = RequestStatus(status=status)  # type: ignore
        self.checkpoint = checkpoint

    def __iter__(self) -> Iterator:
        return self.messages.__iter__()

    def __getitem__(self, item: int) -> Message:
        return self.messages[item]

    def __len__(self) -> int:
        return len(self.messages)
