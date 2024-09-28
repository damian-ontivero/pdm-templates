from abc import ABC
from abc import abstractmethod
from typing import Generic
from typing import TypeVar

from contexts.shared.domain.entity import Entity
from contexts.shared.domain.query_bus.query import Query


T = TypeVar("T", bound=Entity)
U = TypeVar("U", bound=Query)


class QueryHandler(ABC, Generic[T, U]):
    """
    Interface for query handlers.

    Query handlers are responsible for handling queries that are asked
    by the query bus. They contain the business logic that is executed when
    a query is asked.

    Query handlers are subscribed to the queries they handle. When a query
    is asked, the query bus will find the appropriate query handler
    and call its ask method.
    """

    @staticmethod
    @abstractmethod
    def subscribed_to() -> type[U]:
        raise NotImplementedError

    @abstractmethod
    async def handle(self, query: U) -> T | list[T] | int | None:
        raise NotImplementedError
