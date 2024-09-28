from dataclasses import dataclass


@dataclass(frozen=True)
class Query:
    """
    Base class for queries.

    Queries are objects that represent a request for information.
    They are sent to query buses, which ask them to the appropriate
    query handler.
    """

    pass
