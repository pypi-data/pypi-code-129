# coding: utf-8

"""
    Deci Platform API

    Train, deploy, optimize and serve your models using Deci's platform, In your cloud or on premise.  # noqa: E501

    The version of the OpenAPI document: 4.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from deci_lab_client.configuration import Configuration


class ModelBenchmarkResultMetadata(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'batch_size': 'int',
        'batch_inf_time': 'float',
        'batch_inf_time_variance': 'float',
        'memory': 'float',
        'pre_inference_memory_used': 'float',
        'post_inference_memory_used': 'float',
        'total_memory_size': 'float',
        'throughput': 'float',
        'sample_inf_time': 'float',
        'include_io': 'bool',
        'framework_type': 'str',
        'framework_version': 'str',
        'inference_hardware': 'str',
        'infery_version': 'str',
        'date': 'str',
        'ctime': 'int',
        'h_to_d_mean': 'float',
        'd_to_h_mean': 'float',
        'h_to_d_variance': 'float',
        'd_to_h_variance': 'float',
        'error': 'str'
    }

    attribute_map = {
        'batch_size': 'batchSize',
        'batch_inf_time': 'batchInfTime',
        'batch_inf_time_variance': 'batchInfTimeVariance',
        'memory': 'memory',
        'pre_inference_memory_used': 'preInferenceMemoryUsed',
        'post_inference_memory_used': 'postInferenceMemoryUsed',
        'total_memory_size': 'totalMemorySize',
        'throughput': 'throughput',
        'sample_inf_time': 'sampleInfTime',
        'include_io': 'includeIo',
        'framework_type': 'frameworkType',
        'framework_version': 'frameworkVersion',
        'inference_hardware': 'inferenceHardware',
        'infery_version': 'inferyVersion',
        'date': 'date',
        'ctime': 'ctime',
        'h_to_d_mean': 'hToDMean',
        'd_to_h_mean': 'dToHMean',
        'h_to_d_variance': 'hToDVariance',
        'd_to_h_variance': 'dToHVariance',
        'error': 'error'
    }

    def __init__(self, batch_size=None, batch_inf_time=None, batch_inf_time_variance=None, memory=None, pre_inference_memory_used=None, post_inference_memory_used=None, total_memory_size=None, throughput=None, sample_inf_time=None, include_io=None, framework_type=None, framework_version=None, inference_hardware=None, infery_version=None, date=None, ctime=None, h_to_d_mean=None, d_to_h_mean=None, h_to_d_variance=None, d_to_h_variance=None, error=None, local_vars_configuration=None):  # noqa: E501
        """ModelBenchmarkResultMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._batch_size = None
        self._batch_inf_time = None
        self._batch_inf_time_variance = None
        self._memory = None
        self._pre_inference_memory_used = None
        self._post_inference_memory_used = None
        self._total_memory_size = None
        self._throughput = None
        self._sample_inf_time = None
        self._include_io = None
        self._framework_type = None
        self._framework_version = None
        self._inference_hardware = None
        self._infery_version = None
        self._date = None
        self._ctime = None
        self._h_to_d_mean = None
        self._d_to_h_mean = None
        self._h_to_d_variance = None
        self._d_to_h_variance = None
        self._error = None
        self.discriminator = None

        if batch_size is not None:
            self.batch_size = batch_size
        if batch_inf_time is not None:
            self.batch_inf_time = batch_inf_time
        if batch_inf_time_variance is not None:
            self.batch_inf_time_variance = batch_inf_time_variance
        if memory is not None:
            self.memory = memory
        if pre_inference_memory_used is not None:
            self.pre_inference_memory_used = pre_inference_memory_used
        if post_inference_memory_used is not None:
            self.post_inference_memory_used = post_inference_memory_used
        if total_memory_size is not None:
            self.total_memory_size = total_memory_size
        if throughput is not None:
            self.throughput = throughput
        if sample_inf_time is not None:
            self.sample_inf_time = sample_inf_time
        if include_io is not None:
            self.include_io = include_io
        if framework_type is not None:
            self.framework_type = framework_type
        if framework_version is not None:
            self.framework_version = framework_version
        if inference_hardware is not None:
            self.inference_hardware = inference_hardware
        if infery_version is not None:
            self.infery_version = infery_version
        if date is not None:
            self.date = date
        if ctime is not None:
            self.ctime = ctime
        if h_to_d_mean is not None:
            self.h_to_d_mean = h_to_d_mean
        if d_to_h_mean is not None:
            self.d_to_h_mean = d_to_h_mean
        if h_to_d_variance is not None:
            self.h_to_d_variance = h_to_d_variance
        if d_to_h_variance is not None:
            self.d_to_h_variance = d_to_h_variance
        if error is not None:
            self.error = error

    @property
    def batch_size(self):
        """Gets the batch_size of this ModelBenchmarkResultMetadata.  # noqa: E501


        :return: The batch_size of this ModelBenchmarkResultMetadata.  # noqa: E501
        :rtype: int
        """
        return self._batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        """Sets the batch_size of this ModelBenchmarkResultMetadata.


        :param batch_size: The batch_size of this ModelBenchmarkResultMetadata.  # noqa: E501
        :type: int
        """

        self._batch_size = batch_size

    @property
    def batch_inf_time(self):
        """Gets the batch_inf_time of this ModelBenchmarkResultMetadata.  # noqa: E501


        :return: The batch_inf_time of this ModelBenchmarkResultMetadata.  # noqa: E501
        :rtype: float
        """
        return self._batch_inf_time

    @batch_inf_time.setter
    def batch_inf_time(self, batch_inf_time):
        """Sets the batch_inf_time of this ModelBenchmarkResultMetadata.


        :param batch_inf_time: The batch_inf_time of this ModelBenchmarkResultMetadata.  # noqa: E501
        :type: float
        """

        self._batch_inf_time = batch_inf_time

    @property
    def batch_inf_time_variance(self):
        """Gets the batch_inf_time_variance of this ModelBenchmarkResultMetadata.  # noqa: E501


        :return: The batch_inf_time_variance of this ModelBenchmarkResultMetadata.  # noqa: E501
        :rtype: float
        """
        return self._batch_inf_time_variance

    @batch_inf_time_variance.setter
    def batch_inf_time_variance(self, batch_inf_time_variance):
        """Sets the batch_inf_time_variance of this ModelBenchmarkResultMetadata.


        :param batch_inf_time_variance: The batch_inf_time_variance of this ModelBenchmarkResultMetadata.  # noqa: E501
        :type: float
        """

        self._batch_inf_time_variance = batch_inf_time_variance

    @property
    def memory(self):
        """Gets the memory of this ModelBenchmarkResultMetadata.  # noqa: E501


        :return: The memory of this ModelBenchmarkResultMetadata.  # noqa: E501
        :rtype: float
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this ModelBenchmarkResultMetadata.


        :param memory: The memory of this ModelBenchmarkResultMetadata.  # noqa: E501
        :type: float
        """

        self._memory = memory

    @property
    def pre_inference_memory_used(self):
        """Gets the pre_inference_memory_used of this ModelBenchmarkResultMetadata.  # noqa: E501


        :return: The pre_inference_memory_used of this ModelBenchmarkResultMetadata.  # noqa: E501
        :rtype: float
        """
        return self._pre_inference_memory_used

    @pre_inference_memory_used.setter
    def pre_inference_memory_used(self, pre_inference_memory_used):
        """Sets the pre_inference_memory_used of this ModelBenchmarkResultMetadata.


        :param pre_inference_memory_used: The pre_inference_memory_used of this ModelBenchmarkResultMetadata.  # noqa: E501
        :type: float
        """

        self._pre_inference_memory_used = pre_inference_memory_used

    @property
    def post_inference_memory_used(self):
        """Gets the post_inference_memory_used of this ModelBenchmarkResultMetadata.  # noqa: E501


        :return: The post_inference_memory_used of this ModelBenchmarkResultMetadata.  # noqa: E501
        :rtype: float
        """
        return self._post_inference_memory_used

    @post_inference_memory_used.setter
    def post_inference_memory_used(self, post_inference_memory_used):
        """Sets the post_inference_memory_used of this ModelBenchmarkResultMetadata.


        :param post_inference_memory_used: The post_inference_memory_used of this ModelBenchmarkResultMetadata.  # noqa: E501
        :type: float
        """

        self._post_inference_memory_used = post_inference_memory_used

    @property
    def total_memory_size(self):
        """Gets the total_memory_size of this ModelBenchmarkResultMetadata.  # noqa: E501


        :return: The total_memory_size of this ModelBenchmarkResultMetadata.  # noqa: E501
        :rtype: float
        """
        return self._total_memory_size

    @total_memory_size.setter
    def total_memory_size(self, total_memory_size):
        """Sets the total_memory_size of this ModelBenchmarkResultMetadata.


        :param total_memory_size: The total_memory_size of this ModelBenchmarkResultMetadata.  # noqa: E501
        :type: float
        """

        self._total_memory_size = total_memory_size

    @property
    def throughput(self):
        """Gets the throughput of this ModelBenchmarkResultMetadata.  # noqa: E501


        :return: The throughput of this ModelBenchmarkResultMetadata.  # noqa: E501
        :rtype: float
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        """Sets the throughput of this ModelBenchmarkResultMetadata.


        :param throughput: The throughput of this ModelBenchmarkResultMetadata.  # noqa: E501
        :type: float
        """

        self._throughput = throughput

    @property
    def sample_inf_time(self):
        """Gets the sample_inf_time of this ModelBenchmarkResultMetadata.  # noqa: E501


        :return: The sample_inf_time of this ModelBenchmarkResultMetadata.  # noqa: E501
        :rtype: float
        """
        return self._sample_inf_time

    @sample_inf_time.setter
    def sample_inf_time(self, sample_inf_time):
        """Sets the sample_inf_time of this ModelBenchmarkResultMetadata.


        :param sample_inf_time: The sample_inf_time of this ModelBenchmarkResultMetadata.  # noqa: E501
        :type: float
        """

        self._sample_inf_time = sample_inf_time

    @property
    def include_io(self):
        """Gets the include_io of this ModelBenchmarkResultMetadata.  # noqa: E501


        :return: The include_io of this ModelBenchmarkResultMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._include_io

    @include_io.setter
    def include_io(self, include_io):
        """Sets the include_io of this ModelBenchmarkResultMetadata.


        :param include_io: The include_io of this ModelBenchmarkResultMetadata.  # noqa: E501
        :type: bool
        """

        self._include_io = include_io

    @property
    def framework_type(self):
        """Gets the framework_type of this ModelBenchmarkResultMetadata.  # noqa: E501


        :return: The framework_type of this ModelBenchmarkResultMetadata.  # noqa: E501
        :rtype: str
        """
        return self._framework_type

    @framework_type.setter
    def framework_type(self, framework_type):
        """Sets the framework_type of this ModelBenchmarkResultMetadata.


        :param framework_type: The framework_type of this ModelBenchmarkResultMetadata.  # noqa: E501
        :type: str
        """

        self._framework_type = framework_type

    @property
    def framework_version(self):
        """Gets the framework_version of this ModelBenchmarkResultMetadata.  # noqa: E501


        :return: The framework_version of this ModelBenchmarkResultMetadata.  # noqa: E501
        :rtype: str
        """
        return self._framework_version

    @framework_version.setter
    def framework_version(self, framework_version):
        """Sets the framework_version of this ModelBenchmarkResultMetadata.


        :param framework_version: The framework_version of this ModelBenchmarkResultMetadata.  # noqa: E501
        :type: str
        """

        self._framework_version = framework_version

    @property
    def inference_hardware(self):
        """Gets the inference_hardware of this ModelBenchmarkResultMetadata.  # noqa: E501


        :return: The inference_hardware of this ModelBenchmarkResultMetadata.  # noqa: E501
        :rtype: str
        """
        return self._inference_hardware

    @inference_hardware.setter
    def inference_hardware(self, inference_hardware):
        """Sets the inference_hardware of this ModelBenchmarkResultMetadata.


        :param inference_hardware: The inference_hardware of this ModelBenchmarkResultMetadata.  # noqa: E501
        :type: str
        """

        self._inference_hardware = inference_hardware

    @property
    def infery_version(self):
        """Gets the infery_version of this ModelBenchmarkResultMetadata.  # noqa: E501


        :return: The infery_version of this ModelBenchmarkResultMetadata.  # noqa: E501
        :rtype: str
        """
        return self._infery_version

    @infery_version.setter
    def infery_version(self, infery_version):
        """Sets the infery_version of this ModelBenchmarkResultMetadata.


        :param infery_version: The infery_version of this ModelBenchmarkResultMetadata.  # noqa: E501
        :type: str
        """

        self._infery_version = infery_version

    @property
    def date(self):
        """Gets the date of this ModelBenchmarkResultMetadata.  # noqa: E501


        :return: The date of this ModelBenchmarkResultMetadata.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this ModelBenchmarkResultMetadata.


        :param date: The date of this ModelBenchmarkResultMetadata.  # noqa: E501
        :type: str
        """

        self._date = date

    @property
    def ctime(self):
        """Gets the ctime of this ModelBenchmarkResultMetadata.  # noqa: E501


        :return: The ctime of this ModelBenchmarkResultMetadata.  # noqa: E501
        :rtype: int
        """
        return self._ctime

    @ctime.setter
    def ctime(self, ctime):
        """Sets the ctime of this ModelBenchmarkResultMetadata.


        :param ctime: The ctime of this ModelBenchmarkResultMetadata.  # noqa: E501
        :type: int
        """

        self._ctime = ctime

    @property
    def h_to_d_mean(self):
        """Gets the h_to_d_mean of this ModelBenchmarkResultMetadata.  # noqa: E501


        :return: The h_to_d_mean of this ModelBenchmarkResultMetadata.  # noqa: E501
        :rtype: float
        """
        return self._h_to_d_mean

    @h_to_d_mean.setter
    def h_to_d_mean(self, h_to_d_mean):
        """Sets the h_to_d_mean of this ModelBenchmarkResultMetadata.


        :param h_to_d_mean: The h_to_d_mean of this ModelBenchmarkResultMetadata.  # noqa: E501
        :type: float
        """

        self._h_to_d_mean = h_to_d_mean

    @property
    def d_to_h_mean(self):
        """Gets the d_to_h_mean of this ModelBenchmarkResultMetadata.  # noqa: E501


        :return: The d_to_h_mean of this ModelBenchmarkResultMetadata.  # noqa: E501
        :rtype: float
        """
        return self._d_to_h_mean

    @d_to_h_mean.setter
    def d_to_h_mean(self, d_to_h_mean):
        """Sets the d_to_h_mean of this ModelBenchmarkResultMetadata.


        :param d_to_h_mean: The d_to_h_mean of this ModelBenchmarkResultMetadata.  # noqa: E501
        :type: float
        """

        self._d_to_h_mean = d_to_h_mean

    @property
    def h_to_d_variance(self):
        """Gets the h_to_d_variance of this ModelBenchmarkResultMetadata.  # noqa: E501


        :return: The h_to_d_variance of this ModelBenchmarkResultMetadata.  # noqa: E501
        :rtype: float
        """
        return self._h_to_d_variance

    @h_to_d_variance.setter
    def h_to_d_variance(self, h_to_d_variance):
        """Sets the h_to_d_variance of this ModelBenchmarkResultMetadata.


        :param h_to_d_variance: The h_to_d_variance of this ModelBenchmarkResultMetadata.  # noqa: E501
        :type: float
        """

        self._h_to_d_variance = h_to_d_variance

    @property
    def d_to_h_variance(self):
        """Gets the d_to_h_variance of this ModelBenchmarkResultMetadata.  # noqa: E501


        :return: The d_to_h_variance of this ModelBenchmarkResultMetadata.  # noqa: E501
        :rtype: float
        """
        return self._d_to_h_variance

    @d_to_h_variance.setter
    def d_to_h_variance(self, d_to_h_variance):
        """Sets the d_to_h_variance of this ModelBenchmarkResultMetadata.


        :param d_to_h_variance: The d_to_h_variance of this ModelBenchmarkResultMetadata.  # noqa: E501
        :type: float
        """

        self._d_to_h_variance = d_to_h_variance

    @property
    def error(self):
        """Gets the error of this ModelBenchmarkResultMetadata.  # noqa: E501


        :return: The error of this ModelBenchmarkResultMetadata.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ModelBenchmarkResultMetadata.


        :param error: The error of this ModelBenchmarkResultMetadata.  # noqa: E501
        :type: str
        """

        self._error = error

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModelBenchmarkResultMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelBenchmarkResultMetadata):
            return True

        return self.to_dict() != other.to_dict()
