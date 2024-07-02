from abc import ABC, abstractmethod


class FileReader(ABC):
    
    @abstractmethod
    def read(self) -> dict:
        raise NotImplementedError
