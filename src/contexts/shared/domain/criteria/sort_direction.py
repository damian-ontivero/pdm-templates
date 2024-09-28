class SortDirection:
    __slots__ = ("_value",)

    ASC = "ASC"
    DESC = "DESC"
    NONE = "NONE"

    def __init__(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Sort direction must be a string")

        if not len(value) > 0:
            raise ValueError("Sort direction cannot be empty")

        if value not in [SortDirection.ASC, SortDirection.DESC, SortDirection.NONE]:
            raise ValueError("Invalid sort direction")

        self._value = value

    @property
    def value(self) -> str:
        return self._value

    def is_none(self) -> bool:
        return self._value == SortDirection.NONE

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SortDirection):
            return NotImplemented

        return self._value == other._value

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(self._value)

    def __repr__(self) -> str:
        return "{c}(value={value!r})".format(c=self.__class__.__name__, value=self._value)
