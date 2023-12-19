from abc import ABC, abstractmethod


class OutputHandler(ABC):

    @abstractmethod
    def sink(self, metadata, data):
        pass
