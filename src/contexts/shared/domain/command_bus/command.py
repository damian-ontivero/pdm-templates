from dataclasses import dataclass


@dataclass(frozen=True)
class Command:
    """
    Base class for commands.

    Commands are objects that represent an intention to perform an action.
    They are sent to command buses, which dispatch them to the appropriate
    command handler.
    """

    pass
