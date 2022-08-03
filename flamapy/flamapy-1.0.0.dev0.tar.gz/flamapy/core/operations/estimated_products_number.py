from abc import abstractmethod

from flamapy.core.operations import Operation


class EstimatedProductsNumber(Operation):

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_products_number(self) -> int:
        pass
