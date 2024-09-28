class PageNumber:
    __slots__ = ("_value",)

    def __init__(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Page number must be an integer")

        if value < 1:
            raise ValueError("Page number must be greater than 0")

        self._value = value

    @property
    def value(self) -> int:
        return self._value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PageNumber):
            return NotImplemented

        return self._value == other._value

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(self.value)

    def __repr__(self) -> str:
        return "{c}(value={value!r})".format(c=self.__class__.__name__, value=self._value)
