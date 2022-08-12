import inspect
from typing import Any, Dict
import binascii
import os
import random as rand
from typing import Type
import uuid
from mimesis import Person
from mimesis.locales import Locale
from mimesis.enums import Gender
from pathlib import Path
import jwt

class Unset:
    def __str__(self) -> str:
        return "<UNSET>"

    __repr__ = __str__

    def __bool__(self) -> bool:
        return False

    def __copy__(self):
        return UNSET

    def __deepcopy__(self, memo: Dict[int, Any]):
        return UNSET

    @classmethod
    def __get_validators__(cls):
        yield cls._validate

    @classmethod
    def _validate(cls, value: Any):
        if value is not UNSET:
            raise ValueError(f"{value!r} is not UNSET")
        return value


UNSET = Unset()


def exclude_unset(data: Any) -> Any:
    if isinstance(data, dict):
        return data.__class__(
            (k, exclude_unset(v)) for k, v in data.items() if v is not UNSET
        )
    elif data is UNSET:
        return None
    return data


def is_async(obj: Any) -> bool:
    return inspect.isroutine(obj) and inspect.iscoroutinefunction(obj)




person = Person(Locale.EN)


def create_hexstr(size: int) -> str:
    return binascii.b2a_hex(os.urandom(size)).decode("ascii")


def create_full_name() -> str:
    return person.name()


def create_username() -> str:
    return person.username()


def create_email() -> str:
    return person.email()


def create_password(size=32) -> str:
    return person.password(size)


def base_assert(func: bool, exception: Type[BaseException], msg: str) -> None:
    if not func:
        raise exception(msg)


def skip_params(count: int, remaining: int = 1, max_size: int = 10) -> int:
    skip_max = count - (remaining)
    skip = rand.randint(1, skip_max)
    left_after_skip = count - skip

    return skip, min(left_after_skip, max_size)


def gen_ref():
    return uuid.uuid4().hex[:20]


def read_file(file_path: Path | str) -> bytes:
    return Path(file_path).read_bytes()

