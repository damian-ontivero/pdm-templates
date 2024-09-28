import json

from contexts.shared.domain.domain_event import DomainEvent
from contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber


class DomainEventDeserializer(dict[str, type[DomainEvent]]):
    @staticmethod
    def configure(subscribers: list[DomainEventSubscriber[DomainEvent]]) -> "DomainEventDeserializer":
        deserializer = DomainEventDeserializer()

        for subscriber in subscribers:
            for event in subscriber.subscribed_to():
                deserializer[event.EVENT_NAME] = event

        return deserializer

    def deserialize(self, event: str) -> DomainEvent:
        event_data = json.loads(event)
        event_type = event_data["type"]

        return self[event_type].from_primitives(**event_data)
