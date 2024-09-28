from abc import ABC
from abc import abstractmethod
from typing import Generic
from typing import TypeVar

from contexts.shared.domain.domain_event import DomainEvent


T = TypeVar("T", bound=DomainEvent)


class DomainEventSubscriber(ABC, Generic[T]):
    """
    Interface for domain event subscribers.

    Domain event subscribers are subscribed to domain events and are notified
    when a domain event is published.
    """

    @staticmethod
    @abstractmethod
    def subscribed_to() -> list[type[T]]:
        raise NotImplementedError

    @abstractmethod
    async def on(self, event: T) -> None:
        raise NotImplementedError
