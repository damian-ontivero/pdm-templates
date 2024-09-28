from contexts.shared.domain.criteria.condition_field import ConditionField
from contexts.shared.domain.criteria.condition_operator import ConditionOperator
from contexts.shared.domain.criteria.condition_value import ConditionValue


class Condition:
    __slots__ = ("_field", "_operator", "_value")

    def __init__(self, field: ConditionField, operator: ConditionOperator, value: ConditionValue) -> None:
        self._field = field
        self._operator = operator
        self._value = value

    @property
    def field(self) -> str:
        return self._field.value

    @property
    def operator(self) -> str:
        return self._operator.value

    @property
    def value(self) -> str:
        return self._value.value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Condition):
            return NotImplemented

        return self._field == other._field and self._operator == other._operator and self._value == other._value

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((self._field, self._operator, self._value))

    def __repr__(self) -> str:
        return ("{c}(field={field!r}, operator={operator!r}, value={value!r})").format(
            c=self.__class__.__name__, field=self._field, operator=self._operator, value=self._value
        )

    @classmethod
    def from_primitives(cls, field: str, operator: str, value: str) -> "Condition":
        return cls(ConditionField(field), ConditionOperator(operator), ConditionValue(value))

    def to_primitives(self) -> dict:
        return {"field": self._field.value, "operator": self._operator.value, "value": self._value.value}
