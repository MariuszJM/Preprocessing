from abc import ABC, abstractmethod


class AbstractDataProcessor(ABC):
    """
    Abstract class for data processing.
    """

    @abstractmethod
    def process(self, *args, **kwargs):
        pass

    @abstractmethod
    def save(self, processed_data, destination):
        pass
