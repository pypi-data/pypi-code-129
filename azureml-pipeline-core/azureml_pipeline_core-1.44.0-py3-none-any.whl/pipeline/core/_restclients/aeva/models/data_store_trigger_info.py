# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DataStoreTriggerInfo(Model):
    """DataStoreTriggerInfo.

    :param data_store_name:
    :type data_store_name: str
    :param polling_interval:
    :type polling_interval: int
    :param data_path_parameter_name:
    :type data_path_parameter_name: str
    :param path_on_data_store:
    :type path_on_data_store: str
    """

    _attribute_map = {
        'data_store_name': {'key': 'DataStoreName', 'type': 'str'},
        'polling_interval': {'key': 'PollingInterval', 'type': 'int'},
        'data_path_parameter_name': {'key': 'DataPathParameterName', 'type': 'str'},
        'path_on_data_store': {'key': 'PathOnDataStore', 'type': 'str'},
    }

    def __init__(self, data_store_name=None, polling_interval=None, data_path_parameter_name=None, path_on_data_store=None):
        super(DataStoreTriggerInfo, self).__init__()
        self.data_store_name = data_store_name
        self.polling_interval = polling_interval
        self.data_path_parameter_name = data_path_parameter_name
        self.path_on_data_store = path_on_data_store
