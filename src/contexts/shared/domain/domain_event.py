import datetime
import uuid


class DomainEvent:
    """
    Value object that represents a domain event.

    Domain events are used to communicate changes in the domain model. They are
    immutable and cannot be changed once they are created.

    Domain events are compared by value. Two domain events are considered equal
    if they have the same value.
    """

    EVENT_NAME: str

    __slots__ = ("_id", "_type", "_occurred_on", "_attributes")

    def __init__(self, id: str, type: str, occurred_on: str, attributes: dict) -> None:
        self._id = id
        self._type = type
        self._occurred_on = occurred_on
        self._attributes = attributes

    @property
    def id(self) -> str:
        return str(self._id)

    @property
    def type(self) -> str:
        return str(self._type)

    @property
    def occurred_on(self) -> str:
        return str(self._occurred_on)

    @property
    def attributes(self) -> dict:
        return dict(self._attributes)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DomainEvent):
            return NotImplemented

        return self._id == other._id

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(self._id)

    def __repr__(self) -> str:
        return "{c}(id={id!r}, type={type!r}, occurred_on={occurred_on!r}, attributes={attributes!r})".format(
            c=self.__class__.__name__,
            id=self._id,
            type=self._type,
            occurred_on=self._occurred_on,
            attributes=self._attributes,
        )

    @classmethod
    def create(cls, attributes: dict) -> "DomainEvent":
        return cls(str(uuid.uuid4()), cls.EVENT_NAME, datetime.datetime.now(datetime.UTC).isoformat(), attributes)

    @classmethod
    def from_primitives(cls, id: str, type: str, occurred_on: str, attributes: dict) -> "DomainEvent":
        return cls(id, type, occurred_on, attributes)

    def to_primitives(self) -> dict:
        return {"id": self._id, "type": self._type, "occurred_on": self._occurred_on, "attributes": self._attributes}
