from abc import ABC, abstractmethod
import logging.config

logger = logging.getLogger(__name__)


class AbstractMenuModel(ABC):
    def __init__(self, message: str):
        self.running = True
        self.message = message

    @property
    def is_running(self) -> bool:
        return self.running

    def set_running(self, running: bool):
        if self.is_running:
            self.running = running
        else:
            raise ValueError("Menu needs to be running!")

    def get_message(self) -> str:
        return self.message

    @abstractmethod
    def get_choices(self) -> list:
        pass

    @abstractmethod
    def get_methods(self) -> list:
        pass


class YamlMenuModel:
    pass
