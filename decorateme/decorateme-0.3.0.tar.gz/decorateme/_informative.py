"""
Decorators that do nothing.
"""
from typing import Type, TypeVar

T = TypeVar("T", bound=Type)


def overrides(cls: T) -> T:
    """
    Overriding this class is generally recommended (but not required).
    """
    return cls


def override_recommended(cls: T) -> T:
    """
    Overriding this class is suggested.
    """
    return cls


def internal(cls: T) -> T:
    """
    This class or package is meant to be used only by code within this project.
    """
    return cls


def external(cls: T) -> T:
    """
    This class or package is meant to be used *only* by code outside this project.
    """
    return cls


def reserved(cls: T) -> T:
    """
    This package, class, or function is empty but is declared for future use.
    """
    return cls


def thread_safe(cls: T) -> T:
    """
    Just marks that something **is** thread-safe.
    """
    return cls


def not_thread_safe(cls: T) -> T:
    """
    Just marks that something is **not** thread-safe.
    """
    return cls


def recommend_final(cls: T) -> T:
    """
    Marks as "should not override".
    """
    return cls
