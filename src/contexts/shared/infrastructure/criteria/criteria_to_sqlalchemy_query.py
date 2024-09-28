from sqlalchemy import and_
from sqlalchemy import or_
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Query

from contexts.shared.domain.criteria.condition import Condition
from contexts.shared.domain.criteria.criteria import Criteria
from contexts.shared.domain.criteria.filter import Filter
from contexts.shared.domain.criteria.sort import Sort


FILTER_OPERATOR_MAPPER = {
    "EQUALS": lambda m, k, v: getattr(m, k) == v,
    "NOT_EQUALS": lambda m, k, v: getattr(m, k) != v,
    "CONTAINS": lambda m, k, v: getattr(m, k).ilike(f"%{v}%"),
    "NOT_CONTAINS": lambda m, k, v: getattr(m, k).notilike(f"%{v}%"),
    "IS_ANY_OF": lambda m, k, v: getattr(m, k).in_(v.split(",")),
    "IS_NOT_ANY_OF": lambda m, k, v: getattr(m, k).notin_(v.split(",")),
    "IS_EMPTY": lambda m, k, v: getattr(m, k).is_(None),
    "IS_NOT_EMPTY": lambda m, k, v: getattr(m, k).isnot(None),
    "STARTS_WITH": lambda m, k, v: getattr(m, k).istartswith(f"{v}%"),
    "ENDS_WITH": lambda m, k, v: getattr(m, k).iendswith(f"%{v}"),
    "GT": lambda m, k, v: getattr(m, k) > v,
    "GE": lambda m, k, v: getattr(m, k) >= v,
    "LT": lambda m, k, v: getattr(m, k) < v,
    "LE": lambda m, k, v: getattr(m, k) <= v,
}


def _process_condition(condition: Condition, model: type[DeclarativeBase]):
    return FILTER_OPERATOR_MAPPER[condition.operator](model, condition.field, condition.value)


def _process_filter(filter: Filter, model: type[DeclarativeBase]):
    filters = []

    for condition in filter.conditions:
        if isinstance(condition, Filter):
            filters.append(_process_filter(condition, model))
        elif isinstance(condition, Condition):
            filters.append(_process_condition(condition, model))

    if filter.conjunction == "AND":
        return and_(*filters)

    return or_(*filters)


def _process_sort(sort: Sort, model: type[DeclarativeBase]):
    return getattr(model, sort.field).asc() if sort.direction == "ASC" else getattr(model, sort.field).desc()


def criteria_to_sqlalchemy_query(query: Query, model: type[DeclarativeBase], criteria: Criteria) -> Query:
    """
    Convert a Criteria domain object to a SQLAlchemy query.
    """
    filters = []
    if criteria.filter is not None:
        filters.append(_process_filter(criteria.filter, model))

    if filters:
        query = query.filter(*filters)

    if criteria.sort is not None:
        for sort in criteria.sort:
            query = query.order_by(_process_sort(sort, model))

    if criteria.page_size is not None:
        query = query.limit(criteria.page_size.value)

    if criteria.page_size is not None and criteria.page_number is not None:
        query = query.offset((criteria.page_number.value - 1) * criteria.page_size.value)

    return query
