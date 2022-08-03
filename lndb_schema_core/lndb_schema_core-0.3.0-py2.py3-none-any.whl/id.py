import random
import string


def id_base62(n_char: int) -> str:
    base62 = string.digits + string.ascii_letters.swapcase()
    id = "".join(random.choice(base62) for i in range(n_char))
    return id


def id_base26(n_char: int):
    base26 = string.ascii_lowercase
    id = "".join(random.choice(base26) for i in range(n_char))
    return id


def id_schema_module():
    return id_base26(4)


def id_dobject() -> str:
    """IDs for dobject.

    21 characters (62**21=4e+37 possibilities) outperform UUID (2*122=5e+36).
    """
    return id_base62(n_char=21)


def id_dtransform() -> str:
    return id_base62(n_char=22)


def id_user() -> str:
    """User ID with 8 base62 characters.

    Consistent with 1M users producing 1k notebooks.
    Safe for 100k users producing 10k notebooks.

    Allows >2e14 users.

    This is one of 2 IDs that are centralized.

    Collision probability in decentralized system is:

    ======= ===========
    n_users p_collision
    ======= ===========
    100k    2e-05
    1M      2e-03
    """
    return id_base62(n_char=8)


def id_usage() -> str:
    return id_base62(n_char=24)


def id_secret() -> str:
    return id_base62(n_char=40)


def id_instance() -> str:
    return id_base62(n_char=12)
