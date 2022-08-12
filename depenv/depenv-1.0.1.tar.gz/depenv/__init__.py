import importlib
import inspect
import os
import sys
from abc import ABC


class Injectable(ABC):
    def __new__(cls, *args, **kwargs):
        # Don't inject grandchildren of Injectable classes
        if any(
            issubclass(base, Injectable) and not base == Injectable
            for base in cls.__bases__
        ):
            return super().__new__(cls)

        case_sensitive_module = cls.__module__.replace(".", "_")
        case_insensitive_module = case_sensitive_module.upper()
        case_sensitive_name = cls.__name__
        case_insensitive_name = cls.__name__.upper()

        env_vars = [
            case_sensitive_module + "_" + case_sensitive_name,
            case_sensitive_module + "_" + case_insensitive_name,
            case_insensitive_module + "_" + case_sensitive_name,
            case_insensitive_module + "_" + case_insensitive_name,
            case_sensitive_name,
            case_insensitive_name,
        ]

        implementations = [os.getenv("DEPENV_" + env_var) for env_var in env_vars]

        # No implementation is specified in the environment
        if not any(implementations):
            return super().__new__(cls)

        # Use the most specific environment variable that matches
        implementation = next(
            implementation
            for implementation in implementations
            if implementation is not None
        )

        split = implementation.rsplit(".", 1)
        # The implementation specifies a module and class
        if len(split) > 1:
            module_name, class_name = split
            # Memoize imports
            if not sys.modules.get(module_name):
                module = importlib.import_module(module_name)
            else:
                module = sys.modules[module_name]

            obj = getattr(module, class_name)

        # The implementation only specifies a class
        else:
            class_name = implementation

            caller_locals = inspect.currentframe().f_back.f_locals
            local_class = caller_locals.get(class_name)
            # The class is in the caller's local scope
            if local_class:
                obj = caller_locals.get(class_name)
            # The class is in the caller's module
            else:
                module_name = cls.__module__
                module = sys.modules[module_name]
                obj = getattr(module, class_name)

        return obj(*args, **kwargs)
