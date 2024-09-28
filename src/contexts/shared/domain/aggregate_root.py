from contexts.shared.domain.domain_event import DomainEvent
from contexts.shared.domain.entity import Entity
from contexts.shared.domain.entity_id import EntityId


class AggregateRoot(Entity):
    """
    Base class for aggregate roots.

    Aggregate roots are entities that are the root of an aggregate.

    Aggregate roots are the only entities that can be accessed from outside the
    aggregate. They are responsible for enforcing the invariants of the aggregate
    and ensuring that the aggregate remains in a consistent state.

    Aggregate roots can record domain events that occurred during the execution
    of a use case. These domain events can be published to the event bus to notify
    other parts of the system that something has happened.
    """

    def __init__(self, id: EntityId) -> None:
        super().__init__(id)

        self._events: list[DomainEvent] = []

    def pull_events(self) -> list[DomainEvent]:
        """
        Pulls the domain events that were recorded by the aggregate root. The
        domain events are then cleared from the aggregate root.
        """
        events = self._events.copy()

        self._events.clear()

        return events

    def record(self, event: DomainEvent) -> None:
        """
        Records a domain event that occurred during the execution of a use case.
        """
        if event is None:
            raise RegisteredDomainEventError("Domain event cannot be None")

        self._events.append(event)


class RegisteredDomainEventError(Exception):
    pass
