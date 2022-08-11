from __future__ import annotations

import re
from itertools import product
from typing import List, Tuple

from fuzzywuzzy import fuzz


def search(search_string: str, content: List[str]) -> List[str]:
    r: List[str] = []
    search_string = f"^{search_string.replace('*', '.+')}$"
    for s in content:
        if re.search(search_string, s):
            r.append(s)
    return r


def fuzzy_match(search_string: str,
                contents: List[str],
                min_match_score: int = 75) -> List[Tuple[str, str]]:
    """

    Args:
        search_string: string to fuzzy match on
        contents: list of strings to match against
        min_match_score: whole number percentage score

    Returns: List of tuples (search_string, match)

    """
    r = fuzzy_match_lists(strings1=[search_string], strings2=contents, min_match_score=min_match_score)
    return r


def fuzzy_match_lists(strings1: List[str],
                      strings2: List[str],
                      min_match_score: int) -> List[Tuple[str, str]]:
    """

    Args:
        strings1: list of strings to match on
        strings2: list of strings to match against
        min_match_score: whole number percentage score

    Returns: List of tuples (search_string, match)

    """
    carteasien = set(product(set(strings1), set(strings2)))
    l: List[Tuple[str, str]] = []

    for i in carteasien:
        r = fuzz.token_set_ratio(i[0], i[1])
        if r >= min_match_score:
            l.append(i)

    return l
