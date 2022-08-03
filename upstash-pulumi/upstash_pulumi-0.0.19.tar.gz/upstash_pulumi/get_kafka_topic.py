# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetKafkaTopicResult',
    'AwaitableGetKafkaTopicResult',
    'get_kafka_topic',
    'get_kafka_topic_output',
]

@pulumi.output_type
class GetKafkaTopicResult:
    """
    A collection of values returned by getKafkaTopic.
    """
    def __init__(__self__, cleanup_policy=None, cluster_id=None, creation_time=None, id=None, max_message_size=None, multizone=None, partitions=None, password=None, region=None, rest_endpoint=None, retention_size=None, retention_time=None, state=None, tcp_endpoint=None, topic_id=None, topic_name=None, username=None):
        if cleanup_policy and not isinstance(cleanup_policy, str):
            raise TypeError("Expected argument 'cleanup_policy' to be a str")
        pulumi.set(__self__, "cleanup_policy", cleanup_policy)
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if creation_time and not isinstance(creation_time, int):
            raise TypeError("Expected argument 'creation_time' to be a int")
        pulumi.set(__self__, "creation_time", creation_time)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if max_message_size and not isinstance(max_message_size, int):
            raise TypeError("Expected argument 'max_message_size' to be a int")
        pulumi.set(__self__, "max_message_size", max_message_size)
        if multizone and not isinstance(multizone, bool):
            raise TypeError("Expected argument 'multizone' to be a bool")
        pulumi.set(__self__, "multizone", multizone)
        if partitions and not isinstance(partitions, int):
            raise TypeError("Expected argument 'partitions' to be a int")
        pulumi.set(__self__, "partitions", partitions)
        if password and not isinstance(password, str):
            raise TypeError("Expected argument 'password' to be a str")
        pulumi.set(__self__, "password", password)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if rest_endpoint and not isinstance(rest_endpoint, str):
            raise TypeError("Expected argument 'rest_endpoint' to be a str")
        pulumi.set(__self__, "rest_endpoint", rest_endpoint)
        if retention_size and not isinstance(retention_size, int):
            raise TypeError("Expected argument 'retention_size' to be a int")
        pulumi.set(__self__, "retention_size", retention_size)
        if retention_time and not isinstance(retention_time, int):
            raise TypeError("Expected argument 'retention_time' to be a int")
        pulumi.set(__self__, "retention_time", retention_time)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tcp_endpoint and not isinstance(tcp_endpoint, str):
            raise TypeError("Expected argument 'tcp_endpoint' to be a str")
        pulumi.set(__self__, "tcp_endpoint", tcp_endpoint)
        if topic_id and not isinstance(topic_id, str):
            raise TypeError("Expected argument 'topic_id' to be a str")
        pulumi.set(__self__, "topic_id", topic_id)
        if topic_name and not isinstance(topic_name, str):
            raise TypeError("Expected argument 'topic_name' to be a str")
        pulumi.set(__self__, "topic_name", topic_name)
        if username and not isinstance(username, str):
            raise TypeError("Expected argument 'username' to be a str")
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="cleanupPolicy")
    def cleanup_policy(self) -> str:
        return pulumi.get(self, "cleanup_policy")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> int:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="maxMessageSize")
    def max_message_size(self) -> int:
        return pulumi.get(self, "max_message_size")

    @property
    @pulumi.getter
    def multizone(self) -> bool:
        return pulumi.get(self, "multizone")

    @property
    @pulumi.getter
    def partitions(self) -> int:
        return pulumi.get(self, "partitions")

    @property
    @pulumi.getter
    def password(self) -> str:
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="restEndpoint")
    def rest_endpoint(self) -> str:
        return pulumi.get(self, "rest_endpoint")

    @property
    @pulumi.getter(name="retentionSize")
    def retention_size(self) -> int:
        return pulumi.get(self, "retention_size")

    @property
    @pulumi.getter(name="retentionTime")
    def retention_time(self) -> int:
        return pulumi.get(self, "retention_time")

    @property
    @pulumi.getter
    def state(self) -> str:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="tcpEndpoint")
    def tcp_endpoint(self) -> str:
        return pulumi.get(self, "tcp_endpoint")

    @property
    @pulumi.getter(name="topicId")
    def topic_id(self) -> str:
        return pulumi.get(self, "topic_id")

    @property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> str:
        return pulumi.get(self, "topic_name")

    @property
    @pulumi.getter
    def username(self) -> str:
        return pulumi.get(self, "username")


class AwaitableGetKafkaTopicResult(GetKafkaTopicResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKafkaTopicResult(
            cleanup_policy=self.cleanup_policy,
            cluster_id=self.cluster_id,
            creation_time=self.creation_time,
            id=self.id,
            max_message_size=self.max_message_size,
            multizone=self.multizone,
            partitions=self.partitions,
            password=self.password,
            region=self.region,
            rest_endpoint=self.rest_endpoint,
            retention_size=self.retention_size,
            retention_time=self.retention_time,
            state=self.state,
            tcp_endpoint=self.tcp_endpoint,
            topic_id=self.topic_id,
            topic_name=self.topic_name,
            username=self.username)


def get_kafka_topic(topic_id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKafkaTopicResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_upstash as upstash

    kafka_topic_data = upstash.get_kafka_topic(topic_id=resource["upstash_kafka_topic"]["exampleKafkaTopic"]["topic_id"])
    ```
    """
    __args__ = dict()
    __args__['topicId'] = topic_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
    __ret__ = pulumi.runtime.invoke('upstash:index/getKafkaTopic:getKafkaTopic', __args__, opts=opts, typ=GetKafkaTopicResult).value

    return AwaitableGetKafkaTopicResult(
        cleanup_policy=__ret__.cleanup_policy,
        cluster_id=__ret__.cluster_id,
        creation_time=__ret__.creation_time,
        id=__ret__.id,
        max_message_size=__ret__.max_message_size,
        multizone=__ret__.multizone,
        partitions=__ret__.partitions,
        password=__ret__.password,
        region=__ret__.region,
        rest_endpoint=__ret__.rest_endpoint,
        retention_size=__ret__.retention_size,
        retention_time=__ret__.retention_time,
        state=__ret__.state,
        tcp_endpoint=__ret__.tcp_endpoint,
        topic_id=__ret__.topic_id,
        topic_name=__ret__.topic_name,
        username=__ret__.username)


@_utilities.lift_output_func(get_kafka_topic)
def get_kafka_topic_output(topic_id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKafkaTopicResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_upstash as upstash

    kafka_topic_data = upstash.get_kafka_topic(topic_id=resource["upstash_kafka_topic"]["exampleKafkaTopic"]["topic_id"])
    ```
    """
    ...
