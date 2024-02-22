import logging.config

logger = logging.getLogger(__name__)


class MenuController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        """
        repeat the menu until exit is triggered
        """
        while self.model.is_running:
            logger.debug("Open menu!")
            # populate view with model
            choice = self.__main_menu()
            self.__choice_checker(choice)
            if choice != "Exit":
                choice = self.__next_menu()
                self.__choice_checker(choice)

    def __main_menu(self):
        return self.view.display(
            self.model.get_message(),
            self.model.get_choices()
        )

    def __next_menu(self):
        return self.view.display(
            "Next",
            ["Continue", "Exit"]
        )

    def __choice_checker(self, choice):
        if choice == "Exit":
            self.stop()
            logger.debug("Triggered exit option!")
        elif choice == "Continue":
            pass
        else:
            method = self.model.get_methods().get(choice)
            if method:
                logger.debug("Execute method!")
                method()
                logger.debug("Run continue, exit prompt.")
            else:
                logger.error(f"Method for choice = {choice} not found.")

    def stop(self):
        self.model.set_running(False)
