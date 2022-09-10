import toml
from app.core.utils import get_config_path


class CommandStart:
    def __init__(self, command: dict) -> None:
        self._name = command["name"]
        self._message = command["message"]

    @property
    def name(self) -> str:
        return self._name

    @property
    def message(self) -> str:
        return self._message


class Commands:
    def __init__(self, commands: dict):
        self._start = CommandStart(commands["start"])

    @property
    def start(self) -> CommandStart:
        return self._start


class Button:
    def __init__(self, button: dict) -> None:
        self._name = button["name"]
        self._message = button["message"]
        self._use_keyboard = False if "use_keyboard" not in button.keys() else button["use_keyboard"]

    @property
    def name(self) -> str:
        return self._name

    @property
    def message(self) -> str:
        return self._message

    @property
    def use_keyboard(self) -> bool:
        return self._use_keyboard


class Buttons:
    def __init__(self, buttons: dict) -> None:
        self._ready_buttons = []
        name_buttons = buttons.keys()

        if len(name_buttons) == 0:
            return

        for name in name_buttons:
            button = Button(buttons[name])
            self._ready_buttons.append(button)

    @property
    def ready_buttons(self):
        return self._ready_buttons


class Messages:
    def __init__(self, messages: dict) -> None:
        self._error = messages["command_error"]

    @property
    def error(self) -> str:
        return self._error


class Config:
    def __init__(self, data: dict) -> None:
        self._commands = Commands(data["commands"])
        self._buttons = Buttons(data["buttons"])
        self._messages = Messages(data["messages"])

    @property
    def commands(self) -> Commands:
        return self._commands

    @property
    def buttons(self) -> Buttons:
        return self._buttons

    @property
    def messages(self) -> Messages:
        return self._messages


__factory = None


def get_config() -> Config:
    global __factory

    if __factory is None:
        config_path = get_config_path()
        with open(config_path, 'r', encoding='utf-8') as rf:
            data = toml.loads(rf.read())
            __factory = Config(data)

    return __factory
