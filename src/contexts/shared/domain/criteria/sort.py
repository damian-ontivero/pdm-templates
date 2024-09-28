from contexts.shared.domain.criteria.sort_direction import SortDirection
from contexts.shared.domain.criteria.sort_field import SortField


class Sort:
    __slots__ = ("_field", "_direction")

    def __init__(self, field: SortField, direction: SortDirection) -> None:
        self._field = field
        self._direction = direction

    @property
    def field(self) -> str:
        return self._field.value

    @property
    def direction(self) -> str:
        return self._direction.value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Sort):
            return NotImplemented

        return self._field == other._field and self._direction == other._direction

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((self._field, self._direction))

    def __repr__(self) -> str:
        return "{c}(field={field!r}, direction={direction!r})".format(
            c=self.__class__.__name__, field=self._field, direction=self._direction
        )

    @classmethod
    def none(cls) -> "Sort":
        return cls(SortField(""), SortDirection("NONE"))

    @classmethod
    def from_primitives(cls, field: str | None, direction: str) -> "Sort":
        if field is None:
            return cls.none()

        return cls(SortField(field), SortDirection(direction))

    def to_primitives(self) -> dict:
        return {"field": self._field.value, "direction": self._direction.value}

    def is_none(self) -> bool:
        return self._direction.is_none()
