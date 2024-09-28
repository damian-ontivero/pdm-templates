from abc import ABC
from abc import abstractmethod

from contexts.shared.domain.domain_event import DomainEvent
from contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber


class EventBus(ABC):
    """
    Interface for event buses.

    Event buses are responsible for publishing domain events and subscribing to them.
    """

    def __init__(self, subscribers: list[DomainEventSubscriber]) -> None:
        self._subscribers = subscribers

    @abstractmethod
    async def add_subscribers(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def publish(self, domain_events: list[DomainEvent]) -> None:
        raise NotImplementedError
