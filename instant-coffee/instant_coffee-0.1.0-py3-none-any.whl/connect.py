"""
Accessory methods for Connect
"""

class ParameterIsMissingException(Exception):
    """
    Class to manage 'Parameter is missing' exception
    """

    def __init__(self, param_id: str):
        super().__init__('Parameter {} is missing'.format(param_id))

def generate_collection(params, param_ids: set):
    """
    Generate an array of parameters for the param_ids set
    """
    coll = []
    for param in params:
        if param.id in param_ids:
            coll.append(param)
    return coll

def reset_value_errors(asset) -> set:
    """
    Set the value errors of all parameters to '' if they were set
    """
    param_ids = set()
    for param in asset.params:
        if param.valueError:
            param.valueError = ''
            param_ids.add(param.id)
    return param_ids
