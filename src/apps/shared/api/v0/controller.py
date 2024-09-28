from abc import ABC
from abc import abstractmethod


class Controller(ABC):
    """
    Controller interface.

    This interface defines the methods that must be provided by the
    controllers.
    """

    @abstractmethod
    async def run(self, *args, **kwargs):
        raise NotImplementedError
