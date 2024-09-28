from typing import List
from typing import Union

from contexts.shared.domain.criteria.condition import Condition


Conditions = List[Union[Condition, "Filter"]]


class Filter:
    def __init__(self, conjunction: str, conditions: Conditions):
        if conjunction not in ["AND", "OR"]:
            raise ValueError("Conjunction must be 'AND' or 'OR'")

        self._conjunction = conjunction
        self._conditions = conditions

    @property
    def conjunction(self) -> str:
        return self._conjunction

    @property
    def conditions(self) -> Conditions:
        return self._conditions

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Filter):
            return NotImplemented

        return self._conjunction == other._conjunction and self._conditions == other._conditions

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((self._conjunction, self._conditions))

    def __repr__(self) -> str:
        return ("{c}(conjunction={conjunction!r}, conditions={conditions!r})").format(
            c=self.__class__.__name__, conjunction=self._conjunction, conditions=self._conditions
        )

    @classmethod
    def from_primitives(cls, conjunction: str, conditions: list) -> "Filter":
        _conditions: Conditions = []

        for condition in conditions:
            if "conditions" in condition:
                _conditions.append(Filter.from_primitives(**condition))
            else:
                _conditions.append(Condition.from_primitives(**condition))

        return cls(conjunction, _conditions)

    def is_empty(self) -> bool:
        return len(self._conditions) == 0
