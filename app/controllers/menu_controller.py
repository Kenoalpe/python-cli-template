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
            choice = self.view.display(
                self.model.get_message(),
                self.model.get_choices()
            )
            if choice == 'Exit':
                self.stop()
                logger.debug("Triggered exit Option!")
            else:
                method = self.model.get_methods().get(choice)
                logger.debug("Execute function!")
                method()

    def stop(self):
        self.model.set_running(False)
