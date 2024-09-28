class ConditionOperator:
    __slots__ = ("_value",)

    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    CONTAINS = "CONTAINS"
    NOT_CONTAINS = "NOT_CONTAINS"
    IS_ANY_OF = "IS_ANY_OF"
    IS_NOT_ANY_OF = "IS_NOT_ANY_OF"
    IS_EMPTY = "IS_EMPTY"
    IS_NOT_EMPTY = "IS_NOT_EMPTY"
    STARTS_WITH = "STARTS_WITH"
    ENDS_WITH = "ENDS_WITH"
    GT = "GT"
    GE = "GE"
    LT = "LT"
    LE = "LE"

    def __init__(self, value: str) -> None:
        if value not in (
            ConditionOperator.EQUALS,
            ConditionOperator.NOT_EQUALS,
            ConditionOperator.CONTAINS,
            ConditionOperator.NOT_CONTAINS,
            ConditionOperator.IS_ANY_OF,
            ConditionOperator.IS_NOT_ANY_OF,
            ConditionOperator.IS_EMPTY,
            ConditionOperator.IS_NOT_EMPTY,
            ConditionOperator.STARTS_WITH,
            ConditionOperator.ENDS_WITH,
            ConditionOperator.GT,
            ConditionOperator.GE,
            ConditionOperator.LT,
            ConditionOperator.LE,
        ):
            raise ValueError("Invalid condition operator")

        self._value = value

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ConditionOperator):
            return NotImplemented
        return self._value == other._value

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash(self._value)

    def __repr__(self) -> str:
        return "{c}(value={value!r})".format(c=self.__class__.__name__, value=self._value)
