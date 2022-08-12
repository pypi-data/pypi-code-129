"""General utility functions."""


def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    """Combines two dictionaries where each key's value is a list.

    Both dictionaries should resemble:
        {
            "a": [...],
            "b": [...],
            ...
        }

    Args:
        dict1 (dict): First dictionary to merge
        dict2 (dict): Second dictionary to merge

    Returns:
        dict: Union of keys across both dicts and their lists extended
    """
    merged_dicts = {}
    unique_keys = list(set().union(dict1.keys(), dict2.keys()))
    for key in unique_keys:
        merged_dicts[key] = get_item_list(dict1, key) + get_item_list(dict2, key)

    return merged_dicts


def get_item_list(source: dict, key: str) -> list:
    """Retrieves a list from a dictionary even if the key is not present.

    Args:
        source (dict): The dictionary to search through
        key (str): The lookup key, noting it does not have to exist in the dict

    Returns:
        list: The corresponding list for the given key or an empty list if not present
    """
    items = source.get(key)
    items = items if isinstance(items, list) else []
    return items
