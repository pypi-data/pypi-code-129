"""Represents an item."""

from typing import Any, Dict


class Item:
    def __init__(
        self, item_id: str, name: str, properties: Dict[str, Any] = None
    ) -> None:
        """Creates an item, which minimally has an ID and a canonical name,
        and can optionally have any number of properties, which are represented
        as key-value pairs.

        Args:
            item_id: Item ID.
            name: Item name.
            properties: Dictionary of item properties (key-value pairs).
                Defaults to None.
        """
        # TODO Optionally, connect items to an ontology and allow only for
        # properties that correspond to ontology classes.
        # See: https://github.com/iai-group/dialoguekit/issues/42
        self._item_id = item_id
        self._name = name
        self._properties = properties

    @property
    def id(self) -> str:
        return self._item_id

    @property
    def name(self) -> str:
        return self._name

    def get_property(self, key: str) -> Any:
        """Returns a given item property.

        Args:
            key: Name of property.

        Returns:
            Value of property or None.
        """
        return self._properties.get(key)

    def set_property(self, key: str, value: Any) -> None:
        """Sets the value of a given item property (or overwrites if it already
        exists).

        Args:
            key: Property name.
            value: Property value.
        """
        self._properties[key] = value
