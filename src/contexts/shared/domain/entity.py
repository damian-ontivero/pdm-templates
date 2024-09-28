from abc import ABC
from abc import abstractmethod

from contexts.shared.domain.entity_id import EntityId


class Entity(ABC):
    """
    Base class for entities.

    Entities are objects that have an identity. Two entities are considered equal
    if they have the same identity.

    Once an entity is created, its identity cannot be changed.
    """

    @abstractmethod
    def __init__(self, id: EntityId) -> None:
        self._id = id

    @property
    def id(self) -> EntityId:
        return self._id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Entity):
            return NotImplemented

        return self._id == other._id

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(self._id)
