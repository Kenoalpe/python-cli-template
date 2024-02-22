from app.models import TupleMenuModel
from app.views import MenuView
from app.controllers import MenuController

import logging.config

logger = logging.getLogger(__name__)


def run():
    logger.info("Welcome to the app!")
    # menu logic
    MenuController(
        TupleMenuModel(
            "Option",
            (("Option1", method1), ("Option2", method2))
        ),
        MenuView()
    ).run()


def method1():
    print("Hello")


def method2():
    print("Hello2")
