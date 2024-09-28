from contexts.shared.domain.criteria.filter import Filter
from contexts.shared.domain.criteria.page_number import PageNumber
from contexts.shared.domain.criteria.page_size import PageSize
from contexts.shared.domain.criteria.sort import Sort


class Criteria:
    __slots__ = ("_filter", "_sort", "_page_size", "_page_number")

    def __init__(
        self, filter: Filter | None, sort: list[Sort] | None, page_size: PageSize | None, page_number: PageNumber | None
    ) -> None:
        self._filter = filter
        self._sort = sort
        self._page_size = page_size
        self._page_number = page_number

    @property
    def filter(self) -> Filter | None:
        return self._filter

    @property
    def sort(self) -> list[Sort] | None:
        return self._sort

    @property
    def page_size(self) -> PageSize | None:
        return self._page_size

    @property
    def page_number(self) -> PageNumber | None:
        return self._page_number

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Criteria):
            return NotImplemented

        return (
            self._filter == other._filter
            and self._sort == other._sort
            and self._page_size == other._page_size
            and self._page_number == other._page_number
        )

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((self._filter, self._sort, self._page_size, self._page_number))

    def __repr__(self) -> str:
        return (
            "{c}(filter={filter!r}, sort={sort!r}, page_size={page_size!r}, " "page_number={page_number!r})"
        ).format(
            c=self.__class__.__name__,
            filter=self._filter,
            sort=self._sort,
            page_size=self._page_size,
            page_number=self._page_number,
        )

    @classmethod
    def from_primitives(
        cls, filter: dict | None, sort: list[dict] | None, page_size: int | None, page_number: int | None
    ) -> "Criteria":
        return cls(
            filter=Filter.from_primitives(**filter) if filter else None,
            sort=[Sort.from_primitives(**s) for s in sort] if sort else None,
            page_size=PageSize(page_size) if page_size else None,
            page_number=PageNumber(page_number) if page_number else None,
        )
