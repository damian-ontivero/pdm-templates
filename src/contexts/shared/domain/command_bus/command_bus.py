from abc import ABC
from abc import abstractmethod

from contexts.shared.domain.command_bus.command import Command


class CommandBus(ABC):
    """
    Interface for command buses.

    Command buses are responsible for dispatching commands to the appropriate
    command handler.
    """

    @abstractmethod
    async def dispatch(self, command: Command) -> None:
        raise NotImplementedError


class CommandHandlerNotFound(Exception):
    pass
