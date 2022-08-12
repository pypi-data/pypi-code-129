"""
Utilities for decorateme.
"""
from typing import Callable, Optional, Set


class _SpecialStr(str):
    """
    A string that can be displayed with Jupyter with line breaks and tabs.
    """

    def __init__(self, s: str):
        super().__init__()
        self.s = str(s)

    def __repr__(self):
        return repr(self.s)

    def __str__(self):
        return str(self.s)

    def _repr_html_(self):
        return str(self.s.replace("\n", "<br />").replace("\t", "&emsp;&emsp;&emsp;&emsp;"))


class _InfoSpecialStr(_SpecialStr):
    def _repr_html_(self):
        if len(self.s) == 0:
            return self.s
        lines = self.s.split("\n")
        built = "<strong>" + lines[0] + "</strong><br/>\n"
        if len(lines) > 1:
            for line in lines[1:-1]:
                if "=" in line:
                    k, v = line[: line.index("=")], line[line.index("=") :]
                    built += "&emsp;&emsp;&emsp;&emsp;<strong>" + k + "</strong>" + v + "<br/>\n"
                else:
                    built += line + "<br />\n"
        built += "<strong>)</strong>\n"
        return str(built)


class _Utils:
    def gen_str(
        self,
        only: Optional[Set[str]] = None,
        exclude: Optional[Callable[[str], bool]] = None,
        bold_surround: Callable[[str], str] = str,
        em_surround: Callable[[str], str] = str,
        delim: str = ", ",
        eq: str = "=",
        opening: str = "(",
        closing: str = ")",
        with_address: bool = True,
    ):
        if exclude is None:
            exclude = lambda _: False
        _vars = _Utils.var_items(self, only, exclude)
        return (
            bold_surround(self.__class__.__name__)
            + opening
            + delim.join([k + eq + str(v) for k, v in _vars])
            + em_surround(" @ " + str(hex(id(self))) if with_address else "")
            + closing
        )

    @classmethod
    def var_items(cls, obj, only, exclude):
        return [
            (key, value)
            for key, value in vars(obj).items()
            if (only is None) or (key in only)
            if not exclude(key)
        ]

    @classmethod
    def var_values(cls, obj, only, exclude):
        items = vars(obj).items()
        return [
            value
            for key, value in items
            if ((only is None) or key in only) and not exclude(key) and value is not None
        ]

    @classmethod
    def auto_hash(cls, self, only: Optional[Set[str]], exclude: Optional[Callable[[str], bool]]):
        if exclude is None:
            exclude = lambda _: False
        return hash(tuple(_Utils.var_values(self, only, exclude)))

    @classmethod
    def auto_eq(
        cls,
        self,
        other,
        only: Optional[Set[str]],
        exclude: Optional[Callable[[str], bool]],
    ):
        if type(self) != type(other):
            raise TypeError(f"Type {type(self)} is not the same as type {type(other)}")
        if exclude is None:
            exclude = lambda _: False
        return _Utils.var_values(self, only=only, exclude=exclude) == _Utils.var_values(
            other, only, exclude
        )
