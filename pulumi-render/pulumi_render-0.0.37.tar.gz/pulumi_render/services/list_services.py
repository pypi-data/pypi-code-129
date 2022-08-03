# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'ListServicesResult',
    'AwaitableListServicesResult',
    'list_services',
]

@pulumi.output_type
class ListServicesResult:
    def __init__(__self__, items=None):
        if items and not isinstance(items, list):
            raise TypeError("Expected argument 'items' to be a list")
        pulumi.set(__self__, "items", items)

    @property
    @pulumi.getter
    def items(self) -> Sequence['outputs.ListServiceResponse']:
        return pulumi.get(self, "items")


class AwaitableListServicesResult(ListServicesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListServicesResult(
            items=self.items)


def list_services(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListServicesResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('render:services:listServices', __args__, opts=opts, typ=ListServicesResult).value

    return AwaitableListServicesResult(
        items=__ret__.items)
