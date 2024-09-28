from contexts.shared.domain.command_bus.command import Command
from contexts.shared.domain.command_bus.command_bus import CommandBus
from contexts.shared.domain.command_bus.command_bus import CommandHandlerNotFound
from contexts.shared.domain.command_bus.command_handler import CommandHandler


class InMemoryCommandBus(CommandBus):
    def __init__(self, command_handlers: list[CommandHandler]) -> None:
        self._command_handler_map = {
            command_handler.subscribed_to(): command_handler for command_handler in command_handlers
        }

    async def dispatch(self, command: Command) -> None:
        handler = self._command_handler_map.get(type(command))

        if handler is None:
            raise CommandHandlerNotFound(f"Command handler not found for {command.__class__.__name__}")

        await handler.handle(command)
