from abc import ABC
from abc import abstractmethod

from contexts.shared.domain.query_bus.query import Query


class QueryBus(ABC):
    """
    Interface for query buses.

    Query buses are responsible for asking queries to the appropriate query handler.
    """

    @abstractmethod
    async def ask(self, query: Query):
        raise NotImplementedError


class QueryHandlerNotFound(Exception):
    pass
